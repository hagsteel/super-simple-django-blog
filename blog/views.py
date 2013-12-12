from django.views.generic import DetailView, ListView
from .models import BlogEntry


class BlogView(DetailView):
    model = BlogEntry

    def get_object(self, queryset=None):
        if (self.request.user.is_authenticated()):
            return self.model.objects.get(slug=self.kwargs[self.slug_url_kwarg])
        return self.model.objects.get(slug=self.kwargs[self.slug_url_kwarg], is_published=True)


class BlogListView(ListView):
    model = BlogEntry
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(is_published=True)


class BlogListByTagView(BlogListView):
    def get_queryset(self):
        qs = super(BlogListByTagView, self).get_queryset()
        return qs.filter(tags__name=self.request.GET.get('tag'))
