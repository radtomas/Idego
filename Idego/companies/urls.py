from django.conf.urls import url

from .views import (
    IndexView,
    CompaniesListView,
    CompaniesCreateView,
    UsersListView,
    UsersDetailView,
    UsersCreateView,
    UsersEditView,
    UsersDeleteView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^companies/$', CompaniesListView.as_view(), name='companies'),
    url(r'^companies/create/$', CompaniesCreateView.as_view(), name='company-add'),
    url(r'^users/$', UsersListView.as_view(), name='users'),
    url(r'^users/create/$', UsersCreateView.as_view(), name='user-add'),
    url(r'^users/(?P<pk>[0-9]+)/$', UsersDetailView.as_view(), name='user-detail'),
    url(r'^users/edit/(?P<pk>[0-9]+)/$', UsersEditView.as_view(), name='user-edit'),
    url(r'^users/delete/(?P<pk>[0-9]+)/$', UsersDeleteView.as_view(), name='user-delete'),
]