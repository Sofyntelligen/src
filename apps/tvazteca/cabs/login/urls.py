from django.conf.urls import url
from apps.tvazteca.cabs.login.views import startLogin, evaluationLogin, closeSession

urlpatterns = [
    url(r'^$', startLogin, name='start_login'),
    url(r'^start$', evaluationLogin, name='login'),
    url(r'^close$', closeSession, name='close_login'),
]
