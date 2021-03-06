/* ---------------------------------------------------------------------- */
/*  Google Analytics
/* ---------------------------------------------------------------------- */

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-38582644-1', 'auto');
ga('send', 'pageview');
/* ---------------------------------------------------------------------- */
/*  My scripts
/* ---------------------------------------------------------------------- */

document.addEventListener("DOMContentLoaded", function(event) {
  /* ---------------------------------------------------------------------- */
  /*  Check and post form
  /* ---------------------------------------------------------------------- */
  $(':submit').on('click', function(event){
      event.preventDefault();
      event.isDefaultPrevented();
      if($("input[name='name']").val() === "")
          {
          alert('please enter your name');
      }
      else if($("input[name='email']").val() === "")
        {
          alert('please enter your email');
      }
      else if($("textarea[name='text']").val() === "")
        {
          alert('please leave some message');
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
            alert('Thanks, your message is sent');

            $('#form .progress').hide();
            $('#form button').show();
            });
      }
  });

    $('.navigation div').on('click', function(){
        var color = $(this).css("background-color");
        $('body').css("background-color", color);
    })
});
