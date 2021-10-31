'''hello everyone!!! I am Pratyush and this is a basic pybullet project to make a keyboard controlled car(husky) using torque control(you can use velocity control instead) and to show the information about joints this car is having.

controls:
          1. forward arrow key ==> forward
          2. backward arrow key ==> backward
          3. left arrow key ==> left rotate
          4. right arrow key ==> right rotate
          5. 'r' button ==> reverse
          6. 'a' button ==> increase speed''' 

import pybullet as p
import pybullet_data

p.connect(p.GUI)  #or p.SHARED_MEMORY or p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
p.setGravity(0, 0, -10)     #setting environment gravity
carpos = [0, 0, 0.1]        

car = p.loadURDF("husky/husky.urdf", carpos[0], carpos[1], carpos[2])

numJoints = p.getNumJoints(car)        #getting information of joints
for joint in range(numJoints):
  print(p.getJointInfo(car, joint)[0:2])

a=0
maxForce = 50 #Newton

while (1):
	keys = p.getKeyboardEvents()
	
	for k, v in keys.items():
	
		if (v & p.KEY_IS_DOWN):
			if (k == p.B3G_LEFT_ARROW ):
		    
		    		targetVel = 1.51
			    
		    		for joint in range(2, 6):
		    			p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,force = 49.8)
					
			    
				
		    		p.setJointMotorControl2(car,jointIndex=2,controlMode=p.TORQUE_CONTROL,force = -62.3-a)
		    		p.setJointMotorControl2(car,jointIndex=3,controlMode=p.TORQUE_CONTROL,force = 62.3+a)
		    		p.setJointMotorControl2(car,jointIndex=4,controlMode=p.TORQUE_CONTROL,force = -62.3-a)
		    		p.setJointMotorControl2(car,jointIndex=5,controlMode=p.TORQUE_CONTROL,force = 62.3+a)
				
		    		p.stepSimulation()
			if (k == p.B3G_RIGHT_ARROW ):
		    
		    		targetVel = 1.51
			    
		    		for joint in range(2, 6):
		    			p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,force = 49.8)
					
					
		    		p.setJointMotorControl2(car,jointIndex=2,controlMode=p.TORQUE_CONTROL,force = 62.3+ a)
		    		p.setJointMotorControl2(car,jointIndex=3,controlMode=p.TORQUE_CONTROL,force = -62.3-a)
		    		p.setJointMotorControl2(car,jointIndex=4,controlMode=p.TORQUE_CONTROL,force = 62.3+a)
		    		p.setJointMotorControl2(car,jointIndex=5,controlMode=p.TORQUE_CONTROL,force = -62.3-a)
				
		    		p.stepSimulation()
		    
			if (k == p.B3G_UP_ARROW ):
				
				
				targetVel = -1.51 - a
				for joint in range(2, 6):
					p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel,force = maxForce)
			    
				p.stepSimulation()
				
			if (k == p.B3G_DOWN_ARROW ):
				targetVel = 1.51 + a
				for joint in range(2, 6):
					p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel,force = maxForce)
			    
				p.stepSimulation()
				
			if (k == ord('r')):
		    
		    		targetVel = 1.51
			    
		    		for joint in range(2, 6):
		    			p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,force = 49.8)
					
					
		    		p.setJointMotorControl2(car,jointIndex=2,controlMode=p.TORQUE_CONTROL,force = 62.3)
		    		p.setJointMotorControl2(car,jointIndex=3,controlMode=p.TORQUE_CONTROL,force = -62.3)
		    		p.setJointMotorControl2(car,jointIndex=4,controlMode=p.TORQUE_CONTROL,force = 62.3)
		    		p.setJointMotorControl2(car,jointIndex=5,controlMode=p.TORQUE_CONTROL,force = -62.3)
				
		    		p.stepSimulation()
		    		
			
			
		
		if (v & p.KEY_WAS_RELEASED):
		
			targetVel = 0
			for joint in range(2, 6):
				p.setJointMotorControl2(car, joint, p.VELOCITY_CONTROL,targetVelocity = targetVel,force = maxForce)
		    
			p.stepSimulation()
			
		if (k == ord('a')):
			if (v & p.KEY_WAS_RELEASED):
				a=a+1
			
			
			
p.getContactPoints(car)
p.disconnect()

print("import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
")
