
from tkinter import *
from PIL import ImageTk, Image
import random # for lifeline

root = Tk()
root.geometry("800x500")
root.title(" ------------------------------------------------   KAUN BANEGA CROREPATI   ------------------------------------------------ ")
root.config(bg="#0b1a34")
root.resizable(False, False)
root.wm_iconbitmap("D:\\coding\\Python\\KBC Project\\KBC-Project\\images\\NEW_KBC_GOOGLE_ICON.ico")   # always support .ico file


# questions list
questions = [
    {
        "question": "1.  ( Price:  Rs. 1K ) : Who was the first person to walk on the Moon?",
        "options": ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"],
        "answer": "Neil Armstrong",
        "prize": 1000
    },
    {
        "question": "2.   ( Price:  Rs. 2K ) : In which year did Pakistan win its first Cricket World Cup?",
        "options": ["1992", "1987", "1999", "2003"],
        "answer": "1992",
        "prize": 2000
    },
    {
        "question": "3.   ( Price:  Rs. 5K ) : In Python, what does 'self' represent in a class?",
        "options": ["It refers to parent class", "It’s a keyword", "It refers to current object", "It means nothing"],
        "answer": "It refers to current object",
        "prize": 5000
    },
    {
        "question": "4.   ( Price:  Rs. 10K ) :  Which planet in our solar system has the shortest day (just under 10 hours) ?",
        "options":  [ " Mercury",  "Jupiter", "Earth", "Mars"],
        "answer": "Jupiter",
        "prize": 10000
    },
    {
        "question": "5.   ( Price:  Rs. 25K ) : Which of the following is used to convert a message into an unreadable format for security?",
        "options": ["Encryption", "Hashing", "Compression", "Encoding"],
        "answer": "Encryption",
        "prize": 25000
    },
    {
        "question": "6.   ( Price:  Rs. 100K ) : What is the purpose of a “foreign key” in SQL ?",
        "options": [ "Encrypt data ", "Store date/timeSet",  "primary record", "Join two tables"],
        "answer": "Join two tables",
        "prize": 100000
    },
    {
        "question": "7.   ( Price:  Rs.500K ) : Which concept in AI refers to the ability of a system to learn from data and improve over time without being explicitly programmed?",
        "options": ["Deep Learning", "Machine Learning", "Reinforcement Learning", "Rule-Based System"],
        "answer": "Machine Learning",
        "prize": 500000
    },
    {
        "question": "8.   ( Price:  Rs. 700K ) : You are running in a race. You overtake the runner who is in second place. What is your current position ?",
        "options": [ "First", "Third",  "Second" ,"Fourth"],
        "answer": "Second",
        "prize": 700000
    },
    {
        "question": "9.   ( Price:  Rs. 1157K ) : Which of the following is required to achieve runtime polymorphism in C++ ?",
        "options": [ "Virtual Function", " Function Overloading", "Constructor Overloading", " Static Binding"],
        "answer": "Virtual Function",
        "prize": 1157000
    },
    {
        "question": "10.   ( Price:  Rs. 2500K ) : Which Pakistani scientist was awarded the Nobel Prize in Physics ?",
        "options": [ "Dr. Abdul Qadeer Khan", "Dr. Abdus Salam", "Dr. Samar Mubarakman", "Dr. Atta-ur-Rahman"],
        "answer": "Dr. Abdus Salam",
        "prize": 2500000
    },
]

# global variables
current = 0         # current question index
current_winning = 0  # current amount index
lifeline_used = False



# Welcome frame 
frame1 = Frame(root, bg="#102E60")
frame1.pack(fill="both", expand=True)

Label(frame1, text="Welcome to Kaun Banega Crorepati", font=("Times New Roman", 20, "italic", "bold"),
        bg="#0b1a34", fg="gold").pack(side=TOP,  pady=30)


# for import image
img = Image.open("D:\\coding\\Python\\KBC Project\\KBC-Project\\images\\kbc pic.png")
img = img.resize((430,370))
photo = ImageTk.PhotoImage(img)

img_label = Label(frame1, image=photo,bg= "gold")
img_label.pack(padx=20, pady=20, side=LEFT)


def start():
    frame1.pack_forget()
    frame2.pack(fill="both", expand=True)
    next_question()

def end():
    root.destroy()

Button(frame1, text=" Start Game ", font=("Times New Roman", 20, "italic", "bold"),
        bg="green", fg="white", padx=20, pady=30, command=start, borderwidth=15).pack()

Button(frame1, text="Exit Game", font=("Times New Roman", 20, "italic", "bold"),
        bg="red", fg="white", padx=20, pady=30, command=end, borderwidth=15).pack(pady=25)

Label(frame1, text="Made By Nabeel Shahid", font=("Times New Roman", 14, "italic","bold"),
        bg="#0b1a34", fg="gold").pack(padx=10, pady=30, anchor="e", side=RIGHT)


frame2 = Frame(root, bg="#102E60")

q_label = Label(frame2, text="", font=("Times New Roman", 16, "bold", "italic"),
                bg="#114406", fg="gold", wraplength=500, borderwidth=10, relief=GROOVE)
q_label.pack(pady=30)




def check(i):
    
    global current, current_winning
    selected = btns[i].cget("text").split(": ", 1)[-1] # only one time split and give last element(jo answer hoga)
    if selected == questions[current]["answer"]:
        prize = (questions[current]["prize"])
        current_winning += prize
        result.config(text="CONGRATULATIONs!     Your Answer Is Correct ", fg="lime")
        money.config(text=f" You WON Rs.{prize} \n Your Total Winning Amount Is: \n Rs.{current_winning}", fg="lime")
        
    else:   
        result.config(text=f" WRONG!     Correct answer is : {questions[current]['answer']}", fg="red")
        money.config(text=f"Your Total Winning Amount Is: \n Rs.{current_winning}", fg="lime")
        
        next_btn.config(state="disabled")
        quit_button.config(state="disabled")
        fifty_fifty_btn.config(state="disabled")
        
        exit_after_incorrect = Button(frame2, text="Exit", font=("Times New Roman", 20, "italic", "bold"),
        bg="green", fg="white", padx=20, pady=10, command=end).pack(pady=25)
        
    for b in btns:
        b.config(state="disabled")
    current += 1

options_frame = Frame(frame2, bg="#102E60")
options_frame.pack(pady=10)


btns = []
def options_buttons():
    for i in range(4):
        
        b = Button(options_frame, text="", font=("Times New Roman", 14, "italic", "bold"),
                width=30, bg="gold", command=lambda i=i: check(i))
        b.grid(row=i//2, column=i%2, padx=20, pady=10)
        btns.append(b)


options_buttons()

result = Label(frame2, text="", font=("Times New Roman", 14, "italic", "bold"),
            bg="#1c1c1c", fg="lime")
result.pack(pady=10)

money = Label(frame2, text="", font=("Times New Roman", 14, "italic", "bold"),
            bg="#1c1c1c", fg="lime")
money.pack(pady=10)


def next_question():
    global current
    result.config(text='')
    money.config(text=f"Your Total Winning Amount is: \n Rs. {current_winning}", fg="lime")
    if current < len(questions):
        q = questions[current]
        q_label.config(text=q["question"])
        option_A_B_C_D = ["A : ", "B : ", "C : ", "D : "]
        for i in range(4):
            btns[i].config(text=option_A_B_C_D[i] + q["options"][i], state="normal")
    else:
        q_label.config(text=" Big Congratulations, Game has been completed.", font=("Times New Roman", 20, "italic", "bold"))
        
        
        exit_que_complete = Button(frame2, text="Exit", font=("Times New Roman", 20, "italic", "bold"),
            bg="green", fg="white", padx=20, pady=10, command=end).pack(pady=25)
        for b in btns:
            b.pack_forget()
        next_btn.pack_forget()
        quit_button.pack_forget()
        options_frame.pack_forget()
        result.pack_forget()
        fifty_fifty_btn.pack_forget()

def quit_press():
    for b in btns:
        b.pack_forget()
    next_btn.pack_forget()
    quit_button.pack_forget()
    options_frame.pack_forget()
    result.pack_forget()

    quit_label = Label(frame2)
    quit_label.pack()
    quit_exit= Button(frame2, text="Exit", font=("Times New Roman", 20, "italic", "bold"),
            bg="green", fg="white", padx=20, pady=10, command=end).pack(pady=25)

def use_fifty_fifty():
    global lifeline_used
    if lifeline_used:
        return
    lifeline_used = True
    correct_answer = questions[current]['answer']
    correct_index = -1
    for i in range(4):
        option_text = btns[i].cget("text").split(": ", 1)[-1]
        if option_text == correct_answer:
            correct_index = i
            break
    incorrect_indexes = [i for i in range(4) if i != correct_index]
    disable = random.sample(incorrect_indexes, 2)
    for i in disable:
        btns[i].config(state="disabled")
    fifty_fifty_btn.config(state="disabled")


next_btn = Button(frame2, text="NEXT", font=("Times New Roman", 14, "italic", "bold"),
                bg="green", fg="white", command=next_question)
next_btn.pack(padx=70, side=LEFT)

quit_button = Button(frame2, text="QUIT ", font=("Times New Roman", 14, "italic", "bold"),
                bg="green", fg="white", command=quit_press)
quit_button.pack(padx=70, side=RIGHT)

fifty_fifty_btn = Button(frame2, text="50-50 Lifeline", font=("Times New Roman", 14, "italic", "bold"),
                bg="black", fg="white", command=use_fifty_fifty)
fifty_fifty_btn.pack(pady=20 , side=LEFT)

root.mainloop()
