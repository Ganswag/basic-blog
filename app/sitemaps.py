from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):

    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)
