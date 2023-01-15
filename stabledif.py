import tkinter as tk
from tkinter import simpledialog
import webbrowser

# import the replicate library
import replicate

# get the model and version
model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478")

# create the main window
root = tk.Tk()
root.geometry("400x200")
root.configure(bg='gray')
root.title("Replicate")

# create a function to get the input from the user
def get_prompt():
    prompt = simpledialog.askstring("Input", "Enter the prompt:", parent=root)
    if prompt:
        output = version.predict(prompt=prompt)
        webbrowser.open(output[0])

# create a button to run the function
button = tk.Button(root, text="Submit", command=get_prompt)
button.pack()

# show the window
root.mainloop()

