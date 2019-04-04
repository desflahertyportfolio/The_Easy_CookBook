 $(document).ready(function() {
  
            $('.collapsible').collapsible();
            $('select').material_select();
            $(".button-collapse").sideNav();
             $('.modal').modal({
      dismissible: true, // Modal can be dismissed by clicking outside of the modal
      opacity: .5, // Opacity of modal background
      inDuration: 300, // Transition in duration
      outDuration: 200, // Transition out duration
      startingTop: '4%', // Starting top style attribute
      endingTop: '10%', // Ending top style attribute
    }
            );
            $('.modal-trigger').modal();
            $('#modal1').find("#image_url").val('asd');
 });
        

