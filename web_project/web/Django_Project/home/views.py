from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home_page.html'
    extra_context = {}