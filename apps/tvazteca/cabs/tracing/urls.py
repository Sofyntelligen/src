from django.conf.urls import url
from apps.tvazteca.cabs.tracing.views import startViewTracing, dateTableTracingJSON

urlpatterns = [
    url(r'^$', startViewTracing, name='start_tracing'),
    url(r'^json_00030$', dateTableTracingJSON, name='datatable_tracing_json'),
]