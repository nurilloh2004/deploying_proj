$(window).on('load',function(){
	setTimeout(function(){ // allowing 3 secs to fade out loader
	$('.page-loader').fadeOut('slow');
	},1500);
});


window.replainSettings = { id: '8665d7b9-a0f2-4754-bc34-fe17e6ee5f5f' };
(function(u){var s=document.createElement('script');s.async=true;s.src=u;
var x=document.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x);
})('https://widget.replain.cc/dist/client.js');







   // Crol to top
  var $btnTop = $(".btn-top");
  $(window).on("scroll",function(){
    if($(window).scrollTop() >= 20)
    {
      $btnTop.fadeIn();
    }
    else{
      $btnTop.fadeOut();
    }
 });
  $btnTop.on("click",function(){
    $("html,body").animate({scrollTop:0},1200)
  });


  
$(document).ready(function(){

  $('.customer-logos').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 3500,
      arrows: false,
      dots: false,
      pauseOnHover: false,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
              slidesToShow: 3
          }
      },{
          breakpoint: 768,
          settings: {
              slidesToShow: 2
          }
      }, {
          breakpoint: 520,
          settings: {
              slidesToShow: 1
          }
      }]
  });

});
