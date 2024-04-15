$(document).ready(function () {
     // let userMessage; 
     var csrfToken = $('meta[name="csrf-token"]').attr('content');  
     $("#chat-widget-button").on("click", function (){
          $("#chat-widget").toggleClass("d-none")
     }); 
  
     $("#chat-widget-close-button").on("click", function (){
          $("#chat-widget").addClass("d-none")
     });
     
     $("#chat-widget-input").keypress(function(event) {
          if(event.which === 13){
              let userMessage = $("#chat-widget-input").val(); 
              $("#chat-widget-input").val("")
              // Append user message to the chatbox
              $("#chat-widget-messages").append("<div><strong>You:</strong> " + userMessage + "</div>")
              
              // AJAX call moved inside here
              $.ajax({
                  type: "POST",
                  url: "/webhook/",
                  contentType: "application/json",
                  data: JSON.stringify({message: userMessage}),
                  headers: {"X-CSRFToken": csrfToken}, // Ensure CSRF token is sent
                  success: function (data) {
                      let botResponse = data.response;
                      // append bot message to the chatbox
                      $("#chat-widget-messages").append("<div><strong>AINA🤖:</strong> " + botResponse + "</div>")
                  },
                  error: function () {
                      console.error("Error sending message");
                  }
              });
          }
      });
});
  