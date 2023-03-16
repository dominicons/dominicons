import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import openai
# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define function to send email
def send_email(recipient, subject, body):
    # Set up SMTP connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    
    # Create email message
    message = f'Subject: {subject}\n\n{body}'
    
    # Send email
    server.sendmail('your_email@gmail.com', recipient, message)
    
    # Close SMTP connection
    server.close()

# Greet user
hour = datetime.datetime.now().hour
if hour >= 0 and hour < 12:
    speak('Good morning!')
elif hour >= 12 and hour < 18:
    speak('Good afternoon!')
else:
    speak('Good evening!')

# Listen for commands
while True:
    try:
        with sr.Microphone() as source:
            print('Listening...')
            audio = r.listen(source)
            command = r.recognize_google(audio)
            print(f'You said: {command}\n')
            
            # Process command
            if 'Wikipedia' in command:
                speak('Searching Wikipedia...')
                command = command.replace('Wikipedia', '')
                results = wikipedia.summary(command, sentences=2)
                speak('According to Wikipedia, ')
                speak(results)
                
            elif 'open YouTube' in command:
                webbrowser.open('https://www.youtube.com')
                
            elif 'open Google' in command:
                webbrowser.open('https://www.google.com')
                
            elif 'play music' in command:
                music_dir = 'C:\\Users\\Username\\Music\\'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
                
            elif 'what time is it' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak(f'The time is {time}')
                
            elif 'send email to' in command:
                try:
                    speak('What should I say?')
                    body_audio = r.listen(source)
                    body_text = r.recognize_google(body_audio)
                    
                    speak('Who should I send it to?')
                    recipient_audio = r.listen(source)
                    recipient_text = r.recognize_google(recipient_audio)
                    
                    send_email(recipient_text, 'Test Email', body_text)
                    
                    speak('Email sent successfully!')
                except Exception as e:
                    print(e)
                    speak('Sorry, I was not able to send the email.')
                
            elif 'exit' in command:
                speak('Goodbye!')
                break
            
    except Exception as e:
        print(e)
        speak('DIem quynh da den cat moi.')
