from django.db import models
import markdown

class Corporate(models.Model):
    section = models.CharField(max_length=255)
    details_html = models.TextField(blank=True,null=True)
    details_markdown = models.TextField('Details',blank=True,null=True)
    class Meta:
        ordering = ('section',)
        verbose_name_plural = 'corporate Info'

    def __unicode__(self):
        return u'%s' %(self.section)

    def save(self):
         self.details_html = markdown.markdown(self.details_markdown, safe_mode = False)
         super(Entry, self).save()
