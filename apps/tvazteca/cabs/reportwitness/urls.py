from django.conf.urls import url
from apps.tvazteca.cabs.reportwitness.views import startReportWitness, listSubReportJSON, listActionReportJSON

urlpatterns = [
    url(r'^(?P<id>\S+)/$', startReportWitness, name='start_report_witness_id'),
    url(r'^$', startReportWitness, name='start_report_witness'),
    url(r'^json_00040$', listSubReportJSON, name='list_sub_report'),
    url(r'^json_00050$', listActionReportJSON, name='list_action_report'),
]
