$(function () {

    $( ".signInForm" ).submit(function() {

        //show preloader
        $("#submitSignIn").hide();     
        $("#signInNotice").hide();
        $("#in-preloader").show();

        // send req with data
        $.ajax({
            beforeSend: function(request, settings){
                setCSRF(request, settings);
                request.setRequestHeader("FORMNAME", "signInForm");
            },
            data: $(this).serialize(), 
            type: $(this).attr('method'), 
            url: $(this).attr('action'),
            success: function(jsonResult){
                //hide preloader, show note
                $("#in-preloader").hide();
                $("#submitSignIn").show();
                $("#signInNotice").show();   
                //is smth is wrong show message 
                if (jsonResult["status"] == "wrong"){
                    $("#signInNotice").text(jsonResult["signInNotice"]);
                    $("#signInNotice").css("display", "inline-block"); 
                }
                else if (jsonResult["status"] == "banned"){
                    return false//tell user when he is unbanned and hhat he was banned for
                }
                else if (jsonResult["status"] == "deleted"){
                    return false//ask user whether he wants to revive his page
                }
                //reвirect to necessary url
                else if (jsonResult["status"] == "right"){
                    window.location.href = jsonResult["signInNotice"];
                }
            },
        });
        return false
    });

    $(".signUpForm").submit(function(){

        //display message if password is too short
        if (this.password.value.length < 6){
            $("#signUpNotice").text("Password must be at least 6 characters.");
            $("#signUpNotice").css("display", "inline-block"); 
            return false
        }      

        //show preloader
        $("#signUpNotice").hide();
        $("#submitSignUp").hide();    
        $("#up-preloader").show();
        $.ajax({
            beforeSend: function(request, settings){
                setCSRF(request, settings);
                request.setRequestHeader("FORMNAME", "signUpForm");
            },
            data: $(this).serialize(), 
            type: $(this).attr('method'), 
            url: $(this).attr('action'),
            success: function(jsonResult){
                $("#up-preloader").hide();
                $("#submitSignUp").show();    
                $("#signUpNotice").show();
                //show message
                if (jsonResult["status"] == "wrong" || jsonResult["status"] == "check mail"){
                    $("#signUpNotice").text(jsonResult["signUpNotice"]);
                    $("#signUpNotice").css("display", "inline-block");     
                }
            },
        });
        return false
    });

});
