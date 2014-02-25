$(document).ready(function(){
    $("#tinymce").keypress(function(){
        console.log("xd")
    });
    var mensaje = $($("#id_mensaje").text()).text();

    //console.log($(mensaje).text())
    console.log(mensaje)
})

