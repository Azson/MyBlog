"""chapter2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from mainsite.views import homepage, showpost, login, showMark, contact, showMark2, login2, userinfo, logout, login3, showBlog, writeBlog, showProblem

urlpatterns = [
    url(r'^$', homepage),
    url(r'^captcha/', include("captcha.urls")),
    url(r'^mark/$', showMark),
    url(r'post02/$', showMark2),
    url(r'^contact/$', contact),
    url(r'^mark/mark/(\d+)/(\w+)$', showMark),
    url(r'^login/', login3),
    url(r'^login/', login),
    url(r'^logout/', logout),

    url(r'showBlog/', showBlog),
    url(r'writeBlog/', writeBlog),

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'^post/(\w+)$', showpost),
    url(r'^userinfo/', userinfo),
    url(r'^admin/', admin.site.urls),

    url(r'^showProblem/$', showProblem),

    url(r'', homepage),
]