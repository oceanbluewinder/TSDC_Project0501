from django.urls import path, include
from industry import views

app_name = "industry"
urlpatterns = [
    path('aboutus1',views.aboutus1,name='aboutus1'),

    path('question1',views.question1,name='question1'),
    path('question2',views.question2,name='question2'),
    path('question3',views.question3,name='question3'),

    path('report_2324',views.report_2324,name='report_2324'),
    path('report_2357',views.report_2357,name='report_2357'),
    path('report_2365',views.report_2365,name='report_2365'),
    path('report_2365',views.report_2365,name='report_2365'),
    path('report_2382',views.report_2382,name='report_2382'),
    path('report_2809',views.report_2809,name='report_2809'),
    path('report_2832',views.report_2832,name='report_2832'),
    path('report_2849',views.report_2849,name='report_2849'),
    path('report_2886',views.report_2886,name='report_2886'),
    path('report_2891',views.report_2891,name='report_2891'),
    path('report_3231',views.report_3231,name='report_3231'),

    path('chip_2324',views.chip_2324,name='chip_2324'),
    path('chip_2357',views.chip_2357,name='chip_2357'),
    path('chip_2365',views.chip_2365,name='chip_2365'),
    path('chip_2365',views.chip_2365,name='chip_2365'),
    path('chip_2382',views.chip_2382,name='chip_2382'),
    path('chip_2809',views.chip_2809,name='chip_2809'),
    path('chip_2832',views.chip_2832,name='chip_2832'),
    path('chip_2849',views.chip_2849,name='chip_2849'),
    path('chip_2886',views.chip_2886,name='chip_2886'),
    path('chip_2891',views.chip_2891,name='chip_2891'),
    path('chip_3231',views.chip_3231,name='chip_3231'),

    path('index_2324',views.index_2324,name='index_2324'),
    path('index_2357',views.index_2357,name='index_2357'),
    path('index_2365',views.index_2365,name='index_2365'),
    path('index_2365',views.index_2365,name='index_2365'),
    path('index_2382',views.index_2382,name='index_2382'),
    path('index_2809',views.index_2809,name='index_2809'),
    path('index_2832',views.index_2832,name='index_2832'),
    path('index_2849',views.index_2849,name='index_2849'),
    path('index_2886',views.index_2886,name='index_2886'),
    path('index_2891',views.index_2891,name='index_2891'),
    path('index_3231',views.index_3231,name='index_3231'),
]