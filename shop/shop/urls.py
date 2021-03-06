"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from products.views import index_view, ProductListView, AboutTemplateView, ProductDetailView, MessageFormView
import debug_toolbar
from userapp.views import RegisterView, AuthView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index_view),
    path('', ProductListView.as_view()),
    path('about/', AboutTemplateView.as_view()),
    path('product/', index_view),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('message/', MessageFormView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', AuthView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('__debug__/', include(debug_toolbar.urls))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)