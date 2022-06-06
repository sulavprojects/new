from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from home.views import privacypolicy
from .models import Fonts

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['allfonts', 'home', 'arabic fonts', 'aboutus', 'contact', 'our_page', 'privacypolicy', 'termsandcondition', 'install_fonts_on_linux', 'install_fonts_on_windows']

    def location(self, item):
        return reverse(item)


class SnippetSitemap(Sitemap):
    def items(self):
        return Fonts.objects.all()