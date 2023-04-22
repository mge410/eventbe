ymaps.ready(init);

function init() {
  var myMap = new ymaps.Map(
    "map",
    {
      center: [55.76, 37.64],
      zoom: 10,
      controls: [
        "zoomControl",
        "searchControl",
        "typeSelector",
        "fullscreenControl",
      ],
    },
    {
      searchControlProvider: "yandex#search",
    }
  );
  myMap.container.fitToViewport();

  var input_x = document.getElementById("id_location_x");
  var input_y = document.getElementById("id_location_y");

  var coords = [
    input_y.innerHTML.trim().replace(",", "."),
    input_x.innerHTML.trim().replace(",", "."),
  ];

  console.log(coords);

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

  get_weather(coords);
}

function get_weather(coords) {
  var apikey = "9fc94432db02a33b7772a666cd0d0f5f";
  var url = "https://api.openweathermap.org/data/2.5/forecast";
  var lang = document.getElementById("id_lang_code").innerHTML;
  console.log(lang);
  var res = $.get(
    url,
    (data = {
      lat: coords[1],
      lon: coords[0],
      exclude: "daily",
      APPID: apikey,
      units: "metric",
      lang: lang,
      cnt: 16,
      dt: Math.floor(Date.now() / 1000),
    }),
    function (data) {
      var weather_container = document.getElementById("id_weather");
      var temp_container = document.getElementById("id_temp");
      var pressure_container = document.getElementById("id_pressure");
      var humidity_container = document.getElementById("id_humidity");

      weather_container.innerHTML = data.list[0].weather[0]["description"];
      temp_container.innerHTML = data.list[0].main["temp"];
      pressure_container.innerHTML = data.list[0].main["pressure"];
      humidity_container.innerHTML = data.list[0].main["humidity"];
    }
  );
}
