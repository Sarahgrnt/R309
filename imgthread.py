import requests
import threading
import time

img_url = [
#   'https://pixabay.com/images/id-1046544/'
    "https://cdn.pixabay.com/photo/2015/11/16/22/14/cat-1046544_1280.jpg",
    "https://cdn.pixabay.com/photo/2019/09/18/10/39/victoria-crowned-pigeon-4486154_1280.jpg"
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4] + ".jpg"
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__== '__main__':
    start = time.perf_counter()
    t = threading.Thread(target=download_image, args=[img_url[0]])
    t1 = threading.Thread(target=download_image, args=[img_url[1]])
    t.start()
    t1.start()
    t.join()
    t1.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

