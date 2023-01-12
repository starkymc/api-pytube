import requests
from pytube import YouTube
import colorama
from colorama import Fore
from colorama import Style

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

        video.download("G:/video")
        #video.download("F:/")
        #print(f"La canción {yt.title} se ha descargado con éxito.")
        print(Fore.BLUE + Style.BRIGHT + f"La canción {yt.title} se ha descargado con éxito." + Style.RESET_ALL)
    

# Crea una lista de títulos de canciones
song_titles = [
 "agua marina vol -1 mix antiguas"
]

# Tu clave de API de YouTube
# Si no funciona el codigo cambiar de api
api_key = "AIzaSyA32BGxbsXTQDF4kLjQVAehfrNgAiBHm9I"

# Itera sobre cada título de la lista
for i,title in enumerate(song_titles):
    # Descarga la canción utilizando la función download_song()
    try:
        download_song(title, api_key)
        #print(f"{i+1}: {title}")
        print(Fore.BLUE + Style.BRIGHT + f"{i+1}: {title}" + Style.RESET_ALL)
    except Exception as e:
        colorama.init()
        print(Fore.RED  + f"Error al descargar la canción {title}: {e}" + Style.RESET_ALL)
        #print(f"Error al descargar la canción {title}: {e}")

print(Fore.YELLOW +f"Se han descargado todas las canciones de la lista." + Style.RESET_ALL)

