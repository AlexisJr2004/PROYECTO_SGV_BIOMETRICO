
from django.conf import settings
from django.conf.urls.static import static
from app.core import views as core
from django.contrib import admin
from django.urls import path, include
from app.core.views.home import HomeTemplateView
from app.core.views.modulos import ModuloTemplateView
urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('',HomeTemplateView.as_view(), name='home'),
    path('modulos/',ModuloTemplateView.as_view(), name='modulos'),
    path('security/', include('app.security.urls', namespace='security')),
    path('core/', include('app.core.urls', namespace='core')),
    path('sale/', include('app.sales.urls', namespace='sale')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
