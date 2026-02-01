
import win32com.client as wincom

def speak(text):
    """Converts text to speech using the Windows SAPI engine."""
    speaker = wincom.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

if __name__ == '__main__':
    print("Welcome to Robo Guy --- By Abhay")
    while True:
        txt=str(input("Write to make me Speak : "))
        if txt=="exit":
            speak("Lo Siento, Wilson")
            break
        speak(txt)
