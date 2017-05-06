$(document).ready(function(){
    $("#submitUnfollow").click(function(){
    var name = $("#unfollow").val();

    // Returns successful data submission message when the entered information is stored in database.
    var dataString = 'unfollow='+ name;
    if(name=='')
    {
    alert("An error ocurred");
    }
    else
    {
    // AJAX Code To Submit Form.
    $.ajax({
        type: "POST",
        url: "/unfollow",
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