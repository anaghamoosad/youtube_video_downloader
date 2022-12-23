$(document).ready(function() {
 

    // get progressbar percentage using socket connection
    var socket = io();
    socket.on('progress_perct', function(msg) {  
        var prog_bar = document.getElementById("newprog");  
        var prog_lbl = document.getElementById("proglbl")                 
        prog_bar.style.width = msg.data + '%';    
        prog_lbl.textContent = msg.data + '%'; 
        document.getElementById("progressbars").style.visibility= "visible";   
 
    });

   
    //show progressbar on download_video button click
    document.getElementById("video").onclick = function() {
        document.getElementById("progressbars").style.visibility= "visible";       
    }  
    //show progressbar on download_audio button click
    document.getElementById("audio").onclick = function() {
        document.getElementById("progressbars").style.visibility= "visible";       
    }  

        //show progressbar on download_video button click
        document.getElementById("typeText").onclick = function() {
            document.getElementById("progressbars").style.visibility= "hidden"; 
            const element = document.getElementById("flash-msg");
    	    element.remove();
        }  

});

 
 