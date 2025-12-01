"""
🤖 Smart AI Assistant - Intelligent Chatbot
Developer: [Mohammed]
Specialization: Python Programming & AI Applications
"""

class SmartAssistant:
    def __init__(self):
        self.responses = {
            "hello": "Hello! 🌟 How can I assist you today?",
            "hi": "Hi there! Ready to build something amazing? 🚀",
            "programming": "I have advanced Python skills and AI solution development! 💻",
            "price": "Starting from $50 for simple projects - Affordable prices or everyone 💰",
            "project": "I can develop: Websites - AI Applications - Data Analysis - Chatbots 🚀",
            "python": "Python is my specialty! I build AI models, web apps, and automation scripts",
            "ai": "I develop machine learning models, chatbots, and intelligent systems",
            "website": "I create responsive websites with modern technologies",
            "thanks": "You're welcome! 😊 I'm always here to help",
            "bye": "Goodbye! Have a wonderful day! 🌸"
            "portfolio": "Check my GitHub: github.com/[modoxmodo96] for all my projects"
        }
    
    def start_chat(self):
        print("=" * 60)
        print("🤖 Smart AI Assistant - Python & AI Developer")
        print("=" * 60)
        print("Hello! I'm your AI assistant. You can ask me about:")
        print("• Programming & Development • Pricing • Projects • AI Solutions")
        print("=" * 60)
        
        while True:
            user_input = input("👤 You: ").strip().lower()
           
            if user_input in ['exit', 'quit', 'bye', 'goodbye']:
                print("🤖 Assistant: Goodbye! Keep chasing your big dreams! 🚀")
                break
            
            response = self.responses.get(user_input, 
                "🤖 Assistant: That's interesting! Currently I focus on Python programming and AI. Try 'programming', 'price', or 'project'")
            
            print(f"🤖 Assistant: {response}")

# Run the assistant
if __name__ == "__main__":
    assistant  SmartAssistant()
    assistant.start_chat()
