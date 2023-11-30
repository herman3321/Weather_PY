from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city= searchText.get()
        geoLocator= Nominatim(user_agent="geoapiExercises")
        location = geoLocator.geocode(city)
        tf = TimezoneFinder()
        result = tf.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        localTime = datetime.now(home)
        currentTime = localTime.strftime("%I: %M %p")
        clock.config(text=currentTime)
        name.config(text="CURRENT WEATHER")
        weatherAPI = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2694ef3058f39dc7b2258d90e3a62565"
        jsonData = requests.get(weatherAPI).json()
        condition = jsonData['weather'][0]['main']
        description = jsonData['weather'][0]['description']
        tempValue = float(jsonData['main']['temp']-273.15)
        temp = round(tempValue, 2)
        pressure = jsonData['main']['pressure']
        humidity = jsonData['main']['humidity']
        wind = jsonData['wind']['speed']
        
        t.config(text=(temp,"8\u00b0") )
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "8\u00b0"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror('Weather App', "Invalid Entry")



#**********************GUI******************#

#search-container
searchBar = PhotoImage(file="G:\Projects\Python\Apps\weatherApp\searchBar.png")
mySearchBar = Label(image=searchBar)
mySearchBar.place(x=20, y=20)

searchText = tk.Entry(root,
                    justify="center",
                    width=17,
                    font=("Roboto",25,"bold"),
                    bg="#404040",
                    border=0,
                    fg="white")
searchText.place(x=50, y=40)
searchText.focus()

searchIcon = PhotoImage(file="G:\Projects\Python\Apps\weatherApp\searchIcon.png")
mySearchIcon = Button(image=searchIcon,border=0, borderwidth=0, cursor="hand2", background="#404040", command=getWeather)
mySearchIcon.place(x=400, y=44)

#logo-container

logoIcon = PhotoImage(file="G:\Projects\Python\Apps\weatherApp\weatherIcon.png")
myLogoIcon = Label(image=logoIcon)
myLogoIcon.place(x=150, y=100)

#box-container

boxContainer = PhotoImage(file="G:\Projects\Python\Apps\weatherApp\container.png")
myBoxContainer = Label(image=boxContainer, border=0)
myBoxContainer.pack(padx=5, pady=5, side=BOTTOM)

#time-container

name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helevetica", 20))
clock.place(x=30, y=150)


#temp-container

labelWind = Label(root, text="Wind", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
labelWind.place(x=120, y=400)

labelHumidity = Label(root, text="Humidity", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
labelHumidity.place(x=250, y=400)

labelDesc = Label(root, text="Description", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
labelDesc.place(x=430, y=400)

labelPressure = Label(root, text="Pressure", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
labelPressure.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=270, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef", justify="center")
d.place(x=440, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)


root.mainloop()