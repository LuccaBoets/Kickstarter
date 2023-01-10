//leaflet
async function pointInsideCircle(point) {
    var list = await getAllRegions();

    for (let index = 0; index < list.length; index++) {
        var circle = list[index]
        latLng = { circle["lat"], circle["long"] };
        if (point.distanceTo(latLng) > circle["radius"]) {
            alert("in circle");
            return true;
        }
    }
    return false;
}