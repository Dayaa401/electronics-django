"""
URL configuration for mypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path  # ✅ Include re_path here
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve  # ✅ Needed to serve media files when DEBUG=False
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('add-to-cart/', views.add_to_cart),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]

# Serve static and media files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
