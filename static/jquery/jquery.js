 $(document).ready(function() {

  $('.collapsible').collapsible();
  $('select').material_select(); //form creation
  $(".button-collapse").sideNav({//side nav for mobile view
   menuWidth: 150,
   closeOnClick: true,
   edge: 'right', // <---side nav open on right
  }); 
  $('#modal1').modal(); //Delete message confirmation popup
  // HTML Form validation for dropdown menus
  $("select[required]").css({ display: "block", height: 0, padding: 0, width: 0, position: 'absolute' });


  //validate passwords match on login
  $("#password").on("focusout", function(e) {
   if ($(this).val() != $("#password1").val()) {
    $("#password1").removeClass("valid").addClass("invalid");
   }
   else {
    $("#password1").removeClass("invalid").addClass("valid");
   }
  });
  $("#password1").on("keyup", function(e) {
   if ($("#password").val() != $(this).val()) {
    $(this).removeClass("valid").addClass("invalid");
   }
   else {
    $(this).removeClass("invalid").addClass("valid");
   }
  });
 });
 