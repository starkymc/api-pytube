import requests
from pytube import YouTube

def download_song(title, api_key):
    # Utiliza la API de búsqueda de YouTube para obtener el ID del video
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=id&type=video&q={title}&key={api_key}"
    search_response = requests.get(search_url)
    search_data = search_response.json()
    video_id = search_data["items"][0]["id"]["videoId"]

    # Utiliza el ID del video para obtener la URL del video
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Descarga el video utilizando pytube
    
    
    yt = YouTube(video_url)
    if yt:
        video = yt.streams.filter(progressive=True, resolution="360p").first()

        video.download("G:/vid")
        #video.download("F:/")
        print(f"La canción {yt.title} se ha descargado con éxito.")
    

# Crea una lista de títulos de canciones
song_titles = [
"nancy bolo primicia 2021 huancavelicano",
"nancy bolo 2019 HD chimaychi",
"los hermanos bazan de conopa"

   
   
]

# Tu clave de API de YouTube
# Si no funciona el codigo cambiar de api
api_key = "AIzaSyA32BGxbsXTQDF4kLjQVAehfrNgAiBHm9I"

# Itera sobre cada título de la lista
for i,title in enumerate(song_titles):
    # Descarga la canción utilizando la función download_song()
    try:
        download_song(title, api_key)
        print(f"{i+1}: {title}")
    except Exception as e:
        print(f"Error al descargar la canción {title}: {e}")

print("Se han descargado todas las canciones de la lista.")
