ymaps.ready(init);

function init() {
  var myMap = new ymaps.Map(
    "map",
    {
      center: [55.76, 37.64],
      zoom: 10,
    },
    {
      searchControlProvider: "yandex#search",
    }
  );
  var myPlacemark = null;
  var input_x = document.getElementById("id_location_x");
  var input_y = document.getElementById("id_location_y");

  myMap.events.add("click", function (event) {
    var coords = event.get("coords");

    input_x.value = coords[1];
    input_y.value = coords[0];

    if (myPlacemark) {
      myPlacemark.geometry.setCoordinates(coords);
    } else {
      myPlacemark = new ymaps.Placemark(
        coords,
        {},
        {
          iconLayout: "default#image",
          iconImageHref: "https://img.icons8.com/color/48/000000/marker.png",
          iconImageSize: [48, 48],
          iconImageOffset: [-24, -48],
        }
      );

      myMap.geoObjects.add(myPlacemark);
    }
  });
}

document.addEventListener("DOMContentLoaded", function () {
  var mapContainer = document.getElementById("map");
  var location_table = document.getElementById("location_table");
  var checkbox = document.getElementById("id_is_offline");

  mapContainer.style.display = "none";
  location_table.style.display = "none";

  checkbox.addEventListener("change", function () {
    if (checkbox.checked) {
      mapContainer.style.display = "block";
      location_table.style.display = "block";
    } else {
      mapContainer.style.display = "none";
      location_table.style.display = "none";
    }
  });
});
