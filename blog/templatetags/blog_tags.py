from django import template
from django.conf import settings
from ..models import BlogEntry

register = template.Library()


@register.inclusion_tag('blog/blog_roll.html', takes_context=True)
def blog_roll(context, max_entries=None):
    if not max_entries:
        max_entries = settings.BLOG_ROLL_ENTRIES
    blog_entries = BlogEntry.objects.filter(is_published=True)[:max_entries]
    return {'blog_entries': blog_entries}
