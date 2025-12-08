import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid[{api_key}&units=metric"# Units = metric for celcius

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]

        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        print(f"Weather in {city}: ")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print(f"Error: {data['message']}")

if __name__ == "__main__":
    api_key = "42e13bb19ee16f192e3be226014cb77d"
    city_name = input("Enter city name: ")
    get_weather(city_name, api_key)