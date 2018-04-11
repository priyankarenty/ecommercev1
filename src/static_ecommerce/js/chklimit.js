 $("input[name=chk]").change(function(){
    var max= 4;
    if( $("input[name=chk]:checked").length == max ){
      alert("You can only select a maximum of " + max + " checkboxes")
        $("input[name=chk]").attr('disabled', 'disabled');
        $("input[name=chk]:checked").removeAttr('disabled');
    }else{
         $("input[name=chk]").removeAttr('disabled');

    }
})