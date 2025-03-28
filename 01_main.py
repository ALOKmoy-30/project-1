import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musiclibrary
import requests
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
news_apikey = "b667e0a67878404bbe060850161a5f00"

def speak(text):
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
   if  "open google" in c.lower():
       webbrowser.open("https://google.com")
   elif "open instagram" in c.lower():
       webbrowser.open("https://instagram.com")
   elif "open facebbok" in c.lower():
       webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
       webbrowser.open("https://youtube.com")
   elif "open github" in c.lower():
       webbrowser.open("https://github.com")
   elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
   elif "news" in c.lower():
       r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_apikey}")
       if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
   else:
    #    let open ai handle the request
        pass
        
if __name__ == '__main__':
    speak("hey alok")
    while True :
    
        try: 
             # listen for the wake word "hello jarvis"
             # obtain audio from the microphone
             r = sr.Recognizer()
             with sr.Microphone() as source:
                print("listening.....")
                audio = r.listen(source,timeout=2,phrase_time_limit=2)
                word = r.recognize_google(audio)
              
        # recognize speech using google
        
             print("recognizing....")
    
             if (word.lower() == "jarvis"):
                 speak("ya")
                 with sr.Microphone() as source:
                     print("jarvis is listening.....")
                     audio = r.listen(source)
                     command = r.recognize_google(audio)
                     print(command)
             
                     processcommand(command)
             
             else:
                 print(f"Recognized word: {word}")
                 speak(f"You said {word}")
        # listen for command
        except Exception as e:
            print(f"error: {e}")

        
