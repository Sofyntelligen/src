# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CatPerfiles(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=128)
    enabled = models.NullBooleanField()
    permiso_transferencia = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'cat_perfiles'


class CatProgramasTestigos13(models.Model):
    id_programa = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=128)
    id_seccion = models.ForeignKey('CatSecciones', models.DO_NOTHING, db_column='id_seccion', blank=True, null=True)
    id_tipo_clip = models.ForeignKey('CatTiposClip', models.DO_NOTHING, db_column='id_tipo_clip', blank=True, null=True)
    abreviatura = models.CharField(max_length=5, blank=True, null=True)
    enabled = models.NullBooleanField()
    fecha_registro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_programas_testigos_13'


class CatProgramasTestigos7(models.Model):
    id_programa = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=128)
    id_seccion = models.ForeignKey('CatSecciones', models.DO_NOTHING, db_column='id_seccion', blank=True, null=True)
    id_tipo_clip = models.ForeignKey('CatTiposClip', models.DO_NOTHING, db_column='id_tipo_clip', blank=True, null=True)
    abreviatura = models.CharField(max_length=5, blank=True, null=True)
    enabled = models.NullBooleanField()
    fecha_registro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_programas_testigos_7'


class CatSecciones(models.Model):
    id_seccion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=128)
    abreviatura = models.CharField(max_length=5)
    enabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'cat_secciones'


class CatTiposClip(models.Model):
    id_tipo_clip = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=128)
    abreviatura = models.CharField(max_length=5)
    enabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'cat_tipos_clip'


class ComparadorSenalesMaestras(models.Model):
    id = models.BigIntegerField()
    descripcion = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'comparador_senales_maestras'


class ComparadorSenalesSecundarias(models.Model):
    id = models.BigIntegerField()
    descripcion = models.CharField(max_length=64)
    tabla_guia = models.CharField(max_length=32, blank=True, null=True)
    tabla_guia_aux = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comparador_senales_secundarias'


class ConsolidadoAlertas(models.Model):
    numero_ev = models.IntegerField(primary_key=True)
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()
    id_testigo = models.IntegerField()
    comentario = models.CharField(max_length=256, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consolidado_alertas'
        unique_together = (('numero_ev', 'hora_inicio', 'fecha', 'id_testigo'),)


class ConsolidadoAlertasAza(models.Model):
    numero_ev = models.IntegerField(primary_key=True)
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()
    id_testigo = models.IntegerField()
    comentario = models.CharField(max_length=256, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consolidado_alertas_aza'
        unique_together = (('numero_ev', 'hora_inicio', 'fecha', 'id_testigo'),)


class CorreoAnalisis(models.Model):
    remitente = models.CharField(max_length=128, blank=True, null=True)
    remitente_dir = models.CharField(max_length=128, blank=True, null=True)
    dirs_envio = models.CharField(max_length=1024, blank=True, null=True)
    asunto = models.CharField(max_length=128, blank=True, null=True)
    program = models.CharField(max_length=128, blank=True, null=True)
    reply = models.CharField(max_length=128, blank=True, null=True)
    msg = models.CharField(max_length=4000, blank=True, null=True)
    enviado = models.NullBooleanField()
    id = models.BigIntegerField(blank=True, null=True)
    adjunto_loc = models.CharField(max_length=256, blank=True, null=True)
    adjunto_env = models.CharField(max_length=256, blank=True, null=True)
    tipo_destino = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correo_analisis'


class CorreoAnalisisAza(models.Model):
    remitente = models.CharField(max_length=128, blank=True, null=True)
    remitente_dir = models.CharField(max_length=128, blank=True, null=True)
    dirs_envio = models.CharField(max_length=1024, blank=True, null=True)
    asunto = models.CharField(max_length=128, blank=True, null=True)
    program = models.CharField(max_length=128, blank=True, null=True)
    reply = models.CharField(max_length=128, blank=True, null=True)
    msg = models.CharField(max_length=4000, blank=True, null=True)
    enviado = models.NullBooleanField()
    id = models.BigIntegerField(blank=True, null=True)
    adjunto_loc = models.CharField(max_length=256, blank=True, null=True)
    adjunto_env = models.CharField(max_length=256, blank=True, null=True)
    tipo_destino = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correo_analisis_aza'


class CorreoContinuidad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    asunto = models.CharField(max_length=128)
    msg = models.CharField(max_length=4000)
    enviado = models.NullBooleanField()
    id_transmisor = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'correo_continuidad'


class CorreoContinuidadAza(models.Model):
    id = models.BigIntegerField(primary_key=True)
    asunto = models.CharField(max_length=128)
    msg = models.CharField(max_length=4000)
    enviado = models.NullBooleanField()
    id_transmisor = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'correo_continuidad_aza'


class CortesTestigoWeb(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_testigo = models.IntegerField()
    fecha_video = models.IntegerField()
    hora_ini_corte = models.IntegerField()
    duracion_corte = models.IntegerField()
    nombre_exporta = models.CharField(max_length=512)
    fecha_peticion = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    id_cortador = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cortes_testigo_web'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EstadoConciliadores(models.Model):
    id_tst = models.IntegerField(primary_key=True)
    hora_alive = models.IntegerField(blank=True, null=True)
    fecha_alive = models.IntegerField(blank=True, null=True)
    hora_conc = models.IntegerField(blank=True, null=True)
    fecha_conc = models.IntegerField(blank=True, null=True)
    hora_bloq = models.IntegerField(blank=True, null=True)
    fecha_bloq = models.IntegerField(blank=True, null=True)
    hora_audio = models.IntegerField(blank=True, null=True)
    fecha_audio = models.IntegerField(blank=True, null=True)
    dir_ip = models.CharField(max_length=15, blank=True, null=True)
    version = models.CharField(max_length=64, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    desase_hora = models.IntegerField(blank=True, null=True)
    bloq_total = models.IntegerField(blank=True, null=True)
    aire_bloq = models.IntegerField(blank=True, null=True)
    aire_aud = models.IntegerField(blank=True, null=True)
    huella_ne = models.IntegerField(blank=True, null=True)
    bloq_conc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_conciliadores'


class Guia13Cabs(models.Model):
    num = models.IntegerField()
    ev_tst = models.IntegerField()
    h_ini = models.CharField(max_length=11)
    tipo = models.CharField(max_length=1)
    nombre = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    duracion = models.CharField(max_length=11)
    ev_cabs = models.IntegerField()
    rec_key = models.IntegerField()
    estado = models.IntegerField()
    hora_ms = models.IntegerField()
    rack = models.CharField(max_length=16, blank=True, null=True)
    fecha_aire = models.IntegerField()
    fecha_guia = models.IntegerField()
    archivo_fuente = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'guia_13_cabs'


class Guia40Cabs(models.Model):
    num = models.IntegerField()
    ev_tst = models.IntegerField()
    h_ini = models.CharField(max_length=11)
    tipo = models.CharField(max_length=1)
    nombre = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    duracion = models.CharField(max_length=11)
    ev_cabs = models.IntegerField()
    rec_key = models.IntegerField()
    estado = models.IntegerField()
    hora_ms = models.IntegerField()
    rack = models.CharField(max_length=16, blank=True, null=True)
    fecha_aire = models.IntegerField()
    fecha_guia = models.IntegerField()
    archivo_fuente = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'guia_40_cabs'


class Guia7Cabs(models.Model):
    num = models.IntegerField()
    ev_tst = models.IntegerField()
    h_ini = models.CharField(max_length=11)
    tipo = models.CharField(max_length=1)
    nombre = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    duracion = models.CharField(max_length=11)
    ev_cabs = models.IntegerField()
    rec_key = models.IntegerField()
    estado = models.IntegerField()
    hora_ms = models.IntegerField()
    rack = models.CharField(max_length=16, blank=True, null=True)
    fecha_aire = models.IntegerField()
    fecha_guia = models.IntegerField()
    archivo_fuente = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'guia_7_cabs'


class GuiaAaEsteCabs(models.Model):
    num = models.IntegerField()
    ev_tst = models.IntegerField()
    h_ini = models.CharField(max_length=11)
    tipo = models.CharField(max_length=1)
    nombre = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    duracion = models.CharField(max_length=11)
    ev_cabs = models.IntegerField()
    rec_key = models.IntegerField()
    estado = models.IntegerField()
    hora_ms = models.IntegerField()
    rack = models.CharField(max_length=16, blank=True, null=True)
    fecha_aire = models.IntegerField()
    fecha_guia = models.IntegerField()
    archivo_fuente = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'guia_aa_este_cabs'


class GuiaAaOesteCabs(models.Model):
    num = models.IntegerField()
    ev_tst = models.IntegerField()
    h_ini = models.CharField(max_length=11)
    tipo = models.CharField(max_length=1)
    nombre = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    duracion = models.CharField(max_length=11)
    ev_cabs = models.IntegerField()
    rec_key = models.IntegerField()
    estado = models.IntegerField()
    hora_ms = models.IntegerField()
    rack = models.CharField(max_length=16, blank=True, null=True)
    fecha_aire = models.IntegerField()
    fecha_guia = models.IntegerField()
    archivo_fuente = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'guia_aa_oeste_cabs'


class GuiaAguascalientes13(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_aguascalientes_13'


class GuiaAlCabs(models.Model):
    num = models.IntegerField()
    ev_tst = models.IntegerField()
    h_ini = models.CharField(max_length=11)
    tipo = models.CharField(max_length=1)
    nombre = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    duracion = models.CharField(max_length=11)
    ev_cabs = models.IntegerField()
    rec_key = models.IntegerField()
    estado = models.IntegerField()
    hora_ms = models.IntegerField()
    rack = models.CharField(max_length=16, blank=True, null=True)
    fecha_aire = models.IntegerField()
    fecha_guia = models.IntegerField()
    archivo_fuente = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'guia_al_cabs'


class GuiaConc13(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()
    id_testigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guia_conc_13'


class GuiaConc7(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()
    id_testigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guia_conc_7'


class GuiaConcEast(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()
    id_testigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guia_conc_east'


class GuiaConcWest(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()
    id_testigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guia_conc_west'


class GuiaMonterrey13(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_monterrey_13'


class GuiaReal007(models.Model):
    fecha_aire = models.IntegerField()
    hora_aire = models.CharField(max_length=11)
    reconcile_key = models.CharField(max_length=8)
    rack_fuente = models.CharField(max_length=32, blank=True, null=True)
    titulo_louth = models.CharField(max_length=32, blank=True, null=True)
    nombre_optv = models.CharField(max_length=50, blank=True, null=True)
    hora_fin = models.CharField(max_length=11)
    estado_guia = models.IntegerField()
    estado_aire = models.IntegerField()
    guia_origen = models.CharField(max_length=12)
    ev_cabs = models.IntegerField(blank=True, null=True)
    ev_testi = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_real_007'


class GuiaSecundaria1(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_1'


class GuiaSecundaria10Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_10_aux'


class GuiaSecundaria11Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_11_aux'


class GuiaSecundaria12Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_12_aux'


class GuiaSecundaria13Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_13_aux'


class GuiaSecundaria14Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_14_aux'


class GuiaSecundaria15Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_15_aux'


class GuiaSecundaria16Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_16_aux'


class GuiaSecundaria17Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_17_aux'


class GuiaSecundaria18Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_18_aux'


class GuiaSecundaria19Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_19_aux'


class GuiaSecundaria1Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_1_aux'


class GuiaSecundaria2(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_2'


class GuiaSecundaria20Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_20_aux'


class GuiaSecundaria21Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_21_aux'


class GuiaSecundaria22Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_22_aux'


class GuiaSecundaria23Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_23_aux'


class GuiaSecundaria24Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_24_aux'


class GuiaSecundaria25Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_25_aux'


class GuiaSecundaria26Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_26_aux'


class GuiaSecundaria27Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_27_aux'


class GuiaSecundaria28Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_28_aux'


class GuiaSecundaria29Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_29_aux'


class GuiaSecundaria2Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_2_aux'


class GuiaSecundaria3(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_3'


class GuiaSecundaria30Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_30_aux'


class GuiaSecundaria31Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_31_aux'


class GuiaSecundaria32Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_32_aux'


class GuiaSecundaria33Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_33_aux'


class GuiaSecundaria34Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_34_aux'


class GuiaSecundaria35Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_35_aux'


class GuiaSecundaria3Aux(models.Model):
    evento_tst = models.BigIntegerField(primary_key=True)
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_3_aux'
        unique_together = (('evento_tst', 'fecha'),)


class GuiaSecundaria4(models.Model):
    evento_tst = models.BigIntegerField(primary_key=True)
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_4'
        unique_together = (('evento_tst', 'fecha'),)


class GuiaSecundaria4Aux(models.Model):
    evento_tst = models.BigIntegerField(primary_key=True)
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_4_aux'
        unique_together = (('evento_tst', 'fecha'),)


class GuiaSecundaria5(models.Model):
    evento_tst = models.BigIntegerField(primary_key=True)
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_5'
        unique_together = (('evento_tst', 'fecha'),)


class GuiaSecundaria5Aux(models.Model):
    evento_tst = models.BigIntegerField(primary_key=True)
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_5_aux'
        unique_together = (('evento_tst', 'fecha'),)


class GuiaSecundaria6(models.Model):
    evento_tst = models.BigIntegerField(primary_key=True)
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_6'
        unique_together = (('evento_tst', 'fecha'),)


class GuiaSecundaria6Aux(models.Model):
    evento_tst = models.BigIntegerField(primary_key=True)
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_6_aux'
        unique_together = (('evento_tst', 'fecha'),)


class GuiaSecundaria7Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_7_aux'


class GuiaSecundaria8Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_8_aux'


class GuiaSecundaria9Aux(models.Model):
    evento_tst = models.BigIntegerField()
    fecha = models.BigIntegerField()
    senal_detectada = models.CharField(max_length=128, blank=True, null=True)
    usuarios_detectados = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_secundaria_9_aux'


class GuiaTest0(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_0'


class GuiaTest100(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_100'


class GuiaTest101(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_101'


class GuiaTest105(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_105'


class GuiaTest108(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_108'


class GuiaTest109(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_109'


class GuiaTest110(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_110'


class GuiaTest111(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_111'


class GuiaTest114(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_114'


class GuiaTest115(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_115'


class GuiaTest118(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_118'


class GuiaTest119(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_119'


class GuiaTest12(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_12'


class GuiaTest121(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_121'


class GuiaTest122(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_122'


class GuiaTest123(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_123'


class GuiaTest126(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_126'


class GuiaTest127(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_127'


class GuiaTest128(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_128'


class GuiaTest129(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_129'


class GuiaTest131(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_131'


class GuiaTest132(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_132'


class GuiaTest133(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_133'


class GuiaTest134(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_134'


class GuiaTest135(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_135'


class GuiaTest136(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_136'


class GuiaTest137(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_137'


class GuiaTest138(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_138'


class GuiaTest139(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_139'


class GuiaTest140(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_140'


class GuiaTest141(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_141'


class GuiaTest142(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_142'


class GuiaTest143(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_143'


class GuiaTest144(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_144'


class GuiaTest145(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_145'


class GuiaTest146(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_146'


class GuiaTest147(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_147'


class GuiaTest148(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_148'


class GuiaTest149(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_149'


class GuiaTest15(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_15'


class GuiaTest150(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_150'


class GuiaTest151(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_151'


class GuiaTest154(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_154'


class GuiaTest155(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_155'


class GuiaTest156(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_156'


class GuiaTest157(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_157'


class GuiaTest158(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_158'


class GuiaTest159(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_159'


class GuiaTest160(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_160'


class GuiaTest163(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_163'


class GuiaTest164(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_164'


class GuiaTest165(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_165'


class GuiaTest166(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_166'


class GuiaTest167(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_167'


class GuiaTest168(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_168'


class GuiaTest169(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_169'


class GuiaTest170(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_170'


class GuiaTest171(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_171'


class GuiaTest172(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_172'


class GuiaTest173(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_173'


class GuiaTest174(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_174'


class GuiaTest175(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_175'


class GuiaTest178(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_178'


class GuiaTest179(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_179'


class GuiaTest180(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_180'


class GuiaTest181(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_181'


class GuiaTest182(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_182'


class GuiaTest183(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_183'


class GuiaTest184(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_184'


class GuiaTest185(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_185'


class GuiaTest186(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_186'


class GuiaTest187(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_187'


class GuiaTest188(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_188'


class GuiaTest189(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_189'


class GuiaTest190(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_190'


class GuiaTest191(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_191'


class GuiaTest194(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_194'


class GuiaTest195(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_195'


class GuiaTest203(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_203'


class GuiaTest207(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_207'


class GuiaTest212(models.Model):
    numero_ev = models.IntegerField(primary_key=True)
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_212'
        unique_together = (('numero_ev', 'fecha'),)


class GuiaTest213(models.Model):
    numero_ev = models.IntegerField(primary_key=True)
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_213'
        unique_together = (('numero_ev', 'fecha'),)


class GuiaTest216(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_216'


class GuiaTest217(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_217'


class GuiaTest218(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_218'


class GuiaTest219(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_219'


class GuiaTest26(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_26'


class GuiaTest31(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_31'


class GuiaTest32(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_32'


class GuiaTest33(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_33'


class GuiaTest34(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_34'


class GuiaTest35(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_35'


class GuiaTest36(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_36'


class GuiaTest37(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_37'


class GuiaTest38(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_38'


class GuiaTest39(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_39'


class GuiaTest40(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_40'


class GuiaTest401(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_401'


class GuiaTest403(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_403'


class GuiaTest41(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_41'


class GuiaTest43(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_43'


class GuiaTest44(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_44'


class GuiaTest45(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_45'


class GuiaTest46(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_46'


class GuiaTest47(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_47'


class GuiaTest48(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_48'


class GuiaTest49(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_49'


class GuiaTest50(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_50'


class GuiaTest51(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_51'


class GuiaTest52(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_52'


class GuiaTest520(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_520'


class GuiaTest521(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_521'


class GuiaTest522(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_522'


class GuiaTest525(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_525'


class GuiaTest527(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_527'


class GuiaTest53(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_53'


class GuiaTest532(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_532'


class GuiaTest535(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_535'


class GuiaTest54(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_54'


class GuiaTest549(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_549'


class GuiaTest55(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_55'


class GuiaTest554(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_554'


class GuiaTest56(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_56'


class GuiaTest560(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_560'


class GuiaTest567(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_567'


class GuiaTest57(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_57'


class GuiaTest574(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_574'


class GuiaTest575(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_575'


class GuiaTest576(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_576'


class GuiaTest577(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_577'


class GuiaTest578(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_578'


class GuiaTest579(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_579'


class GuiaTest58(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_58'


class GuiaTest581(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_581'


class GuiaTest582(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_582'


class GuiaTest585(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_585'


class GuiaTest588(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_588'


class GuiaTest589(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_589'


class GuiaTest59(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_59'


class GuiaTest60(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_60'


class GuiaTest601(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_601'


class GuiaTest602(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_602'


class GuiaTest61(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_61'


class GuiaTest62(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_62'


class GuiaTest63(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_63'


class GuiaTest64(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_64'


class GuiaTest65(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_65'


class GuiaTest66(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_66'


class GuiaTest67(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_67'


class GuiaTest68(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_68'


class GuiaTest69(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_69'


class GuiaTest70(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_70'


class GuiaTest71(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_71'


class GuiaTest72(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_72'


class GuiaTest74(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_74'


class GuiaTest75(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_75'


class GuiaTest76(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_76'


class GuiaTest77(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_77'


class GuiaTest78(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_78'


class GuiaTest79(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_79'


class GuiaTest80(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_80'


class GuiaTest81(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_81'


class GuiaTest82(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_82'


class GuiaTest83(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_83'


class GuiaTest836(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_836'


class GuiaTest84(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_84'


class GuiaTest85(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_85'


class GuiaTest86(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_86'


class GuiaTest87(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_87'


class GuiaTest88(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_88'


class GuiaTest89(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_89'


class GuiaTest90(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_90'


class GuiaTest91(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_91'


class GuiaTest92(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_92'


class GuiaTest93(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_93'


class GuiaTest94(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_94'


class GuiaTest95(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_95'


class GuiaTest96(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_96'


class GuiaTest97(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_97'


class GuiaTest973(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_973'


class GuiaTest974(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_974'


class GuiaTest975(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_975'


class GuiaTest976(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_976'


class GuiaTest977(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_977'


class GuiaTest978(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_978'


class GuiaTest979(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_979'


class GuiaTest98(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_98'


class GuiaTest981(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_981'


class GuiaTest982(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_982'


class GuiaTest985(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_985'


class GuiaTest986(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_986'


class GuiaTest989(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_989'


class GuiaTest99(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)
    comando_cabs = models.IntegerField(blank=True, null=True)
    num_paquete_cabs = models.IntegerField(blank=True, null=True)
    eventos_cabs = models.IntegerField(blank=True, null=True)
    videos_cabs = models.IntegerField(blank=True, null=True)
    codigo_cabs = models.CharField(max_length=12, blank=True, null=True)
    tx_c_cabs = models.BigIntegerField(blank=True, null=True)
    sen_ocasional = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'guia_test_99'


class GuiaTestPrueba(models.Model):
    numero_ev = models.IntegerField()
    hora_inicio = models.IntegerField()
    tipo_evento = models.IntegerField()
    cliente = models.CharField(max_length=256, blank=True, null=True)
    version = models.CharField(max_length=256, blank=True, null=True)
    duracion = models.IntegerField()
    no_rack = models.IntegerField()
    fecha = models.BigIntegerField()
    evento_testigos = models.IntegerField(blank=True, null=True)
    cruce_guia = models.IntegerField(blank=True, null=True)
    evento_cabs = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guia_test_prueba'


class ListaDestinosFtp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    dir_ip = models.CharField(max_length=15)
    puerto = models.BigIntegerField()
    usuario = models.CharField(max_length=64)
    clave = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=256, blank=True, null=True)
    directorio_remoto = models.CharField(max_length=128, blank=True, null=True)
    enabled = models.BooleanField()
    tipo = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'lista_destinos_ftp'


class ListaLocales(models.Model):
    nombre_testigo = models.CharField(max_length=50)
    id_testigo = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'lista_locales'


class ListaTestigos(models.Model):
    indice = models.IntegerField(unique=True)
    nombre_testigo = models.CharField(max_length=50, blank=True, null=True)
    id_testigo = models.IntegerField(unique=True)
    id_guia = models.CharField(max_length=25, blank=True, null=True)
    id_tx = models.IntegerField(blank=True, null=True)
    id_cadena = models.IntegerField(blank=True, null=True)
    canal_local = models.IntegerField(blank=True, null=True)
    nombre_tabla = models.CharField(max_length=25, blank=True, null=True)
    direccion_servidor = models.CharField(max_length=15, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=24, blank=True, null=True)
    clave_usuario = models.CharField(max_length=24, blank=True, null=True)
    ruta_videos = models.CharField(max_length=255, blank=True, null=True)
    ruta_videos2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_guia = models.IntegerField(blank=True, null=True)
    tipo_sec = models.IntegerField(blank=True, null=True)
    grupo_testigos = models.IntegerField(blank=True, null=True)
    tipo_despliegue = models.IntegerField(blank=True, null=True)
    tst_state = models.BigIntegerField(blank=True, null=True)
    id_calidad = models.IntegerField(blank=True, null=True)
    tabla_guia = models.CharField(max_length=64, blank=True, null=True)
    info_respaldo = models.IntegerField()
    ruta_videos3 = models.CharField(max_length=255, blank=True, null=True)
    desfase_hora = models.IntegerField(blank=True, null=True)
    desfase_grabador_ms = models.IntegerField(blank=True, null=True)
    monitoreo_llegada = models.IntegerField(blank=True, null=True)
    id_monitor = models.IntegerField(blank=True, null=True)
    ip_grabador = models.CharField(max_length=15, blank=True, null=True)
    tipo_mux = models.IntegerField(blank=True, null=True)
    siglas = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_testigos'


class MonitoreoTestigosE(models.Model):
    fecha_guia = models.IntegerField(primary_key=True)
    id_tst = models.IntegerField()
    codigo_error = models.BigIntegerField()
    hora_deteccion = models.BigIntegerField(blank=True, null=True)
    hora_exito = models.BigIntegerField(blank=True, null=True)
    ultima_verificacion = models.BigIntegerField(blank=True, null=True)
    conocimiento = models.NullBooleanField()
    msg_alerta_cc = models.BigIntegerField(blank=True, null=True)
    evento = models.BigIntegerField()
    ultimo_msg = models.BigIntegerField(blank=True, null=True)
    duracion_esperada = models.BigIntegerField(blank=True, null=True)
    duracion_video = models.BigIntegerField(blank=True, null=True)
    duracion_audio = models.BigIntegerField(blank=True, null=True)
    tamanio = models.BigIntegerField(blank=True, null=True)
    hora_transmision = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitoreo_testigos_e'
        unique_together = (('fecha_guia', 'id_tst', 'evento'),)


class MontestConcentradoError(models.Model):
    id_test = models.IntegerField(primary_key=True)
    total_err_dur = models.IntegerField(blank=True, null=True)
    total_err_ne = models.IntegerField(blank=True, null=True)
    total_err_tam = models.IntegerField(blank=True, null=True)
    fecha = models.IntegerField()
    ult_vid = models.IntegerField(blank=True, null=True)
    revisados = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'montest_concentrado_error'
        unique_together = (('id_test', 'fecha'),)


class MontestDetalleError(models.Model):
    num_ev = models.IntegerField(primary_key=True)
    fecha = models.IntegerField()
    tam = models.IntegerField(blank=True, null=True)
    dur = models.IntegerField(blank=True, null=True)
    tipo_err = models.IntegerField()
    id_testigo = models.IntegerField()
    revisado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'montest_detalle_error'
        unique_together = (('num_ev', 'fecha', 'id_testigo'),)


class PerfilesDestinos(models.Model):
    id_perfil = models.ForeignKey(CatPerfiles, models.DO_NOTHING, db_column='id_perfil', primary_key=True)
    id_destino = models.ForeignKey(ListaDestinosFtp, models.DO_NOTHING, db_column='id_destino')

    class Meta:
        managed = False
        db_table = 'perfiles_destinos'
        unique_together = (('id_perfil', 'id_destino'),)


class PeticionesExporta(models.Model):
    red = models.IntegerField(blank=True, null=True)
    fecha = models.IntegerField(blank=True, null=True)
    programa = models.IntegerField(blank=True, null=True)
    pos_guia = models.CharField(max_length=512, blank=True, null=True)
    fecha_ingreso = models.IntegerField(blank=True, null=True)
    fecha_termino = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    senal = models.IntegerField(blank=True, null=True)
    cortador = models.IntegerField(blank=True, null=True)
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'peticiones_exporta'


class PeticionesGuia(models.Model):
    fecha_peticion = models.IntegerField(blank=True, null=True)
    fecha_guia = models.IntegerField(primary_key=True)
    id_testigo = models.IntegerField()
    estado = models.IntegerField(blank=True, null=True)
    pos_ini = models.IntegerField(blank=True, null=True)
    pos_fin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peticiones_guia'
        unique_together = (('fecha_guia', 'id_testigo'),)


class ProgramasExporta(models.Model):
    id = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    abreviatura = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programas_exporta'


class SoporteReportes(models.Model):
    nombre_inge_abre = models.CharField(max_length=30, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    area = models.CharField(max_length=30, blank=True, null=True)
    aplicacion = models.CharField(max_length=30, blank=True, null=True)
    descrip_problema = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    nombre_inge_cierra = models.CharField(max_length=30, blank=True, null=True)
    numero_reporte = models.IntegerField(primary_key=True)
    solucion_problema = models.CharField(max_length=255, blank=True, null=True)
    hora_apertura = models.CharField(max_length=10, blank=True, null=True)
    hora_cierre = models.CharField(max_length=10, blank=True, null=True)
    fecha_apertura = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'soporte_reportes'


class TestigoHuecoMaterial(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    id_testigo = models.IntegerField()
    evento_inicio = models.IntegerField(blank=True, null=True)
    evento_fin = models.IntegerField(blank=True, null=True)
    hora_inicio = models.CharField(max_length=20, blank=True, null=True)
    hora_fin = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigo_hueco_material'


class Testigos0001(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0001'


class Testigos0002(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0002'


class Testigos0003(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0003'


class Testigos0004(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0004'


class Testigos0007(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0007'


class Testigos0012(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0012'


class Testigos0013(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0013'


class Testigos0014(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0014'


class Testigos0015(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0015'


class Testigos0019(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0019'


class Testigos0020(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0020'


class Testigos0021(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0021'


class Testigos0022(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0022'


class Testigos0023(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0023'


class Testigos0024(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0024'


class Testigos0025(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0025'


class Testigos0030(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0030'


class Testigos0040(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0040'


class Testigos0041(models.Model):
    id_video = models.CharField(primary_key=True, max_length=24)
    nom_video = models.CharField(max_length=32, blank=True, null=True)
    fecha_archivo = models.IntegerField(blank=True, null=True)
    hora_archivo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    cuadros_video = models.IntegerField()
    tam_arch_bajo = models.IntegerField()
    tam_arch_alto = models.IntegerField()
    pista_fecha = models.CharField(max_length=64, blank=True, null=True)
    timecode_aire = models.CharField(max_length=16, blank=True, null=True)
    codec_video = models.CharField(max_length=16, blank=True, null=True)
    codec_audio = models.CharField(max_length=16, blank=True, null=True)
    id_red = models.IntegerField(blank=True, null=True)
    evento_guia = models.IntegerField(blank=True, null=True)
    muestreo_audio = models.IntegerField(blank=True, null=True)
    video_tam_vertical = models.IntegerField(blank=True, null=True)
    video_tam_horiz = models.IntegerField(blank=True, null=True)
    razon_bits_vid = models.IntegerField(blank=True, null=True)
    razon_bits_aud = models.IntegerField(blank=True, null=True)
    cuadros_x_seg = models.IntegerField(blank=True, null=True)
    razon_bits = models.IntegerField(blank=True, null=True)
    fecha_aire = models.IntegerField(blank=True, null=True)
    hora_aire = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    estado_desc = models.CharField(max_length=25, blank=True, null=True)
    fecha_registro = models.IntegerField(blank=True, null=True)
    checksum = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_0041'


class TestigosAcapulco(models.Model):
    indice = models.IntegerField()
    nombre_testigo = models.CharField(max_length=50, blank=True, null=True)
    id_testigo = models.IntegerField()
    id_guia = models.CharField(max_length=25, blank=True, null=True)
    id_tx = models.IntegerField(blank=True, null=True)
    id_cadena = models.IntegerField(blank=True, null=True)
    canal_local = models.IntegerField(blank=True, null=True)
    nombre_tabla = models.CharField(max_length=25, blank=True, null=True)
    direccion_servidor = models.CharField(max_length=15, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=24, blank=True, null=True)
    clave_usuario = models.CharField(max_length=24, blank=True, null=True)
    ruta_videos = models.CharField(max_length=255, blank=True, null=True)
    ruta_videos2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_guia = models.IntegerField(blank=True, null=True)
    tipo_sec = models.IntegerField(blank=True, null=True)
    grupo_testigos = models.IntegerField(blank=True, null=True)
    tipo_despliegue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_acapulco'


class TestigosCiudadJuarez(models.Model):
    indice = models.IntegerField()
    nombre_testigo = models.CharField(max_length=50, blank=True, null=True)
    id_testigo = models.IntegerField()
    id_guia = models.CharField(max_length=25, blank=True, null=True)
    id_tx = models.IntegerField(blank=True, null=True)
    id_cadena = models.IntegerField(blank=True, null=True)
    canal_local = models.IntegerField(blank=True, null=True)
    nombre_tabla = models.CharField(max_length=25, blank=True, null=True)
    direccion_servidor = models.CharField(max_length=15, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=24, blank=True, null=True)
    clave_usuario = models.CharField(max_length=24, blank=True, null=True)
    ruta_videos = models.CharField(max_length=255, blank=True, null=True)
    ruta_videos2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_guia = models.IntegerField(blank=True, null=True)
    tipo_sec = models.IntegerField(blank=True, null=True)
    grupo_testigos = models.IntegerField(blank=True, null=True)
    tipo_despliegue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_ciudad_juarez'


class TestigosDeportes(models.Model):
    indice = models.IntegerField()
    nombre_testigo = models.CharField(max_length=50, blank=True, null=True)
    id_testigo = models.IntegerField()
    id_guia = models.CharField(max_length=25, blank=True, null=True)
    id_tx = models.IntegerField(blank=True, null=True)
    id_cadena = models.IntegerField(blank=True, null=True)
    canal_local = models.IntegerField(blank=True, null=True)
    nombre_tabla = models.CharField(max_length=25, blank=True, null=True)
    direccion_servidor = models.CharField(max_length=15, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=24, blank=True, null=True)
    clave_usuario = models.CharField(max_length=24, blank=True, null=True)
    ruta_videos = models.CharField(max_length=255, blank=True, null=True)
    ruta_videos2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_guia = models.IntegerField(blank=True, null=True)
    tipo_sec = models.IntegerField(blank=True, null=True)
    grupo_testigos = models.IntegerField(blank=True, null=True)
    tipo_despliegue = models.IntegerField(blank=True, null=True)
    envio_edicion = models.IntegerField(blank=True, null=True)
    ruta_ar1 = models.CharField(max_length=255, blank=True, null=True)
    ruta_ar2 = models.CharField(max_length=255, blank=True, null=True)
    ruta_ar3 = models.CharField(max_length=255, blank=True, null=True)
    ruta_ar4 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_deportes'


class TestigosGuadalajara(models.Model):
    indice = models.IntegerField()
    nombre_testigo = models.CharField(max_length=50, blank=True, null=True)
    id_testigo = models.IntegerField()
    id_guia = models.CharField(max_length=25, blank=True, null=True)
    id_tx = models.IntegerField(blank=True, null=True)
    id_cadena = models.IntegerField(blank=True, null=True)
    canal_local = models.IntegerField(blank=True, null=True)
    nombre_tabla = models.CharField(max_length=25, blank=True, null=True)
    direccion_servidor = models.CharField(max_length=15, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=24, blank=True, null=True)
    clave_usuario = models.CharField(max_length=24, blank=True, null=True)
    ruta_videos = models.CharField(max_length=255, blank=True, null=True)
    ruta_videos2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_guia = models.IntegerField(blank=True, null=True)
    tipo_sec = models.IntegerField(blank=True, null=True)
    grupo_testigos = models.IntegerField(blank=True, null=True)
    tipo_despliegue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_guadalajara'


class TestigosGuatemala(models.Model):
    indice = models.IntegerField()
    nombre_testigo = models.CharField(max_length=50, blank=True, null=True)
    id_testigo = models.IntegerField()
    id_guia = models.CharField(max_length=25, blank=True, null=True)
    id_tx = models.IntegerField(blank=True, null=True)
    id_cadena = models.IntegerField(blank=True, null=True)
    canal_local = models.IntegerField(blank=True, null=True)
    nombre_tabla = models.CharField(max_length=25, blank=True, null=True)
    direccion_servidor = models.CharField(max_length=15, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=24, blank=True, null=True)
    clave_usuario = models.CharField(max_length=24, blank=True, null=True)
    ruta_videos = models.CharField(max_length=255, blank=True, null=True)
    ruta_videos2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_guia = models.IntegerField(blank=True, null=True)
    tipo_sec = models.IntegerField(blank=True, null=True)
    grupo_testigos = models.IntegerField(blank=True, null=True)
    tipo_despliegue = models.IntegerField(blank=True, null=True)
    tst_state = models.BigIntegerField(blank=True, null=True)
    id_calidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_guatemala'


class TestigosMorelia(models.Model):
    indice = models.IntegerField()
    nombre_testigo = models.CharField(max_length=50, blank=True, null=True)
    id_testigo = models.IntegerField()
    id_guia = models.CharField(max_length=25, blank=True, null=True)
    id_tx = models.IntegerField(blank=True, null=True)
    id_cadena = models.IntegerField(blank=True, null=True)
    canal_local = models.IntegerField(blank=True, null=True)
    nombre_tabla = models.CharField(max_length=25, blank=True, null=True)
    direccion_servidor = models.CharField(max_length=15, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=24, blank=True, null=True)
    clave_usuario = models.CharField(max_length=24, blank=True, null=True)
    ruta_videos = models.CharField(max_length=255, blank=True, null=True)
    ruta_videos2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_guia = models.IntegerField(blank=True, null=True)
    tipo_sec = models.IntegerField(blank=True, null=True)
    grupo_testigos = models.IntegerField(blank=True, null=True)
    tipo_despliegue = models.IntegerField(blank=True, null=True)
    tst_state = models.BigIntegerField(blank=True, null=True)
    id_calidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_morelia'


class TestigosPcs(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=80)
    ip_remota = models.CharField(max_length=15)
    ruta_mapeo = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'testigos_pcs'


class TestigosTepic(models.Model):
    indice = models.IntegerField()
    nombre_testigo = models.CharField(max_length=50, blank=True, null=True)
    id_testigo = models.IntegerField()
    id_guia = models.CharField(max_length=25, blank=True, null=True)
    id_tx = models.IntegerField(blank=True, null=True)
    id_cadena = models.IntegerField(blank=True, null=True)
    canal_local = models.IntegerField(blank=True, null=True)
    nombre_tabla = models.CharField(max_length=25, blank=True, null=True)
    direccion_servidor = models.CharField(max_length=15, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=24, blank=True, null=True)
    clave_usuario = models.CharField(max_length=24, blank=True, null=True)
    ruta_videos = models.CharField(max_length=255, blank=True, null=True)
    ruta_videos2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_guia = models.IntegerField(blank=True, null=True)
    tipo_sec = models.IntegerField(blank=True, null=True)
    grupo_testigos = models.IntegerField(blank=True, null=True)
    tipo_despliegue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_tepic'


class TestigosTorreon(models.Model):
    indice = models.IntegerField()
    nombre_testigo = models.CharField(max_length=50, blank=True, null=True)
    id_testigo = models.IntegerField()
    id_guia = models.CharField(max_length=25, blank=True, null=True)
    id_tx = models.IntegerField(blank=True, null=True)
    id_cadena = models.IntegerField(blank=True, null=True)
    canal_local = models.IntegerField(blank=True, null=True)
    nombre_tabla = models.CharField(max_length=25, blank=True, null=True)
    direccion_servidor = models.CharField(max_length=15, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=24, blank=True, null=True)
    clave_usuario = models.CharField(max_length=24, blank=True, null=True)
    ruta_videos = models.CharField(max_length=255, blank=True, null=True)
    ruta_videos2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_guia = models.IntegerField(blank=True, null=True)
    tipo_sec = models.IntegerField(blank=True, null=True)
    grupo_testigos = models.IntegerField(blank=True, null=True)
    tipo_despliegue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testigos_torreon'


class UsuarioCorreoAnalisis(models.Model):
    usuario = models.CharField(max_length=256, blank=True, null=True)
    correo = models.CharField(max_length=128, blank=True, null=True)
    tipo_destino = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_correo_analisis'


class UsuarioCorreoAnalisisAza(models.Model):
    usuario = models.CharField(max_length=256, blank=True, null=True)
    correo = models.CharField(max_length=128, blank=True, null=True)
    tipo_destino = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_correo_analisis_aza'


class UsuariosContinuidad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    usuario = models.CharField(max_length=256)
    correo = models.CharField(max_length=128, blank=True, null=True)
    celular = models.CharField(max_length=128, blank=True, null=True)
    tipo_destino = models.IntegerField(blank=True, null=True)
    enabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'usuarios_continuidad'


class UsuariosContinuidadAza(models.Model):
    id = models.BigIntegerField(primary_key=True)
    usuario = models.CharField(max_length=256)
    correo = models.CharField(max_length=128, blank=True, null=True)
    celular = models.CharField(max_length=128, blank=True, null=True)
    tipo_destino = models.IntegerField(blank=True, null=True)
    enabled = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'usuarios_continuidad_aza'


class UsuariosContinuidadTx(models.Model):
    id_usuario_continuidad = models.ForeignKey(UsuariosContinuidad, models.DO_NOTHING, db_column='id_usuario_continuidad')
    id_transmisor = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios_continuidad_tx'


class UsuariosContinuidadTxAza(models.Model):
    id_usuario_continuidad = models.BigIntegerField()
    id_transmisor = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios_continuidad_tx_aza'


class UsuariosTestigos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    usuario = models.CharField(unique=True, max_length=16)
    nombre_real = models.CharField(max_length=128, blank=True, null=True)
    activo = models.NullBooleanField()
    permisos = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_testigos'


class VideoTestigo(models.Model):
    fecha_guia = models.BigIntegerField(blank=True, null=True)
    id_tst = models.BigIntegerField(blank=True, null=True)
    evento_cabs = models.BigIntegerField(blank=True, null=True)
    evento_tst = models.BigIntegerField(blank=True, null=True)
    duracion_esperada = models.BigIntegerField(blank=True, null=True)
    duracion_video = models.BigIntegerField(blank=True, null=True)
    duracion_audio = models.BigIntegerField(blank=True, null=True)
    tamanio_arch = models.BigIntegerField(blank=True, null=True)
    nombre_arch = models.CharField(max_length=20, blank=True, null=True)
    existe_testigo = models.BigIntegerField(blank=True, null=True)
    error_cc = models.BigIntegerField(blank=True, null=True)
    ultima_verificacion = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_testigo'


class VideosTestigos(models.Model):
    id_testigo = models.IntegerField(primary_key=True)
    fecha = models.IntegerField()
    evento = models.IntegerField()
    duracion = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    tam = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'videos_testigos'
        unique_together = (('id_testigo', 'evento', 'fecha'),)
