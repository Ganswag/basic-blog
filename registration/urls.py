from django.urls import path
from .views import ProfileUpdate, SignUpView


urlpatterns = [
    path('mi-perfil', ProfileUpdate.as_view(), name='my-profile'),
    path('registro/', SignUpView.as_view(), name='sign-up'),
]
