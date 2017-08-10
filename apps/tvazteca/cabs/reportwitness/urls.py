from django.conf.urls import url
from apps.tvazteca.cabs.reportwitness.views import startReportWitness

urlpatterns = [
    url(r'^$', startReportWitness, name='start_report_witness'),
]
