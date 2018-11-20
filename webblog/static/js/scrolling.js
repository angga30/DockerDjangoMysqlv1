$(window).scroll(function(){
    var scr = $(window).scrollTop();
    document.getElementById("mybod").style.marginTop = (-100 -0.5* scr) +"px";

    if(scr > 170){
        $("#navia").addClass("bg-dark");

    }else{
        $("#navia").removeClass("bg-dark");


    }

});