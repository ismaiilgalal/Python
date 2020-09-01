import tkinter as tk
from tkinter import font
import requests

# API KEY: 49d8aef4735165dfa51eb6cc22168946
# API CALL: api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={your api key}
def test_function (entry):
    print ('This is the entry:', entry)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (C): %s ' % (name, desc, temp)
    except:
        final_str = 'Cannot retrieve this city info, you sure it is a real city?'
    return final_str

def get_weather(city):
    weather_key = '49d8aef4735165dfa51eb6cc22168946'
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APIKEY':weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(weather_url,params=params)
    weather = response.json()

    label ['text'] = format_response(weather)

HEIGHT = 500
WIDTH = 600

root = tk.Tk()
canvas = tk.Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='Landscape.png')
background_label = tk.Label (root, image = background_image)
background_label.place(relwidth=1, relheight=1)
#upper frame
frame = tk.Frame(root, bg='#80c1ff', bd = 5)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor = 'n' )

entry = tk.Entry(frame, font = ('old style', 10))
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", font = ('old style', 10), command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

#lowerframe

lowerframe = tk.Frame(root,bg='#80c1ff', bd = 10)
lowerframe.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor = 'n' )

label = tk.Label(lowerframe, font = ('old style', 12),  anchor = 'nw', justify = 'left', bd = '5')
label.place(relheight=1, relwidth=1)


root.mainloop()
