command = ""
car_status = False
while True:
    command = input('> ').lower()

    if command == "start":
        if car_status:
            print('Car is already running')
        else:
            car_status = True
            print('Car started... ready to go')
    elif command == "stop":
        if car_status:
            car_status = False
            print('Car stopped')
        else:
            print('Car is already stopped')
    elif command == "help":
        print("""
start - to start car
stop - to stop car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that")

