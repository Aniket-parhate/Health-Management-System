                                           # Health Management System
# 3 clients - John, Alex and Harry
from datetime import datetime
k = 1
while k:
    current_date = datetime.now()
    print(current_date.strftime("%H:%M"))
    print("Do you want to log or retrieve the data")
    a = (input())
    if a == "log" :
        print("whose data you want to log John, Alex or Harry")
        b = (input())
        if b == "John" :
            print("Do you want to log exercise or food")
            c = (input())
            if c == "exercise":
                f = open("JohnExercise.txt", "a")
                print("Which exercise have you done?")
                exercise = (input())
                f.writelines(exercise)
                f.writelines(" - ")
                f.write(current_date.strftime("%H:%M") + '\n')
                f.close()
            elif c == "food":
                f = open("Johnfood.txt", "a")
                print("What food have you taken in your meal?")
                food = (input())
                f.writelines(food)
                f.writelines(" - ")
                f.write(current_date.strftime("%H:%M") + '\n')
                f.close()
        elif b == "Alex":
            print("Do you want to log exercise or food")
            c = (input())
            if c == "exercise":
                f = open("AlexExecise.txt", "a")
                print("Which exercise have you done?")
                exercise = (input())
                f.writelines(exercise)
                f.writelines(" - ")
                f.write(current_date.strftime("%H:%M") + '\n')
                f.close()
            elif c == "food":
                f = open("Alexfood.txt", "a")
                print("What food have you taken in your meal?")
                food = (input())
                f.writelines(food)
                f.writelines(" - ")
                f.write(current_date.strftime("%H:%M") + '\n')
                f.close()
        elif b == "Harry" :
            print("Do you want to log exercise or food")
            c = (input())
            if c == "exercise":
                f = open("HarryExercise.txt", "a")
                print("Which exercise have you done?")
                exercise = (input())
                f.writelines(exercise)
                f.writelines(" - ")
                f.write(current_date.strftime("%H:%M") + '\n')
                f.close()
            elif c == "food":
                f = open("Harryfood.txt", "a")
                print("What food have you taken in your meal?")
                food = (input())
                f.writelines(food)
                f.writelines(" - ")
                f.write(current_date.strftime("%H:%M") + '\n')
                f.close()

    if a == "retrieve" :
        print("whose diet want you to retrieve John, Alex or Harry")
        b = (input())
        if b == "John":
            print("Do you want to retrieve exercise or food")
            c = (input())
            if c == "exercise":
                f = open("JohnExercise.txt")
                print(f.read())
            elif c == "food":
                f = open("Johnfood.txt")
                print(f.read())
        if b == "Alex":
            print("Do you want to retrieve exercise or food")
            c = (input())
            if c == "exercise":
                f = open("AlexExecise.txt")
                print(f.read())
            elif c == "food":
                f = open("Alexfood.txt")
                print(f.read())
        if b == "Harry":
            print("Do you want to retrieve exercise or food")
            c = (input())
            if c == "exercise":
                f = open("HarryExercise.txt")
                print(f.read())
            elif c == "food":
                f = open("Harryfood.txt")
                print(f.read())