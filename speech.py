import speech_recognition as sr
import webbrowser as wb
v1=sr.Recognizer()
v2=sr.Recognizer()
with sr.Microphone() as source:
    print("search youtube")
    print ("speak now")
    audio=v2.listen(source)
if 'video' in v1.recognize_google(audio):
    v1=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print("search for video")
        audio=v1.listen(source)
        try:
            get=v1.recognize_goole(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnkownValueError:
            print("could not understand")
        except sr.RequestError as e:
            print("failed to get results".format(e))