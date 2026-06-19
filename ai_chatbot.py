# Goal:
# Create a simple rule-based chatbot that responds to predefined user inputs.
# Key Requirements:
# • Handle greetings and exit commands
# • Use if-else logic for responses
# • Run in a continuous loop
# Key Skills:
# Control flow, decision-making logic, basic AI concepts

# Rule-Based AI Chatbot

knowledge_base = {
    'sun rises': 'in the east',
    'sunset': 'in the west',
    'earth satellite': 'the moon',
    'planets': 'there are 8 planets in our solar system',
}

greetings = ['hi', 'hello', 'hey']
exit_commands = ['exit', 'bye', 'quit']

def chatbot():
    print("Bot: Hello! I'm a rule-based chatbot. Ask me something or type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input in exit_commands:
            print("Bot: Goodbye! Have a great day.")
            break
        
        elif user_input in greetings:
            print("Bot: Hi there! How can I help you?")
        
        elif user_input in knowledge_base:
            print("Bot:", knowledge_base[user_input])
        
        elif user_input == '':
            print("Bot: Please type something.")
        
        else:
            print("Bot: Sorry, I don't have an answer for that. Try asking about the sun, moon, or planets.")


chatbot()