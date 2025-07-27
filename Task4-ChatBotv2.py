import random
import time

def get_bot_response(user_input):
    """
    Main function that processes user input and returns appropriate response
    Uses if-elif chains to match patterns and return responses
    """
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()
    
    # Greeting responses
    if any(greeting in user_input for greeting in ['hello', 'hi', 'hey', 'greetings']):
        greetings = [
            "Hi there! How can I help you today?",
            "Hello! Nice to meet you!",
            "Hey! What's up?",
            "Greetings! How are you doing?",
            "Hi! I'm excited to chat with you!"
        ]
        return random.choice(greetings)
    
    # How are you responses
    elif any(phrase in user_input for phrase in ['how are you', 'how do you do', 'how\'s it going']):
        responses = [
            "I'm doing great, thanks for asking! How about you?",
            "I'm fine, thanks! Having a wonderful day chatting with people.",
            "Fantastic! I love helping people. How are you feeling?",
            "I'm doing well! Ready to assist you with anything you need.",
            "Great! I'm here and ready to chat. How's your day going?"
        ]
        return random.choice(responses)
    
    # Name-related questions
    elif any(phrase in user_input for phrase in ['what is your name', 'what\'s your name', 'who are you']):
        return "I'm ChatBot, your friendly AI assistant! What's your name?"
    
    elif any(phrase in user_input for phrase in ['my name is', 'i am', 'i\'m', 'call me']):
        # Try to extract the name
        name = extract_name(user_input)
        if name:
            return f"Nice to meet you, {name}! That's a lovely name."
        else:
            return "Nice to meet you! Thanks for telling me your name."
    
    # Age-related questions
    elif any(phrase in user_input for phrase in ['how old', 'your age', 'age are you']):
        return "I don't have an age like humans do, but I was created recently! How old are you?"
    
    # Help requests
    elif any(word in user_input for word in ['help', 'assist', 'support']):
        return "I'm here to help! You can ask me about myself, chat casually, or just say hello. What would you like to know?"
    
    # Compliments
    elif any(word in user_input for word in ['good', 'great', 'awesome', 'amazing', 'cool', 'nice']):
        responses = [
            "Thank you! That's very kind of you to say.",
            "I appreciate the compliment! You're pretty awesome too!",
            "Thanks! I'm glad you think so. You made my day!",
            "That's so nice! I try my best to be helpful.",
            "Thank you! You're making me blush (if I could)!"
        ]
        return random.choice(responses)
    
    # Feelings and emotions
    elif any(word in user_input for word in ['sad', 'unhappy', 'depressed', 'down']):
        return "I'm sorry to hear you're feeling down. Sometimes talking helps. Want to share what's bothering you?"
    
    elif any(word in user_input for word in ['happy', 'excited', 'great', 'wonderful']):
        return "That's fantastic! I love hearing when people are happy. What's making you feel so good?"
    
    elif any(word in user_input for word in ['tired', 'sleepy', 'exhausted']):
        return "You sound tired! Make sure to get some rest. Sleep is important for your health."
    
    # Weather (basic response since we can't check real weather)
    elif any(word in user_input for word in ['weather', 'rain', 'sunny', 'cold', 'hot']):
        return "I can't check the actual weather, but I hope it's nice where you are! What's the weather like?"
    
    # Time-related
    elif any(word in user_input for word in ['time', 'date', 'day']):
        return "I don't have access to real-time information, but I hope you're having a great day whenever it is!"
    
    # Food-related
    elif any(word in user_input for word in ['food', 'eat', 'hungry', 'pizza', 'burger']):
        return "I don't eat, but I love hearing about food! What's your favorite dish?"
    
    # Technology/Programming
    elif any(word in user_input for word in ['python', 'programming', 'code', 'computer']):
        return "I love talking about technology! Python is amazing for programming. Are you learning to code?"
    
    # Jokes
    elif any(word in user_input for word in ['joke', 'funny', 'laugh']):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the programmer quit his job? He didn't get arrays! (a raise)",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What's a computer's favorite snack? Microchips!"
        ]
        return random.choice(jokes)
    
    # Questions about the bot
    elif any(phrase in user_input for phrase in ['what can you do', 'what do you do', 'your abilities']):
        return "I can chat with you, answer basic questions, tell jokes, and try to be helpful! I'm still learning though."
    
    # Goodbye responses
    elif any(word in user_input for word in ['bye', 'goodbye', 'see you', 'farewell', 'exit', 'quit']):
        farewells = [
            "Goodbye! It was great chatting with you!",
            "See you later! Have a wonderful day!",
            "Farewell! Thanks for the lovely conversation!",
            "Bye! Hope to chat with you again soon!",
            "Take care! It was a pleasure talking with you!"
        ]
        return random.choice(farewells)
    
    # Default responses for unrecognized input
    else:
        default_responses = [
            "That's interesting! Tell me more about that.",
            "I'm not sure I understand, but I'm listening!",
            "Could you rephrase that? I want to make sure I understand.",
            "Hmm, that's something new for me. Can you explain more?",
            "I'm still learning! Could you try asking that differently?",
            "That sounds fascinating! I'd love to learn more about it.",
            "I'm not quite sure how to respond to that, but I'm here to chat!"
        ]
        return random.choice(default_responses)

def extract_name(user_input):
    """
    Simple function to extract name from user input
    Looks for patterns like "my name is John" or "I am Jane"
    """
    user_input = user_input.lower()
    
    # Common patterns for name introduction
    patterns = [
        'my name is ',
        'i am ',
        'i\'m ',
        'call me '
    ]
    
    for pattern in patterns:
        if pattern in user_input:
            # Find the position after the pattern
            start_pos = user_input.find(pattern) + len(pattern)
            # Extract the word after the pattern
            remaining = user_input[start_pos:].strip()
            if remaining:
                # Take the first word as the name
                name = remaining.split()[0]
                # Capitalize the first letter
                return name.capitalize()
    
    return None

def typing_effect(text, delay=0.03):
    """
    Creates a typing effect for bot responses
    Makes the conversation feel more natural
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line after the message

def display_welcome():
    """
    Display welcome message and instructions
    """
    print("=" * 60)
    print("           🤖 WELCOME TO CHATBOT! 🤖")
    print("=" * 60)
    print("Hi! I'm a friendly chatbot ready to chat with you!")
    print("I can respond to greetings, questions, and casual conversation.")
    print("\nTry saying things like:")
    print("  • Hello, hi, hey")
    print("  • How are you?")
    print("  • What's your name?")
    print("  • Tell me a joke")
    print("  • Help")
    print("  • Bye (to exit)")
    print("\nType 'quit' or 'exit' anytime to end our conversation.")
    print("=" * 60)

def main():
    """
    Main chatbot loop
    Handles user input and bot responses
    """
    display_welcome()
    
    conversation_count = 0
    
    print("\nChatBot: Hi there! I'm excited to chat with you! 😊")
    
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Check for empty input
            if not user_input:
                print("ChatBot: I'm listening... please say something!")
                continue
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'stop']:
                print("ChatBot: Thanks for chatting! Have a great day! 👋")
                break
            
            # Get bot response
            bot_response = get_bot_response(user_input)
            
            # Display response with typing effect
            print("ChatBot: ", end="")
            typing_effect(bot_response)
            
            conversation_count += 1
            
            # Add some variety every few messages
            if conversation_count % 5 == 0:
                encouragement = [
                    "\n(I'm enjoying our conversation! Keep it going! 😄)",
                    "\n(You're a great conversationalist! 🌟)",
                    "\n(This is fun! What else would you like to talk about? 💬)"
                ]
                print(random.choice(encouragement))
                
        except KeyboardInterrupt:
            print("\n\nChatBot: Oops! Looks like you pressed Ctrl+C. Goodbye! 👋")
            break
        except Exception as e:
            print(f"\nChatBot: Sorry, I encountered an error: {e}")
            print("But I'm still here to chat! Try again.")

# Additional utility functions
def get_conversation_stats():
    """
    Could be used to track conversation statistics
    """
    pass

def save_conversation_log():
    """
    Could be used to save conversation history
    """
    pass

# Run the chatbot
if __name__ == "__main__":
    main()
