
from nltk.chat.util import Chat, reflections
import tkinter as tk


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
[
        r"سلام",
        ["سلام چطوری؟",]
    ],
[
        r"اسم من (.*) است",
        ["سلام %1 شما میتوانید پیام خود را برای ما ارسال نمایید.",]
    ],
[
        r"سازنده",
        ["ساخته شده توسط محراب استکی",]
    ],
[
        r"ساعت چند است",
        ["4:15:34",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
]

def chatbot_response(user_input):
    chat = Chat(pairs, reflections)
    return chat.respond(user_input)

def send_message():
    user_input = user_entry.get()
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chat_log.insert(tk.END, "Mbot: " + chatbot_response(user_input) + "\n")
    user_entry.delete(0, tk.END)


window = tk.Tk()
window.title("Mbot")
window.geometry("400x500")


chat_log = tk.Text(window, bd=0, bg="white", height="8", width="50", font="Arial")



scrollbar = tk.Scrollbar(window, command=chat_log.yview, cursor="heart")
chat_log['yscrollcommand'] = scrollbar.set


user_entry = tk.Entry(window, bd=0, bg="white", font="Arial")
user_entry.bind("<Return>", lambda event: send_message())


send_button = tk.Button(window, text="Send", width="12", height=5,
                        bd=0, bg="#0080ff", activebackground="#00bfff",
                        fg='#ffffff', font="Arial", command=send_message)


scrollbar.place(x=376, y=6, height=386)
chat_log.place(x=6, y=6, height=386, width=370)
user_entry.place(x=128, y=401, height=90, width=265)
send_button.place(x=6, y=401, height=90)


window.mainloop()
