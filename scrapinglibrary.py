from bs4 import BeautifulSoup
import requests
import pandas as pd
import selenium
html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- iid: 863 -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
            
    <link href="https://static-assets-us.libcal.com/css_610/bootstrap3.min.css" rel="stylesheet">


    <link href="//cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <link href="https://static-assets-us.libcal.com/css_610/LibCal_public.min.css" rel="stylesheet">
    <link href="https://static-assets-us.libcal.com/css_610/print.min.css" rel="stylesheet" media="print">
    
<script src="https://static-assets-us.libcal.com/js_610/jquery.min.js"></script>


<script src="https://static-assets-us.libcal.com/js_610/bootstrap3.min.js"></script>
    <script src="https://static-assets-us.libcal.com/js_610/LibCal_public.min.js"></script>
        <script>
    springSpace.dateFormat = "dddd, MMMM D, YYYY";
    springSpace.dateShortFormat = "dddd, MMMM D, YYYY";
    springSpace.timeFormat = "h:mma";
    springSpace.timezone = 'America/New_York';
    springSpace.currency = "USD";
    springSpace.currencySymbol = "$";

    springSpace.language = 'en'; // en
    springSpace.locale = 'en-US'; // en-US

    springSpace.phpTimeFormat = 'g:ia';

    springSpace.bootstrapAsset = 'https://static-assets-us.libcal.com/css_610/bootstrap3_16.min.css';
    springSpace.publicCssAsset = 'https://static-assets-us.libcal.com/css_610/LibCal_public.min.css';
    springSpace.adminCssAsset = 'https://static-assets-us.libcal.com/css_610/LibCal_admin.min.css';
</script>
        <title>
                    Space Availability -
                UVA Library Calendar -
        UVA Library
    </title>
    <style>
            #s-lc-public-banner {
            padding: 0;
            margin: 0;
        }

        .s-lc-public-footer {
            margin: 0;
        }
    </style>
            <style>
/* NEW 2024 */
header a {
    color: #2b2b2b;
}
/*CHRISTOPHER: the item below was applied globally (*), which changed all fonts on all pages. So I changed it to header since the fonts were then too small. Can address this in redesign in spring.*/

header {
    font-family: franklin-gothic-urw, Arial, Helvetica, sans-serif !important;
}
ul li a {
    text-decoration: underline !important;
}
a:not([class]) {
    text-decoration-skip-ink: auto;
}
#header {
    font-size: 17px;
    /*border-bottom: 5px solid #232d4b;*/
    /*margin-left: -4.5rem;
    margin-right: -4.5rem;*/
}

#header-inner {
    margin-top: 20px;
    margin-right: 1.5rem; 
    margin-bottom: 0;
    margin-left: 1.5rem; 
}
#main-navigation {
    margin-top: 0;
    margin-right: 0.5rem;
    margin-bottom: 0.25rem;
    margin-left: 0.5rem;
}

.visually-hidden {
    position: absolute !important;
    overflow: hidden;
    clip: rect(1px, 1px, 1px, 1px);
    width: 1px;
    height: 1px;
    word-wrap: normal;
}
.logo-utility {
    display: flex;
    justify-content: space-between;
}

.search-icon {
    display: flex;
    justify-content: space-between;    
    width: 75px;
}
.search-icon svg {
    align-self: center;
    height: 17px;
    width: 17px;
}

#utility-nav {
    margin-top: 0.65rem;
}
#utility-nav a {
    color: #232d4b !important;
}
#utility-nav ul:first-of-type {
    display: flex;
    list-style-type: none;
    gap: 1.5rem;
}
#utility-nav a:hover {
    text-decoration: none !important;
}

nav #uvalibrary-nav .mainlibrary-nav {
    background-color: #fff;
    display: flex;
    list-style-type: none;
    padding: 0;
    margin: 0;
}
nav #uvalibrary-nav .mainlibrary-nav a {
    align-items: center;
    background-color: transparent;
    display: flex;
    padding: 11.5px 1rem;
    font-weight: 500;
    text-decoration: none !important;
}
nav #uvalibrary-nav .mainlibrary-nav a:hover {
    background-color: #dadada;
    color: #232d4b;
    text-decoration: underline !important;
}
.open-mobile-menu {
    display: none;
}
.mobilemenu-content {
    display: none;
}
@media (max-width: 780px) {
    nav.main-nav {
        display: none;
    }
    .utility-nav {
        display: none;
    }
    .open-mobile-menu {
        display: block;
        float: right;
        margin-top: 0.8rem;
        margin-right: 0;
        width: 44px;
        height: 44px;
        border: none;
        background-color: #fff;
        cursor: pointer;
        order: 2;
    }
    .open-mobile-menu svg:hover {
        stroke: #E57200;
    }
    .open-mobile-menu svg:focus {
        outline: 1px dashed #2b2b2b;
    }
    .mobilemenu-content.open {
        display: block;
        height: auto;
        width: fit-content;
    }
    .mobilemenu-content ul {
        overflow: hidden;
        list-style: none;
        position: absolute;
        top: 8.8rem;
        right: 0;
        background-color: #fff;
        border-top-width: 5px;
        border-radius: 0 0 4px 4px;
        display: block;
        list-style-type: none;
        margin: 0;
        min-width: 200px;
        padding: 0;
        z-index: 1000;
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }
    .mobilemenu-content ul li {
        float: none;
        text-align: left;
        width: 100%;
        margin: 0;
    }
    .mobilemenu-content ul li a {
        color: #232D4B;
        font-weight: 400;
        padding: 10px;
        display: block;
        margin: 0;
        text-decoration: underline !important;
        width: 100%;
    }
    .mobilemenu-content ul li a:hover {
        text-decoration: none !important;
        background-color: #DADADA;
    }
    .search-icon svg {
        padding-right: 0.25rem;
    }
    .menu-spacer {
        border-bottom: 1px solid #808080;
    }
}
.extended-hr {
    border-bottom: 5px solid #232d4b;
    margin-left: -1vw;
    margin-right: -1vw;
}
/* NEW 2024 END */


/* keep anchor links from getting stuck behind the fixed header */
html {
scroll-padding-top: 120px;
}
/* MAPS */
 .s-lc-map-link-shape:hover {fill: #EF3F6B; outline: dashed red;}
 .s-lc-map-link-shape:focus {outline: dashed red;}

#s-lc-event-tool-btns {
  padding-bottom: 15px;
}
/*#s-lc-public-bc {
  margin-top: 130px;
}*/
.s-lc-public-footer {
    border-top: none;
   padding: 15px;
}
#s-lg-guide-header-search {
  display: none;
}
#s-lg-guide-header {
      margin-top: 130px;
}
#s-lib-public-header {
  margin-top: 130px;
}
.main-links {
  float: right;
}

.logo {
     width: 215px; 
}

@media only screen and (max-width: 900px) {
  .logo {
    display: none;
  } 
}
.cd-auto-hide-header {
  position: fixed;
  z-index: 4;
  top: 0;
  left: 0;
  width: 100%;
  height: 56px;
  background-color: #141E3C;
  /* Force Hardware Acceleration */
  -webkit-transform: translateZ(0);
          transform: translateZ(0);
  will-change: transform;
  -webkit-transition: -webkit-transform .5s;
  transition: -webkit-transform .5s;
  transition: transform .5s;
  transition: transform .5s, -webkit-transform .5s;
}
.cd-auto-hide-header::after {
  clear: both;
  content: "";
  display: block;
}
.cd-auto-hide-header.is-hidden {
  -webkit-transform: translateY(-100%);
      -ms-transform: translateY(-100%);
          transform: translateY(-100%);
}
@media only screen and (min-width: 1024px) {
  .cd-auto-hide-header {
    height: 47px;
  }
}

.cd-auto-hide-header .logo,
.cd-auto-hide-header .nav-trigger {
  position: absolute;
  top: 50%;
  bottom: auto;
  -webkit-transform: translateY(-50%);
      -ms-transform: translateY(-50%);
          transform: translateY(-50%);
}

.cd-auto-hide-header .logo {
  left: 5%;
}
.cd-auto-hide-header .logo a, .cd-auto-hide-header .logo img {
  display: block;
}

.cd-auto-hide-header .nav-trigger {
  /* vertically align its content */
  display: table;
  height: 100%;
  padding: 0 1em;
  font-size: 1.2rem;
  text-transform: uppercase;
  color: #ffffff;
  font-weight: bold;
  right: 0;
}
.cd-auto-hide-header .nav-trigger span {
  /* vertically align inside parent element */
  display: table-cell;
  vertical-align: middle;
  padding-top: 10px;
}
.cd-auto-hide-header .nav-trigger em, .cd-auto-hide-header .nav-trigger em::after, .cd-auto-hide-header .nav-trigger em::before {
  /* this is the menu icon */
  display: block;
  position: relative;
  height: 3px;
  width: 22px;
  background-color: #ffffff;
  -webkit-backface-visibility: hidden;
          backface-visibility: hidden;
}
.cd-auto-hide-header .nav-trigger em {
  /* this is the menu central line */
  margin: 6px auto 14px;
  -webkit-transition: background-color .2s;
  transition: background-color .2s;
}
.cd-auto-hide-header .nav-trigger em::before, .cd-auto-hide-header .nav-trigger em::after {
  position: absolute;
  content: '';
  left: 0;
  -webkit-transition: -webkit-transform .2s;
  transition: -webkit-transform .2s;
  transition: transform .2s;
  transition: transform .2s, -webkit-transform .2s;
}
.cd-auto-hide-header .nav-trigger em::before {
  /* this is the menu icon top line */
  -webkit-transform: translateY(-6px);
      -ms-transform: translateY(-6px);
          transform: translateY(-6px);
}
.cd-auto-hide-header .nav-trigger em::after {
  /* this is the menu icon bottom line */
  -webkit-transform: translateY(6px);
      -ms-transform: translateY(6px);
          transform: translateY(6px);
}
@media only screen and (min-width: 1024px) {
  .cd-auto-hide-header .nav-trigger {
    display: none;
  }
}

.cd-auto-hide-header.nav-open .nav-trigger em {
  /* transform menu icon into a 'X' icon */
  background-color: rgba(255, 255, 255, 0);
}
.cd-auto-hide-header.nav-open .nav-trigger em::before {
  /* rotate top line */
  -webkit-transform: rotate(-45deg);
      -ms-transform: rotate(-45deg);
          transform: rotate(-45deg);
}
.cd-auto-hide-header.nav-open .nav-trigger em::after {
  /* rotate bottom line */
  -webkit-transform: rotate(45deg);
      -ms-transform: rotate(45deg);
          transform: rotate(45deg);
}

.cd-primary-nav {
  display: inline-block;
  float: right;
  height: 100%;
  padding-right: 5%;
}
.cd-primary-nav > ul {
  position: absolute;
  z-index: 2;
  top: 60px;
  left: 0;
  width: 100%;
  background-color: #1f7eca;
  display: none;
  list-style-type: none;
  box-shadow: 0 14px 20px rgba(0, 0, 0, 0.2);
}
.cd-primary-nav > ul a {
  /* target primary-nav links */
  display: block;
  height: 50px;
  line-height: 50px;
  padding-left: 5%;
  color: #F4FAFD;
  //border-top: 1px solid #f2f2f2;
  text-decoration: none;
}
.cd-primary-nav > ul a:hover, .cd-primary-nav > ul a.active {
    color: #a9a9a9;
}
@media only screen and (min-width: 1024px) {
  .cd-primary-nav {
    /* vertically align its content */
    display: table;
  }
  .cd-primary-nav > ul {
    /* vertically align inside parent element */
    display: table-cell;
    vertical-align: middle;
    /* reset mobile style */
    position: relative;
    width: auto;
    top: 0;
    padding: 0;
    background-color: transparent;
    box-shadow: none;
  }
  .cd-primary-nav > ul::after {
    clear: both;
    content: "";
    display: block;
  }
  .cd-primary-nav > ul li {
    display: inline-block;
    float: left;
    margin-right: 1.5em;
  }
  .cd-primary-nav > ul li:last-of-type {
    margin-right: 0;
  }
  .cd-primary-nav > ul a {
    /* reset mobile style */
    height: auto;
    line-height: normal;
    padding: 15px;
    font-size: 14px;
    border: none;
    text-transform: uppercase;
  }
}

.nav-open .cd-primary-nav ul,
.cd-primary-nav ul:target {
  /* 
  	show primary nav - mobile only 
  	:target is used to show navigation on no-js devices
  */
  display: block;
}
@media only screen and (min-width: 1024px) {
  .nav-open .cd-primary-nav ul,
  .cd-primary-nav ul:target {
    display: table-cell;
  }
}

/* -------------------------------- 

2. Auto-Hiding Navigation - with Sub Nav

-------------------------------- */
.cd-secondary-nav {
  position: relative;
  z-index: 1;
  clear: both;
  width: 100%;
  height: 50px;
  //background-color: #e9f0f4;
  background: #0d3268;
  /* Force Hardware Acceleration */
  -webkit-transform: translateZ(0);
          transform: translateZ(0);
  will-change: transform;
  -webkit-transition: -webkit-transform .5s;
  transition: -webkit-transform .5s;
  transition: transform .5s;
  transition: transform .5s, -webkit-transform .5s;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);
}

.cd-secondary-nav.nav-end::after {
  opacity: 0;
}
.cd-secondary-nav ul, .cd-secondary-nav li, .cd-secondary-nav a {
  height: 100%;
}
.cd-secondary-nav ul {
  /* enables a flex context for all its direct children */
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  padding: 0 5%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
.cd-secondary-nav ul::after {
  clear: both;
  content: "";
  display: block;
}
.cd-secondary-nav li {
  display: inline-block;
  float: left;
  /* do not shrink - elements float on the right of the element */
  -webkit-flex-shrink: 0;
      -ms-flex-negative: 0;
          flex-shrink: 0;
}
.cd-secondary-nav li:last-of-type {
  padding-right: 20px;
}
.cd-secondary-nav a {
  display: block;
  color: #ffffff;
  font-weight: 700;
  line-height: 50px;
  padding: 0 2em;
  text-transform: uppercase;
}
.cd-secondary-nav a:hover {
  opacity: 1;
  text-decoration: none;
  background-color: #1c4694;
}
.cd-secondary-nav a:active {
  opacity: 1;
  text-decoration: none;
  background-color: #0f54d8;
}
@media only screen and (min-width: 1024px) {
  .cd-secondary-nav {
    height: 70px;
    overflow: visible;
  }
  .cd-secondary-nav ul {
    /* reset mobile style */
    display: block;
    text-align: center;
  }
  .cd-secondary-nav li {
    /* reset mobile style */
    float: none;
    -webkit-flex-shrink: 1;
        -ms-flex-negative: 1;
            flex-shrink: 1;
  }
  .cd-secondary-nav a {
    line-height: 70px;
    font-size: 14px;
  }
  .cd-secondary-nav a.active {
    box-shadow: inset 0 -3px #e57200;
  }
}

/* -------------------------------- 

3. Auto-Hiding Navigation - with Sub Nav + Hero Image

-------------------------------- */
.cd-secondary-nav.fixed {
  position: fixed;
  top: 60px;
}
.cd-secondary-nav.slide-up {
  -webkit-transform: translateY(-60px);
      -ms-transform: translateY(-60px);
          transform: translateY(-60px);
}
@media only screen and (min-width: 1024px) {
  .cd-secondary-nav.fixed {
    top: 80px;
    /* fixes a bug where nav and subnab move with a slight delay */
    box-shadow: 0 -6px 0 #25283D;
  }
  .cd-secondary-nav.slide-up {
    -webkit-transform: translateY(-80px);
        -ms-transform: translateY(-80px);
            transform: translateY(-80px);
  }
}

/* -------------------------------- 

Main content

-------------------------------- */
.cd-main-content {
  padding: 60px 5% 2em;
  overflow: hidden;
}
.cd-main-content.sub-nav {
  /* to be used if there is sub nav */
  padding-top: 110px;
}
.cd-main-content.sub-nav-hero {
  /* to be used if there is hero image + subnav */
  padding-top: 0;
}
.cd-main-content.sub-nav-hero.secondary-nav-fixed {
  margin-top: 50px;
}
.cd-main-content p {
  max-width: 1024px;
  line-height: 1.6;
  margin: 2em auto;
  font-family: "David Libre", serif;
  color: #a5a8a9;
}
@media only screen and (min-width: 1024px) {
  .cd-main-content {
    padding-top: 80px;
  }
  .cd-main-content.sub-nav {
    padding-top: 150px;
  }
  .cd-main-content.sub-nav-hero.secondary-nav-fixed {
    margin-top: 70px;
  }
  .cd-main-content p {
    font-size: 2.4rem;
  }
}

/*
	adjust the positioning of in-page links
	http://nicolasgallagher.com/jump-links-and-viewport-positioning/
*/
.cd-main-content.sub-nav :target::before,
.cd-main-content.sub-nav-hero :target::before {
  display: block;
  content: "";
  margin-top: -50px;
  height: 50px;
  visibility: hidden;
}
@media only screen and (min-width: 1024px) {
  .cd-main-content.sub-nav :target::before,
  .cd-main-content.sub-nav-hero :target::before {
    margin-top: -70px;
    height: 70px;
  }
}

/* -------------------------------- 

Intro Section

-------------------------------- */
.cd-hero {
  /* vertically align its content */
  display: table;
  width: 100%;
  margin-top: 60px;
  height: 300px;
  background: url(../img/cd-hero-background.jpg) no-repeat center center;
  background-size: cover;
}
.cd-hero .cd-hero-content {
  /* vertically align inside parent element */
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}
@media only screen and (min-width: 768px) {
  .cd-hero {
    height: 400px;
  }
}
@media only screen and (min-width: 1024px) {
  .cd-hero {
    height: 600px;
    margin-top: 80px;
  }
}
</style>
<style>

.cd-secondary-nav {
  background: #232D4B;
}
.donate-btn {
  margin-top: 10px;
  text-transform: uppercase;
}

.copyright {
  padding-top: 10px;
  color: #fff;
}

.copyright,
.centered-img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 150px;
}

.footer {
  background-color: #232D4B;
  font-family: 'Open Sans', sans-serif;
  margin: 50px -15px 0px -15px;
}
.footer a {
  color: #fff;
  margin-bottom: 5px;
}
.footer img {
  padding-top: 20%;
}

.footer_wrap {
  padding: 25px 0;
}
.footer_wrap h4 {
  color: #fff;
  font-family: 'Open Sans', sans-serif;
  font-weight: 600;
  margin-bottom: 18px;
}
.footer_wrap ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
.footer_wrap ul li {
  color: #fff;
  padding: 5px 0;
}

.footer_wrap ul li a {
  color: #9FB2CE;
}

.footer-extended {
  background-color: #141E3C;
  display: block;
  width: 100%;
  height: 60px;
  bottom: 0;
}
#s-lib-footer-public {
  display: none;
}
.footer-extended-left {
  margin-left: 40px;
  float: left;
  padding-left: 20px;
  padding-top: 22px;
  color: #fff;
}

.footer-extended-right {
  margin-right: 40px;
  float: right;
  padding-top: 22px;
}
.footer-extended-right img {
  width: 50px;
}

ul li.divider {list-style-type: none; padding-bottom: 15px;}
ul li.dropdown-header {font-weight: bold; color: #000;}

.name span {
    font-size: 14px !important;
    height: 14px !important;
}

.name {
    white-space: normal !important;
}
.col-item .info-details {
    min-height: 40px;
    max-height: 40px;
}

</style>
<script>
jQuery(document).ready(function($){
	var mainHeader = $('.cd-auto-hide-header'),
		secondaryNavigation = $('.cd-secondary-nav'),
		//this applies only if secondary nav is below intro section
		belowNavHeroContent = $('.sub-nav-hero'),
		headerHeight = mainHeader.height();
	
	//set scrolling variables
	var scrolling = false,
		previousTop = 0,
		currentTop = 0,
		scrollDelta = 10,
		scrollOffset = 150;

	mainHeader.on('click', '.nav-trigger', function(event){
		// open primary navigation on mobile
		event.preventDefault();
		mainHeader.toggleClass('nav-open');
	});

	$(window).on('scroll', function(){
		if( !scrolling ) {
			scrolling = true;
			(!window.requestAnimationFrame)
				? setTimeout(autoHideHeader, 250)
				: requestAnimationFrame(autoHideHeader);
		}
	});

	$(window).on('resize', function(){
		headerHeight = mainHeader.height();
	});

	function autoHideHeader() {
		var currentTop = $(window).scrollTop();

		( belowNavHeroContent.length > 0 ) 
			? checkStickyNavigation(currentTop) // secondary navigation below intro
			: checkSimpleNavigation(currentTop);

	   	previousTop = currentTop;
		scrolling = false;
	}

	function checkSimpleNavigation(currentTop) {
		//there's no secondary nav or secondary nav is below primary nav
	    if (previousTop - currentTop > scrollDelta) {
	    	//if scrolling up...
	    	mainHeader.removeClass('is-hidden');
	    } else if( currentTop - previousTop > scrollDelta && currentTop > scrollOffset) {
	    	//if scrolling down...
	    	mainHeader.addClass('is-hidden');
	    }
	}

	function checkStickyNavigation(currentTop) {
		//secondary nav below intro section - sticky secondary nav
		var secondaryNavOffsetTop = belowNavHeroContent.offset().top - secondaryNavigation.height() - mainHeader.height();
		
		if (previousTop >= currentTop ) {
	    	//if scrolling up... 
	    	if( currentTop < secondaryNavOffsetTop ) {
	    		//secondary nav is not fixed
	    		mainHeader.removeClass('is-hidden');
	    		secondaryNavigation.removeClass('fixed slide-up');
	    		belowNavHeroContent.removeClass('secondary-nav-fixed');
	    	} else if( previousTop - currentTop > scrollDelta ) {
	    		//secondary nav is fixed
	    		mainHeader.removeClass('is-hidden');
	    		secondaryNavigation.removeClass('slide-up').addClass('fixed'); 
	    		belowNavHeroContent.addClass('secondary-nav-fixed');
	    	}
	    	
	    } else {
	    	//if scrolling down...	
	 	  	if( currentTop > secondaryNavOffsetTop + scrollOffset ) {
	 	  		//hide primary nav
	    		mainHeader.addClass('is-hidden');
	    		secondaryNavigation.addClass('fixed slide-up');
	    		belowNavHeroContent.addClass('secondary-nav-fixed');
	    	} else if( currentTop > secondaryNavOffsetTop ) {
	    		//once the secondary nav is fixed, do not hide primary nav if you haven't scrolled more than scrollOffset 
	    		mainHeader.removeClass('is-hidden');
	    		secondaryNavigation.addClass('fixed').removeClass('slide-up');
	    		belowNavHeroContent.addClass('secondary-nav-fixed');
	    	}

	    }
	}
});

/* NEW 2024 */
$(document).ready(function(){
    $(".open-mobile-menu").on("click", function(){
        $(".mobilemenu-content").toggleClass("open");
    });
});
</script>
<script src="//static.lib.virginia.edu/js/controllers/libcal.js"></script>
</head>
<body id="equip_" class="s-lc-public s-lc-public-page-5">


<a id="s-lc-public-skiplink" class="s-lc-skiplink alert-info" href="#s-lc-public-title-area">Skip to Main Content</a>

<div id="s-lc-public-cust-header" role="banner">        <link rel="stylesheet" media="all" href="https://use.typekit.net/oym8nvz.css" />
        <header id="header" role="banner" aria-label="Site header">
            <div id="header-inner" class="logo-utility">
                <button id="openmobilemenu" tabindex="0" class="open-mobile-menu" aria-label="open menu">
                    <svg
                        aria-hidden="true"
                        role="img"
                        xmlns="http://www.w3.org/2000/svg"
                        width="28"
                        height="28"
                        viewBox="0 0 24 24"
                        fill="transparent"
                        stroke="#232d4b"
                        stroke-width="2"
                        stroke-linecap="butt"
                        stroke-linejoin="bevel">
                        <line x1="3" y1="12" x2="21" y2="12"></line>
                        <line x1="3" y1="6" x2="21" y2="6"></line>
                        <line x1="3" y1="18" x2="21" y2="18"></line>
                    </svg>
                </button>
                <div id="block-uvalibrary-v2a-branding">
                    <a href="https://www.library.virginia.edu/" title="Home" rel="home" class="site-logo">
                        <svg
                            version="1.1"
                            id="svg1"
                            width="225.99001"
                            height="50.999939"
                            viewBox="0 0 225.99005 50.99994"
                            sodipodi:docname="library_lovo-web.svg"
                            inkscape:version="1.3 (0e150ed, 2023-07-21)"
                            xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
                            xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
                            xmlns="http://www.w3.org/2000/svg"
                            xmlns:svg="http://www.w3.org/2000/svg">
                            <defs id="defs1" />
                            <sodipodi:namedview
                                id="namedview1"
                                pagecolor="#ffffff"
                                bordercolor="#000000"
                                borderopacity="0.25"
                                inkscape:showpageshadow="2"
                                inkscape:pageopacity="0.0"
                                inkscape:pagecheckerboard="0"
                                inkscape:deskcolor="#d1d1d1"
                                inkscape:zoom="8.7644228"
                                inkscape:cx="84.77455"
                                inkscape:cy="10.496983"
                                inkscape:window-width="2144"
                                inkscape:window-height="945"
                                inkscape:window-x="0"
                                inkscape:window-y="25"
                                inkscape:window-maximized="0"
                                inkscape:current-layer="g1"
                                showguides="true"
                                showborder="true"
                                shape-rendering="auto">
                                <inkscape:page
                                    x="0"
                                    y="0"
                                    inkscape:label="1"
                                    id="page1"
                                    width="225.99005"
                                    height="50.999939"
                                    margin="0"
                                    bleed="0" />
                            </sodipodi:namedview>
                            <g id="g1" inkscape:groupmode="layer" inkscape:label="1">
                                <g id="uvaliblogo" transform="matrix(0.51765451,0,0,0.51763689,0,0.00262142)">
                                    <title id="title1">University of Virginia Library</title>
                                    <path
                                        id="path2"
                                        d="m 1689.58,0.00390625 h -6.32 V 738.938 h 6.32 V 0.00390625"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path3"
                                        d="m 218.199,391.609 h 27.215 V 261.984 h -27.215 v 129.625"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path4"
                                        d="M 71.2266,391.609 H 97.5859 V 261.984 H 71.2266 v 129.625"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path5"
                                        d="m 106.652,391.609 h 28.106 V 261.984 h -28.106 v 129.625"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path6"
                                        d="m 143.836,391.609 h 28.105 V 261.984 h -28.105 v 129.625"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path7"
                                        d="m 209.117,261.984 h -28.101 v 129.625 h 28.101 V 261.984"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path8"
                                        d="M 233.723,400.77 H 82.3242 l 77.7108,47.812 z"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path9"
                                        d="m 0.0351563,449.07 v -48.3 H 64.8945 l 78.5155,48.3 H 0.0351563"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path10"
                                        d="M 176.066,449.07 H 315.742 V 400.773 H 250.5 l -74.434,48.297"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path11"
                                        d="M 295.754,458.23 H 20.0313 c 26.996,48.7 78.6093,81.622 137.8477,81.622 59.246,0 110.867,-32.922 137.875,-81.622"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path12"
                                        d="m 0.0351563,369.223 v 7.527 L 1.85156,375.434 0.535156,371.391 Z M 53.7617,261.984 H 41.5391 l 6.1093,4.446 z m 8.3985,0 h -8.3516 l -2.3359,7.207 6.1718,4.493 h -7.6367 l -2.3594,7.265 -2.3554,-7.265 h -7.6367 l 6.1875,-4.493 -2.3516,-7.207 H 0.0351563 L 0,340.148 l 0.0351563,28.184 5.7968737,4.203 6.17187,-4.48 -2.35937,7.261 6.17577,4.481 H 8.19141 l -2.35938,7.262 -1.07812,-3.313 -1.48438,-3.949 H 0.0351563 v 11.812 H 62.1602 Z M 0,340.148 l 6.1875,-4.48 -2.36719,-7.266 6.17578,4.481 6.17191,-4.481 -2.3594,7.266 6.1797,4.48 h -7.6328 l -2.35941,7.258 -2.35937,-7.258 z m 21.2695,-41.21 -2.3672,-7.254 6.1719,4.48 6.1836,-4.48 -2.3594,7.254 6.168,4.484 h -7.6328 l -2.3594,7.266 -2.3594,-7.266 h -7.6289 l 6.1836,-4.484"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path13"
                                        d="M 0.0351563,218.422 H 62.1602 v 34.414 H 0.0351563 v -34.414"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path14"
                                        d="m 254.484,252.836 h 61.254 v -34.414 h -61.254 v 34.414"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path15"
                                        d="m 161.656,218.422 h -6.988 l 3.473,2.527 z m -47.031,10.117 -2.379,-7.266 6.184,4.481 6.172,-4.481 -2.36,7.266 6.176,4.481 h -7.629 l -2.359,7.265 -2.36,-7.265 h -7.632 z m 39.711,-4.816 -1.727,-5.301 H 71.2266 v 34.414 h 10.0351 l -1.7422,-5.391 h -7.6367 l 6.1914,-4.484 -2.3789,-7.254 6.1797,4.481 6.168,-4.481 -2.3477,7.254 6.1719,4.484 h -7.6328 l -1.7461,5.391 H 233.711 l -1.746,-5.391 h -7.629 l 6.172,-4.484 -2.356,-7.254 6.176,4.481 6.172,-4.481 -2.375,7.254 6.188,4.484 h -7.625 l -1.754,5.391 h 10.48 v -34.414 h -81.73 l -1.723,5.301 6.176,4.484 H 160.5 l -2.359,7.254 -2.36,-7.254 h -7.629 z m 46.133,4.816 6.187,4.481 h -7.636 l -2.356,7.265 -2.355,-7.265 h -7.637 l 6.18,-4.481 -2.364,-7.266 6.176,4.481 6.176,-4.481 -2.371,7.266"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path16"
                                        d="m 315.742,376.449 v -5.937 l -1.562,4.797 z m 0,-114.453 h -41.035 -12.269 -7.95 v 129.617 h 61.254 v -11.808 h -3.012 l -2.359,7.254 -2.363,-7.254 h -7.625 l 6.172,-4.496 -2.36,-7.254 6.176,4.48 5.371,-3.902 v -28.485 h -7.176 l -2.359,7.258 -2.359,-7.258 h -7.629 l 6.164,-4.48 -2.356,-7.266 6.18,4.481 6.172,-4.481 -2.367,7.266 5.73,4.148 z m -41.035,0 -2.352,7.207 6.184,4.481 h -7.633 l -2.355,7.265 -2.363,-7.265 h -7.633 l 6.179,-4.481 -2.343,-7.207 6.16,4.434 6.105,-4.434 z m 20.215,36.942 6.191,4.492 h -7.636 l -2.356,7.246 -2.359,-7.246 h -7.633 l 6.176,-4.492 -2.364,-7.266 6.18,4.492 6.168,-4.492 -2.367,7.266"
                                        style="fill: #e5691a; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path17"
                                        d="m 440.859,364.016 c 22.239,0 37.84,5.879 48.063,15.336 14.312,12.273 19.941,28.378 21.476,49.343 0.766,9.969 1.274,54.707 1.274,58.285 0,3.575 0,39.883 0.512,42.43 0.765,3.074 1.535,10.231 10.996,10.231 h 10.484 c 1.274,0 1.527,1.027 1.527,2.558 v 5.621 c 0,0.766 -0.253,1.793 -2.558,1.793 -2.301,-0.008 -10.477,-0.765 -28.113,-0.765 -17.137,0 -28.895,0.757 -31.454,0.757 -1.531,0.008 -1.785,-0.5 -1.785,-1.785 v -6.136 c 0,-1.278 0.254,-2.043 1.785,-2.043 h 11.258 c 6.645,0 10.735,-4.598 11.496,-11.25 0.774,-6.387 1.278,-21.215 1.278,-40.645 v -54.707 c 0,-18.922 -3.321,-34.262 -13.293,-44.992 -8.942,-9.207 -23.77,-14.059 -38.34,-14.059 -14.832,0 -31.192,4.606 -40.649,18.407 -5.878,8.687 -7.925,20.707 -8.183,32.464 -0.254,8.18 -1.274,40.649 -1.274,54.196 v 16.871 c 0,13.039 0.258,30.937 0.508,33.23 0.512,5.625 4.856,10.485 12.27,10.485 h 12.781 c 1.793,0 2.047,0.507 2.047,1.789 v 6.644 c 0,1.031 -0.254,1.539 -2.301,1.539 -2.805,-0.008 -15.086,-0.765 -35.023,-0.765 -19.938,0 -32.465,0.757 -35.02,0.757 -2.047,0.008 -2.301,-0.5 -2.301,-2.039 v -5.625 c 0,-1.793 0.254,-2.3 1.789,-2.3 h 12.016 c 7.926,0 9.711,-4.09 9.711,-13.036 v -60.839 c 0,-33.493 1.027,-50.618 4.094,-62.125 4.086,-16.106 13.035,-27.356 30.418,-34.258 8.437,-3.574 21.222,-5.367 34.511,-5.367"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path18"
                                        d="m 650.754,452.16 c 0,11.383 -0.559,28.883 0.836,41.66 0.551,3.887 1.941,5.832 8.887,5.832 h 2.773 c 1.113,0 1.668,0.832 1.668,1.942 v 5.84 c 0,1.664 -0.555,2.218 -1.941,2.218 -1.946,0 -11.668,-0.836 -17.497,-0.836 -8.89,0 -20.835,0.836 -22.777,0.836 -1.387,0 -1.949,-0.554 -1.949,-1.386 v -6.672 c 0,-1.379 0.562,-1.942 1.949,-1.942 h 4.727 c 4.715,0 8.886,-1.668 10.273,-4.996 1.387,-3.336 2.215,-19.441 2.215,-26.109 0.559,-8.891 0.84,-17.5 0.84,-33.332 v -18.332 h -1.113 c -3.329,3.613 -29.165,36.109 -34.165,41.941 -5.832,6.942 -37.773,47.219 -38.609,48.328 -1.109,1.664 -2.773,2.227 -6.664,2.227 -3.332,0 -9.164,-0.563 -13.609,-0.563 -3.055,0 -7.5,0.282 -11.11,0.563 -3.613,0 -6.664,0.273 -7.218,0.273 -1.114,0 -1.672,-0.836 -1.672,-1.668 v -6.668 c 0,-1.101 0.558,-1.664 1.672,-1.664 h 2.492 c 7.785,0 14.726,-4.718 14.726,-14.718 V 455.77 c 0,-31.387 -0.554,-51.11 -0.832,-54.438 C 543.82,394.945 539.383,393 536.602,393 h -6.391 c -0.828,0 -1.113,-0.277 -1.113,-0.84 v -7.222 c 0,-1.379 0.285,-1.942 0.836,-1.942 2.222,0 14.722,0.84 18.613,0.84 8.051,0 19.16,-0.84 21.101,-0.84 1.395,0 1.395,0.563 1.395,1.672 v 6.664 c 0,1.113 0,1.668 -1.395,1.668 h -5.828 c -2.773,0 -5.84,3.059 -6.672,9.438 -0.55,2.507 -1.66,30.281 -1.66,46.941 v 38.055 h 0.547 c 4.449,-5 26.945,-35 33.621,-42.774 3.051,-3.605 14.992,-17.777 27.766,-33.055 11.387,-13.605 20.832,-24.996 22.773,-26.937 1.114,-0.832 3.887,-2.781 6.395,-2.781 3.332,0 4.164,2.781 4.164,5.281 v 64.992"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path19"
                                        d="m 716.707,454.934 c 0,1.945 0.277,35 0.277,37.773 0.274,5.836 2.774,6.949 10.274,6.949 h 4.726 c 1.387,0 1.668,0.836 1.668,1.942 v 6.664 c 0,0.832 -0.558,1.394 -1.668,1.394 -2.226,0 -16.39,-0.836 -24.445,-0.836 -13.055,-0.277 -30.273,0.836 -31.941,0.836 -1.106,0 -1.664,-0.562 -1.664,-1.672 v -6.386 c 0,-1.106 0.277,-1.942 1.664,-1.942 h 5 c 11.664,0 14.168,-2.777 14.168,-5.84 0,-3.882 0.554,-31.66 0.554,-36.109 v -12.211 c 0,-9.441 -0.281,-44.723 -0.554,-47.219 -0.555,-5 -5.004,-5.277 -11.946,-5.277 h -6.109 c -1.113,0 -1.664,-0.832 -1.664,-1.664 v -6.117 c 0,-1.383 0.551,-2.219 1.664,-2.219 1.66,0 17.773,0.836 27.223,0.836 12.492,0 26.937,-0.836 29.16,-0.836 1.39,0 1.664,0.836 1.664,1.945 v 6.664 c 0,0.829 -0.274,1.391 -1.664,1.391 h -4.172 c -8.047,0 -11.383,3.887 -11.938,10.273 -0.277,4.172 -0.277,36.106 -0.277,37.774 v 13.887"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path20"
                                        d="m 1019.4,494.656 c 0,5 4.17,6.106 8.33,6.106 11.11,0 18.88,-2.496 26.38,-7.215 5,-3.332 9.17,-10.832 9.17,-19.168 0,-7.223 -4.72,-28.895 -35.55,-28.895 -3.61,0 -6.4,0.286 -8.33,0.563 z M 998.281,447.16 c -0.273,-16.941 0,-33.328 -0.273,-46.937 0,-6.114 -3.328,-7.223 -9.988,-7.223 h -3.34 c -1.114,0 -1.672,-0.555 -1.672,-1.391 v -6.386 c 0,-1.391 0.558,-2.223 1.672,-2.223 1.937,0 16.1,0.832 23.05,0.832 9.17,0 24.16,-0.832 26.11,-0.832 1.67,0 2.23,0.555 2.23,1.945 v 6.664 c 0,0.836 -0.56,1.391 -1.68,1.391 h -7.22 c -5.55,0 -7.22,3.055 -7.77,6.938 v 30 6.667 c 1.93,0.555 4.44,0.555 7.22,0.555 11.66,0 15.83,-6.113 25.83,-23.328 2.49,-4.172 14.72,-26.664 20,-30.555 4.72,0.278 11.38,0.555 17.78,0.555 2.77,0 6.1,-0.277 8.6,-0.277 2.78,-0.278 5,-0.555 5.56,-0.555 1.1,0 1.67,0.832 1.67,1.945 v 5.551 c 0,1.672 -0.28,2.504 -1.4,2.504 -5,0 -8.6,0.277 -12.49,3.055 -5.28,3.883 -11.67,12.218 -15.56,17.777 -11.38,16.106 -16.94,24.715 -23.33,26.102 v 0.562 c 21.94,7.774 32.77,18.887 32.77,38.047 0,6.387 -3.61,14.441 -9.72,20.273 -6.93,6.118 -19.43,10.84 -36.11,10.84 -3.6,0 -27.77,-0.836 -31.1,-0.836 -5,0 -22.218,0.836 -23.612,0.836 -1.106,0 -1.66,-0.562 -1.66,-1.394 v -6.664 c 0,-1.114 0.273,-1.942 1.105,-1.942 h 2.781 c 7.782,0 10.274,-3.058 10.547,-8.613 V 464.379 447.16"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path21"
                                        d="m 1153.09,380.5 c 25.27,0 38.6,17.777 38.6,38.605 0,13.891 -3.33,20.833 -8.88,26.665 -6.94,7.222 -17.22,10.277 -30,15 -5.27,1.949 -15.28,6.109 -19.44,11.386 -3.06,3.614 -4.44,9.442 -4.44,13.61 0,5 4.44,16.941 19.71,16.941 8.06,0 14.17,-2.777 18.34,-7.492 5.83,-6.672 8.06,-16.391 9.72,-19.723 0.27,-0.836 0.83,-1.394 1.66,-1.113 l 5.01,1.113 c 0.82,0.278 1.1,0.828 1.1,1.664 -0.28,3.891 -2.77,21.942 -2.77,31.11 0,1.39 -0.28,2.496 -2.5,2.496 -2.23,0 -3.05,0 -3.61,-0.832 l -1.11,-1.946 c -0.56,-1.386 -1.95,-1.113 -4.73,0.559 -3.33,1.664 -9.16,3.609 -19.71,3.609 -10,0 -18.9,-2.496 -26.12,-8.332 -6.11,-5.273 -11.94,-13.886 -11.94,-23.328 0,-13.613 3.34,-22.5 9.73,-28.609 8.32,-7.504 21.66,-12.5 27.21,-14.445 14.72,-5.555 25.56,-12.493 25.56,-28.329 0,-11.941 -13.33,-18.89 -22.23,-18.89 -10.27,0 -19.43,5.554 -23.6,13.89 -5,9.164 -5,14.996 -5,18.887 0,1.109 -1.11,1.664 -2.22,1.949 l -5,0.551 c -1.11,0 -1.66,-0.836 -1.95,-1.941 -0.27,-4.45 -2.22,-26.668 -3.05,-34.442 -0.28,-1.39 0.55,-2.504 2.22,-3.054 2.22,-0.559 3.61,0 4.16,1.386 l 0.84,2.223 c 0.56,2.219 2.23,1.941 4.17,0.551 6.39,-5 16.1,-9.719 30.27,-9.719"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path22"
                                        d="m 1238.75,454.934 c 0,1.945 0.27,35 0.27,37.773 0.28,5.836 2.78,6.949 10.27,6.949 h 4.73 c 1.39,0 1.67,0.836 1.67,1.942 v 6.664 c 0,0.832 -0.56,1.394 -1.67,1.394 -2.22,0 -16.38,-0.836 -24.44,-0.836 -13.05,-0.277 -30.28,0.836 -31.94,0.836 -1.11,0 -1.68,-0.562 -1.68,-1.672 v -6.386 c 0,-1.106 0.29,-1.942 1.68,-1.942 h 4.99 c 11.67,0 14.17,-2.777 14.17,-5.84 0,-3.882 0.56,-31.66 0.56,-36.109 v -12.211 c 0,-9.441 -0.28,-44.723 -0.56,-47.219 -0.55,-5 -4.99,-5.277 -11.94,-5.277 h -6.1 c -1.12,0 -1.67,-0.832 -1.67,-1.664 v -6.117 c 0,-1.383 0.55,-2.219 1.67,-2.219 1.66,0 17.77,0.836 27.21,0.836 12.5,0 26.94,-0.836 29.16,-0.836 1.39,0 1.66,0.836 1.66,1.945 v 6.664 c 0,0.829 -0.27,1.391 -1.66,1.391 h -4.16 c -8.06,0 -11.39,3.887 -11.95,10.273 -0.27,4.172 -0.27,36.106 -0.27,37.774 v 13.887"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path23"
                                        d="m 491.418,303.246 c -4.219,0 -8.082,3.34 -8.082,8.965 0,8.262 4.219,18.984 10.191,28.477 8.789,14.238 18.106,20.917 25.489,20.917 5.8,0 8.964,-4.406 8.785,-9.843 0,-11.602 -18.102,-48.516 -36.383,-48.516 m 2.637,-8.43 c 25.488,0 40.781,34.973 40.781,54.309 0,11.945 -7.035,20.559 -18.809,20.559 -23.379,0 -40.078,-30.051 -40.078,-52.2 0,-13.359 8.438,-22.668 18.106,-22.668"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path24"
                                        d="m 783.602,290.344 c 0,1.953 0.277,35 0.277,37.785 0.277,5.82 2.777,6.934 10.277,6.934 h 4.723 c 1.391,0 1.668,0.839 1.668,1.941 v 6.68 c 0,0.82 -0.559,1.386 -1.668,1.386 -2.227,0 -16.391,-0.84 -24.445,-0.84 -13.051,-0.273 -30.274,0.84 -31.942,0.84 -1.105,0 -1.66,-0.566 -1.66,-1.668 v -6.398 c 0,-1.102 0.277,-1.941 1.66,-1.941 h 5 c 11.668,0 14.168,-2.774 14.168,-5.821 0,-3.898 0.555,-31.672 0.555,-36.113 v -12.227 c 0,-9.433 -0.281,-44.707 -0.555,-47.207 -0.555,-5 -5.008,-5.285 -11.945,-5.285 h -6.102 c -1.121,0 -1.672,-0.828 -1.672,-1.668 v -6.105 c 0,-1.387 0.551,-2.227 1.672,-2.227 1.66,0 17.77,0.84 27.215,0.84 12.492,0 26.945,-0.84 29.16,-0.84 1.391,0 1.664,0.84 1.664,1.953 v 6.66 c 0,0.832 -0.273,1.387 -1.664,1.387 h -4.172 c -8.046,0 -11.382,3.899 -11.937,10.285 -0.277,4.16 -0.277,36.102 -0.277,37.762 v 13.887"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path25"
                                        d="m 846.699,330.063 c 0,5 4.168,6.113 8.336,6.113 11.106,0 18.883,-2.5 26.383,-7.219 4.996,-3.328 9.164,-10.828 9.164,-19.168 0,-7.219 -4.727,-28.887 -35.547,-28.887 -3.617,0 -6.394,0.282 -8.336,0.555 z M 823.996,282.57 c -0.277,-16.941 0,-33.32 -0.277,-46.933 0,-6.114 -3.34,-7.227 -10.008,-7.227 h -3.332 c -1.106,0 -1.66,-0.547 -1.66,-1.387 v -6.386 c 0,-1.395 0.554,-2.227 1.66,-2.227 1.945,0 16.105,0.832 23.051,0.832 9.175,0 24.168,-0.832 26.113,-0.832 1.66,0 2.227,0.559 2.227,1.945 v 6.668 c 0,0.84 -0.567,1.387 -1.665,1.387 h -7.222 c -5.563,0 -7.223,3.059 -7.785,6.945 v 30 6.668 c 1.945,0.547 4.445,0.547 7.222,0.547 11.66,0 15.825,-6.101 25.832,-23.32 2.5,-4.168 14.715,-26.68 20,-30.566 4.727,0.285 11.391,0.558 17.774,0.558 2.777,0 6.105,-0.273 8.613,-0.273 2.777,-0.285 4.988,-0.559 5.555,-0.559 1.113,0 1.664,0.832 1.664,1.945 v 5.555 c 0,1.672 -0.274,2.5 -1.387,2.5 -5,0 -8.617,0.285 -12.504,3.059 -5.273,3.886 -11.664,12.215 -15.551,17.781 -11.386,16.105 -16.945,24.707 -23.332,26.105 v 0.555 c 21.942,7.774 32.774,18.887 32.774,38.047 0,6.387 -3.613,14.445 -9.727,20.273 -6.937,6.125 -19.437,10.84 -36.097,10.84 -3.614,0 -27.774,-0.84 -31.11,-0.84 -5,0 -22.219,0.84 -23.613,0.84 -1.113,0 -1.66,-0.566 -1.66,-1.394 v -6.66 c 0,-1.114 0.281,-1.953 1.109,-1.953 h 2.778 c 7.781,0 10.281,-3.047 10.558,-8.606 v -26.66 -17.227"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path26"
                                        d="m 1035.77,257.023 c 0,4.719 5.27,5.832 8.05,5.832 h 4.73 c 0.83,0 1.38,0.84 1.38,1.668 v 6.661 c 0,0.839 -0.55,1.386 -1.68,1.386 -1.1,0 -13.6,-0.547 -23.87,-0.547 -15,0 -28.61,0.547 -30.271,0.547 -1.121,0 -1.398,-0.547 -1.398,-1.386 v -6.661 c 0,-0.828 0.277,-1.394 1.398,-1.394 h 6.661 c 7.22,0 13.61,-1.934 13.61,-8.332 v -10.274 c 0,-5.554 -0.56,-9.168 -4.17,-11.941 -4.45,-3.605 -13.327,-6.113 -23.046,-6.113 -7.781,0 -18.887,4.168 -26.664,12.5 -10.836,11.386 -16.949,27.215 -16.949,48.601 0,12.5 6.113,27.219 14.445,36.387 10.281,11.113 21.113,14.172 29.719,14.172 12.775,0 20.555,-5.559 28.055,-13.332 6.67,-6.668 11.38,-15.281 13.33,-19.727 0.84,-2.226 1.38,-2.5 2.22,-2.226 l 5.28,1.679 c 0.83,0.266 1.11,0.821 1.11,2.207 -0.55,5 -4.17,30.833 -4.17,32.227 0,1.945 -0.55,3.059 -3.06,3.059 -2.21,0 -3.05,-0.84 -3.6,-1.946 l -1.39,-2.507 c -0.56,-0.821 -1.67,-0.821 -3.89,1.113 -5.28,3.887 -18.33,8.894 -31.662,8.894 -19.723,0 -36.661,-5.84 -49.711,-16.953 -13.336,-11.66 -20.559,-28.601 -20.559,-45.547 0,-21.66 5.555,-36.66 16.672,-48.875 13.043,-14.445 35.269,-20.285 49.711,-20.285 17.769,0 32.769,3.887 47.489,11.113 1.95,0.84 3.06,1.672 3.06,3.047 0,1.399 -0.83,3.059 -0.83,5.567 v 21.386"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path27"
                                        d="m 1086.69,290.344 c 0,1.953 0.28,35 0.28,37.785 0.28,5.82 2.77,6.934 10.27,6.934 h 4.73 c 1.38,0 1.66,0.839 1.66,1.941 v 6.68 c 0,0.82 -0.56,1.386 -1.66,1.386 -2.23,0 -16.39,-0.84 -24.44,-0.84 -13.06,-0.273 -30.28,0.84 -31.95,0.84 -1.1,0 -1.67,-0.566 -1.67,-1.668 v -6.398 c 0,-1.102 0.29,-1.941 1.67,-1.941 h 5 c 11.67,0 14.17,-2.774 14.17,-5.821 0,-3.898 0.55,-31.672 0.55,-36.113 v -12.227 c 0,-9.433 -0.27,-44.707 -0.55,-47.207 -0.56,-5 -4.99,-5.285 -11.95,-5.285 h -6.11 c -1.11,0 -1.66,-0.828 -1.66,-1.668 v -6.105 c 0,-1.387 0.55,-2.227 1.66,-2.227 1.68,0 17.78,0.84 27.23,0.84 12.5,0 26.94,-0.84 29.15,-0.84 1.39,0 1.67,0.84 1.67,1.953 v 6.66 c 0,0.832 -0.28,1.387 -1.67,1.387 h -4.15 c -8.06,0 -11.39,3.899 -11.95,10.285 -0.28,4.16 -0.28,36.102 -0.28,37.762 v 13.887"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path28"
                                        d="m 1236.8,287.57 c 0,11.387 -0.55,28.887 0.84,41.672 0.55,3.887 1.94,5.828 8.88,5.828 h 2.78 c 1.11,0 1.67,0.832 1.67,1.934 v 5.84 c 0,1.672 -0.56,2.219 -1.95,2.219 -1.94,0 -11.66,-0.833 -17.5,-0.833 -8.89,0 -20.83,0.833 -22.77,0.833 -1.39,0 -1.95,-0.547 -1.95,-1.379 v -6.68 c 0,-1.387 0.56,-1.934 1.95,-1.934 h 4.72 c 4.72,0 8.88,-1.679 10.28,-5 1.39,-3.34 2.22,-19.441 2.22,-26.101 0.55,-8.899 0.83,-17.5 0.83,-33.34 v -18.332 h -1.11 c -3.34,3.613 -29.16,36.113 -34.16,41.945 -5.84,6.934 -37.77,47.215 -38.61,48.328 -1.12,1.66 -2.78,2.219 -6.66,2.219 -3.34,0 -9.16,-0.559 -13.62,-0.559 -3.05,0 -7.5,0.286 -11.11,0.559 -3.6,0 -6.67,0.274 -7.22,0.274 -1.11,0 -1.67,-0.833 -1.67,-1.661 v -6.672 c 0,-1.113 0.56,-1.66 1.67,-1.66 h 2.5 c 7.78,0 14.72,-4.726 14.72,-14.726 v -29.16 c 0,-31.387 -0.55,-51.114 -0.83,-54.442 -0.83,-6.387 -5.28,-8.32 -8.05,-8.32 h -6.39 c -0.83,0 -1.11,-0.285 -1.11,-0.84 v -7.227 c 0,-1.386 0.28,-1.945 0.84,-1.945 2.21,0 14.71,0.832 18.6,0.832 8.05,0 19.17,-0.832 21.11,-0.832 1.39,0 1.39,0.559 1.39,1.672 v 6.66 c 0,1.113 0,1.68 -1.39,1.68 h -5.84 c -2.77,0 -5.83,3.047 -6.66,9.433 -0.56,2.5 -1.68,30.282 -1.68,46.942 v 38.047 h 0.57 c 4.44,-5 26.93,-35 33.6,-42.774 3.06,-3.613 15,-17.773 27.78,-33.047 11.39,-13.613 20.83,-25 22.78,-26.941 1.1,-0.84 3.88,-2.785 6.38,-2.785 3.33,0 4.17,2.785 4.17,5.285 v 64.988"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: evenodd; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path29"
                                        d="m 554.449,360.199 h -15.648 c -0.879,0 -1.305,0.864 -0.957,2.09 l 0.707,2.992 c 0.351,1.227 1.566,4.043 2.969,4.043 h 15.293 c 5.273,15.117 10.386,27.418 19.703,37.793 4.922,5.621 14.593,11.949 26.015,11.949 10.196,0 15.821,-6.16 15.821,-10.378 0,-5.442 -3.516,-8.079 -7.032,-8.079 -5.625,0 -7.207,3.168 -7.73,7.032 -0.18,1.757 -1.938,5.097 -7.211,5.097 -16.348,0 -19.883,-23.218 -25.676,-42.91 0,0 24.426,-0.648 44.363,-0.648 21.477,0 32.981,0.765 35.282,0.765 2.3,0 2.558,-0.765 2.558,-1.789 v -5.886 c 0,-1.278 -0.258,-2.297 -2.047,-2.297 h -12.277 c -7.156,0 -10.73,-2.305 -10.73,-6.649 0,-2.043 0.253,-5.109 1.015,-8.683 1.539,-9.207 10.996,-39.629 15.602,-53.946 3.066,-9.715 17.89,-53.679 23.773,-69.277 5.875,12.012 25.817,64.668 27.863,70.559 2.559,6.902 12.274,36.296 16.102,47.539 2.043,6.394 3.586,10.996 3.586,14.578 0,3.066 -1.789,5.879 -8.184,5.879 h -6.644 c -1.027,0 -1.277,0.765 -1.277,2.297 v 5.886 c 0,1.274 0.25,1.789 1.531,1.789 2.293,0 14.062,-0.765 30.164,-0.765 18.664,0 25.055,0.765 27.347,0.765 1.54,0 1.797,-0.515 1.797,-1.789 v -6.39 c 0,-1.028 -0.257,-1.793 -1.797,-1.793 h -6.894 c -8.438,0 -13.293,-4.09 -18.148,-9.969 -6.649,-8.184 -27.098,-60.586 -31.446,-71.328 -3.07,-8.438 -36.043,-89.727 -37.324,-92.278 -1.023,-2.05 -2.301,-3.328 -3.574,-3.328 -2.051,0 -3.071,2.559 -4.356,5.879 -8.172,23.524 -28.883,81.805 -32.207,91.004 l -2.554,8.692 c -6.137,18.156 -18.149,55.226 -21.473,62.89 -2.555,5.891 -5.113,8.438 -10.484,8.438 l -23.774,0.226 c -4.566,-14.238 -12.656,-44.316 -21.441,-66.816 -10.723,-27.414 -23.2,-46.934 -42.012,-46.934 -7.027,0 -12.656,4.754 -12.656,10.379 0,4.043 2.992,7.559 7.558,7.559 5.098,0 7.735,-4.922 8.262,-7.918 0.352,-1.75 1.586,-2.981 2.988,-2.981 8.442,0 17.93,14.766 27.422,47.278 l 17.832,59.433"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path30"
                                        d="m 1269.38,510.066 c 0.35,0.25 0.24,0.25 1.08,0.157 4.32,-0.481 20.08,-1.957 50.59,-1.957 h 11.11 c 9.09,0 18.86,0.371 29.44,0.808 5.32,0.153 37.95,-0.258 44.61,-0.258 6.11,0 25,0.836 26.95,0.836 1.11,0 1.94,-0.554 1.94,-1.945 v -6.113 c 0,-1.11 -0.27,-1.942 -1.94,-1.942 h -4.17 c -4.99,0 -5.28,-3.054 -4.16,-4.718 1.66,-2.504 24.72,-39.442 29.16,-46.11 4.16,6.946 27.22,40.555 28.34,42.774 2.21,4.441 2.49,8.054 -3.62,8.054 h -4.45 c -1.39,0 -1.94,0.832 -1.94,1.942 v 6.113 c 0,1.109 0.55,1.945 1.94,1.945 1.67,0 15.56,-0.836 23.89,-0.836 5,0 14.72,0.836 16.39,0.836 1.39,0 1.94,-0.554 1.94,-2.222 v -5.836 c 0,-1.379 -0.55,-1.942 -1.66,-1.942 h -2.79 c -4.44,0 -7.49,-0.832 -9.99,-2.222 -4.17,-2.223 -36.39,-47.492 -42.78,-57.215 v -23.332 c 0.28,-6.945 0,-14.445 0.56,-17.778 0.56,-5.832 5.01,-6.109 10,-6.109 h 3.6 c 1.4,0 1.96,-0.551 1.96,-1.383 v -6.668 c 0,-1.113 -0.56,-1.949 -2.23,-1.949 -1.66,0 -17.21,0.836 -26.39,0.836 -6.11,0 -22.21,-0.836 -23.88,-0.836 -1.38,0 -1.94,0.563 -1.94,2.227 v 6.109 c 0,0.828 0.56,1.664 1.66,1.664 h 4.16 c 8.9,0 10.57,1.672 10.84,5.559 0.28,2.492 0.28,12.5 0.28,28.883 v 10 c -2.5,4.996 -36.38,54.714 -40.83,58.882 -2.35,2.352 -6.29,3.106 -8.8,3.285 1.66,-7.523 3.9,-17.386 4.78,-22.171 0.28,-1.114 -0.27,-1.668 -1.38,-2.219 l -4.73,-1.395 c -1.66,-0.55 -2.49,-0.273 -3.05,1.114 -3.34,6.937 -8.07,16.113 -13.88,21.386 -6.95,2.5 -27.27,2.778 -32.27,2.778 v -46.664 c 0,-29.161 0,-49.996 0.28,-52.215 0.55,-4.442 1.94,-7.223 6.39,-7.223 h 10.54 c 1.4,0 1.96,-0.836 1.96,-2.496 v -5.84 c 0,-0.828 -0.56,-1.664 -1.96,-1.664 -1.94,0 -19.16,0.836 -28.32,0.836 -7.78,0 -25.83,-0.836 -28.05,-0.836 -1.67,0 -2.23,0.836 -2.23,2.504 v 5.555 c 0,1.39 0.56,1.941 1.67,1.941 h 11.12 c 4.16,0 6.1,2.223 6.38,4.442 0.83,10.558 0.83,25.281 0.83,41.945 v 59.715 c -5.28,0 -20.87,0.273 -31.15,-2.5 -6.94,-5.278 -12.77,-14.164 -16.38,-21.383 -0.56,-1.117 -1.4,-1.945 -2.51,-1.395 l -4.99,1.946 c -1.39,0.554 -1.39,1.668 -1.11,2.781 1.6,5.047 6.42,22.168 8.68,30.578 0.12,0.441 0.16,0.703 0.51,0.941"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path31"
                                        d="m 1302.76,290.344 v -13.887 c 0,-1.66 0,-33.602 0.27,-37.762 0.56,-6.386 3.89,-10.285 11.94,-10.285 h 3.21 c 4.72,0 9.17,2.785 11.39,5.832 1.94,2.227 16.11,35.555 22.77,49.434 1.95,3.894 18.33,41.668 20,46.387 0.55,1.679 2.23,4.726 0.27,5.566 -0.55,0.547 -1.38,1.941 -1.11,2.773 -0.27,0.555 0.28,1.387 2.78,1.942 5.28,0.832 13.07,5.84 15.56,8.058 0.56,1.114 1.66,1.942 3.33,1.942 1.67,0 2.22,-1.114 2.78,-3.047 3.89,-11.121 18.06,-50.84 21.66,-61.942 4.17,-13.886 16.11,-46.66 18.06,-49.433 3.6,-5.012 8.33,-7.512 13.05,-7.512 h 5.28 c 1.11,0 1.39,-0.828 1.39,-1.668 v -5.832 c 0,-0.828 -0.28,-2.5 -1.95,-2.5 -3.33,0 -18.05,0.84 -24.44,0.84 -5.28,0 -21.66,-0.84 -25.27,-0.84 -1.95,0 -2.22,1.387 -2.22,2.5 v 5.832 c 0,0.84 0.27,1.668 1.38,1.668 h 4.45 c 3.33,0 4.44,2.5 4.44,4.719 -1.11,5.566 -8.61,27.781 -10.83,34.168 h -44.72 c -1.11,-3.328 -10,-26.387 -11.12,-29.715 -1.66,-5.559 -0.82,-9.172 5.01,-9.172 h 6.95 c 1.66,0 1.94,-0.828 1.94,-1.941 v -6.106 c 0,-1.113 -0.28,-1.953 -1.67,-1.953 -2.22,0 -16.94,0.84 -21.39,0.84 h -45.97 c -9.45,0 -25.55,-0.84 -27.22,-0.84 -1.11,0 -1.66,0.84 -1.66,2.227 v 6.105 c 0,0.84 0.55,1.668 1.66,1.668 h 6.11 c 6.95,0 11.38,0.285 11.94,5.285 0.28,2.5 0.56,37.774 0.56,47.207 v 12.227 c 0,4.441 -0.56,32.215 -0.56,36.113 0,3.047 -2.5,5.821 -14.17,5.821 h -4.99 c -1.39,0 -1.67,0.839 -1.67,1.941 v 6.398 c 0,1.102 0.55,1.668 1.67,1.668 1.67,0 18.88,-1.113 31.94,-0.84 8.05,0 22.22,0.84 24.44,0.84 1.11,0 1.66,-0.566 1.66,-1.386 v -6.68 c 0,-1.102 -0.28,-1.941 -1.66,-1.941 h -4.73 c -7.49,0 -9.99,-1.114 -10.27,-6.934 0,-2.785 -0.27,-35.832 -0.27,-37.785 m 57.64,-14.16 h 37.78 c -1.12,3.886 -14.18,45.546 -14.73,47.773 -0.56,1.672 -0.83,2.773 -1.66,2.773 -0.84,0 -1.39,-0.828 -2.23,-3.054 -0.84,-2.219 -17.77,-44.707 -19.16,-47.492"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path32"
                                        d="m 795.715,507.707 v -6.391 c 0,-1.101 -0.844,-1.664 -1.945,-1.664 h -6.395 c -3.605,0 -7.77,-0.554 -7.77,-4.168 0,-6.39 4.719,-17.218 12.219,-40.55 2.227,-6.938 12.504,-39.161 14.164,-43.61 h 0.836 c 1.66,5.836 15.274,40.281 16.664,44.446 10.547,30.828 14.164,38.324 14.164,41.109 0,1.387 -1.109,2.773 -5.828,2.773 h -3.058 c -1.114,0 -1.676,0.563 -1.676,1.942 v 6.39 c 0,0.832 0.562,1.668 1.676,1.668 1.664,0 16.109,-0.836 22.5,-0.836 h 42.457 l 62.203,0.282 c 2.785,0 6.394,0.554 7.5,0.554 0.566,0 1.117,-0.554 1.679,-3.886 0.551,-2.504 8.333,-26.387 8.887,-28.332 0.274,-1.114 0.274,-1.668 -0.281,-1.942 l -4.441,-1.945 c -0.563,-0.277 -1.676,-0.277 -2.504,1.105 -0.547,0.84 -13.895,16.395 -18.61,20.832 -3.324,3.059 -7.773,4.168 -10.547,4.168 l -29.453,0.563 v -47.223 c 1.676,0 18.063,0.832 20.274,1.387 7.222,1.941 10.004,5.836 10.004,14.441 0,1.114 0.273,1.395 1.386,1.395 l 6.11,-0.281 c 1.113,0 1.953,-0.555 1.675,-1.664 -0.562,-2.5 -0.562,-17.223 -0.562,-19.723 0,-6.113 0.84,-14.723 1.113,-18.328 0,-1.114 -0.551,-1.395 -1.386,-1.395 l -5.836,-0.551 c -0.836,0 -1.387,0 -1.664,1.11 -1.387,6.941 -3.059,11.39 -10.278,13.051 -8.336,1.949 -18.054,1.949 -20.836,1.949 v -9.449 c 0,-9.715 0.563,-25.825 0.563,-29.438 0,-13.051 8.051,-13.887 19.992,-13.887 12.223,0 20,0.274 29.449,7.774 2.211,1.664 11.938,14.164 14.719,18.613 1.387,1.942 2.773,2.223 3.601,1.664 l 4.454,-2.5 c 0.546,-0.277 1.105,-1.105 0.824,-1.941 l -9.992,-29.446 c -0.555,-1.386 -1.946,-2.777 -3.059,-2.777 -1.941,0 -16.656,0.836 -74.984,0.836 -5.012,0 -20.278,-0.836 -23.618,-0.836 -1.386,0 -1.667,0.836 -1.667,1.942 v 6.394 c 0,1.113 0.566,1.664 1.945,1.664 h 2.504 c 13.051,0 13.886,1.113 13.886,5.004 v 41.934 17.226 c 0,14.719 -0.273,32.774 -0.554,35.547 -0.832,5.836 -2.496,6.945 -13.61,6.945 h -2.183 -0.59 -3.859 c -5.274,0 -9.161,-1.668 -11.661,-4.168 -5.277,-5.277 -20.281,-41.66 -23.054,-48.879 -2.496,-5.832 -25.274,-60.273 -27.492,-63.886 -0.832,-1.387 -2.231,-2.219 -4.454,-2.219 -2.211,0 -3.601,1.945 -4.445,4.16 -6.101,16.387 -20.828,56.664 -23.043,62.774 l -1.949,6.113 c -4.715,12.777 -13.051,38.051 -14.996,40.824 -2.227,3.059 -4.445,5.281 -8.055,5.281 h -2.773 c -1.114,0 -1.387,0.832 -1.387,1.664 v 6.95 c 0,0.832 0.547,1.386 1.664,1.386 1.383,0 16.66,-0.836 23.887,-0.836 6.672,0 23.605,0.836 25.269,0.836 1.676,0 2.227,-0.554 2.227,-1.945"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path33"
                                        d="m 2069.09,312.668 c 0.63,-0.625 0.63,-1.25 0.63,-3.133 -1.25,-1.875 -13.78,-53.859 -15.66,-62.305 -8.14,0.313 -98.32,0.938 -130.26,0.938 -28.17,0 -39.45,-0.938 -43.21,-0.938 -2.5,0 -2.5,0.625 -2.5,2.813 v 7.207 c 0,1.875 0,2.5 1.87,2.5 h 12.53 c 11.27,0 13.16,4.383 13.16,8.457 0,5.633 1.25,83.914 1.25,102.703 v 17.535 c 0,20.039 -0.63,53.235 -1.25,58.555 -0.64,8.145 -1.89,11.273 -10.02,11.273 h -13.16 c -1.88,0 -2.51,1.879 -2.51,2.821 v 7.199 c 0,1.883 0.63,2.508 2.51,2.508 3.13,0 14.41,-0.942 43.21,-0.942 33.81,0 46.98,0.942 49.48,0.942 2.5,0 3.12,-1.258 3.12,-2.821 v -7.203 c 0,-1.254 -0.62,-2.504 -3.12,-2.504 h -16.92 c -9.39,0 -10.64,-3.128 -10.64,-11.585 0,-4.383 -1.25,-51.352 -1.25,-73.27 v -26.93 c 0,-5.636 0,-73.273 1.25,-86.738 h 17.54 c 17.54,0 40.08,0 52.61,1.563 17.52,2.507 37.56,40.085 41.95,51.98 1.25,1.262 1.87,1.887 3.76,1.262 l 5.63,-1.887"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path34"
                                        d="m 2149.1,349.621 c 0,-3.133 0.64,-75.156 0.64,-78.601 0,-10.02 5.01,-11.27 12.52,-11.27 h 13.15 c 1.25,0 2.5,-0.625 2.5,-2.187 v -7.833 c 0,-1.875 -1.25,-2.5 -3.12,-2.5 -3.76,0 -16.29,0.938 -45.73,0.938 -31.3,0 -45.08,-0.938 -48.22,-0.938 -1.87,0 -2.5,0.625 -2.5,2.188 v 8.457 c 0,1.25 0.63,1.875 2.5,1.875 h 12.53 c 6.26,0 13.15,0.625 14.4,9.082 0.63,4.383 1.25,72.02 1.25,88.926 v 21.922 c 0,7.515 -0.62,63.879 -0.93,67.949 -0.94,7.516 -4.07,10.644 -12.83,10.644 h -16.29 c -1.88,0 -2.5,0.625 -2.5,2.196 v 8.136 c 0,1.571 0.62,2.196 1.87,2.196 3.76,0 20.04,-0.942 50.72,-0.942 30.07,0 40.09,0.942 44.48,0.942 1.87,0 2.5,-1.258 2.5,-2.821 v -7.203 c 0,-1.879 -1.25,-2.504 -2.5,-2.504 h -11.91 c -6.88,0 -11.89,-2.503 -11.89,-8.457 0,-3.128 -0.64,-72.015 -0.64,-75.769 v -24.426"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path35"
                                        d="m 2298.42,257.25 c 24.42,0 46.96,11.582 46.96,49.785 0,25.672 -12.52,41.953 -30.06,48.848 -11.89,5.008 -25.05,5.633 -35.69,5.633 h -8.14 v -62.625 c 0,-29.434 6.89,-41.641 26.93,-41.641 z m -26.93,114.285 c 5.01,-0.312 9.39,-0.312 14.4,-0.312 13.78,0 26.31,3.449 33.19,9.082 11.91,9.394 16.28,23.175 16.28,36.949 0,11.898 -3.75,24.426 -13.77,31.937 -11.28,8.145 -26.31,10.961 -35.7,10.961 -3.12,0 -6.88,0 -9.39,-0.629 -1.88,-0.625 -3.75,-2.5 -4.07,-5.003 -0.31,-5.954 -0.94,-32.883 -0.94,-59.184 z m -38.21,13.156 c 0,11.274 -0.62,49.473 -0.93,54.793 -0.94,18.164 -5.95,18.789 -17.85,18.789 h -10.02 c -1.88,0 -2.51,0.625 -2.51,2.504 v 7.203 c 0,1.879 0.63,2.821 2.51,2.821 4.39,0 19.42,-1.258 45.72,-0.942 10.02,0 28.81,0.942 45.71,0.942 23.8,0 43.85,-2.196 55.12,-8.457 17.54,-9.399 23.8,-23.797 23.8,-42.586 0,-25.047 -13.16,-40.078 -42.59,-51.039 v -1.563 c 35.69,-9.398 56.36,-28.187 56.36,-61.371 0,-16.914 -9.4,-39.453 -24.43,-47.597 -13.14,-7.52 -33.18,-10.958 -68.26,-10.958 -12.52,0 -33.18,0.938 -45.71,0.938 -24.43,0 -37.58,-0.938 -44.15,-0.938 -1.25,0 -2.2,0.938 -2.2,2.5 v 7.833 c 0,1.562 0.95,2.187 2.2,2.187 h 13.46 c 9.4,0 11.59,3.758 12.52,13.465 0.63,7.512 1.25,48.848 1.25,74.523 v 36.953"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path36"
                                        d="m 2688.91,346.801 c 2.19,7.207 30.36,84.23 31.62,88.304 0.94,2.817 2.19,4.067 4.06,4.067 1.26,0 1.89,-1.879 3.14,-5.641 1.88,-6.258 23.17,-77.648 26.3,-86.73 z m -199.9,10.332 c -3.76,0 -7.52,0.625 -11.91,1.254 l 0.64,90.179 c 0,3.754 1.25,7.516 3.75,9.082 2.5,1.563 6.26,1.875 11.28,1.875 15.65,0 30.05,-3.441 41.32,-13.46 7.84,-7.204 13.77,-20.665 13.77,-35.075 0,-14.398 -10.01,-53.855 -58.85,-53.855 z m 360.85,-97.383 h -10.03 c -6.26,0 -14.41,3.758 -20.04,14.402 -4.39,8.457 -24.43,66.7 -31.95,91.125 -5.63,20.039 -30.06,90.18 -35.68,109.594 -0.64,1.879 -1.89,5.637 -3.77,5.637 -1.56,0 -2.81,-1.258 -4.7,-3.133 -3.75,-3.758 -20.97,-13.148 -30.99,-15.656 -2.5,-0.625 -3.13,-1.883 -3.13,-3.133 0,-0.938 0.94,-2.816 1.88,-3.754 1.88,-1.887 0,-7.516 -0.63,-10.644 l -30.69,-82.047 c -9.39,-26.297 -31.94,-82.664 -35.07,-88.301 -5.63,-9.707 -14.91,-14.11 -24.6,-14.11 -9.69,0 -14.85,3.211 -18.42,5.34 -3.57,2.141 -24.73,32.571 -26.61,35.703 -2.51,3.762 -21.92,33.196 -25.67,38.196 -4.4,5.644 -10.03,11.277 -18.79,14.402 v 1.262 c 34.43,5.633 58.24,21.918 58.24,61.371 0,11.898 -5.64,25.051 -16.91,35.066 -12.53,11.274 -31.95,19.731 -57,19.731 -9.39,0 -38.2,-0.942 -55.73,-0.942 -30.68,0 -40.71,0.942 -42.9,0.942 -1.56,0 -2.19,-0.625 -2.19,-2.196 v -8.453 c 0,-1.254 0.63,-1.879 2.19,-1.879 h 12.22 c 5.63,0 10.01,-5.007 10.01,-15.66 v -82.347 c 0,-29.434 0,-58.868 -0.63,-90.184 0,-8.457 -5,-10.332 -11.89,-10.332 h -10.65 c -1.25,0 -1.87,-0.937 -1.87,-2.5 v -7.207 c 0,-1.875 0.62,-2.813 2.5,-2.813 3.12,0 10.64,0.938 41.33,0.938 32.57,0 38.83,-0.938 42.9,-0.938 2.5,0 3.44,0.625 3.44,2.813 v 7.52 c 0,1.25 -0.63,2.187 -2.51,2.187 h -15.65 c -5.01,0 -7.2,5.633 -8.13,11.895 -0.64,4.707 -1.26,39.773 -1.26,58.562 v 16.906 c 3.44,0.313 8.77,0.625 10.02,0.625 13.15,0 20.35,-8.457 28.18,-19.414 5.01,-6.886 13.77,-21.289 16.91,-26.926 2.82,-5.007 15.02,-27.558 20.67,-36.328 4.07,-6.57 10.02,-15.027 13.77,-17.84 6.89,0.313 18.79,0.938 27.57,0.938 h 56.48 c 21.91,0 35.06,-0.938 39.45,-0.938 1.88,0 2.5,1.25 2.5,3.125 v 7.833 c 0,0.937 -0.62,1.562 -3.12,1.562 h -13.16 c -6.26,0 -11.28,3.445 -11.28,7.52 0,1.562 0,4.062 0.63,6.57 1.56,8.457 16.91,53.234 19.41,60.441 h 72.65 c 3.76,-11.593 16.29,-51.672 18.79,-62.949 1.88,-8.449 -0.63,-11.582 -9.4,-11.582 h -8.13 c -1.89,0 -2.51,-0.625 -2.51,-2.5 v -6.27 c 0,-1.875 0.62,-3.75 3.13,-3.75 6.89,0 17.53,0.938 43.83,0.938 34.46,0 40.72,-0.938 46.36,-0.938 2.5,0 3.13,1.875 3.13,3.75 v 6.583 c 0,1.562 -0.63,2.187 -2.5,2.187"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path37"
                                        d="m 2926.42,358.387 c 4.37,-0.629 8.13,-1.254 11.9,-1.254 48.84,0 58.86,39.457 58.86,53.855 0,14.41 -5.95,27.871 -13.77,35.075 -11.28,10.019 -25.67,13.46 -41.34,13.46 -5.02,0 -8.77,-0.312 -11.28,-1.875 -2.5,-1.566 -3.75,-5.328 -3.75,-9.082 z m -0.63,-28.18 c 0,-18.789 0.63,-53.855 1.25,-58.562 0.94,-6.262 3.13,-11.895 8.14,-11.895 h 15.65 c 1.89,0 2.51,-0.937 2.51,-2.187 v -7.52 c 0,-2.188 -0.94,-2.813 -3.45,-2.813 -4.06,0 -10.32,0.938 -42.89,0.938 -30.69,0 -38.2,-0.938 -41.33,-0.938 -1.88,0 -2.5,0.938 -2.5,2.813 v 7.207 c 0,1.563 0.62,2.5 1.87,2.5 h 10.65 c 6.89,0 11.9,1.875 11.9,10.332 0.62,31.316 0.62,60.75 0.62,90.18 v 82.351 c 0,10.649 -4.38,15.66 -10.02,15.66 h -12.21 c -1.56,0 -2.19,0.625 -2.19,1.879 v 8.453 c 0,1.571 0.63,2.196 2.19,2.196 2.2,0 12.21,-0.942 42.9,-0.942 17.54,0 46.34,0.942 55.74,0.942 25.05,0 44.46,-8.457 56.99,-19.731 11.26,-10.015 16.91,-23.168 16.91,-35.066 0,-39.453 -23.81,-55.742 -58.25,-61.371 v -1.262 c 8.76,-3.125 14.4,-8.758 18.79,-14.402 3.76,-5 23.18,-34.434 25.68,-38.203 1.87,-3.125 21.91,-31.309 26.61,-35.696 5.95,-5.32 14.72,-5.945 22.24,-5.945 1.87,0 2.5,-0.937 2.5,-2.187 v -6.583 c 0,-2.187 -0.63,-3.125 -2.5,-3.125 -2.51,0 -10.65,0.938 -30.69,0.938 -8.78,0 -20.66,-0.625 -27.56,-0.938 -3.76,2.813 -9.7,11.27 -13.78,17.84 -5.63,8.77 -17.84,31.321 -20.66,36.328 -3.13,5.637 -11.9,20.04 -16.9,26.926 -7.85,10.957 -15.04,19.414 -28.2,19.414 -1.25,0 -6.57,-0.312 -10.01,-0.625 v -16.906"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                    <path
                                        id="path38"
                                        d="m 3179.05,306.41 c 0,-11.906 0.63,-32.57 0.94,-36.015 0.94,-10.02 5.95,-10.645 12.21,-10.645 h 10.33 c 1.57,0 2.2,-0.937 2.2,-2.187 v -7.208 c 0,-2.187 -0.63,-3.125 -2.2,-3.125 -3.44,0 -15.97,0.938 -44.14,0.938 -30.69,0 -40.72,-0.938 -43.53,-0.938 -1.57,0 -2.2,1.25 -2.2,2.813 v 7.207 c 0,1.25 0.63,2.5 2.2,2.5 h 12.84 c 8.13,0 10.64,3.133 10.95,7.832 0.33,4.375 0.95,28.809 0.95,58.242 v 15.028 c -5.02,9.394 -55.74,99.57 -64.51,110.535 -3.76,4.383 -10.65,6.886 -15.65,6.886 h -5.65 c -1.87,0 -2.5,0.625 -2.5,2.196 v 8.449 c 0,1.258 0.63,1.883 2.5,1.883 2.51,0 17.54,-0.942 41.34,-0.942 31.94,0 43.21,0.942 46.35,0.942 1.87,0 2.5,-0.625 2.5,-2.196 v -7.203 c 0,-1.879 -0.63,-3.129 -2.5,-3.129 h -8.15 c -6.88,0 -9.39,-2.503 -8.77,-9.082 0.63,-5.632 38.21,-75.144 46.66,-92.683 10.65,17.539 51.04,82.664 51.67,90.492 0.63,5.637 -1.26,11.273 -10.65,11.273 h -8.14 c -1.88,0 -2.51,0.938 -2.51,2.504 v 7.828 c 0,1.571 0.63,2.196 1.89,2.196 3.12,0 16.28,-0.942 38.19,-0.942 20.05,0 26.94,0.942 30.06,0.942 1.88,0 2.51,-0.625 2.51,-2.196 v -7.203 c 0,-1.879 -0.63,-3.129 -2.51,-3.129 h -6.88 c -4.39,0 -11.91,-1.878 -16.92,-7.203 -5,-5.632 -56.98,-85.793 -68.88,-106.457 V 306.41"
                                        style="fill: #232b47; fill-opacity: 1; fill-rule: nonzero; stroke: none"
                                        transform="matrix(0.13333333,0,0,-0.13333333,0,98.52)" />
                                </g>
                            </g>
                        </svg>
                    </a>
                    <div class="site-name-slogan"></div>
                </div>
                <nav role="navigation" id="block-uvalibrary-v2a-utilitynavmain" class="utility-nav">
                    <h2 class="visually-hidden" id="block-uvalibrary-v2a-utilitynavmain-menu">Utility Nav-main</h2>

                    <div id="utility-nav">
                        <ul role="menu">
                            <li>
                                <a href="https://search.lib.virginia.edu/account">My account</a>
                            </li>
                            <li>
                                <a href="https://library.virginia.edu/askalibrarian">Ask a Librarian</a>
                            </li>
                            <li>
                                <a href="https://library.virginia.edu/hours">Hours</a>
                            </li>
                            <li>
                                <a href="https://library.virginia.edu/support-library">Give</a>
                            </li>
                            <li>
                                <a href="https://library.virginia.edu/search" class="search-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M507.3 484.7l-141.5-141.5C397 306.8 415.1 259.7 415.1 208c0-114.9-93.13-208-208-208S-.0002 93.13-.0002 208S93.12 416 207.1 416c51.68 0 98.85-18.96 135.2-50.15l141.5 141.5C487.8 510.4 491.9 512 496 512s8.188-1.562 11.31-4.688C513.6 501.1 513.6 490.9 507.3 484.7zM208 384C110.1 384 32 305 32 208S110.1 32 208 32S384 110.1 384 208S305 384 208 384z" fill="#2B2B2B"/></svg>Search</a>
                            </li>
                        </ul>
                    </div>
                </nav>
            </div>
            <div id="main-navigation" class="main-navigation-wrapper">
                <nav
                    role="navigation"
                    aria-labelledby="block-uvalibrary-v2a-main-menu-menu"
                    id="block-uvalibrary-v2a-main-menu"
                    class="main-nav">
                    <h2 class="visually-hidden" id="block-uvalibrary-v2a-main-menu-menu">Main navigation</h2>

                    <div id="uvalibrary-nav">
                        <ul class="mainlibrary-nav">
                            <li>
                                <a href="https://www.library.virginia.edu/about-uva-library">About</a>
                            </li>
                            <li>
                                <a href="https://www.library.virginia.edu/services">Using the Library</a>
                            </li>
                            <li>
                                <a href="https://www.library.virginia.edu/teaching-and-writing">Teaching &amp; publication support</a>
                            </li>
                            <li>
                                <a href="https://www.library.virginia.edu/help" class="link-main">Get help</a>
                            </li>
                        </ul>
                    </div>
                </nav>
            </div>
            <div class="mobilemenu-content">
                <ul>
                    <li>
                        <a href="https://www.library.virginia.edu/about-uva-library">About</a>
                    </li>
                    <li>
                        <a href="https://www.library.virginia.edu/services">Using the Library</a>
                    </li>
                    <li>
                        <a href="https://www.library.virginia.edu/teaching-and-writing">Teaching &amp; publication support</a>
                    </li>
                    <li>
                        <a href="https://www.library.virginia.edu/help" class="link-main">Get help</a>
                    </li>
                    <li class="menu-spacer">
                    </li>
                    <li>
                        <a href="https://search.lib.virginia.edu/account">My account</a>
                    </li>
                    <li>
                        <a href="https://library.virginia.edu/askalibrarian">Ask a Librarian</a>
                    </li>
                    <li>
                        <a href="https://library.virginia.edu/hours">Hours</a>
                    </li>
                    <li>
                        <a href="https://library.virginia.edu/support-library">Give</a>
                    </li>
                    <li>
                        <a href="https://library.virginia.edu/search" class="search-icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><!--! Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M507.3 484.7l-141.5-141.5C397 306.8 415.1 259.7 415.1 208c0-114.9-93.13-208-208-208S-.0002 93.13-.0002 208S93.12 416 207.1 416c51.68 0 98.85-18.96 135.2-50.15l141.5 141.5C487.8 510.4 491.9 512 496 512s8.188-1.562 11.31-4.688C513.6 501.1 513.6 490.9 507.3 484.7zM208 384C110.1 384 32 305 32 208S110.1 32 208 32S384 110.1 384 208S305 384 208 384z" fill="#2B2B2B"/></svg>Search</a>
                    </li>
                </ul>
            </div>
        </header>
<div class="extended-hr"></div></div>
<div class="container">
    
    <div id="s-lc-public-bc" class="row">
        <div class="col-md-12">
            <nav aria-label="Breadcrumb">
                <ol class="breadcrumb">
                    <li><a href="http://www.library.virginia.edu/">UVA Library</a></li>

                    <li class="s-lc-desktop-only"><a href="https://cal.lib.virginia.edu">UVA Library Calendar</a></li>

                                            <li><a href="/r/accessible?lid=1411&amp;gid=2181&amp;zone=7108&amp;space=8403&amp;capacity=2">New Reservation</a></li>
                    
                    
                                        </ol>
            </nav>
        </div>
    </div>

    <noscript>
        <div class="alert alert-danger" id="noscript">Your browser has javascript disabled. Without javascript some functions will not work.</div>
    </noscript>

    <div id="s-lc-public-title-area">
            <div id="s-lc-public-title" class="row s-lc-spaces-setup-info">
        <div class="col-md-12">
            <h1 id="s-lc-public-pt">
                    Space For 5-8 people

@ Brown Science &amp; Engineering Library (Clark Hall)
            </h1>
        </div>
    </div>
    </div>

    <main>
            <div id="s-lc-public-main" class="s-lc-public-main">
        <div id="s-lc-public-page-content" class="row">
            <div id="col1" class="col-md-12 center">
                <div id="s-lc-eq-times" aria-live="polite" class="s-lc-spaces-setup-info">
                    

    <p id="s-lc-new-reservation-filter-text" class="s-lc-spaces-setup-info">
        There are 1 booking option(s) available for         the &quot;Group Study Rooms&quot; category and         the &quot;Main Floor - Brown&quot; zone.

        
                    <a id="s-lc-new-reservation-go-back" href="/r/accessible?lid=1411&amp;gid=2181&amp;zone=7108&amp;space=8403&amp;capacity=2">You can go back and change the filters.</a>
            </p>

                                            <form id="s-lc-eq-filters-form" method="get" action="/r/accessible/availability">
                            <input type="hidden" id="lid" name="lid" value="1411">

                            <input type="hidden" id="gid" name="gid" value="2181">

                            <input type="hidden" id="zone" name="zone" value="7108">

                            <input type="hidden" id="space" name="space" value="8403">

                            <input type="hidden" id="capacity" name="capacity" value="2">

                            
                            <div class="form-group">
                                <label class="control-label" for="date">
                                    Date
                                </label>

                                <select id="date" name="date" class="form-control">
                                    
                                                                            <option value="2024-11-04" >
                                            Monday, November 4, 2024
                                        </option>
                                                                            <option value="2024-11-05" selected="selected">
                                            Tuesday, November 5, 2024
                                        </option>
                                                                            <option value="2024-11-06" >
                                            Wednesday, November 6, 2024
                                        </option>
                                                                            <option value="2024-11-07" >
                                            Thursday, November 7, 2024
                                        </option>
                                                                            <option value="2024-11-08" >
                                            Friday, November 8, 2024
                                        </option>
                                                                            <option value="2024-11-09" >
                                            Saturday, November 9, 2024
                                        </option>
                                                                            <option value="2024-11-10" >
                                            Sunday, November 10, 2024
                                        </option>
                                                                            <option value="2024-11-11" >
                                            Monday, November 11, 2024
                                        </option>
                                                                            <option value="2024-11-12" >
                                            Tuesday, November 12, 2024
                                        </option>
                                                                            <option value="2024-11-13" >
                                            Wednesday, November 13, 2024
                                        </option>
                                                                            <option value="2024-11-14" >
                                            Thursday, November 14, 2024
                                        </option>
                                                                            <option value="2024-11-15" >
                                            Friday, November 15, 2024
                                        </option>
                                                                            <option value="2024-11-16" >
                                            Saturday, November 16, 2024
                                        </option>
                                                                            <option value="2024-11-17" >
                                            Sunday, November 17, 2024
                                        </option>
                                                                            <option value="2024-11-18" >
                                            Monday, November 18, 2024
                                        </option>
                                                                            <option value="2024-11-19" >
                                            Tuesday, November 19, 2024
                                        </option>
                                                                            <option value="2024-11-20" >
                                            Wednesday, November 20, 2024
                                        </option>
                                                                            <option value="2024-11-21" >
                                            Thursday, November 21, 2024
                                        </option>
                                                                            <option value="2024-11-22" >
                                            Friday, November 22, 2024
                                        </option>
                                                                            <option value="2024-11-23" >
                                            Saturday, November 23, 2024
                                        </option>
                                                                            <option value="2024-11-24" >
                                            Sunday, November 24, 2024
                                        </option>
                                                                            <option value="2024-11-25" >
                                            Monday, November 25, 2024
                                        </option>
                                                                    </select>
                            </div>

                            <div class="form-group">
                                <button class="btn btn-primary" type="submit" id="s-lc-submit-filters">
                                    Show Availability
                                </button>
                            </div>
                        </form>

                        <div id="s-lc-group-area">
                            <form id="s-lc-eq-times-form" method="post">
                                <div id="s-lc-eq-checkboxes" role="main" style="clear: both;">
                                    
            
        <div class="panel panel-default">
            <div class="panel-heading">
                <h2 class="panel-title">
                    Brown 147

                                            <span class="pull-right s-lc-eqw-rcap text-muted">
                            Capacity
                            6
                        </span>
                    
                    
                </h2>
            </div>

            <div class="panel-body" id="slots-8403">
                
                <fieldset>
                    <legend class="sr-only">
                        Brown 147
                    </legend>

                    

                    
                            
            
                    <p>Tuesday, November 5, 2024</p>
    
    
    <div class="checkbox">
        <label for="s8403_0_1730782800">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730782800"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 00:00:00"
                   data-end="2024-11-05 00:30:00"
                   data-crc="e89533d9ab112aa6c78b8911b9c401d2"
            >
                    
                    12:00AM - 12:30AM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730784600">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730784600"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 00:30:00"
                   data-end="2024-11-05 01:00:00"
                   data-crc="bffaec223c5c0dbf195e0b24d7d6aae4"
            >
                    
                    12:30AM - 1:00AM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730786400">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730786400"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 01:00:00"
                   data-end="2024-11-05 01:30:00"
                   data-crc="cc1e82a57b66071b8a9ae03c7a7f1256"
            >
                    
                    1:00AM - 1:30AM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730788200">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730788200"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 01:30:00"
                   data-end="2024-11-05 02:00:00"
                   data-crc="e44e7e19090b292144b55c866e683bb6"
            >
                    
                    1:30AM - 2:00AM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730811600">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730811600"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 08:00:00"
                   data-end="2024-11-05 08:30:00"
                   data-crc="c2f86635cea933f462d8974966813356"
            >
                    
                    8:00AM - 8:30AM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730813400">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730813400"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 08:30:00"
                   data-end="2024-11-05 09:00:00"
                   data-crc="80c6fa1e0957798bd5cb1a24e209f698"
            >
                    
                    8:30AM - 9:00AM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730815200">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730815200"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 09:00:00"
                   data-end="2024-11-05 09:30:00"
                   data-crc="b862c34a983628d5c7be0ce38e48ac83"
            >
                    
                    9:00AM - 9:30AM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730847600">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730847600"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 18:00:00"
                   data-end="2024-11-05 18:30:00"
                   data-crc="c60c35cad0e8f438ceb9bbbdfa7d00b7"
            >
                    
                    6:00PM - 6:30PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730849400">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730849400"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 18:30:00"
                   data-end="2024-11-05 19:00:00"
                   data-crc="aa2808f9544fb694179354e4b692d377"
            >
                    
                    6:30PM - 7:00PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730851200">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730851200"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 19:00:00"
                   data-end="2024-11-05 19:30:00"
                   data-crc="624dacd2d7ccba49b4945835fad490c2"
            >
                    
                    7:00PM - 7:30PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730853000">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730853000"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 19:30:00"
                   data-end="2024-11-05 20:00:00"
                   data-crc="a9a110fdeecfe935dd29d4fb1522183a"
            >
                    
                    7:30PM - 8:00PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730854800">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730854800"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 20:00:00"
                   data-end="2024-11-05 20:30:00"
                   data-crc="1ee1b8f0deed09df48c8a4a762c836a0"
            >
                    
                    8:00PM - 8:30PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730856600">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730856600"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 20:30:00"
                   data-end="2024-11-05 21:00:00"
                   data-crc="3c5acd5ed736d8b8b946a63a34e4aded"
            >
                    
                    8:30PM - 9:00PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730858400">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730858400"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 21:00:00"
                   data-end="2024-11-05 21:30:00"
                   data-crc="07acaa0b40a73480e617f5fd9d08e510"
            >
                    
                    9:00PM - 9:30PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730860200">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730860200"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 21:30:00"
                   data-end="2024-11-05 22:00:00"
                   data-crc="d5ad2130b1af072934d21f23b7023b89"
            >
                    
                    9:30PM - 10:00PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730862000">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730862000"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 22:00:00"
                   data-end="2024-11-05 22:30:00"
                   data-crc="e7d532184c1c5875ff1fb0752da4eb4c"
            >
                    
                    10:00PM - 10:30PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730863800">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730863800"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 22:30:00"
                   data-end="2024-11-05 23:00:00"
                   data-crc="5ff85f0aedafa49615a1d9c5bb2e02d5"
            >
                    
                    10:30PM - 11:00PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730865600">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730865600"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 23:00:00"
                   data-end="2024-11-05 23:30:00"
                   data-crc="644f79519f60070e8e940cdb7c63e578"
            >
                    
                    11:00PM - 11:30PM
            
        </label>
    </div>
                    
                            
            
    
    
    <div class="checkbox">
        <label for="s8403_0_1730867400">
            <input type="checkbox" name="times[]" value="1" class="booking-checkbox"
                   id="s8403_0_1730867400"
                   data-eid="8403"
                   data-seat="0"
                   data-start="2024-11-05 23:30:00"
                   data-end="2024-11-05 23:59:59"
                   data-crc="58f9e817e37b4ee5b5388088db54e982"
            >
                    
                    11:30PM - 11:59PM
            
        </label>
    </div>
                </fieldset>
            </div>
        </div>
    
    <div class="form-group">
        <button class="btn btn-primary" type="submit" id="s-lc-submit-times" disabled="disabled">
            Submit Times
        </button>
    </div>
                                </div>
                            </form>
                        </div>
                                    </div>

                <div id="s-lc-eq-form" style="clear:both; display: none;" aria-live="polite">
                </div>

                <div id="s-lc-eq-errors" class="alert alert-danger" style="display: none;" role="region" aria-live="polite">
                </div>

                <div id="s-lc-eq-success" style="display: none;" aria-live="polite" tabindex="-1">
                </div>
            </div>
        </div>
    </div>
    </main>

    <footer id="s-lc-public-footer" class="row s-lc-public-footer">
        <div id="s-lc-public-footer-brand">
            <span title="libcal-us-2">Powered by</span> <a href="https://www.springshare.com">Springshare</a>.
        </div>
        <div id="s-lc-public-footer-rights">
            All rights reserved.
        </div>

                    <div id="s-lc-footer-support-link">
                <a href="mailto:library@virginia.edu">Report a tech support issue.</a>
            </div>
        
                
        <div id="s-lc-public-footer-admin-links" role="navigation" aria-label="Admin Footer">
                            <a id="s-lc-sign-in" href="https://virginia.libapps.com/libapps/login.php?site_id=4306&amp;target=">Login to LibApps</a>
                    </div>

        <div class="s-lc-public-footer-actions">
    
<div id="s-lc-language">
    <select id="s-lc-language-selector" aria-label="Select Language">
                <option value="ca" >català</option>
                <option value="cy" >Cymraeg</option>
                <option value="en" selected>English</option>
                <option value="es" >español</option>
                <option value="fr" >français</option>
                <option value="ga" >Irish</option>
                <option value="ja" >日本語 Nihongo</option>
                <option value="nl" >Nederlands</option>
                <option value="sl" >slovenski jezik</option>
                <option value="vi" >Tiếng Việt</option>
                <option value="zh" >中文 Zhōngwén</option>
            </select>
</div>
</div>
    </footer>

    <!-- Matomo -->
<script>
var _paq = window._paq = window._paq || [];
/* tracker methods like "setCustomDimension" should be called before "trackPageView" */
_paq.push(["setDoNotTrack", true]);
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
var u="https://analytics.lib.virginia.edu/";
_paq.push(['setTrackerUrl', u+'matomo.php']);
_paq.push(['setSiteId', '57']);
var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
})();
</script>
<noscript><p><img src="https://analytics.lib.virginia.edu/matomo.php?idsite=57&rec=1" style="border:0;" alt="" /></p></noscript>
<!-- End Matomo Code -->
</div>

<div id="s-lc-public-cust-footer"><section class="footer">
  <div class="container">
    <div class="row">
      <div class="col-sm-3">
        <div class="footer_wrap">
          <h4>Contact Us</h4>
         <ul>
            <li class="line_rv"><a href="tel:+1-434-924-3021">434-924-3021</a></li>
            <li><a href="mailto:library@virginia.edu">library@virginia.edu</a></li>
            <li><a href="http://www.library.virginia.edu/askalibrarian/">Ask a Librarian</a></li>
            <li><address>UVA Shannon Library<br>
P.O. Box 400113<br>
160 McCormick Road<br>
Charlottesville, VA 22904</address>
           </li>
          </ul>
        </div>
      </div>
      <div class="col-sm-3 col-centered">
        <div class="footer_wrap">
          <h4>About the Library</h4>
          <ul>
            <li class="line_rv"><a href="http://www.library.virginia.edu/hours/#!/">Hours</a></li>
            <li><a href="http://static.lib.virginia.edu/directory/">Staff Directory</a></li>
            <li><a href="http://www.library.virginia.edu/jobs/">Jobs</a></li>
            <li><a href="http://www.library.virginia.edu/press/">Press</a></li>
            <li><a href="http://www.library.virginia.edu/jobs/fellowships/">Fellowships</a></li>
          </ul>
          <a class="btn btn-primary donate-btn" href="http://www.library.virginia.edu/support/" role="button">Give to the Library</a>
        </div>
      </div>
      <div class="col-sm-3 col-centered">
        <div class="footer_wrap">
          <h4>Using the Library</h4>
          <ul>
            <li><a href="http://www.library.virginia.edu/policies/">Library Use Policies</a></li>
            <li><a href="http://www.library.virginia.edu/services/off-grounds-access/">Off-Grounds Access</a></li>
            <li><a href="http://its.virginia.edu/accounts/createacct.html">ITS Computing Accounts</a></li>
            <li><a href="http://www.library.virginia.edu/services/accessibility-services/">Accessibility Services</a></li>
            <li><a href="http://www.library.virginia.edu/emergency/">Emergency Information</a></li>
            <li><a href="http://www.virginia.edu/siteinfo/privacy" class="footer-link">UVA Privacy Policy</a></li>
            <li><a href="http://analytics.lib.virginia.edu/index.php?module=CoreAdminHome&action=optOut&language=en">Tracking Opt-out</a></li>
          </ul>
        </div>
      </div>

      <div class="col-sm-3 col-centered">
        <div class="footer_wrap">
          <h4>Other Sites</h4>
          <ul>
            <li class="line_rv"><a href="https://collab.itc.virginia.edu/portal">UVaCollab</a></li>
            <li><a href="https://sisuva.admin.virginia.edu/psp/epprd/EMPLOYEE/EMPL/h/?tab=PAPP_GUEST">SIS</a></li>
            <li><a href="http://its.virginia.edu/home.php">ITS</a></li>
            <li><a href="http://www.virginia.edu/cavalieradvantage/">Cavalier Advantage</a></li>
            <li><a href="http://www.virginia.edu/">UVA Home</a></li>
            <li><a href="http://staffweb.lib.virginia.edu/">Library Staff Site</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="footer-extended">
    <div class="footer-extended-left">
      <a href="http://www.library.virginia.edu/policies/" class="footer-link">Terms</a>   |  
      <a href="mailto:site-feedback@virginia.edu" class="footer-link">Feedback</a>
    </div>
    <div class="footer-extended-right">
      <a href="https://virginia.libapps.com/libapps/login.php?site_id=73" class="footer-link">Login to LibApps</a>
    </div>
  </div>
</section></div>
    <script defer src="https://static-assets-us.libcal.com/js_610/direct/public/equipment/spaces.min.js"></script>
    <script defer src="https://static-assets-us.libcal.com/js_610/direct/public/equipment/session.min.js"></script>
    <script defer src="https://static-assets-us.libcal.com/js_610/direct/public/equipment/spaces-accessible.min.js"></script>
        <script>
        var springLang = {
            eq_js_until_det: 'until...',
            eq_js_rem_pending: 'Remove\u0020Pending\u0020Booking',
            eq_js_cart_tt: 'Create\u0020a\u0020shopping\u0020cart\u0020with\u0020these\u0020space\u0020bookings,\u0020and\u0020go\u0020to\u0020equipment\u0020booking\u0020page\u0020to\u0020add\u0020more\u0020items\u0020to\u0020the\u0020cart.',
            eq_js_isRequired: 'is\u0020required\u0021',
        };
    </script>
            <script>
            var springyPage = {
                returnUrl: '/r/accessible?lid=1411&gid=2181&zone=7108&space=8403&capacity=2',
                locationId: 1411,
                bookingMethod: 14,
                                isMultipleItemsAllowed: 0,
                isMultipleSlotsForItemAllowed: 0,
                lang: {
                    multipleItemsNotAllowed: 'Forbidden\u0020from\u0020booking\u0020different\u0020resources\u0020in\u0020a\u0020single\u0020booking.',
                    multipleTimesNotAllowed: 'Forbidden\u0020from\u0020booking\u0020same\u0020resource\u0020multiple\u0020times\u0020in\u0020a\u0020single\u0020booking.\u003Cbr\u003E\u003Cbr\u003EPlease\u0020only\u0020select\u0020sequential\u0020checkboxes.',
                },
            };
        </script>
    

</body>
</html>
"""
soup=BeautifulSoup(html_doc, 'html.parser')
#times written in label tags inside fieldset tag on accessible availability page
#TODO: Implement this
def get_time_slots():
  times = []
  for label in soup.find_all('label'):
      #extracts and strips whitespace
      time_slot = label.get_text(strip=True)
      #only take in time labels
      if time_slot[0].isdigit():
          times.append(time_slot)
  print(times)
  print("There are", len(times), "study sessions available")

get_time_slots()