from django.conf.urls import url
from apps.tvazteca.cabs.viewfinderweb.views import startViewFinderWeb, dateTableViewFinderJSON, \
    dateTableViewDetailsJSON, dateCheck, getUrlMedia

urlpatterns = [
    url(r'^viewweb/$', startViewFinderWeb, name='start_viewfinderweb'),
    url(r'^viewweb/json_00010$', dateTableViewFinderJSON, name='datatable_viewfinderweb_json'),
    url(r'^viewweb/json_00020$', dateTableViewDetailsJSON, name='datatable_viewdetailsweb_json'),
    url(r'^viewweb/datecheck$', dateCheck, name='datatable_datecheck'),
    url(r'^viewweb/get/$', getUrlMedia, name='get_media'),
    url(r'^viewweb/get/(?P<id>\S+)/(?P<date>\S+)/(?P<event>\S+)/(?P<url>\S+)/(?P<name>\S+)/$', getUrlMedia, name='get_media'),
]
