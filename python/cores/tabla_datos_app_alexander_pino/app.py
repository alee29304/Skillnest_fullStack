from flask import Flask, render_template

app = Flask(__name__)

# Base de datos ficticia de plataformas digitales
datos = [
    {"nombre":"Discord","logo":"discord.png","usuarios":"250M","fundado":"2015","pais":"EE.UU."},
    {"nombre":"Instagram","logo":"instagram.png","usuarios":"2.35B","fundado":"2010","pais":"EE.UU."},
    {"nombre":"Netflix","logo":"netflix.png","usuarios":"247M","fundado":"1997","pais":"EE.UU."},
    {"nombre":"Spotify","logo":"spotify.png","usuarios":"515M","fundado":"2006","pais":"Suecia"},
    {"nombre":"TikTok","logo":"tiktok.png","usuarios":"1.7B","fundado":"2016","pais":"China"},
    {"nombre":"Twitch","logo":"twitch.png","usuarios":"140M","fundado":"2011","pais":"EE.UU."},
    {"nombre":"YouTube","logo":"youtube.png","usuarios":"2.5B","fundado":"2005","pais":"EE.UU."},
]

# Ruta para mostrar la tabla con datos
@app.route("/tabla")
def mostrar_tabla():

    return render_template("tabla.html", datos=datos)


if __name__ == "__main__":
   app.run(debug=True)