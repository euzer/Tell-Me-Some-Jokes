from urllib import request
import json
import pyttsx3

# fetch an url data of jokes
url = "https://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
print(r.getcode())
data = r.read()
jsonData = json.loads(data)
print(jsonData)

class Joke:

    def __init__(self, setup, punchline):
        self.setup = setup
        self.punchline = punchline

    def __str__(self):
        return f"Setup: {self.setup} Punchline: {self.punchline}"

jokes = []


for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"Got {len(jokes)} jokes")

for joke in jokes:
    print(joke)
    pyttsx3.speak("Setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("The Punchline")
    pyttsx3.speak(joke.setup)

    
