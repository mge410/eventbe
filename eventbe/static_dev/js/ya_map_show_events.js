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

  myMap.container.fitToViewport();

  $.get({
    url: "/events/ajax/offline_events",
    success: function (data) {
      create_placemarks(myMap, data);
    },
  }).fail(function () {
    alert("error");
  });
}

function create_placemarks(ya_map, events) {
  for (const event_model of events["events"]) {
    coords = [event_model.location_y, event_model.location_x];
    console.log(event_model);

    placemark = new ymaps.Placemark(
      coords,
      {
        hintContent: event_model.title,
        balloonContent:
          "<a href='/events/" +
          event_model.id +
          "'>" +
          event_model.title +
          "</a>",
      },
      {
        iconLayout: "default#image",
        iconImageHref: "https://img.icons8.com/color/48/000000/marker.png",
        iconImageSize: [48, 48],
        iconImageOffset: [-24, -48],
        iconCaptionMaxWidth: "50",
      }
    );

    ya_map.geoObjects.add(placemark);
  }
}
