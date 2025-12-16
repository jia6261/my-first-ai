import re
import random
import time

import AIGC_Interview_Data # Import the new data module

responses = {
    # Basic Greetings
    r'\b(hello|hi|hey)\b': [
        "Hello! How can I help you today?",
        "Hi there! What's on your mind?",
        "Hey! Ask me anything."
    ],

    # Basic Inquiry
    r'\b(how are you|how you doing)\b': [
        "I'm a simple bot, I'm doing great, thanks for asking!",
        "I'm functioning optimally.",
        "Just crunching numbers and waiting for your commands."
    ],

    # Identity/Name
    r'\b(what is your name|who are you)\b': [
        "I'm a Python chatbot, your friendly digital assistant.",
        "You can call me Bot.",
        "I don't have a name, but I'm here to chat!"
    ],

    # Capabilities/Help
    r'\b(what can you do|help)\b': [
        "I can answer simple questions based on my programming.",
        "I can chat with you, tell the time, or just listen!",
        "Try asking me the current time or a simple fact."
    ],

    # Time (Requires specific function logic, handled below)
    r'\b(time|what time is it)\b': [
        "It is currently {current_time}." # Placeholder for dynamic info
    ],

    # A simple math example
    r'\b(2\+2|what is 2\+2|two plus two)\b': [
        "That's easy! 2 + 2 equals 4.",
        "The answer is 4."
    ],
    
    # Exit commands
    r'\b(bye|exit|quit|goodbye)\b': [
        "Goodbye! Have a great day!",
        "See you later! Stay curious.",
        "Chat terminated. Farewell!"
    ]
}

def get_bot_response(user_input):
    """Checks user input against patterns and returns a response."""
    user_input_lower = user_input.lower()
    
    for pattern, response_list in responses.items():
        # Use re.search to find the pattern anywhere in the input string
        if re.search(pattern, user_input_lower):
            # Handle special dynamic responses (e.g., time)
            chosen_response = random.choice(response_list)
            
            if "{current_time}" in chosen_response:
                # Fetch real-time info
                current_time = time.strftime("%H:%M:%S", time.localtime())
                return chosen_response.format(current_time=current_time)
            
            return chosen_response
            
    # Check AIGC Interview Data first
    aigc_answer = AIGC_Interview_Data.get_aigc_interview_answer(user_input)
    if aigc_answer:
        return f"根据AIGC面试知识库，答案是：{aigc_answer}"

    # Default response if no pattern matches
    return "I don't understand that yet. Can you rephrase or ask something else?"

if __name__ == '__main__':
    # Simple test loop for the module itself
    print("--- intelagnce.py Test Mode ---")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'exit', 'quit', 'goodbye']:
            print("Bot: Goodbye!")
            break
        print(f"Bot: {get_bot_response(user_input)}")
