$(document).ready(function(){
    $("#submitFollow").click(function(){
        var name = $("#follow").val();

    // Returns successful data submission message when the entered information is stored in database.
    var dataString = 'follow='+ name;
    if(name=='')
    {
    alert("An error ocurred");
    }
    else
    {
    // AJAX Code To Submit Form.
    $.ajax({
        type: "POST",
        url: "/follow",
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