$(function () {
  $(window).scroll(function () {
    if ($(document).scrollTop() > 300) {
      $('#CloudView').slideDown(500);
      $('#CloudImg').fadeIn(700);
    }
    if ($(document).scrollTop() > 700) {
      $('#CmsView').slideDown(500);
      $('#CmsImg').fadeIn(700);
    }
    if ($(document).scrollTop() > 1000) {
      $('#EduView').slideDown(500);
      $('#EduImg').fadeIn(700);
    }
    if ($(document).scrollTop() > 1600) {
      $('#webView').slideDown(500);
      $('#jsView').slideDown(500);
      $('#dockerView').slideDown(500);
    }
    if ($(document).scrollTop() > 1800) {
      $('#unityView').slideDown(500);
    }
    if ($(document).scrollTop() > 2000) {
      $('#jenkinsView').slideDown(500);
      $('#gitView').slideDown(500);
    }
    if ($(document).scrollTop() > 2200) {
      $('#awsView').slideDown(500);
    }
    if ($(document).scrollTop() > 2700) {
      $('.webView').slideDown(500);
    }
    if ($(document).scrollTop() > 3100) {
      $('.softwareView').slideDown(500);
    }
  });
});

function scrollToEle(element){
  $('#CloudView').slideDown(1000);
  $('#CloudImg').fadeIn(1000);
  $('#CmsView').slideDown(1000);
  $('#CmsImg').fadeIn(1000);
  $('#EduView').slideDown(1000);
  $('#EduImg').fadeIn(1000);
  $('#webView').slideDown(0);
  $('#jsView').slideDown(0);
  $('#dockerView').slideDown(0);
  $('#unityView').slideDown(0);
  $('#jenkinsView').slideDown(0);
  $('#gitView').slideDown(0);
  $('#jenkinsView').slideDown(0);
  $('#gitView').slideDown(0);
  $('#awsView').slideDown(0);
  $('.webView').slideDown(1000);
  $('.softwareView').slideDown(1000);
  $([document.documentElement, document.body]).animate({
    scrollTop: $(element).offset().top - 100
  }, 0);
}