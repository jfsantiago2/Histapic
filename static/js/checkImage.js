$(document).ready(function(){
    $('#i_submit').click( function() {
    //check whether browser fully supports all File API
    if (window.File && window.FileReader && window.FileList && window.Blob)
    {
        //get the file size and file type from file input field
        var fsize = $('#i_file')[0].files[0].size;

        if(fsize>1048576) //do something if file size more than 1 mb (1048576)
        {
            alert(fsize/1048576 +" MB\nToo big image! ! Only 1MB allowed");
            return false;
        }
    }else{
        alert("Please upgrade your browser, because your current browser lacks some new features we need!");
    }
    return true;
});
});
