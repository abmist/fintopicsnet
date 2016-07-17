$(function(){

  //Marker: UK office
  var myCenter=new google.maps.LatLng(51.5237038, -0.1585531);
  var marker;

  //Marker: Ireland office
  var myCenter2=new google.maps.LatLng(53.3389021,-6.252878499999952);
  var marker2;

  //Marker: US office
  var myCenter3=new google.maps.LatLng(40.7060006, -74.008801);
  var marker3;

  function initialize() {

    //Map UK office ---------------------------------------------------
    var mapProp = {
      center:new google.maps.LatLng(51.5237038, -0.1585531),
      zoom:15,
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

    var map=new google.maps.Map(document.getElementById("map"), mapProp);

    var marker=new google.maps.Marker({
          position:myCenter,
          animation:google.maps.Animation.BOUNCE
      });

    marker.setMap(map);

    // Zoom when clicking on marker
    google.maps.event.addListener(marker,'click',function() {
      map.setZoom(17);
      map.setCenter(marker.getPosition());

    });

    //Map Ireland office ------------------------------------------
    var mapProp2 = {
      center:new google.maps.LatLng(53.3389021,-6.252878499999952),
      zoom:15,
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

    var map2=new google.maps.Map(document.getElementById("map2"), mapProp2);

    var marker2=new google.maps.Marker({
          position:myCenter2,
          animation:google.maps.Animation.BOUNCE
      });

    marker2.setMap(map2);

    // Zoom when clicking on marker
    google.maps.event.addListener(marker2,'click',function() {
      map2.setZoom(17);
      map2.setCenter(marker2.getPosition());
    });

    //Map US office ---------------------------------------------------
    var mapProp3 = {
      center:new google.maps.LatLng(40.7060006, -74.008801),
      zoom:15,
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

    var map3=new google.maps.Map(document.getElementById("map3"), mapProp3);

    var marker3=new google.maps.Marker({
          position:myCenter3,
          animation:google.maps.Animation.BOUNCE
      });

    marker3.setMap(map3);

    // Zoom when clicking on marker
    google.maps.event.addListener(marker3,'click',function() {
      map3.setZoom(17);
      map3.setCenter(marker3.getPosition());

    });

}

google.maps.event.addDomListener(window, 'load', initialize);
});
