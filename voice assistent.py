import speech_recognition as sr
import pyttsx3
import datetime
import pyaudio
import wikipedia
import smtplib
import pyowm

# Initialize speech recognition and synthesis engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out the assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def recognize_voice():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        command = ''

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
        except sr.RequestError:
            print("Sorry, speech service is unavailable.")
        
        return command.lower()

# Function to get weather updates
def get_weather(city):
    try:
        owm = pyowm.OWM('bd5e378503939ddaee76f12ad7a97608')
        observation = owm.weather_at_place(city)
        weather = observation.get_weather()
        temperature = weather.get_temperature('celsius')['temp']
        status = weather.get_status()
        return f"The weather in {city} is currently {status} with a temperature of {temperature} degrees Celsius."
    except Exception as e:
        return "Failed to fetch weather information."

# Function to handle user queries
def handle_query(query):
    if 'hello' in query:
        speak("Hello! How can I assist you today?")
    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif 'date' in query:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}.")
    elif 'search' in query:
        search_query = query.replace("search", "").strip()
        speak("Searching the web...")
        try:
            result = wikipedia.summary(search_query, sentences=2)
            speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("It seems there are multiple results for your query. Can you please specify?")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any relevant information.")
    else:
        speak("I'm sorry, I didn't understand that.")

# Main function to handle user commands
def main():
    speak("Hello! I'm your voice assistant. How can I help you today?")
    while True:
        command = recognize_voice()
        
        if 'exit' in command:
            speak("Goodbye!")
            break
        
        handle_query(command)

if __name__ == "__main__":
    main()
