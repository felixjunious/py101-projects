class TemperatureConverter:
    @staticmethod
    def celcius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celcius(f):
        return (f - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        c = TemperatureConverter.fahrenheit_to_celcius(f)
        return TemperatureConverter.celsius_to_kelvin(c)

    @staticmethod
    def kelvin_to_fahrenheit(k):
        c = TemperatureConverter.kelvin_to_celsius(k)
        return TemperatureConverter.celcius_to_fahrenheit(c)

if __name__ == '__main__':
    f = TemperatureConverter.celcius_to_fahrenheit(100)
    c = TemperatureConverter.fahrenheit_to_celcius(100)
    k = TemperatureConverter.celsius_to_kelvin(100)

    print(f,c,k)