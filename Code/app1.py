import tkinter as tk
import requests

h = 500
w = 500


def test(en):
    print("this is the entry", en)


def format(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        tem = weather['main']['temp']
        final = 'City:%s \n Report:%s \n Temperature:%s '%(name,desc,tem)
    except:
        final="No such location is found"
    return final


def forcast(city):
    key = '34d826edbbd414f47e7e71686e07099e'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'Appid': key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    lb['text'] = format(weather)


root = tk.Tk()

backgroundImage = tk.PhotoImage(file='green.png')
backgroundLabel = tk.Label(root, image=backgroundImage)
backgroundLabel.pack()

canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()

f = tk.Frame(root, bg='#737CA1', bd='5')
f.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.075, anchor='n')

en = tk.Entry(f, font='40')
en.place(relheight=0.78, relwidth=0.78)

button = tk.Button(f, text="Test Weather", bg='yellow', command=lambda: forcast(en.get()))
button.place(relx=0.8, relheight=0.78, relwidth=0.2)

lf = tk.Frame(root, bg='#737CA1', bd='10')
lf.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.5, anchor='n')

lb = tk.Label(lf,font='40',anchor='nw',justify='left')
lb.place(relheight=1, relwidth=1)

root.mainloop()
