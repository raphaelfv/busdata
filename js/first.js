"use strict";
$( document ).ready(function(){
    $('.img_block').hover(
        function() {
            $(this).find(" > button").show();
        },
        function() {
            $(this).find(" > button").hide();
        },
    );
});
