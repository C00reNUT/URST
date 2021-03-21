from PIL import Image
from tqdm import tqdm
import os

if __name__ == '__main__':
    os.makedirs("speed_test/", exist_ok=True)
    for i in tqdm(range(10)):
        size = 10000 - i * 1000
        image = Image.open("content/pexels-paulo-marcelo-martins-2412603.jpg")
        image = image.resize((size, size))
        image.save("speed_test/%d.jpg" % size)
