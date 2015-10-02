function pasuser(form) {
    if (form.username.value=="xiaomins") {
        if (form.password.value=="123") {
            location="message.html"
        } else {
            alert("Invalid Password")
        }
    } else {
        alert("Invalid UserID")
    }
}