$(function () {
    $( ".signInForm" ).submit(function() {
        $("#submitSignIn").hide();     
        $("#signInNotice").hide();
        $("#in-preloader").show();
        $.ajax({
            beforeSend: function(request){
                request.setRequestHeader("FORMNAME", "signInForm");
            },
            data: $(this).serialize(), 
            type: $(this).attr('method'), 
            url: $(this).attr('action'),
        })
        .done(function(jsonResult){
            $("#in-preloader").hide();
            $("#submitSignIn").show();
            $("#signInNotice").show();    
            if (jsonResult["status"] == "wrong"){
                $("#signInNotice").text(jsonResult["signInNotice"]);
                $("#signInNotice").css("display", "inline-block"); 
            }
            else if (jsonResult["status"] == "banned"){
                return false//tell user when he is unbanned and that he is banned
            }
            else if (jsonResult["status"] == "deleted"){
                return false//ask user whether he wants to revive his page
            }
            else if (jsonResult["status"] == "right"){
                window.location.href = jsonResult["signInNotice"];
            }
        })
        
        return false
    });
    $(".signUpForm").submit(function(){
        if (this.password.value.length < 6){
            $("#signUpNotice").text("Password must be at least 6 characters.");
            $("#signUpNotice").css("display", "inline-block"); 
            return false
        }      
        $("#up-preloader").show();
        $("#signUpNotice").hide();
        $("#submitSignUp").hide() ;    
        $.ajax({
            data: $(this).serialize(), 
            type: $(this).attr('method'), 
            url: $(this).attr('action'),
            headers: {"FORMNAME":"signUpForm"}
        })
        .done(function(jsonResult){
            $("#up-preloader").hide();
            $("#submitSignUp").show();    
            $("#signUpNotice").show();
            if (jsonResult["status"] == "wrong" || jsonResult["status"] == "check mail"){
                $("#signUpNotice").text(jsonResult["signUpNotice"]);
                $("#signUpNotice").css("display", "inline-block");     
            }
        })
        
        return false
    });
});
