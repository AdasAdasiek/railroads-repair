import os
print("Pobieranie requests")
os.system('pip install requests')
print("Pomyślnie pobrano.")
import requests
folder = input("Podaj folder w którym wgrany jest RailRoads: ")
link = "https://github.com/AdasAdasiek/railroads-repair/raw/main/files/RailRoads.exe"

def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        print("Nie ma takiego folderu.")
        exit()

    filename = url.split('/')[-1].replace(" ", "_")  
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("Zapisywanie do", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))

download(link, dest_folder=folder)
print("Pobrano plik")
