from django.conf.urls import url

from apps.tvazteca.cabs.viewfinderweb.views import startViewFinderWeb, dateTableViewFinderJSON, \
    dateTableViewDetailsJSON, dateCheck, getUrlMedia

urlpatterns = [
    url(r'^$', startViewFinderWeb, name='start_viewfinderweb'),
    url(r'^json_00010$', dateTableViewFinderJSON, name='datatable_viewfinderweb_json'),
    url(r'^json_00020$', dateTableViewDetailsJSON, name='datatable_viewdetailsweb_json'),
    url(r'^datecheck$', dateCheck, name='datatable_datecheck'),
    url(r'^get/$', getUrlMedia, name='get_media'),
    url(r'^get/(?P<id>\S+)/(?P<date>\S+)/(?P<event>\S+)/(?P<url>\S+)/(?P<name>\S+)/$', getUrlMedia, name='get_media'),
]
