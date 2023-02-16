import requests
from tkinter import *
from os import environ as env
from dotenv import load_dotenv

category = "inspirational"
api_url = f"https://api.api-ninjas.com/v1/quotes?category={category}"

load_dotenv()

QUOTES_TOKEN = env["QUOTES_TOKEN"]  # Your token


def get_quote():
    """
    It makes a request to the API, checks for errors, and then displays the quote on the canvas
    """
    response = requests.get(api_url, headers={"X-Api-Key": QUOTES_TOKEN})
    response.raise_for_status()

    data = response.json()
    quote = data[0]["quote"]
    canvas.itemconfig(quote_txt, text=f"{quote}", fill="black")


window = Tk()
window.title("Quotes")
window.config(padx=20, pady=20)

canvas = Canvas(width=400, height=500)
bck_img = PhotoImage(file="background.png")
canvas.create_image(200, 250, image=bck_img)
canvas.grid(row=0, column=0)

quote_txt = canvas.create_text(200, 250, font=("Arial", 18, "bold"), width=300)

btn_img = PhotoImage(file="bitmoji.png")
btn = Button(width=64, height=64, image=btn_img, command=get_quote)
btn.grid(row=1, column=0)

get_quote()

window.mainloop()
# https://api-ninjas.com/api/quotes
# https://stackoverflow.com/questions/4121362/version-of-canvas-create-text-that-supports-word-wrap
