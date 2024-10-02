import random

class Garden:
    def __init__(self, plant_growth=0, health=10):
        self.plant_growth = plant_growth
        self.health = health

    def show_status(self):
        print(f"Plant growth: {self.plant_growth}, Health: {self.health}")

class Weather:
    def __init__(self, temperature, humidity, day):
        self.temperature = temperature
        self.humidity = humidity
        self.day = day

    def __str__(self):
        return f'Day {self.day}: Temperature: {self.temperature}°C, Humidity: {self.humidity}%'

    def affect(self, garden):
        garden.plant_growth += 1
        garden.health += 1

class RainyWeather(Weather):
    def __init__(self, temperature, humidity, rain_inches, day):
        super().__init__(temperature, humidity, day)
        self.rain_inches = rain_inches

    def __str__(self):
        return f'Day {self.day}: Rainy Weather - Temperature: {self.temperature}°C, Humidity: {self.humidity}%, Rain: {self.rain_inches} inches'

    def affect(self, garden):
        garden.plant_growth += 2
        garden.health += 2
        if garden.plant_growth > 10:
            garden.health -= 1
            print("Too much rain! Plant health decreases.")

class SunnyWeather(Weather):
    def __init__(self, temperature, humidity, uv_index, day):
        super().__init__(temperature, humidity, day)
        self.uv_index = uv_index

    def __str__(self):
        return f'Day {self.day}: Sunny Weather - Temperature: {self.temperature}°C, Humidity: {self.humidity}%, UV Index: {self.uv_index}'

    def affect(self, garden):
        garden.plant_growth += 3
        garden.health += 1

        if self.uv_index > 8:
            garden.health -= 1
            print("High UV index! Plant health decreases.")

def simulate_weather():
    garden = Garden()
    
    for day in range(1, 11):
        weather_type = random.choice([RainyWeather, SunnyWeather])
        temperature = random.randint(15, 35)
        humidity = random.randint(30, 100)
        if weather_type == RainyWeather:
            rain_inches = round(random.uniform(0.5, 3.0), 1)
            weather = RainyWeather(temperature, humidity, rain_inches, day)
        else:
            uv_index = random.randint(1, 11)
            weather = SunnyWeather(temperature, humidity, uv_index, day)
        
        print(weather)
        weather.affect(garden)
        garden.show_status()
        print()
simulate_weather()
