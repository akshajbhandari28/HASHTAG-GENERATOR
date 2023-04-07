import tkinter as tk
import openai
import pyperclip as pc

root = tk.Tk()

root.geometry('1024x700')
root.title('HASHTAG GENERATOR')


label = tk.Label(root, text="WELCOME TO HASHTAG GENERATOR!", font=('Arial', 30))
label.pack(padx=20, pady=20)

e = tk.Entry(root, width=100, borderwidth=7)
e.pack()
e.insert(0, 'Please Enter Video Name: ')



def Myclick():
    maybe_prompt = e.get()
    actual_prompt = maybe_prompt.replace('Please Enter Video Name: ', '')
    openai.api_key = "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"
    model_engine = "text-davinci-003"
    prompt = f"give me 15 hashtags of a video titled, {actual_prompt}"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    global response
    response = completion.choices[0].text
    completed_label = tk.Label(root, text='HASHTAGS SUCCESSFULLY GENERATED!', font=('Arial', 25))
    completed_label.place(x=175, y=250)


button = tk.Button(root, text='GENERATE HASHTAGS', font=('Arial', 20),command=Myclick)
button.place(x=350, y=150)


def CopyToClipboard():
    hastags = response
    pc.copy(hastags)
    completed_label = tk.Label(root, text='HASHTAGS SUCCESSFULLY COPIED TO CLIPBOARD!', font=('Arial', 25))
    completed_label.place(x=75, y=450)


button = tk.Button(root, text='COPY HASHTAGS TO CLIPBOARD', font=('Arial', 20), command=CopyToClipboard)
button.place(x=300, y=350)


def exit():
    root.destroy()


exit_button = tk.Button(root, text='EXIT', font=('Arial', 20), command=exit)
exit_button.place(x=475, y=600)

root.mainloop()
