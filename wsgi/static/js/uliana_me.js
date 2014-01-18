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
/*  My scripts
/* ---------------------------------------------------------------------- */
(function(){
  /* hide all sections, show only one with class initial */
  $(".section").hide();
  $(".initial").show();

  /* ---------------------------------------------------------------------- */
  /*  Check and post form
  /* ---------------------------------------------------------------------- */
  $(':submit').on('click', function(){
      event.preventDefault();
      event.isDefaultPrevented;
      if($("input[name='name']").val() === "")
          {
          alert('please fill the name field');
      }
      else if($("input[name='email']").val() === "")
        {
          alert('please fill the email field');
      }
      else if($("textarea[name='text']").val() === "")
        {
          alert('please leave some msg');
      }else
      { $('#form button').hide();
        $('#form .progress').show();
        $.ajax({
        type: 'POST',
        url: '/api/contact',
        dataType: 'json',
        data: $('#form').serialize(),
        success: function(data){
        }
        }).done(function() {
            $("#form input").val("");
            $("#form textarea").val("");
            alert('Form submitted');
            
            $('#form .progress').hide();
            $('#form button').show();
            });
      }
  });
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
