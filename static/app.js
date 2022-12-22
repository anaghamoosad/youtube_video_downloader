$(document).ready(function() {
       
    var socket = io();   
    
    // Test response received from server is handled here
    socket.on('test_response', function(msg) {  

        var element2 = document.getElementById("newprog");  
        var element3 = document.getElementById("proglbl")  


        if (msg.data==100) {
            element2.style.width==100;
        } 
        if (msg.data==100) {
            element3.style.width==100;
        } 
        else {
                    
        element2.style.width = msg.data + '%'; 
   
        element3.textContent = msg.data + '%'; 
    }
    })

});
