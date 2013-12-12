from datetime import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager


class BlogEntry(models.Model):
    author = models.ForeignKey(User, related_name='blog_entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.TextField()
    date_published = models.DateTimeField(default=datetime.now())
    is_published = models.BooleanField()
    slug = models.SlugField(null=True, blank=True)

    tags = TaggableManager()

    def __unicode__(self):
        return '%s - %s' % (self.title, self.date_published)

    def get_absolute_url(self):
        return reverse('blog_entry', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(BlogEntry, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-date_published',)