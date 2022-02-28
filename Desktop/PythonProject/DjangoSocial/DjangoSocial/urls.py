
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='user/index.html')),
    path('accounts/', include('allauth.urls')),
    path('user/', include('user.urls'))
]
