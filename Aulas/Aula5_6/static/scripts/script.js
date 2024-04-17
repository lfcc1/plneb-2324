
function delete_conceito(designacao){

    $.ajax({ 
        url: '/delete/' + designacao, 
        type: 'DELETE', 
        success: function (result) { 
        } 
    }); 
}

$(document).ready( function () {
    $('#myTable').DataTable();
} );







$(document).ready( function () {
    $('#myTable').DataTable();
} );


function delete_conceito(conceito) {
    return alert(conceito);
}