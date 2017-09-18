$(function(){
    $("body").click(function(event) {
        // var tgt = $(event.target);
        // if(tgt.size() != 0)
        //     alert(tgt.prop("outerHTML"))
    });

    $("body").find("*").hover(function() {
        $(this).css("border","2px solid red");
        $(this).parents().css("border","none")
    });

    $("body").find("*").mouseout(function(){
        $(this).css("border","none");
    });

    $("a").each(function () {
        $(this).click(function (event) {
            event.preventDefault();
        })
    });

})
