"""developmentWebTVAzteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from apps.tvazteca.cabs.coding.view import error
from apps.tvazteca.cabs.login.views import startLogin

app_name = 'tvazteca'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', startLogin),
    url(r'^error/', error, name='error'),
    url(r'^inventario_testigos/', include('apps.tvazteca.cabs.login.urls'), name='login'),
    url(r'^inventario_testigos/monitoreo_testigos/', include('apps.tvazteca.cabs.viewfinderweb.urls'),
        name='viewfinderweb'),
    url(r'^inventario_testigos/inicio/', include('apps.tvazteca.cabs.tracing.urls'), name='tracing'),
    url(r'^inventario_testigos/reporte_testigo/', include('apps.tvazteca.cabs.reportwitness.urls'),
        name='reportwitness'),
    url(r'^inventario_testigos/metricas/', include('apps.tvazteca.cabs.metrics.urls'),
        name='metrics'),
]
