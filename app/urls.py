from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls import handler404
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView, TemplateView

from .sitemaps import StaticSitemap


sitemaps = {
    'static': StaticSitemap(),
}


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r'^robots\.txt$',
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain"
        )
    ),
    re_path(
        r'^favicon\.ico$',
        RedirectView.as_view(
            url='/static/favicon.ico',
            permanent=True
        )
    ),
    re_path(
        r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path('', include(('core.urls', 'core'), namespace='core')),
    # Apps
    path(
        'blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path(
        'colaboradores/', include(
            ('collaborators.urls', 'collaborators'),
            namespace='collaborators'
        )
    ),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include('registration.urls')),
]


handler404 = 'core.views.view_404'


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
