/**
 * Created by Jose Daniel Hernandez Osorio - isc.danielosorio@hotmail.com -
 * Ingeniero en Sistemas Copmutacionales.
 *
 *
 * https://github.com/brillout/awesome-angular-components
 * https://github.com/DataTorrent/malhar-angular-widgets
 *
 */

var datatable;
var datatabledatails;

$(document).ready(
    function () {

        $("#list_red").change(function () {
            var data = getTypeRed();
            if (null != data) {
                update(search());
            }
        });

        $("#list_error").change(function () {
            var data = getTypeError();
            if (null != data) {
                update(search());
            }
        });

        $("#list_alert").change(function () {
            var data = getLevelAlert();
            if (null != data) {
                update(search());
            }
        });

        $('.combobox').combobox();

        $('.form_date').datetimepicker({
            language: 'es',
            weekStart: 1,
            todayBtn: 1,
            autoclose: 1,
            startView: 2,
            minView: 2
        }).datetimepicker("setDate", new Date()).datetimepicker(
            'setStartDate', '2016-11-01').datetimepicker('setEndDate', new Date()).on('changeDate', function (ev) {
            update(search());
        });

        var data = search();
        update(data);

        var row_danger;
        var row;

        $('#datatable tbody').on('click', 'tr', function () {
            if ($(this).hasClass('selected')) {
                $(row_danger).removeClass('selected');
                $(row_danger).addClass('table-info');
                $(row).removeClass('selected');
                $(row).addClass('table-info');
                var data = datatable.row(this).data();
                $("#modalViewDetails").modal('show');
                var number = data['ID'];
                var datatemporary = searchDetails(number);
                console.log('viewdetails ' + datatemporary);
                showDetails(datatemporary);
            } else {
                $(row_danger).removeClass('table-info');
                $(row).removeClass('table-info');
                $(row_danger).addClass('table-danger');
                if ($(this).hasClass('table-danger')) {
                    row_danger = this;
                    row = null
                    $(this).removeClass('table-danger');
                    datatable.$('tr.selected').removeClass('selected');
                    $(this).addClass('selected');
                } else {
                    row = this;
                    row_danger = null;
                    datatable.$('tr.selected').removeClass('selected');
                    $(this).addClass('selected');
                }
            }
        });

        datatable.on('draw', function () {
            var body = $(datatable.table().body());
            body.unhighlight();
            body.highlight(datatable.search());
        });

        setInterval(function () {
            var datatemporary = search();
            console.log('viewfinder ' + datatemporary);
            update(datatemporary);
        }, 600000);

    });

function update(datas) {

    var number = 0;

    var table = $('#datatable').DataTable();
    table.destroy();

    datatable = $('#datatable').DataTable({
        "language": {
            select: {
                rows: {
                    _: "%d filas seleccionadas",
                    0: "Haga click en la fila para seleccionar",
                    1: "1 fila seleccionada"
                }
            },
            "url": "https://cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
        },
        "searchHighlight": true,
        "scrollX": true,
        "select": true,
        "bLengthChange": false,
        "processing": true,
        "data": datas,
        "pageLength": 20,
        "createdRow": function (row, data, dataIndex) {
            number = number + 1;
            if ((data["TOTAL"] - data["REVISADOS"]) > 10)
                $(row).addClass('table-danger');
        },
        "sDom": '<"row"<"col-sm-3 text-center"f><"col-sm-9 text-center"p>>rti',
        "columns": [
            {"data": "NO"},
            {"data": "NOMBRE"},
            {"data": "ID"},
            {"data": "MUX"},
            {"data": "DURACION"},
            {"data": "NOLLEGAN"},
            {"data": "TAMANO"},
            {"data": "TOTAL"},
            {"data": "REVISADOS"},
            {"data": "ULTIMO"}
        ],
        "columnDefs": [{
            className: "text-center folio",
            "targets": [0],
            "width": "5%"
        }, {
            className: "text-center",
            "targets": [1],
            "width": "50%"
        }, {
            className: "text-center",
            "targets": [2],
            "width": "8%"
        }, {
            className: "text-center",
            "targets": [3],
            "width": "8%"
        }, {
            className: "text-center",
            "targets": [4],
            "width": "10%"
        }, {
            className: "text-center",
            "targets": [5],
            "width": "17%"
        }, {
            className: "text-center",
            "targets": [6],
            "width": "7%"
        }, {
            className: "text-center",
            "targets": [7],
            "width": "8%"
        }, {
            className: "text-center",
            "targets": [8],
            "width": "10%"
        }, {
            className: "text-center",
            "targets": [9],
            "width": "10%"
        }],
        "select": {
            style: "single"
        },
        "order": [[1, "asc"]]
    });
}

function showDetails(datas) {

    var table = $('#datatabledatails').DataTable();
    table.destroy();

    datatabledatails = $('#datatabledatails').DataTable({
        "language": {
            "url": "https://cdn.datatables.net/plug-ins/1.10.15/i18n/Spanish.json"
        },
        "bLengthChange": false,
        "bFilter": false,
        "processing": true,
        "bInfo": true,
        "data": datas,
        "pageLength": 8,
        "createdRow": function (row, data, dataIndex) {
            if (data["REVISADO"] == "NO") {
                $(row).addClass('table-danger');
            }
            $('#title').text(data["NOMBRE"]);
            $('#ip').text(" IP Grabador:  " + data["IP"]);
            $('#shared').text(" Compartido:  " + data["RUTA"]);
            var value = data["MUX"]
            if (value == "1")
                $('#type').text(" Tipo Multiplexor:  D2MUX");
            if (value == "2")
                $('#type').text(" Tipo Multiplexor:  DTP");
            if (value == "3")
                $('#type').text(" Tipo Multiplexor:  NE");
            $('#acronym').text(" Siglas:  " + data["SIGLAS"])
        },
        "columns": [
            {"data": "NO"},
            {"data": "NUM_EVENTO"},
            {"data": "DURACION"},
            {"data": "TAMANO"},
            {"data": "TIPO_ERROR"},
            {"data": "REVISADO"},
            {"data": "DESCARGAR"}
        ],
        "columnDefs": [{
            className: "text-center folio",
            "targets": [0]
        }, {
            className: "text-center",
            "targets": [1]
        }, {
            className: "text-center",
            "targets": [2]
        }, {
            className: "text-center",
            "targets": [3]
        }, {
            className: "text-center",
            "targets": [4]
        }, {
            className: "text-center",
            "targets": [5]
        }, {
            className: "text-center",
            "targets": [6],
            "data": null,
            "defaultContent": "<a href=\"#\" class=\"alert-link\">Descargar</a>."
        }],
        "order": [[1, "asc"]]
    });

}

function search() {
    return JSON.parse($.ajax({
        type: "GET",
        url: "json_00010",
        data: {
            type_network: getTypeRed(),
            type_error: getTypeError(),
            level_alert: getLevelAlert(),
            date_monitoring: getDateMonitoring()
        },
        dataType: 'json',
        async: false,
        success: function (data) {
            return data;
        }
    }).responseText);
}

function searchDetails(id_testigo) {
    return JSON.parse($.ajax({
        type: "GET",
        url: "json_00020",
        data: {
            id_testigo: id_testigo,
            date_monitoring: getDateMonitoring()
        },
        dataType: 'json',
        async: false,
        success: function (data) {
            return data;
        }
    }).responseText);
}

function checkTestigo(id_testigo, check) {
    $.ajax({
        type: "GET",
        url: "datecheck",
        data: {
            id_testigo: id_testigo,
            check: check,
            date_monitoring: getDateMonitoring()
        },
        async: false,
        success: function (data) {
            if (data["result1"] != 0 && data["result2"] != 0) {
                alert("Se ha realizado la revicion del testigo.");
                buttonUpdate();
            } else {
                alert("Posiblemente existe un error con la conexion de la base de datos.");
            }
        }
    });
}

function getTypeRed() {
    var date = $('select[id=list_red]').val();
    return date;
}

function getTypeError() {
    var date = $('select[id=list_error]').val();
    return date;
}

function getLevelAlert() {
    var date = $('select[id=list_alert]').val();
    return date;
}

function getDateMonitoring() {
    var seldate = $('.form_date').datetimepicker('getDate');
    seldate = seldate.getDate() + "-" + (seldate.getMonth() + 1) + "-" + seldate.getFullYear();
    return seldate;
}

function buttonUpdate() {
    datatemporary = search();
    console.log(datatemporary);
    update(datatemporary);
}

function buttonCheck() {
    var data = datatable.row('.selected').data();
    if (data != null) {
        var id = data['ID'];
        var all = data['TOTAL'];
        checkTestigo(id, all, getDateMonitoring());
    } else {
        alert("Debera de selecionar un Testigo");
    }
}

