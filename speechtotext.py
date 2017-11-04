'''
Install PyAudio and Speech Recognition
pip install pyaudio
pip install speechrecognition
'''
import pyaudio
import wave
import speech_recognition as sr


#Definig recognizer
r = sr.Recognizer()

def play_audio(filename):
    chunk = 1024
    #Read audio file as binary i.e chunk
    wf = wave.open(filename, 'rb')
    #Load PyAudio Class
    pa = pyaudio.PyAudio()

    #Stream audio file to obtain data
    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    #Read data stream
    data_stream = wf.readframes(chunk)

    #Until the end of data stream
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


def initSpeech():
    print "Listening..."
    play_audio("./audio/audio_initiate.wav")
    print "Say Something..."

    #Definig the Microphone as Source
    with sr.Microphone() as source:
        audio = r.listen(source)
    play_audio("./audio/audio_end.wav")

    command = ""
    try:
        #Using google to recognize audio
        command = r.recognize_google(audio)
    except:
        print "Something went wrong!"

    print "Result: " + command

def speak_audio():
    '''
    missing link :(
    '''

initSpeech()