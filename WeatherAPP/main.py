import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/tr-TR/weather/today/l/7912d03017522301f5c89f4f1d661d18ad10926c15063cf520ee5ec7ce7c787c"

master = Tk()
master.title("Weather App")
master.config(bg="white")

img_path = "C:/Users/alper/Downloads/4102326_cloud_sun_sunny_weather_icon.png"
img = Image.open(img_path)
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)


locationLabel = Label(master,font=("calibri bold",20),bg="white")
locationLabel.grid(row=0,sticky="N",padx=10)
TemperatureLabel = Label(master,font=("calibri bold",70),bg="white")
TemperatureLabel.grid(row=0,sticky="N",padx=40)
Label(master, image=img,bg="white").grid(row=1 , sticky= "E")
master.mainloop()
