from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question
import json
import requests
import logging


def log_question_to_database(question_text):
    """
    This function attempts to log a question to the database and returns True if successful, False otherwise.
    """
    try:
        Question.objects.create(question_text=question_text)
        logger.info(f"Question logged to database: {question_text}")
        return True
    except Exception as e:
        logger.error(f"Failed to log question to database: {e}")
        return False

# Before calling process_user_message(user_message) in the webhook function, 
# ensure that the question is successfully logged to the database.
# If not, return an appropriate JsonResponse indicating the failure.

logger = logging.getLogger(__name__)

def index(request):
    return render(request, "index.html")

@csrf_exempt
def webhook(request):
    if request.method == "POST":
        try:

            data = json.loads(request.body)
            user_message = data.get("message", "")

            if user_message:
                # Call log_question_to_database here to ensure question is logged before processing
                if log_question_to_database(user_message):
                    bot_response = process_user_message(user_message)
                    return JsonResponse({"response": bot_response})
                else:
                    return JsonResponse({"error": "Failed to log question to database"}, status=500)

            else:
                logger.warning("Empty message received")
                return JsonResponse({"response": "Empty message received"}, status=400)
        except Exception as e:
            logger.error(f"Error processing request {e}")
            return JsonResponse({"Error": "Internal server error"}, status=500)
        
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

        
def process_user_message(message):
    # URL of the Rasa server
    rasa_url = 'http://localhost:5005/webhooks/rest/webhook'
    
    # Payload to send to Rasa
    payload = {
        "sender": "DjangoUser",  # or any unique ID for the user
        "message": message
    }
    
    # Send the message to Rasa and get the response
    response = requests.post(rasa_url, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the text from the first message in the response
        bot_messages = response.json()
        if bot_messages:
            # Assuming you want to return the first response from Rasa
            return bot_messages[0].get('text', 'Sorry, I could not process your message.')
        else:
            return "Sorry, I didn't get that."
    else:
        return "Failed to connect to the chatbot."