import os
from Flask import Flask, request, render_template

app = Flask(__name__)

YT_API_KEY = 'YOUR_API_KEY'

youtube = build("youtube", "v3", credentials=YT_API_KEY)

# Search youtube
def search_youtube(query):
    return

# Root route -> POST
@app.route('/', methods=['GET', 'POST'])
def index():
    videos = []
    belt = 'white'
    position = ' '

    # if POST
    if request.method == 'POST':
        query = f"{position} {belt} jiu jitsu"
        videos = search_youtube(query)
    
    return render_template('index.html', videos=videos, belt=belt, position=position)

if __name__ == "__main__":
    main()
