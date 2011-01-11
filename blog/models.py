from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap
import markdown
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from blog.fields import ThumbnailImageField

PUB_STATUS = (
    (0, 'Draft'),
    (1, 'Published'),
)
class Entry(models.Model):
    carousel = models.BooleanField('Show in Carousel?',default=False)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=200)
    carousel_text = models.CharField('Carousel Text',max_length=25,blank=True,null=True)
    carousel_subtext = models.CharField('Carousel Sub-text',max_length=15,blank=True,null=True)
    leadin_html = models.TextField(blank=True,null=True)
    leadin_markdown = models.TextField('Lead-in Content',blank=True,null=True)
    body_html = models.TextField(blank=True,null=True)
    body_markdown = models.TextField('Content',blank=True,null=True)
    pub_date = models.DateTimeField('Date published')
    tags = TagAutocompleteField('Tags',help_text='Keywords to help searching for content.')
    enable_comments = models.BooleanField(default=True)
    status = models.IntegerField('Publish Status',choices=PUB_STATUS, default=0)
    thumbnail = ThumbnailImageField("Thumbnail Image",upload_to='thumbs')
    slug = models.SlugField(
        unique_for_date='pub_date',
        help_text='Automatically built from the title.',
        blank=True,
        null=True
    )
    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name_plural = 'blog Entries'

    def __unicode__(self):
        return u'%s' %(self.title)

    def get_absolute_url(self):
        return "/blog/%s/%s/" %(self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
    
    def save(self):
         self.body_html = markdown.markdown(self.body_markdown, safe_mode = False)
         self.leadin_html = markdown.markdown(self.leadin_markdown, safe_mode = False)
         super(Entry, self).save()

    def get_previous_published(self):
        return self.get_previous_by_pub_date(status__exact=1)

    def get_next_published(self):
        return self.get_next_by_pub_date(status__exact=1)

    def get_tags(self):
        return Tag.objects.get_for_object(self)

