function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function setCSRF(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain){
        xhr.setRequestHeader("X-CSRFToken", $("[name=csrfmiddlewaretoken]").val())
    }
}