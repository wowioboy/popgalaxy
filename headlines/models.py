from django.db import models

class Headline(models.Model):
    isactive = models.BooleanField('Is Active On Site?',default=False)
    title = models.CharField(max_length=255)
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'headlines'

    def __unicode__(self):
        return u'%s' %(self.title)
