"""Views for Core."""

from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.detail import DetailView

from .models import (SiteData, ContentManagmentSystem)


# Create your views here.
class Home(View):
    """View to home."""

    template_name = 'core/home.html'

    def get(self, request):
        """Get method"""
        return render(
            request,
            self.template_name,
            {
                'site':
                    SiteData.objects.order_by('-created_at')[0]
            }
        )


class ContentManagment(DetailView):
    model = ContentManagmentSystem


def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')
