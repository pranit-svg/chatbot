import cohere

# Replace this with your actual API key
API_KEY = "3KQbrqcqXPDAeUyPvVEpqnHUiis7eiyR39X8W5UX"

# Initialize the client
co = cohere.Client(API_KEY)

def chat_with_cohere(prompt):
    response = co.chat(
        message=prompt,
        model="command-r-plus"  # or use "command-r" or "command-r-plus" (if you have access)
    )
    return response.text

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    reply = chat_with_cohere(user_input)
    print("Bot:", reply)

