$(function () {
    $(".lmRef").click(function (e) {
        if (this.id == "logout"){
            return true
        }
        alert(this.url);
        return false
    });
    $(".rmGetRef").click(function (e) { 
        e.preventDefault();
        alert(this.url);
    });
});