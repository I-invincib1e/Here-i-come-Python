#!/usr/bin/env python3
"""
Weather App - CLI
A simple weather information display.
"""

import random

def get_weather(city):
    """Simulate weather data (in real app, use API)"""
    weathers = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"]
    temp = random.randint(-10, 40)
    humidity = random.randint(20, 100)

    return {
        "city": city,
        "weather": random.choice(weathers),
        "temperature": temp,
        "humidity": humidity
    }

def display_weather(weather_data):
    print(f"\nWeather for {weather_data['city']}:")
    print(f"Condition: {weather_data['weather']}")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Humidity: {weather_data['humidity']}%")

def main():
    print("Weather App")
    print("-" * 20)

    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()

        if city.lower() == 'quit':
            break

        if city:
            weather = get_weather(city)
            display_weather(weather)
        else:
            print("Please enter a city name.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
