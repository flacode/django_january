__author__ = 'Flavia N'
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.ReviewList.as_view(), name='review_list'),
    url(r'^review/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view(), name='review_detail'),
    url(r'^wine/$', views.WineList.as_view(), name='wine_list'),
    url(r'^wine/(?P<pk>[0-9]+)/$', views.wine_detail, name='wine_detail'),
    url(r'^wine/(?P<pk>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),

]
