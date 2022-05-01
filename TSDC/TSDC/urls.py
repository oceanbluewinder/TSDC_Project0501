from django.urls import path, include
from django.conf.urls import url,include
from TSDC import views

app_name = "TSDC"
urlpatterns = [
    path('',views.about,name='about'),
    url(r'^industry/', include('industry.urls')),
]