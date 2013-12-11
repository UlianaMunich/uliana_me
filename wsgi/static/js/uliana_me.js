/* ---------------------------------------------------------------------- */
/*  Google Analytics
/* ---------------------------------------------------------------------- */
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-38582644-1']);
_gaq.push(['_trackPageview']);

(function() {
  var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
  ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
  var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
  /* ---------------------------------------------------------------------- */
  /*  Dresden Google Maps without label mark
  /* ---------------------------------------------------------------------- */
function initialize() {
        var map_canvas = document.getElementById('map_canvas');
        var map_options = {
          center: new google.maps.LatLng(51.04905654967599, 13.739862442016602),
          zoom: 12,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(map_canvas, map_options);
      }
      google.maps.event.addDomListener(window, 'load', initialize);
/* ---------------------------------------------------------------------- */
/*  My scripts
/* ---------------------------------------------------------------------- */
(function(){
  /* hide all sections, show only one with class initial */
  $(".section").hide();
  $(".initial").show();

  /* ---------------------------------------------------------------------- */
  /*  Change background color to a navigation color 
  /* ---------------------------------------------------------------------- */
  $('.navigation .item').click(function(){
    var next_section = $(this).attr("data-section");
    var current_section = $('body').attr("class");
    $('body').removeClass(current_section);
    $('body').addClass(next_section);
    $('#'+ current_section).fadeOut(200, function(){
      $('#'+ next_section).fadeIn(200);
    });
  });

})();
