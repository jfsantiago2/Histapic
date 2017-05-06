$(document).ready(function(){
 $("#submitUnlike").click(function(){
    var id_image = $("#id_image_").val();

    // Returns successful data submission message when the entered information is stored in database.
    var dataString = 'id=' + id_image;
    if(id_image=='')
    {
    return false;
    }
    else
    {
    // AJAX Code To Submit Form.
    $.ajax({
        type: "POST",
        url: "/unlike",
        data: dataString,
        cache: false,
            success: function(){
                $( '#for-reload' ).load('#for-reload');
            }
        });
    }
    return false;
    });
});
