
$(document).ready(function() {
$('#toggle').click(function () {
    //check if checkbox is checked
    if ($(this).is(':checked')) {

        $('#sendNewSms').removeAttr('disabled'); //enable input
        $('#sendNewSms').show();
    } else {
        $('#sendNewSms').attr('disabled', true); //disable input
        $('#sendNewSms').hide();
    }
});

  $('#first_form').submit(function(e) {
    e.preventDefault();
    var student_id=$('#student_id').val();
    var first_name = $('#first_name').val();
    var middle_name = $('#middle_name').val();
    var last_name = $('#last_name').val();
    var father_name = $('#father_name').val();
    var mother_name = $('#mother_name').val();
    var dob = $('#dob').val();
    var course_id = $('#course_id').val();
    var address = $('#address').val();
    var bg = $('#bg').val();
    var reg_date = $('#reg_date').val();
    var contact = $('#contact').val();
    var email = $('#email').val();
    var collageidno =$('#collageidno').val();

    $(".error").remove();
    if (student_id.length < 1) {
      $('#student_id').before('<span class="error">This field is required</span>');
    }
    if (first_name.length < 1) {
      $('#first_name').before('<span class="error">This field is required</span>');
    }
    if (middle_name.length < 1) {
      $('#middle_name').before('<span class="error">This field is required</span>');
    }
    if (last_name.length < 1) {
      $('#last_name').before('<span class="error">This field is required</span>');
    }
    if (father_name.length < 1) {
      $('#father_name').before('<span class="error">This field is required</span>');
    }
    if (mother_name.length < 1) {
      $('#mother_name').before('<span class="error">This field is required</span>');
    }
    if (dob.length < 1) {
      $('#dob').before('<span class="error">This field is required</span>');
    }
    if (course_id.length < 1) {
      $('#course_id').before('<span class="error">This field is required</span>');
    }
    if (address.length < 1) {
      $('#address').before('<span class="error">This field is required</span>');
    }
    if (bg.length < 1) {
      $('#bg').before('<span class="error">This field is required</span>');
    }
    if (reg_date.length < 1) {
      $('#reg_date').before('<span class="error">This field is required</span>');
    }
    if (contact.length < 1) {
      $('#contact').before('<span class="error">This field is required</span>');
    }
    if (email.length < 1) {
      $('#email').before('<span class="error">This field is required</span>');
    }
    else {
      var regEx = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
      var validEmail = regEx.test(email);
      if (!validEmail) {
        $('#email').before('<span class="error">Enter a valid email</span>');
      }
    }
    if(collageidno.length < 1)
    {
        $('#collageidno').before('<span class="error">This field is required</span>');
    }

    if(student_id && first_name && middle_name && last_name && father_name && mother_name && dob && course_id && address && bg && reg_date && contact && email != "")
    {
    alert("Your Data successfully Registered!\n"+"Welcome------> "+first_name+" "+last_name);
    window.location.replace("Login.html");
    }
  });

});
$(window).on("load",function() {
  $("#Admin").hide();
  $("#Student").hide();
  $("#Employee").hide();
$(function () {
    $("#ln").change(function () {
        if ($(this).val() == "Admin") {
            $("#Admin").show();
            $("#Student").hide();
            $("#Employee").hide();
        }
        else if ($(this).val() == "Student") {
            $("#Student").show();
            $("#Admin").hide();
            $("#Employee").hide();
        }
        else if ($(this).val() == "Employee") {
            $("#Employee").show();
            $("#Admin").hide();
            $("#Student").hide();
        }
        else
        {
          $("#Employee").hide();
          $("#Admin").show();
          $("#Student").hide();
        }
    });
});
});
(function ($) {
    "use strict";

    /*[ Load page ]
    ===========================================================*/
    $(".animsition").animsition({
        inClass: 'fade-in',
        outClass: 'fade-out',
        inDuration: 1500,
        outDuration: 800,
        linkElement: '.animsition-link',
        loading: true,
        loadingParentElement: 'html',
        loadingClass: 'animsition-loading-1',
        loadingInner: '<div class="cp-spinner cp-meter"></div>',
        timeout: false,
        timeoutCountdown: 5000,
        onLoadEvent: true,
        browser: [ 'animation-duration', '-webkit-animation-duration'],
        overlay : false,
        overlayClass : 'animsition-overlay-slide',
        overlayParentElement : 'html',
        transition: function(url){ window.location.href = url; }
    });

    /*[ Back to top ]
    ===========================================================*/
    var windowH = $(window).height()/2;

    $(window).on('scroll',function(){
        if ($(this).scrollTop() > windowH) {
            $("#myBtn").css('display','flex');
        } else {
            $("#myBtn").css('display','none');
        }
    });

    $('#myBtn').on("click", function(){
        $('html, body').animate({scrollTop: 0}, 300);
    });


    /*[ Select ]
    ===========================================================*/
    $(".selection-1").select2({
        minimumResultsForSearch: 20,
        dropdownParent: $('#dropDownSelect1')
    });

    /*[ Daterangepicker ]
    ===========================================================*/
    $('.my-calendar').daterangepicker({
        "singleDatePicker": true,
        "showDropdowns": true,
        locale: {
            format: 'DD/MM/YYYY'
        },
    });

    var myCalendar = $('.my-calendar');
    var isClick = 0;

    $(window).on('click',function(){
        isClick = 0;
    });

    $(myCalendar).on('apply.daterangepicker',function(){
        isClick = 0;
    });

    $('.btn-calendar').on('click',function(e){
        e.stopPropagation();

        if(isClick == 1) isClick = 0;
        else if(isClick == 0) isClick = 1;

        if (isClick == 1) {
            myCalendar.focus();
        }
    });

    $(myCalendar).on('click',function(e){
        e.stopPropagation();
        isClick = 1;
    });

    $('.daterangepicker').on('click',function(e){
        e.stopPropagation();
    });


    /*[ Play video 01]
    ===========================================================*/
    var srcOld = $('.video-mo-01').children('iframe').attr('src');

    $('[data-target="#modal-video-01"]').on('click',function(){
        $('.video-mo-01').children('iframe')[0].src += "&autoplay=1";

        setTimeout(function(){
            $('.video-mo-01').css('opacity','1');
        },300);
    });

    $('[data-dismiss="modal"]').on('click',function(){
        $('.video-mo-01').children('iframe')[0].src = srcOld;
        $('.video-mo-01').css('opacity','0');
    });


    /*[ Fixed Header ]
    ===========================================================*/
    var header = $('header');
    var logo = $(header).find('.logo img');
    var linkLogo1 = $(logo).attr('src');
    var linkLogo2 = $(logo).data('logofixed');


    $(window).on('scroll',function(){
        if($(this).scrollTop() > 5 && $(this).width() > 992) {
            $(logo).attr('src',linkLogo2);
            $(header).addClass('header-fixed');
        }
        else {
            $(header).removeClass('header-fixed');
            $(logo).attr('src',linkLogo1);
        }

    });

    /*[ Show/hide sidebar ]
    ===========================================================*/
    $('body').append('<div class="overlay-sidebar trans-0-4"></div>');
    var ovlSideBar = $('.overlay-sidebar');
    var btnShowSidebar = $('.btn-show-sidebar');
    var btnHideSidebar = $('.btn-hide-sidebar');
    var sidebar = $('.sidebar');

    $(btnShowSidebar).on('click', function(){
        $(sidebar).addClass('show-sidebar');
        $(ovlSideBar).addClass('show-overlay-sidebar');
    })

    $(btnHideSidebar).on('click', function(){
        $(sidebar).removeClass('show-sidebar');
        $(ovlSideBar).removeClass('show-overlay-sidebar');
    })

    $(ovlSideBar).on('click', function(){
        $(sidebar).removeClass('show-sidebar');
        $(ovlSideBar).removeClass('show-overlay-sidebar');
    })


    /*[ Isotope ]
    ===========================================================*/
    var $topeContainer = $('.isotope-grid');
    var $filter = $('.filter-tope-group');

    // filter items on button click
    $filter.each(function () {
        $filter.on('click', 'button', function () {
            var filterValue = $(this).attr('data-filter');
            $topeContainer.isotope({filter: filterValue});
        });

    });

    // init Isotope
    $(window).on('load', function () {
        var $grid = $topeContainer.each(function () {
            $(this).isotope({
                itemSelector: '.isotope-item',
                percentPosition: true,
                animationEngine : 'best-available',
                masonry: {
                    columnWidth: '.isotope-item'
                }
            });
        });
    });

    var labelGallerys = $('.label-gallery');

    $(labelGallerys).each(function(){
        $(this).on('click', function(){
            for(var i=0; i<labelGallerys.length; i++) {
                $(labelGallerys[i]).removeClass('is-actived');
            }

            $(this).addClass('is-actived');
        });
    });



})(jQuery);
 function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#blah')
                        .attr('src', e.target.result);
                };

                reader.readAsDataURL(input.files[0]);
            }
        }
