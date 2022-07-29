$(document).ready(function () {
    "use strict";
    $(window).on('scroll', function () {

        if ($(this).scrollTop() > 600) {
            $('.return-to-top').fadeIn();
        } else {
            $('.return-to-top').fadeOut();
        }
    });

    $('.return-to-top').on('click', function () {
        $('html, body').animate({
            scrollTop: 0
        }, 1500);
        return false;
    });

    $("#slider-range").slider({
        range: true,
        min: 0,
        max: 12000,
        values: [2677, 9241],
        slide: function (event, ui) {
            $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
        }
    });
    $("#amount").val("$" + $("#slider-range").slider("values", 0) +
        " - $" + $("#slider-range").slider("values", 1));


    $(".qtyplus").on("click", function () {
        var b = $(this).parents(".quantity-form").find("input.qty"),
            c = parseInt(b.val(), 10) + 1,
            d = parseInt(b.attr("max"), 10);
        d || (d = 9999999999), c <= d && (b.val(c), b.change())
    });
    $(".qtyminus").on("click", function () {
        var b = $(this).parents(".quantity-form").find("input.qty"),
            c = parseInt(b.val(), 10) - 1,
            d = parseInt(b.attr("min"), 10);
        d || (d = 1), c >= d && (b.val(c), b.change())
    });


    function makeTimer() {

        var endTime = new Date("March 7, 2018 12:00:00 PDT");
        var endTime = (Date.parse(endTime)) / 1000;

        var now = new Date();
        var now = (Date.parse(now) / 1000);

        var timeLeft = endTime - now;

        var days = Math.floor(timeLeft / 86400);
        var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
        var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600)) / 60);
        var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));

        if (hours < "10") { hours = "0" + hours; }
        if (minutes < "10") { minutes = "0" + minutes; }
        if (seconds < "10") { seconds = "0" + seconds; }

        $("#days").html(days + '<span class="camp">Days</span>');
        $("#hours").html(hours + '<span class="camp">Hour</span>');
        $("#minutes").html(minutes + '<span class="camp">Minute</span>');
        $("#seconds").html(seconds + '<span class="camp">Second</span>');

    }

    setInterval(function () { makeTimer(); }, 1000);

    var owl = $('#user-feedback-carousel');
    owl.owlCarousel({
        items: 3,
        margin: 0,

        loop: true,
        autoplay: true,
        smartSpeed: 1000,

        dots: true,
        autoplayHoverPause: true,

        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            640: {
                items: 1
            },
            767: {
                items: 2
            },
            992: {
                items: 3
            }
        }


    });


    var owl = $('#users-offers-carousel');
    owl.owlCarousel({
        items: 3,
        margin: 0,

        loop: true,
        autoplay: true,
        smartSpeed: 1000,

        dots: true,
        autoplayHoverPause: true,

        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            740: {
                items: 1
            },
            1267: {
                items: 2
            }
        }

    });
    $('[data-toggle="datepicker"]').datepicker();

    $('.header-area').sticky({
        topSpacing: 0
    });

    $('body').scrollspy({
        target: '.navbar-collapse',
        offset: 0
    });


    $(window).load(function () {

        $(".about-us-txt h2").removeClass("animated fadeInUp").css({ 'opacity': '0' });
        $(".about-us-txt button").removeClass("animated fadeInDown").css({ 'opacity': '0' });
    });

    $(window).load(function () {

        $(".about-us-txt h2").addClass("animated fadeInUp").css({ 'opacity': '0' });
        $(".about-us-txt button").addClass("animated fadeInDown").css({ 'opacity': '0' });
    });

});



function togglePage() {
    var page1 = document.getElementById('firstpage')
    var page2 = document.getElementById('secondpage')

    let temp = page1.style.display;
    page1.style.display = page2.style.display;
    page2.style.display = temp;
}




// ------------Login login_modal-----------
function login_Btn() {
    var login_modal = document.getElementById("login-modal");
    login_modal.style.display = "flex";
}
$('.login-close').click(function () {
    var login_modal = document.getElementById("login-modal");
    login_modal.style.display = "none";
})


// ------------register_modal-----------
function register_Btn() {
    var reg_modal = document.getElementById("register-modal");
    reg_modal.style.display = "flex";
}
$('.register-close').click(function () {
    var reg_modal = document.getElementById("register-modal");
    reg_modal.style.display = "none";
})


// ------------Login login_modal-----------
function guideLoginBtn(){
    var guide_login_modal = document.getElementById("guide-login-modal");
    guide_login_modal.style.display = "flex";
}
$('#guide-login-close').click(function () {
    var guide_login_modal = document.getElementById("guide-login-modal");
    guide_login_modal.style.display = "none";
})



function guide_reg_btn() {
    var guide_reg_modal = document.getElementById("guide-register-modal");
    guide_reg_modal.style.display = "flex";
}
function guide_register_close() {
    var guide_reg_modal = document.getElementById("guide-register-modal");
    guide_reg_modal.style.display = "none";
}

// ------------Login login_modal-----------
$('#admin-login-btn').click(function () {
    var admin_login_modal = document.getElementById("admin-login-modal");
    admin_login_modal.style.display = "flex";
})
$('#admin-login-close').click(function () {
    var admin_login_modal = document.getElementById("admin-login-modal");
    admin_login_modal.style.display = "none";
})


function admin_login_btn() {
    var admin_reg_modal = document.getElementById("admin-login-modal");
    admin_reg_modal.style.display = "flex";
}
function admin_login_close() {
    var admin_reg_modal = document.getElementById("admin-login-modal");
    admin_reg_modal.style.display = "none";
}



