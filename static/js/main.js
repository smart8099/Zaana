

setTimeout(function(){
    $('#message').fadeOut('slow');
}, 2000) 

$(document).ready(function(){
    $('table td').click(function(){
       alert($(this).html());
    });
    
    });