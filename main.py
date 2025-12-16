import time
import intelagnce # Corrected import statement

# Initial simple prints
print("hello")
time.sleep(0.5)
print("i was your ai")
time.sleep(0.5)
print("so tell me a question")

# Print license information for compliance
print("\n--- License Information ---")
print("This project incorporates data from 'WeThinkIn/AIGC-Interview-Book', which is licensed under GPL-3.0.")
print("The entire project is now licensed under GPL-3.0. See the LICENSE file for details.")
print("---------------------------\n")

# --- Main Chat Loop ---

print("\nChatbot: Hi! I am an expanded Python chatbot. How can I help you today?")

while True:
    try:
        # Get input from the user
        user_input = input("You: ")
        
        if not user_input.strip(): # Prevents error if user just hits enter
            continue
            
        # Use the function from the imported module
        bot_response = intelagnce.get_bot_response(user_input)
        print(f"Chatbot: {bot_response}")

        # Exit the loop if the response indicates an exit command was matched
        # A more robust check is to check the response content for exit phrases
        if any(exit_phrase in bot_response for exit_phrase in ["Goodbye!", "See you later!", "Chat terminated."]):
            break

    except EOFError:
        # Handle cases where input stream is closed unexpectedly
        print("\nChatbot: Connection closed. Goodbye!")
        break
    except KeyboardInterrupt:
        # Handle user pressing Ctrl+C
        print("\nChatbot: Chat terminated by user. Goodbye!")
        break
