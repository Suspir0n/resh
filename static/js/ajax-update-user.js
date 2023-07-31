$("button#btnUpdateUser").on("click", function (e) {
    e.preventDefault();

    username = $("input#upUsername").val();
    email = $("input#upEmail").val();
    password = $("input#upPassword").val();
    user_uuid = $("form.form-update-user").attr("data-title");
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    console.log(email)

    $.ajax({
        type: 'POST',
        url: 'update/' + user_uuid,
        data: {
            'username': username,
            'email': email,
            'password': password,
            'csrfmiddlewaretoken': csrftoken,
        },
        datatype: "json",
        success: function (data) {
            window.location.reload();
        }
    });
});