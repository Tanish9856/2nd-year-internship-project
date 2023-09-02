from django.http import JsonResponse
from django.shortcuts import render



def chatbot_view(request):
    if request.method == 'POST':
        print("--------------", request.POST)
        user_message = request.POST.get('message', '')
        print("-------", user_message)
        chatbot_response = process_message(user_message)  # Implement your chatbot logic
        return JsonResponse({'response': chatbot_response})
    else:
        return render(request, 'chatbot_app\chatbot.html')

def process_message(message):
    # Implement your chatbot logic here
    # For this example, just echoing the message
    return message


