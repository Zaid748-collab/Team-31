from django.http import JsonResponse
import json

def chat_respond(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    data = json.loads(request.body)
    question = data.get("question", "").strip()

    responses = {
    # Shipping
    "What are your delivery times?": "We typically deliver within 3–5 business days.",
    "Do you ship internationally?": "At the moment, we only ship within the UK.",
    "How do I track my order?": "Once your order ships, you will receive a tracking link via email.",

    # Returns
    "What is your return policy?": "You can return any item within 30 days for a full refund.",
    "How long do refunds take?": "Refunds are processed within 3–5 business days after receiving the item.",
    "Can I exchange an item?": "Yes, exchanges are available for unused items within 30 days.",

    # Account
    "How do I reset my password?": "Use the 'Change Password' link on the edit profile page.",
    "How do I change my email?": "Go to the edit profile page and update your email address.",
    "How do I delete my account?": "Contact support and we will process your account deletion request.",
}
    

    answer = responses.get(question, "Sorry, I don't have an answer for that yet.")
    return JsonResponse({"answer": answer})
