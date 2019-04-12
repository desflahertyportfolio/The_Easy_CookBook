 $(document).ready(function() {
  
            $('.collapsible').collapsible();
            $('select').material_select();//form creation
            $(".button-collapse").sideNav();//side nav for mobile view
            $('#modal1').modal();//Delete message confirmation popup
            // Form validation for dropdown menus
            $("select[required]").css({display: "block", height: 0, padding: 0, width: 0, position: 'absolute'}); 
 });
        


     