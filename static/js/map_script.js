$(function(){



var myCenter=new google.maps.LatLng(51.508742,-0.120850);
var marker;
    var myCenter2=new google.maps.LatLng(51.508742,-0.120850);
var marker2;

  function initialize() {

  var mapProp = {
    center:new google.maps.LatLng(51.508742,-0.120850),
    zoom:5,
    mapTypeId:google.maps.MapTypeId.ROADMAP,
      panControl:true,
    zoomControl:true,
      zoomControlOptions: {
      style:google.maps.ZoomControlStyle.SMALL
    },
    mapTypeControl:true,
      mapTypeControlOptions: {
      style:google.maps.MapTypeControlStyle.DROPDOWN_MENU

    },
    scaleControl:true,
    streetViewControl:true,
    overviewMapControl:true,
    rotateControl:true,
    draggable: false
  };

  var mapProp2 = {
    center:new google.maps.LatLng(51.408742,-0.140850),
    zoom:5,
    mapTypeId:google.maps.MapTypeId.ROADMAP
  };

    var map=new google.maps.Map(document.getElementById("map"), mapProp);
    var map2=new google.maps.Map(document.getElementById("map2"), mapProp2);

    var marker=new google.maps.Marker({
        position:myCenter,
        animation:google.maps.Animation.BOUNCE
    });

    marker.setMap(map);

  var marker2=new google.maps.Marker({
        position:myCenter2,
        animation:google.maps.Animation.BOUNCE
    });

    marker2.setMap(map2);


      // Zoom to 9 when clicking on marker
google.maps.event.addListener(marker,'click',function() {
  map.setZoom(9);
  map.setCenter(marker.getPosition());
  });


      // Zoom to 9 when clicking on marker
google.maps.event.addListener(marker2,'click',function() {
  map2.setZoom(9);
  map2.setCenter(marker.getPosition());
  });
}
google.maps.event.addDomListener(window, 'load', initialize);
});
