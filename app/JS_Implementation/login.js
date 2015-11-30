function pasuser(form) {
    if (form.username.value=="xiaomins") {
        if (form.password.value=="123") {
            window.location="knnresult.html"
        } else {
            alert("Invalid Password")
        }
    } else {
        alert("Invalid UserID")
    }
}