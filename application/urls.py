from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index),
    path("ecosystem/",ecosystem),
    path("community/",community),
    path("developers/",devlopers),
    path("governance/",governance),
    path("blog/",blog),
    path("faq/",faq),

]