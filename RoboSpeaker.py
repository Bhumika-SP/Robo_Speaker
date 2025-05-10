import pyttsx3


def speak():
    engine = pyttsx3.init()

    while True:
        text = input("What do you want me to say? (Type 'stop' to exit): ")
        if text.lower() == "stop":
            print("Exiting...")
            break

        engine.say(text)
        engine.runAndWait()


speak()