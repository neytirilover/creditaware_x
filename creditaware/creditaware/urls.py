"""creditaware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from views import show_index, user_login, user_logout,login_landing,user_add_card,delete_card
from views import user_register, passwd_chg
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', show_index, name='show_index'),
    url(r'^cmanage/', include('creditmanage.urls')),
    url(r'^login/', user_login, name='user_login'),
	url(r'^logout/', user_logout, name = 'user_logout'),
    url(r'^login_landing/$', login_landing, name = 'login_landing'),
    url(r'^user_add_card/$', user_add_card, name = 'user_add_card'),
    url(r'^user_add_card/login_landing/', login_landing, name = 'back_to_login_landing'),
    url(r'^passwd_chg/', passwd_chg, name = 'passwd_chg'),
    url(r'^delete_card/$', delete_card, name = 'delete_card'),
    url(r'^register/',user_register,name = 'user_register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Creditaware Admin Access'
