class Garden:
    def __init__(self, name, location, size):
        self.name = name

class Weather:
    def __init__(self, temperature, humidity, day):
        self.temperature = temperature
        self.humidity = humidity
        self.day = day
    def __str__(self):
        return f'Day: {self.day} Temperature: {self.temperature}, Humidity: {self.humidity}'
    def pleasant(self):
        return self.temperature > 60 and self.temperature < 80 and self.humidity < 50
    def stormy(self):
        return self.temperature < 60 and self.humidity > 80
class RainyWeather(Weather):
    def __init__(self, temperature, humidity, rain_inches):
        super().__init__(temperature, humidity, thunderstorm)
        self.rain_inches = rain_inches
        self.thunderstorm = thunderstorm

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity}, Inches of rain: {self.rain_amount}'
    def pleasant(self):
        return super().pleasant() and self.rain_inches < 1
    def stormy(self):
        return super().stormy() or self.rain_inches > 2
class SunnyWeather(Weather):
    def __init__(self, temperature, humidity, uv_index):
        super().__init__(temperature, humidity)
        self.uv_index = uv_index

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity}, UV Index: {self.uv_index}'
    def pleasant(self):
        return super().pleasant() and self.uv_index < 6
    def stormy(self): 
        return False

class CloudyWeather(Weather):
    def __init__(self, temperature, humidity, cloud_cover):
        super().__init__(temperature, humidity)
        self.cloud_cover = cloud_cover

    def __str__(self):
        return f'Temperature: {self.temperature}, Humidity: {self.humidity}, Cloud Cover: {self.cloud_cover}'
    def pleasant(self):
        return super().pleasant() and self.cloud_cover < 50
    def stormy(self):
        return super().stormy() or self.cloud_cover > 50
