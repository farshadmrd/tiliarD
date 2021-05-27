

// ----------------signup----------------
let username = document.querySelector("#username");
let email = document.querySelector("#email");
let password = document.querySelector("#password");
let result = document.querySelector("#result");

let btnSend= document.querySelector("btn-send");
// ----------------signup----------------
username.onblur = function () {
    let pattern = /[a-zA-Z0-9]/;
    if (pattern.test(this.value)) {
        result.innerHTML = "";
        this.style.border = "1px solid black";
    }
    else {
        result.innerHTML = "نام کاربری را درست وارد کنید";
        this.style.border = "1px solid red";
    }
}

email.onblur = function () {
    let pattern = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (pattern.test(this.value)) {
        result.innerHTML = "";
        this.style.border = "1px solid black";
    }
    else {
        result.innerHTML = "ایمیل معتبر وارد کنید";
        this.style.border = "1px solid red";
    }
}
password.onblur = function () {
    let pattern = /[a-zA-Z0-9]/;
    if (pattern.test(this.value)) {
        this.style.border = "1px solid black";
        result.innerHTML = "";
    }
    else {
        result.innerHTML = "رمز عبور را درست وارد کنید"
        this.style.border = "1px solid red";
    }
}








// const Http = new XMLHttpRequest();
// const url='';






