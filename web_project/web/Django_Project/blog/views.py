from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = 'blog/blog_page.html'
    extra_context = {}
