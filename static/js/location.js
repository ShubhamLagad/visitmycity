onload = getLocation()

// custom coordinates 
// var coordinates ="18.442330,73.836472" 
// var lat = coordinates.split(',')[0];
// var lon = coordinates.split(',')[1];


// auto coordinates 
var lat;
var lon;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}
function showPosition(position) {
    lat = position.coords.latitude;
    lon = position.coords.longitude;
}

function getCoordinates() {
    return (lat + "," + lon);
}

