$(document).ready(function(){
 $("#deletePic").click(function(){
    var id_image = $("#idimage").val();
    var autor = $("#autor").val();

    // Returns successful data submission message when the entered information is stored in database.
    var dataString = 'id=' + id_image + '&autor=' + autor;
    if(id_image=='' || autor=='')
    {
    alert("An error ocurred");
    }
    else
    {
    // AJAX Code To Submit Form.
    $.ajax({
        type: "POST",
        url: "/deletePic",
        data: dataString,
        cache: false,
            success: function(){
                window.location.replace("/main");
            }
        });
    }
    return false;
    });
});

