$(function () {

    //mark that form has changed to check before send
    $(document).on("change", "#settingsFormBox .settingsForm input, .settingsForm select", function () {
        $("#"+$(this).closest("form").attr('id')).data("changed", true);
    });

    $(document).on('submit', '#settingsFormBox .settingsForm', function () {

        //check if username isn't empty
        if (this.username.value.length == 0){
            $("#settingsFormBox .settingsNote").text("Username can't be empty");//need to redone it
            return false
        }
        //if form has changed send ajax req with data
        if ($(this).data("changed")){
            $.ajax({
                beforeSend: function(request, settings) {
                    //set dob to none if necessary
                    if (document.getElementById("deleteProfilesDob").checked){
                        $("#settingsFormBox #dobInput").val("");
                        $("#settingsFormBox #deleteProfilesDobBox").hide();
                    }
                    setCSRF(request, settings);
                },
                type: $(this).attr("method"),
                url: $(this).attr("action"),
                data: $(this).serialize(),
                success: function (response) {
                    checkAuth(response);
                    //if dob was set - hide this checkbox
                    if (response["showDeleteProfilesDob"]){
                        $("#settingsFormBox #deleteProfilesDobBox").show(); 
                    }
                    //set value to false in order to avoid errors when sending new req
                    if (document.getElementById("deleteProfilesDob").checked){
                        document.getElementById("deleteProfilesDob").checked = false;
                    }
                    $("#settingsFormBox .settingsNote").text(response["message"]);
                },
            });
        //if nothing has changed
        }else{
            $("#settingsFormBox .settingsNote").text("No chages detected)");
        }
        return false
    });
});