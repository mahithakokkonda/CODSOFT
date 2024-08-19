import tkinter as tk
from tkinter import font as tkfont

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Chatbot")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")

        # Set custom fonts
        self.custom_font = tkfont.Font(family="Helvetica", size=12)
        self.bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

        # Chat window
        self.chat_window = tk.Text(self.root, bd=0, bg="#ECF0F1", height=8, width=50, font=self.custom_font)
        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.place(x=6, y=6, height=485, width=488)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.chat_window)
        self.scrollbar.place(relheight=1, relx=0.974)
        self.scrollbar.config(command=self.chat_window.yview)

        # Message entry box
        self.message_box = tk.Entry(self.root, bd=0, bg="#F7F9F9", font=self.custom_font)
        self.message_box.place(x=6, y=500, height=88, width=380)
        self.message_box.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", font=self.bold_font, width=12, height=5, bd=0, bg="#2980B9", fg="#ffffff",
                                     activebackground="#3498DB", command=self.send_message)
        self.send_button.place(x=390, y=500, height=88, width=100)

        # Chatbot responses
        self.responses = {
            "hello": "Hi there! How can I help you today?",
            "weather": "The weather is sunny with a slight chance of rain later today.",
            "name": "I'm your friendly chatbot!",
            "help": "I'm here to assist you with any questions you have.",
            "bye": "Goodbye! Have a great day!",
        }
        self.default_response = "I'm sorry, I didn't understand that. Could you please rephrase?"

    def get_response(self, user_input):
        # Convert input to lowercase
        user_input = user_input.lower()
        for keyword in self.responses:
            if keyword in user_input:
                return self.responses[keyword]
        return self.default_response

    def send_message(self, event=None):
        user_input = self.message_box.get()
        self.chat_window.config(state=tk.NORMAL)
        self.chat_window.insert(tk.END, "You: " + user_input + "\n\n")
        self.chat_window.config(foreground="#34495E", font=self.custom_font)

        response = self.get_response(user_input)
        self.chat_window.insert(tk.END, "Chatbot: " + response + "\n\n")

        self.chat_window.config(state=tk.DISABLED)
        self.chat_window.yview(tk.END)
        self.message_box.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    bot_gui = ChatbotGUI(root)
    bot_gui.run()
