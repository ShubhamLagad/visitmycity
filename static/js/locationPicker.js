$(function () {
    $('#locationPicker').locationpicker(
        {
            location: { latitude: 18.5204303, longitude: 73.8567437 },
            radius: 0,
            inputBinding: {
                latitudeInput: $('#lat'),
                longitudeInput: $('#lng')
            },
            enableAutocomplete: true,
            onchanged: function (currentLocation, radius, isMarkerDropped) {
                // alert("Location changed. New location (" + currentLocation.latitude + ", " + currentLocation.longitude + ")");
            }
        });
});


$(function () {
    $('#locationPicker2').locationpicker(
        {
            location: { latitude: 18.5204303, longitude: 73.8567437 },
            radius: 0,
            inputBinding: {
                latitudeInput: $('#lat2'),
                longitudeInput: $('#lng2')
            },
            enableAutocomplete: true,
            onchanged: function (currentLocation, radius, isMarkerDropped) {
                // alert("Location changed. New location (" + currentLocation.latitude + ", " + currentLocation.longitude + ")");
            }
        });
});

// resident location 
$(function () {
    var residentlat = document.getElementById('residentlat').value;
    var residentlng = document.getElementById('residentlng').value;
    $('#residentlocationPicker').locationpicker(
        {
            location: { latitude: residentlat, longitude: residentlng },
            radius: 0,
            inputBinding: {
                latitudeInput: $('#residentlat'),
                longitudeInput: $('#residentlng')
            },
            enableAutocomplete: true,
            onchanged: function (currentLocation, radius, isMarkerDropped) {
                // alert("Location changed. New location (" + currentLocation.latitude + ", " + currentLocation.longitude + ")");
            }
        });
});
