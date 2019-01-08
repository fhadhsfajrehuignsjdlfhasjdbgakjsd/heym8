$(function () {
    window.addEventListener('popstate', function(event){
        if(event.state){
            url = event.state.url;
            $.ajax({
                type: "GET",
                method: "GET",
                url: url,
                dataType: "json",
                data:{'reqRM':event.state.reqRM},
                success: function (response) {
                    checkAuth(response);
                    $("#content").html(response["content"]);
                    $("#rightMenu").html(response["rm"]);
                },
                error: function (a, b, c) {
                    alert(b);
                }
            });
            return false
        }
        else{
            return true
        }
    });

    $(document).on('click', '.fullAjaxRef, .contentAjaxRef', function () {
        if (this.id == "logout"){
            return true
        }
        reqRM = $(this).attr("class").search("fullAjaxRef") != -1;
        url = $(this).attr('href');
        $.ajax({
            beforeSend: function(request, settings){
                setCSRF(request, settings);
            },
            type: "GET",
            method: "GET",
            url: url,
            dataType: "json",
            data:{'reqRM':reqRM},//if right menu is required
            success: function (response) {
                checkAuth(response);
                $("#content").html(response["content"]);
                if (reqRM){
                    $("#rightMenu").html(response["rm"]);
                }
                if (url != window.location.pathname){
                    history.pushState({'url':url, 'reqRM':reqRM}, null, url);
                }
            }
        });
        return false
    });

    $("textarea").keypress(function (e) {
        if(e.which == 13 && !e.shiftKey) {        
            $(this).closest("form").submit();
            e.preventDefault();
            return false;
        }
    });

});

function checkAuth(response) {
    if (response["isNotAuthenticated"]){
        window.location.href = response["redirectTo"];
    }
}