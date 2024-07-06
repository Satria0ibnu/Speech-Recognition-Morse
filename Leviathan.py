import speech_recognition as sr
from MorseCodePy import encode, play, decode
import pyttsx3 

#pip install SpeechRecognition
#pip install pyaudio        
#pip install MorseCodePy
#pip install pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def capture_voice_input():
    with sr.Microphone() as source:
        print("Listening... (say 'goodbye' to quit)")
        audio = recognizer.listen(source)
    return audio

def speak(text):
    engine.say(text)
    engine.runAndWait()

def convert_voice_to_text(audio):
    # abbreviations source: https://www.yourdictionary.com/articles/morse-code-abbreviations    
    abbreviations = {
    "i have no more to send" : "30",
    "best regards" : "73",
    "love and kisses" : "88",
    "all after" : "AA",
    "all before" : "AB",
    "amplitude modulation" : "AM",
    "break" : "BK",
    "break-in" : "BK",
    "all between" : "BN",
    "been" : "BN",
    "separation" : "BT",
    "before" : "B4",
    "yes, correct" : "C",
    "check" : "CK",
    "call" : "CL",
    "i am closing my station" : "CL",
    "calling any station" : "CQ",
    "see you" : "CU",
    "day" : "DA",
    "from" : "DE",
    "this is" : "DE",
    "down" : "DN",
    "dear" : "DR",
    "distance" : "DX",
    "element" : "EL",
    "and" : "ES",
    "excellent" : "FB",
    "frequency modulation" : "FM",
    "from" : "FM",
    "good afternoon" : "GA",
    "go ahead" : "GA",
    "good evening" : "GE",
    "going" : "GG",
    "good morning" : "GM",
    "good night" : "GN",
    "give" : "GV",
    "error in sending" : "HH",
    "the telegraph laugh" : "HI",
    "high" : "HI",
    "headquarters" : "HQ",
    "here" : "HR",
    "hear" : "HR",
    "have" : "HV",
    "how" : "HW",
    "how copy" : "HW",
    "leave" : "LV",
    "milliamperes" : "MA",
    "no" : "N",
    "negative" : "N",
    "incorrect" : "N",
    "nothing doing" : "ND",
    "no more" : "NM",
    "number" : "NR",
    "now" : "NW",
    "i resume transmission" : "NW",
    "old boy" : "OB",
    "old chap" : "OC",
    "old man" : "OM",
    "operator" : "OP",
    "oldtimer" : "OT",
    "old top" : "OT",
    "point" : "PT",
    "press" : "PX",
    "received as transmitted" : "R",
    "are" : "R",
    "decimal point" : "R",
    "ragchew" : "RC",
    "concerning; regarding" : "RE",
    "receive" : "RX",
    "receiver" : "RX",
    "sweepstakes" : "SS",
    "zero" : "T",
    "transmit" : "TR",
    "transmit or receive" : "T/R",
    "that" : "TT",
    "thank you" : "TU",
    "transmitter" : "TX",
    "you" : "U",
    "very" : "VY",
    "watts" : "W",
    "word after" : "WA",
    "word before" : "WB",
    "word" : "WD",
    "well" : "WL",
    "will" : "WL",
    "weather" : "WX",
    "young lady" : "YL",
    "year" : "YR",
    "about" : "ABT",
    "addressee" : "ADEE",
    "address" : "ADR",
    "again" : "AGN",
    "antenna" : "ANT",
    "broadcast interference" : "BCI",
    "broadcast listener" : "BCL",
    "be seeing you" : "BCNU",
    "better" : "BTR",
    "semi-automatic key" : "BUG",
    "confirm" : "CFM",
    "i confirm" : "CFM",
    "callbook" : "CLBK",
    "called" : "CLD",
    "calling" : "CLG",
    "can't" : "CNT",
    "conditions" : "CONDX",
    "circuit" : "CKT",
    "see you later" : "CUL",
    "come" : "CUM",
    "difference" : "DIFF",
    "delivered" : "DLVD",
    "for" : "FER",
    "ground" : "GND",
    "guess" : "GESS",
    "giving" : "GVG",
    "hope" : "HPE",
    "repeat" : "IMI",
    "say again" : "IMI",
    "info" : "INFO",
    "a poor operator" : "LID",
    "long" : "LNG",
    "later" : "LTR",
    "letter" : "LTR",
    "leaving" : "LVG",
    "typewriter" : "MILL",
    "message" : "MSG",
    "prefix to radiogram" : "MSG",
    "net control station" : "NCS",
    "nothing" : "NIL",
    "i have nothing for you" : "NIL",
    "operator" : "OPR",
    "preamble" : "PBL",
    "package" : "PKG",
    "please" : "PSE",
    "power" : "PWR",
    "received" : "RCD",
    "receiver" : "RCVR",
    "refer to" : "REF",
    "referring to" : "REF",
    "reference" : "REF",
    "radio frequency interference" : "RFI",
    "station equipment" : "RIG",
    "repeat" : "RPT",
    "report" : "RPT",
    "radio teletype" : "RTTY",
    "readability, strength, tone" : "RST",
    "self-addressed, stamped envelope" : "SASE",
    "said" : "SED",
    "says" : "SEZ",
    "signed" : "SGD",
    "signature" : "SIG",
    "signal" : "SIG",
    "operator's personal initials or nickname" : "SINE",
    "schedule" : "SKED",
    "signal for help needed" : "SOS",
    "sorry" : "SRI",
    "single sideband" : "SSB",
    "station" : "STN",
    "some" : "SUM",
    "service" : "SVC",
    "prefix to service message" : "SVC",
    "traffic" : "TFC",
    "tomorrow" : "TMW",
    "thanks": "TNX",
    "tricks" : "TRIX",
    "that is" : "TTS",
    "television interference" : "TVI",
    "text" : "TXT",
    "your" : "UR",
    "yours" : "URS",
    "very fun business" : "VFB",
    "variable frequency oscillator" : "VFO",
    "words" : "WDS",
    "with" : "WID",
    "worked" : "WKD",
    "working" : "WKG",
    "words per minute" : "WPM",
    "word" : "WRD",
    "would" : "WUD",
    "transceiver" : "XCVR",
    "transmitter" : "XMTR",
    "crystal" : "XTAL",
    "wife" : "XYL",
    "end of message" : "AR",
    "stand by" : "AS",
    "invite receiving station to transmit" : "BK",
    "pause" : "BT",
    "break for text" : "BT",
    "beginning of message" : "KA",
    "end of the transmission" : "KN",
    "going off the air" : "CL",
    "clear" : "CL",
    "calling any amateur radio station" : "CQ",
    "go, invite any station to transmit" : "K",
    "go only, invite a specific station to transmit" : "KN",
    "all received OK" : "R",
    "end of contact" : "SK",
    "understood" : "VE"
    }

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        
        for phrase, abbreviation in abbreviations.items():
            if phrase.lower() in text.lower():
                text = text.replace(phrase.lower() + " ", abbreviation + " ")
        
        print("Processed Text:", text)
        print()

    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
        print()
    except sr.RequestError as e:
        text = ""
        print("Error:", e)
    return text

def process_voice_command(text):
    if "hello" in text.lower():
        print("Hello! How can I help you?")
    elif "goodbye" in text.lower():
        print("Goodbye! Have a great day!")
        return True
    return False

def encode_to_morse(text):
    if text:
        cipherText = encode(text, language='english')
        print("The Morse is : " + cipherText)
        print()
        return cipherText
    
def morse_to_sound(text):
    try:
        play(text, delay=0.3, volume=0.7)
    except AttributeError:
        pass

def decode_morse_input(cipherT):
    if cipherT:
        try:
            plainT = decode(cipherT, language='english', dot='.')
            print("\nThe Real Message is : " + plainT)
            speak("The real message is " + plainT)
            print()
        except TypeError:
            pass
    else:
        print("You didn't enter anything. Please enter a Morse code message.")


def homepage():
    print("------------------------------------")
    print("Welcome to the Morse Code Converter!")
    print("------------------------------------")
    print()
    print("1. Encode to Morse Code")
    print("2. Decode from Morse Code")
    print("3. Exit")
    print()
    choice = input("Please enter your choice: [1/2/3]: ")
    print()

    return choice
        

def main():
    while True:
        choice = homepage()

        if choice == '1':
            print("\nYou choose encode to Morse Code.")
            
            end_program = False
            while not end_program:
                audio = capture_voice_input()
                text = convert_voice_to_text(audio)
                end_program = process_voice_command(text)
                
                if end_program:
                    break

                cipherT = encode_to_morse(text)
                morse_to_sound(cipherT)

        elif choice == '2':
            print("\nYou choose to decode from Morse Code.")
            print()

            while True:
                print("\nexample input:")
                print(".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--")
                cipherT = input('please enter the morse message that you want to decode. (type end to quit)\n')

                if cipherT.lower() == "end":
                    print()
                    break

                decode_morse_input(cipherT)

        elif choice == '3':
            print("\nExiting the program...")
            break

        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")
    
    
if __name__ == "__main__":    
    main()