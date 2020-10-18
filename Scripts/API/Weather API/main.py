import requests


def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid=d7b4e2c3794bd6dcd2b27273645e4c78"
    data = requests.get(url).json()
    return data


def display_data(data):
    print("Weather details")
    print("weather-type: " + data['weather'][0]['main'])
    print("temperature: " + str(data['main']['temp']))
    print("pressure: " + str(data['main']['pressure']))
    print("humidity: " + str(data['main']['humidity']))
    print("wind-speed: " + str(data['wind']['speed']))


def complete_func():
    location = input('Enter a valid city\n')
    data = get_weather(location)
    if(data['cod'] != 200):
        print("The city is not valid")
        return

    display_data(data)


if __name__ == '__main__':
    complete_func()
