// chatbot/static/chatbot/script.js
$(document).ready(function () {
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
        }
        // Append user message to the chatbox
        $("#chat-widget-message").append("<div><strong>You:</strong>" + userMessage + "</div>")
   });

   $.ajax({
        type: "POST",
        url: "/webhook",
        contentType: "application/json",
        data: JSON.stringify({message: userMessage}),
        success: function (data) {
            let botResponse = data.response;

            // append bot message to the chatbox
            $("#chat-widget-message").append("<div><strong>You:</strong>" + botResponse + "🤖</div>")
        },
        error: function () {
            console.error();
        }
   });
});
