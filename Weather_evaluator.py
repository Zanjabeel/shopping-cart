temp = float(input("What is the temperature? "))
sky = input('Is it sunny or not outside? (Y/N) ')

if sky.upper() == "Y" and temp > 40:
    print("The weather is HOT!")
    print("and the sun is smiling upon you ☀️!")
elif sky.upper() == "Y" and 20 < temp < 30:
    print("The weather is moderate and crisp!")
    print("It's a nice day 🙂.")
elif sky.upper() == "Y" and temp < 20 :
    print("The weather is very nice but a little cold 🍃!")
    print("The air won't be chilly I guess.")
elif sky.upper() == "N" and temp < 20:
    print("The weather is a little cold!")
    print("it's cloudy ☁️.")
elif sky.upper() == "N" and temp < 10:
    print("The weather is cold ❄️")
    print("And cloudy ☁️")
elif sky.upper() == "N" and temp < 0:
    print("The weather is very cold!")
    print("it's freezing ❄️❄️!")

