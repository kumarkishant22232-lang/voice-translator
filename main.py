import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

from openai import OpenAI

def aiprocess(command):
    client = OpenAI(
        api_key="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"

    )

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=command,
        store=True,
    )

    return response.output_text



if __name__ == "__main__":
    speak(" How can I help you kishant?")
    # listen for voice commands
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        #recognize the voice command
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            speak(f"You said: {command}")


            # process the command
            if "open google" in command.lower() or "google kholie" in command.lower():
                webbrowser.open("https://www.google.com")
                speak("Opening Google" )
            elif "open youtube" in command.lower() or "youtube kholie" in command.lower():
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube" )
            elif "open facebook" in command.lower() or "facebook kholie" in command.lower():
                webbrowser.open("https://www.facebook.com")
                speak("Opening Facebook" )
            elif "open twitter" in command.lower() or "twitter kholie" in command.lower():
                webbrowser.open("https://www.twitter.com")
                speak("Opening Twitter" )
            elif "open instagram" in command.lower() or "instagram kholie" in command.lower():
                webbrowser.open("https://www.instagram.com")
                speak("Opening Instagram" )
            elif "open linkedin" in command.lower() or "linkedin kholie" in command.lower():
                webbrowser.open("https://www.linkedin.com")
                speak("Opening LinkedIn" )
            elif "open github" in command.lower() or "github kholie" in command.lower():
                webbrowser.open("https://www.github.com")
                speak("Opening GitHub" )
            elif "play " in command.lower() or "gaan chalao" in command.lower():
                song = command.lower().replace("play music", "").replace("music chalao", "").replace("play ", "").replace("gaan chalao", "").strip()
                link = musiclibrary.music.get(song)
                print("Song:", song)
                print("Link:", link)
                if link:
                    webbrowser.open(link)
                    speak(f"Playing {song}")
                else:
                    speak("Sorry, I didn't find that song.")
                
            elif "news" in command.lower() or "khabar kholie" in command.lower():
                    webbrowser.open("https://news.google.com")
                    speak("Opening Google News" )

                

            else:
                speak("Sorry, I didn't understand that command.")
                response = aiprocess(command)
                voice_output = response
                print("AI Response:", voice_output)
                speak(voice_output)    
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            speak("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak(f"Could not request results; {e}")