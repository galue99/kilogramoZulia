__author__ = 'edgar'
from django.conf.urls import url
from accounts import views as accounts_views
from rest_framework.urlpatterns import format_suffix_patterns

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^companys/$', accounts_views.CompanyViews.as_view()),
    url(r'^taras/$', accounts_views.TaraViews.as_view()),
    url(r'^weights/$', accounts_views.WeightsViews.as_view()),
    url(r'^weights/(?P<pk>[0-9]+)/$', accounts_views.WeightsDetailsViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)