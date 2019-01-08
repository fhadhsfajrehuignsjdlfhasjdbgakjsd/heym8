$(function () {

    //when user sees last n posts we make ajax requests and add new albums
    // $("#content").on("scroll", function(){
    //     if ($("#whatever").visible(true)){
    //         alert($("#whatever").is(":visible"));
    //     }
    // });

    //edit status
    $(document).on("submit", "#editStatusWindow #editStatusForm", function () {
        //do nothing if status hasn't changed
        if ($.trim(this.status.value) == $.trim($("#userPage #usernameAndStatusBox #statusBox").text())){
            $("#editStatusWindow").modal("hide");
            return false
        }
        //send new status and update status
        $.ajax({
            beforeSend: function(request, settings){
                setCSRF(request, settings);
            },
            data: {"status":$.trim(this.status.value)},
            type: $(this).attr('method'), 
            url: $(this).attr('action'),
            success: function (response){
                checkAuth(response);
                $("#userPage #usernameAndStatusBox #statusBox").text(response["newStatus"]);
                $("#editStatusWindow").modal("hide");
            },
        });
        return false
    });

    //open album pics in new window
    $(document).on("click", ".albumsBox .albumRef", function () {
        window.open($(this).parent().parent().children("a").attr('href'), '_blank');
    });

    //focus on the end of status when modal is opened
    $(document).on("shown.bs.modal", ".modal", function () {
        var textarea = $("#editStatusWindow #statusInput");
        
        val = textarea.val();
    
        textarea
        .focus()
        .val("")
        .val(val);
    });

});