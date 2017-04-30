$(document).ready(function(){
 $("#submitComment").click(function(){
    var name = $("#comment").val();
    var id_image = $("#id_image").val();

    // Returns successful data submission message when the entered information is stored in database.
    var dataString = 'comment='+ name +'&id=' + id_image;
    if(name=='' || id_image=='')
    {
    alert("An error ocurred");
    }
    else
    {
    // AJAX Code To Submit Form.
    $.ajax({
        type: "POST",
        url: "/comment",
        data: dataString,
        cache: false,
            success: function(data){
                location.reload();
            }
        });
    }
    return false;
    });
});
