import time , os 
import pyttsx3 as speaker
import math
import requests, json
from datetime import date
import wikipedia
import webbrowser
from googlesearch import search
import wolframalpha

#todo: setting the engine to speak
engine = speaker.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)




# todo fuctions are here

def search_int(ui):
    global num
    num.clear()
    for word in ui.split():
        if word.isdigit():
            num.append(int(word))
    return num

def product_finder():
        result = 1
        for x in num:
            result =result *x
        return result

def LARGE():
     large=num[0]
     for x in range(1,length):
         if(large<num[x]):
             large=num[x]
     return(large)

def HCF():
    global num
    def gf(x,y):
        while y:
            x,y = y,x%y

        return x

    num1=num[0]
    num2=num[1]
    gcd = gf(num1,num2)
    for i in range(2, len(num)):
        gcd = gf(gcd, num[i])
    return gcd


def LCM():
    large=LARGE()
    for i in range(large,product_finder()+1,large):
        for j in range(length):
            if(length-1==j):
                if(i%num[j]==0):
                    return(i)
            if(i%num[j]==0):
                pass
            else:
                break

def searching(input_user):
            x = input_user.split()
            position = (x.index('about'))
            if ('in' in x) and ('hindi'  in x):
                end_position = (x.index('in'))
                joning_string_in_one = (x[position+1:end_position])
                wikipedia.set_lang("hi")
            else:
                joning_string_in_one = (x[position+1:])
            wiki_keyword= (" ".join(joning_string_in_one))
            try:
                print("This is about ",wiki_keyword) 
                print("********************************************************************")
                result = wikipedia.summary(wiki_keyword,sentences =3)       
                print(result)
                print('********************************************************************')

            except wikipedia.exceptions.PageError :
                print ("Something went wrong , Enter again")
            except :
                print('Try again ; Something went wrong')


def getGenders(names):
    try:
        url = ""
        cnt = 0
        if not isinstance(names,list):
            names = [names,]
        
        for name in names:
            if url == "":
                url = "name[0]=" + name
            else:
                cnt += 1
                url = url + "&name[" + str(cnt) + "]=" + name
            

        req = requests.get("https://api.genderize.io?" + url)
        results = json.loads(req.text)
 
        for result in results:
            if result["gender"] is not None:
                usname = result["name"]
                usgender = result["gender"]
                uspre = result["probability"]
                statement  = f" Name = {usname} \n Gender = {usgender} \n Predicted Accuracy = {uspre*100} "
            else:
                statement = 'gender not found'

        return statement
    except requests.exceptions.ConnectionError :
        return ("Please connect to the Internet")
    except :
        return('Something went wrong , Try agian later')
        



def google_search(ui):
    ui =  ui.split()
    if ("google" in ui) or ("search" in ui):
        if "google" in ui:
            ui.remove("google")
        elif "search" in ui:
            ui.remove("search")
        else:pass
    ui= " ".join(ui)
    links =[]
    try:
        for i in search(ui, tld="co.in", num=10, stop=10, pause=2):
            links.append(i)   
        webbrowser.open(links[1])
    except :
        print("Please connect the Internet ,then search ")



def opening_apps(ui):
    if "note" in ui:
            speaker.speak("opening notepad")
            os.system("Notepad")
    elif ("video player" in ui) or ("vlc" in ui):
        speaker.speak("opening VLC media player ")
        speaker.speak("Please wait some seconds")
        os.system ("VLC")
    elif ("excel" in ui):
        speaker.speak("Please wait some seconds")
        speaker.speak("opening MS Excel")   
        os.startfile('"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007.lnk"')
    elif ("slide" in ui)or ("powerpoint" in ui) or ("ppt" in ui):
        speaker.speak("opening MS Powerpoint")
        speaker.speak("Please wait some seconds")
        os.system("powerpnt")
    elif ("word" in ui):
        speaker.speak("opening MS Word")
        speaker.speak("Please wait some seconds")
        os.system("winword")
    elif ("chrome" in ui ) or ("google" in ui):
        speaker.speak("opening google chrome ")
        speaker.speak("Please wait some seconds")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")   
        speaker.speak("It will take time to process")
            
    elif ("typing master" in ui) or ("typing" in ui):
        os.startfile('D:\\TypingMaster\\tmaster.exe')
    else:
        print("Application not exists")
 
def wishing ():
    x=  int(time.strftime('%H'))
    if 4 <= x < 12:
        print('Good Morning')
        speaker.speak('Good Morning sir !')        
    elif 12<= x < 17:
        print('Good Afternoon') 
        speaker.speak('Good Afternoon sir !')        
    elif 17 <= x < 19 : 
        print('Good Evening')
        speaker.speak('Good Evening sir !')        
    else :
        print('Good Night')
        speaker.speak('Good Night sir !')                    
    print("hello sir ! i am Your assistant \n")





# todo ==> lists of the program      
num = []

# todo printing the first iinpression of the program

print('\n======================================================================')
print('            WELCOME TO THE REAL TIME CHAT BOT APP                    ')
print("========================================================================")
print ("  Made By  \"Vinay Prajapati \" \n\n")
speaker.speak("welcome to the real time chat bot app  made by Vinay Prajapati")
wishing()


i =1
while(i):
    print ("________________________________________\n")
    take_input = input ("Ask me :")
    ui =  take_input.lower()
    length = len(num)



    # todo: now the conditional formatting started 

    if 'wish' in ui:
        wishing()

    elif ("hi" in ui ) or ("hello" in ui ):
        print('Hello Sir , I am your Assistant Jarvis')
        speaker.speak('Hello Sir , I am your Assistant Jarvis')


    elif 'lcm' in ui:
        search_int(ui)
        print('The LCM is ',LCM())
        print("")


    elif ('hcf' in ui or 'gcd' in ui):
        search_int(ui)
        print('The HCF is', HCF())
        speaker.speak(f"the highest common factor is {HCF()} . ")
        print("")


    elif 'time' in ui:
        hr = time.strftime('%H')
        min  = time.strftime('%M')
        sec  = time.strftime('%S')
        time_string = time.strftime('%H: %M : %S %p')
        print(f"the current time is {time_string} " )
        speaker.speak(f'the current time is {hr} hours {min} minute and {sec} seconds')
        print("")

    elif  ("you like " in ui ):
        print("I like to solve your problem that you want to search \n") 
        speaker.speak("I like to solve your problem that you want to search")


    elif ("check gender" in ui) or ("check" in ui ):
        name = input("Enter first-name which you want to check gender: ")
        print (getGenders(name))


    elif 'date' in ui:
        date = time.strftime("%d %B %Y")
        print("the today's date is :" ,date )
        speaker.speak(f"sir , Today's date is {date}")
        print("")

        


    elif ('sub' in ui)or ('minus'in ui):
        search_int(ui)
        print (f'the subtraction of {num[0]} from {num[1]} is', num[1]-num[0])
        print("")

    elif ('add' in ui ) or ('sum' in ui):
        search_int(ui)
        print('the sum of the numbers are : ', sum(num))
        print("")
    
    elif ('product'in ui) or ('multiply' in ui):
        search_int(ui)  
        print('the product of the numbers are : ',product_finder() )
        print("")
    
    elif ('divide' in ui) or ("/" in ui):
        search_int(ui)
        print('the quotient is ',num[0]/num[1])
        print('the remainder is ',num[0]%num[1])
        print("")

    elif ('percent' in ui):
        search_int(ui)
        
        print(f'the percentage of given number {num[0]} to total number {num[1]} is {(num[0]/num[1])*100}% \n')
 

    elif ('square root' in ui):
        search_int(ui)
       
        print (f"The square root of {num[0]} is {math.sqrt(num[0])} \n")
     


    elif 'do for me' in ui:
        print('Sir , I am Your Assistant . TO get more information about me :  type  --> help. \n')
    

    elif ('your name' in ui) and ('boss' not in ui) :    
        print('My name is Jarvis \n')
        


    elif (('made' in ui) or ('boss' in ui) or ('invent' in ui)) and  ('who' in ui ):
   
        print(' sir! , My Boss name is "Vinay prajapati" who invent me \n.')
        speaker.speak(" sir! , My Boss name is 'Vinay prajapati' who invent me . ")
        


    elif 'your age' in ui or ('your dob' in ui) or ('your date of birth' in ui):
        cy =date.today().year
        cm =date.today().month
        cd =date.today().day

        x= date(2021,4,18)
        ay = cy - x.year
        am = cm - x.month
        ad = cd - x.day  
        print(f'Sir , My age is {ay} year, {am} month, {ad} days \n')
        speaker.speak(f'Sir , My age is {ay} year, {am} month, {ad} days')


    elif ("about this"in ui) :
        print('**************************************************')
        print ("This is the real bot application that makes your work easier . And this is made by Vinay Prajapati ")
        print('**************************************************')
        take= input ("Do you want to search about this bot inventor : ")
        if "y" in take : 
            print("for more information about Inventor of this bot you can visit : ")
            print("Blogger - 1, \n Github - 2 \n Youtube - 3 \n Faceboo - 4")
            x= int(input ("what you want to search , hit the number button 1/2/3/4 :\n "))
            if x==1:
                webbrowser.open('https://codervinay.blogspot.com/')
            elif x==2:
                webbrowser.open('https://github.com/programmervinay')
            elif x == 3:
                webbrowser.open('https://www.youtube.com/channel/UCO3n_mr_e-BewMEAkrRYsiA')
            else :        
                print("Enter the number that is infront of the keyword of the sites \n")
        else : pass
        
        
    elif ('exit' in ui) or ('quit' in ui) or ('end' in ui):    
        print('Thanks for joning us and using this that is made by ~ @Vinay prajapati ~ \n')
        speaker.speak('Thanks for joning us and using this that is made by Vinay prajapati')
        i=0
    
    elif ('my youtube channel' in ui):     
        print('Sir, Your YouTube Channel name is Terminate learnings \n')
        speaker.speak('Sir, Your YouTube Channel name is Terminate learnings')

    elif ('youtube channel' in ui)and ('my' not in ui ):  
        print('My boss YouTube Channel name is Terminate learnings \n')
        speaker.speak('My boss YouTube Channel name is Terminate learnings')
    
    
    elif ("Who is ") in ui :
        relatives(ui)
        

    # todo searching from internet 
    elif ('search' in ui) and ('wiki' in ui):
        searching(ui)
        print("")


    elif ("google" in ui) or ("search" in ui):
        google_search(ui)
        print("")

#! here we start the application opening 
    elif ('open' in ui) or ('start' in ui):
        opening_apps(ui)

    elif "help" in ui :
        print('_______________________________________________')
        print('               ~~ BOT HELP MENU ~~             ')   
        print('-----------------------------------------------')
        print ("")
        print('Some Commands are given below that you can use it :')
        print ("1. Use as calclator like add , subtract ,etc . \n 2.  Chat as a time pass \n 3. open any app like -->open google chrome ' \n 4. Quick Wikipedia search like --> search wiki/search about Covid 19 \n 5. Quick Check Date and Time \n 6. Most amazing you can check Gender By name; type --> check gender " )

        
    else: 
        try:
            app = wolframalpha.Client ("QW847R-QXARLXVUX7")
            res = app.query(ui)
            print (next(res.results).text)
            speaker.speak(next(res.results).text)
        except Exception:
            print(("Connect to the Internet"))
            speaker.speak("sorry sir , I can't find the usefu result for you")

























