
function passWarn(id) {
    document.getElementById(id).innerHTML = "<small class='text-muted'>Password must be 8-16 characters</small>"
}

function checkPassword(id1,id2,id3,id4) {
    var pass = document.getElementById(id1).value;
    var cpass = document.getElementById(id2).value;
    if (pass != cpass) {
        document.getElementById(id4).disabled = true
        document.getElementById(id3).innerHTML = "<small class='text-danger'>Password must be same!</small>"

    } else {
        document.getElementById(id3).innerHTML = ""
        document.getElementById(id4).disabled = false
    }
}