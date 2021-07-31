import wolframalpha
import pyttsx3 as speaker
import urllib

#todo: setting the engine to speak
engine = speaker.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

while True:
    print("\n____________________________________________\n")
    ui= input("Ask me : ")
    if "your name" in ui:
        print("My name is Jarvis, made by Vinay Prajapati")
        speaker.speak("My name is Jarvis, made by Vinay Prajapati")
    else:
        try: 
            app = wolframalpha.Client("QW847R-QXARLXVUX7")
            res = app.query(ui)
            print (next(res.results).text)
            speaker.speak(next(res.results).text)
            
        except urllib.error.URLError:
                    print(("Connect to the Internet"))
                    speaker.speak("sorry sir , I can't find the useful result for you")
        except StopIteration : 
            print(f"Sorry ,I am not able to {ui} :( ")


# QW847R-QXARLXVUX7



