import os
from flask import Flask, render_template

app = Flask(__name__)

def get_info():
    """Retrieve a list of images from the 'static/images' directory, including subdirectories."""
    images_dir = os.path.join(app.static_folder, 'images')
    info_list = []

    for anime_dir in os.listdir(images_dir):
        anime_path = images_dir+'/'+anime_dir
        
        if os.path.isdir(anime_path):
            info_list.append({
                "name": anime_dir,
                "images": 'images/'+anime_dir
            })
    
    return info_list


def trailer():
    map={}
    for file in os.listdir("static//trailer"):
        file_path = os.path.join("static//trailer", file)
        with open(file_path) as F:
            map[file.split(".")[0]] = F.read()
    return map



def description():
    map={}
    for file in os.listdir("static//description"):
        file_path = os.path.join("static//description", file)
        with open(file_path) as F:
            map[file.split(".")[0]] = F.read()
    return map


@app.route('/')
def index():
    """Render the index page with the list of images."""
    return render_template('index.html', anime_info=get_info(), description=description(), trailer=trailer()    )


if __name__ == '__main__':
    app.run(debug=True)

