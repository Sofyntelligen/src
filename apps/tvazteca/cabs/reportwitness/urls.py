from django.conf.urls import url
from apps.tvazteca.cabs.reportwitness.views import startReportWitness, listSubReportJSON

urlpatterns = [
    url(r'^$', startReportWitness, name='start_report_witness'),
    url(r'^json_00040$', listSubReportJSON, name='list_sub_report'),
]
