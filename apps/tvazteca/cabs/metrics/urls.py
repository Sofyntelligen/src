from django.conf.urls import url

from apps.tvazteca.cabs.metrics.views import startMetrics

urlpatterns = [
    url(r'^$', startMetrics, name='start_metrics'),
]