import datetime
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from blog.fields import ThumbnailImageField

class ManyToManyField_NoSyncdb(models.ManyToManyField):
    def __init__(self, *args, **kwargs):
        super(ManyToManyField_NoSyncdb, self).__init__(*args, **kwargs)
        self.creates_table = False

class Video(models.Model):
    isactive = models.BooleanField('Is Active On Site?',default=False)
    featured = models.BooleanField('Featured Homepage Video?',default=False)
    carousel = models.BooleanField('Show in Carousel?',default=False)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=200)
    carousel_text = models.CharField('Carousel Text',max_length=25,blank=True,null=True)
    carousel_subtext = models.CharField('Carousel Sub-text',max_length=15,blank=True,null=True)
    duration = models.CharField("Video Duration",max_length=20,blank=True,null=True)
    director = models.CharField("Director",max_length=255,blank=True,null=True)
    producer = models.CharField("Producer / Studio",max_length=255,blank=True,null=True)
    details = models.TextField(blank=True,null=True)
    pub_date = models.DateTimeField('Entry Date',blank=True,null=True)
    url_home = models.TextField('Homepage Embed URL',blank=True,null=True)
    url = models.TextField('Detail Embed URL',blank=True,null=True)
    wowio = models.BooleanField('Available to WOWIO?',default=False)
    wevolt = models.BooleanField('Available to WEVolt?',default=False)
    drunkduck = models.BooleanField('Available to DrunkDuck?',default=False)
    syndicate = models.BooleanField('Available for Syndication?',default=False)
    thumbnail = ThumbnailImageField("Thumbnail Image",upload_to='thumbs')
    tags = TagAutocompleteField('Tags',help_text='Keywords to help searching for content.')
    slug = models.SlugField(
        unique_for_date='pub_date',
        help_text='Automatically built from the title. -- DO NOT MODIFY',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['title']
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __unicode__(self):
        return self.title

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

    def get_tags(self):
        return Tag.objects.get_for_object(self)

    @permalink
    def get_absolute_url(self):
        return ("video_detail", None, {'slug':self.slug})


