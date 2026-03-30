import httpx
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

number_to_image = 522
url = f"https://http.cat/{number_to_image}"

# Пошлем get запрос
response = httpx.get(url)

if not response.status_code == 200:
    print(f"Failed to retrieve image. Status code: {response.status_code}")
    exit()

FILE_NAME = Path("answer.jpg")

with open(FILE_NAME, "wb") as f:
    f.write(response.content)

im = plt.imread(FILE_NAME)
plt.imshow(im)
plt.show()
