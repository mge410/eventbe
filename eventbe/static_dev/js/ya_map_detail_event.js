ymaps.ready(init);

function init() {
  var myMap = new ymaps.Map(
    "map",
    {
      center: [55.76, 37.64],
      zoom: 10,
      controls: ['zoomControl', 'searchControl', 'typeSelector',  'fullscreenControl'],
    },
    {
      searchControlProvider: "yandex#search",
    }
  );
  myMap.container.fitToViewport();

  var input_x = document.getElementById("id_location_x");
  var input_y = document.getElementById("id_location_y");

  var coords = [input_y.innerHTML.trim(), input_x.innerHTML.trim()];
 
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
  myMap.setCenter(coords);
  myPlacemark.geometry.setCoordinates(coords);
  myMap.geoObjects.add(myPlacemark);
}
