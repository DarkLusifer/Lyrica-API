# ===================Demo code==================== #
import requests

#GET method
url = "https://lyricaapi.onrender.com/lyrics?song=SONG_NAME"
re = get(url)

print(re.text)

#POST method
url = "https://lyricaapi.onrender.com/lyrics"
data = {
    "song":"SONG_NAME"
    }
re = requests.post(url, json=data)

print(re.text)
# ================================================= #


# API ownership alright received ©️ Mr_darklusifer
