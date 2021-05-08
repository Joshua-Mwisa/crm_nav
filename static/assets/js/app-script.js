
$(function() {
    "use strict";
     
	 
//sidebar menu js
$.sidebarMenu($('.sidebar-menu'));

// === toggle-menu js
$(".toggle-menu").on("click", function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });	 
	   
// === sidebar menu activation js

$(function() {
        for (var i = window.location, o = $(".sidebar-menu a").filter(function() {
            return this.href == i;
        }).addClass("active").parent().addClass("active"); ;) {
            if (!o.is("li")) break;
            o = o.parent().addClass("in").parent().addClass("active");
        }
    }), 	   
	   

/* Top Header */

$(document).ready(function(){ 
    $(window).on("scroll", function(){ 
        if ($(this).scrollTop() > 60) { 
            $('.topbar-nav .navbar').addClass('bg-dark'); 
        } else { 
            $('.topbar-nav .navbar').removeClass('bg-dark'); 
        } 
    });

 });


/* Back To Top */

$(document).ready(function(){ 
    $(window).on("scroll", function(){ 
        if ($(this).scrollTop() > 300) { 
            $('.back-to-top').fadeIn(); 
        } else { 
            $('.back-to-top').fadeOut(); 
        } 
    }); 

    $('.back-to-top').on("click", function(){ 
        $("html, body").animate({ scrollTop: 0 }, 600); 
        return false; 
    }); 
});	   
	    
   
$(function () {
  $('[data-toggle="popover"]').popover()
})


$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})


	 // theme setting
	 $(".switcher-icon").on("click", function(e) {
        e.preventDefault();
        $(".right-sidebar").toggleClass("right-toggled");
    });
	
	$('#theme1').click(theme1);
    $('#theme2').click(theme2);
    $('#theme3').click(theme3);
    $('#theme4').click(theme4);
    $('#theme5').click(theme5);
    $('#theme6').click(theme6);
    $('#theme7').click(theme7);
    $('#theme8').click(theme8);
    $('#theme9').click(theme9);
    $('#theme10').click(theme10);
    $('#theme11').click(theme11);
    $('#theme12').click(theme12);
    $('#theme13').click(theme13);
    $('#theme14').click(theme14);
    $('#theme15').click(theme15);
    $('#theme16').click(theme16);
    $('#theme17').click(theme17);
    $('#theme18').click(theme18);
    $('#theme19').click(theme19);
    $('#theme20').click(theme20);
    $('#theme21').click(theme21);
    $('#theme22').click(theme22);
    $('#theme23').click(theme23);
    $('#theme24').click(theme24);
    $('#theme25').click(theme25);
    $('#theme26').click(theme26);
    $('#theme27').click(theme27);
    $('#theme28').click(theme28);
    $('#theme29').click(theme29);
    $('#theme30').click(theme30);
    $('#theme31').click(theme31);


    function theme1() {
      $('body').attr('class', 'bg-theme bg-theme1');
    }

    function theme2() {
      $('body').attr('class', 'bg-theme bg-theme2');
    }

    function theme3() {
      $('body').attr('class', 'bg-theme bg-theme3');
    }

    function theme4() {
      $('body').attr('class', 'bg-theme bg-theme4');
    }
	
	function theme5() {
      $('body').attr('class', 'bg-theme bg-theme5');
    }
	
	function theme6() {
      $('body').attr('class', 'bg-theme bg-theme6');
    }

    function theme7() {
      $('body').attr('class', 'bg-theme bg-theme7');
    }

    function theme8() {
      $('body').attr('class', 'bg-theme bg-theme8');
    }

    function theme9() {
      $('body').attr('class', 'bg-theme bg-theme9');
    }

    function theme10() {
      $('body').attr('class', 'bg-theme bg-theme10');
    }

    function theme11() {
      $('body').attr('class', 'bg-theme bg-theme11');
    }

    function theme12() {
      $('body').attr('class', 'bg-theme bg-theme12');
    }
	
	function theme13() {
      $('body').attr('class', 'bg-theme bg-theme13');
    }
	
	function theme14() {
      $('body').attr('class', 'bg-theme bg-theme14');
    }
	
	function theme15() {
      $('body').attr('class', 'bg-theme bg-theme15');
    }

    function theme16() {
      $('body').attr('class', 'bg-theme bg-theme16');
    }

    function theme17() {
      $('body').attr('class', 'bg-theme bg-theme17');
    }

    function theme18() {
      $('body').attr('class', 'bg-theme bg-theme18');
    }

    function theme19() {
      $('body').attr('class', 'bg-theme bg-theme19');
    }

    function theme20() {
      $('body').attr('class', 'bg-theme bg-theme20');
    }
    function theme21() {
      $('body').attr('class', 'bg-theme bg-theme21');
    }
    function theme22() {
      $('body').attr('class', 'bg-theme bg-theme22');
    }
    function theme23() {
      $('body').attr('class', 'bg-theme bg-theme23');
    }
    function theme24() {
      $('body').attr('class', 'bg-theme bg-theme24');
    }
    function theme25() {
      $('body').attr('class', 'bg-theme bg-theme25');
    }
    function theme26() {
      $('body').attr('class', 'bg-theme bg-theme26');
    }
    function theme27() {
      $('body').attr('class', 'bg-theme bg-theme27');
    }
    function theme28() {
      $('body').attr('class', 'bg-theme bg-theme28');
    }
    function theme29() {
      $('body').attr('class', 'bg-theme bg-theme29');
    }
    function theme30() {
      $('body').attr('class', 'bg-theme bg-theme30');
    }
    function theme31() {
      $('body').attr('class', 'bg-theme bg-theme31');
    }



});