from tkinter import *

import requests
import json


window = Tk()
window.title("Welcome to DUCAT")
window.config(bg="lightgrey")
l1 = Label(window, text="WEATHER  NOW", bg="orange", fg="blue", width=40,height=2,font=('calibri',12,'bold','underline'))
# l1.pack()
#l1.grid(rows=150, columns=250)
l1.place(x=750, y=220)

img = PhotoImage(file="C:/Users/Danny/Desktop/pythonproject/images/weatherlogo.png")
l2 = Label(window, image=img,width=300)
l2.place(x=690,y=20)

v=StringVar()
def action():
    city=v.get()
# API - application programming interface
# url = "http://api.weatherapi.com/v1/current.json?key=bd962ac5e2c045b590b82104231306&q=Jaipur"
    url = "http://api.weatherapi.com/v1/current.json?key=bd962ac5e2c045b590b82104231306&q=" + city
    df = requests.get(url)
    data = json.loads(df.content)
    l3.config(text="Location ->"  +(str(data['location']['name'])))
    l8.config(text="Temp is-:"+(str(data['current']['temp_c'])))
    l9.config(text="Temp is-:"+(str(data['current']['temp_f'])))
    l10.config(text=""+str(data['location'][ ""'localtime']))
    l26.config(text=""+(str(data['current'][ 'humidity'])))
    l14.config(text="Day->"+(str(data['current']['condition'][ 'text'])))
    l13.config(text="Wind Speed->"+(str(data['current'][ 'wind_kph'])))
    l17.config(text="Wind Direction->"+(str(data['current'][ 'wind_dir'])))
    l18.config(text="Gust->"+(str(data['current'][ 'gust_kph'])))
    l15.config(text="Cloud->"+(str(data['current'][ 'cloud'])))
    # print(f"Temperature of {data['location']['name']} is {data['current']['temp_c']}")

    # print(df.content)




e1 = Entry(window, width=20, font=("Calibri", 20),bg='orange',textvariable=v)
e1.place(x=900, y=290)
b1 = Button(window, text="SUBMIT", bg="skyblue", fg="blUE",width='15',height='2',font=('calibri',11,'bold'),command=action)
b1.place(x=830, y=340)
l3 = Label(window, text="LET'S  CHECK",
           bg="orange", fg="blue", width=40,height=2,font=('calibri',11,'bold'))
l3.place(x=750, y=400)
l4 = Label(window, text="ENTER YOUR CITY NAME : ->",
           bg="royalblue", fg="white", width=40,height=2)
l4.place(x=580, y=290)
#window.minsize(width=100, height=200)
#window.maxsize(width=500, height=800)

l5 = Label(window, text="TEMPERATURE IN CELSIUS: -> ",
           bg="royalBlue", fg="WHITE", width=40,height=1)
l5.place(x=580, y=480)
l6 = Label(window, text="TEMPERATURE IN FERENHEIT: -> ",
           bg="royalBLue", fg="WHITE", width=40)
l6.place(x=580, y=520)
l7 = Label(window, text="LOCAL TIME: -> ",
           bg="royalBlue", fg="WHITE", width=40)
l7.place(x=580, y=560)

l25 = Label(window, text="HUMIDITY: -> ",
           bg="royalBLue", fg="WHITE", width=40)
l25.place(x=580, y=600)
l26 = Label(window, text="",
           bg="orange", fg="BLACK", width=40)
l26.place(x=900, y=600)

l8 = Label(window, text="",
           bg="orange", fg="BLACK", width=40)
l8.place(x=900, y=480)
l9 = Label(window, text="",
           bg="orange", fg="BLACK", width=40)
l9.place(x=900, y=520)
l10 = Label(window, text="",
            bg="orange", fg="BLACK", width=40)
l10.place(x=900, y=560)
l11 = Label(window, text="WEATHER  FORECAST",
            bg="skyblue", fg="black", width=35,height=2,font=('calibri',11,'bold','underline'))
l11.place(x=40, y=18)
#l96 to l99 lables are only for border outside nothing else.....
l96 = Label(window, text="",
            bg="black", fg="black", width=1,height=60)
l96.place(x=0, y=-15)
l97 = Label(window, text="",
            bg="black", fg="black", width=2,height=60)
l97.place(x=1265, y=-15)
l98 = Label(window, text="",
            bg="black", fg="black", width=400,height=1)
l98.place(x=0, y=-17)
l99 = Label(window, text="",
            bg="black", fg="black", width=400,height=1)
l99.place(x=0, y=644)


# img1 = PhotoImage(file="C:/Users/Danny/Desktop/pythonproject/images/cloud2.png")
# l25 = Label(window, image=img1,height=60)
# l25.place(x=140,y=35)
# l12 = Label(window, text="Cloud",bg="black", fg="white", width=40,height=1)
# l12.place(x=90, y=120)

img2 = PhotoImage(file="C:/Users/Danny/Desktop/pythonproject/images/wind.png")
l19 = Label(window, image=img2,width=200,height=70)
l19.place(x=80,y=64)
l13 = Label(window, text="",bg="cyan", fg="black", width=35,height=1)
l13.place(x=60, y=140)

img3 = PhotoImage(file="C:/Users/Danny/Desktop/pythonproject/images/raincopy.png")
l20 = Label(window, image=img3,width=180)
l20.place(x=90,y=160)
l14 = Label(window, text="",bg="pink", fg="black", width=35,height=1)
l14.place(x=60, y=255)

img4 = PhotoImage(file="C:/Users/Danny/Desktop/pythonproject/images/cloudy.png")
l21 = Label(window, image=img4,width=200)
l21.place(x=80,y=275)
l15 = Label(window, text="",bg="skyblue", fg="black", width=35,height=1)
l15.place(x=60, y=388)

# img5 = PhotoImage(file="C:/Users/Danny/Desktop/pythonproject/images/fog.png")
# l22 = Label(window, image=img5,width=400)
# l22.place(x=90,y=400)
# l16 = Label(window, text="Fog",bg="black", fg="white", width=40,height=1)
# l16.place(x=90, y=420)

img6 = PhotoImage(file="C:/Users/Danny/Desktop/pythonproject/images/wind2.png")
l23 = Label(window, image=img6,width=200,height=120)
l23.place(x=80,y=410)
l17 = Label(window, text="",bg="orange", fg="black", width=35,height=1)
l17.place(x=60, y=515)

img7 = PhotoImage(file="C:/Users/Danny/Desktop/pythonproject/images/gust2.png")
l24 = Label(window, image=img7,width=200,height=80)
l24.place(x=80,y=535)
l18 = Label(window, text="",bg="lightgreen", fg="black", width=35,height=1)
l18.place(x=60, y=620)


window.mainloop()
