$(document).ready(function(){
 $("#submitLike").click(function(){
    var id_image = $("#idimage_").val();

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
        url: "/like",
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
