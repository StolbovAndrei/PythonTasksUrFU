import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
from PIL import Image
import requests
from io import BytesIO
from PIL import Image
import os


url = "https://habrastorage.org/r/w780/getpro/habr/post_images/a78/291/807/a7829180746c99c987384e4b2b6df7b8.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content)).convert('L')  # grayscale
img_array = np.array(img)

# Обрежем до размера, кратного 8 (для простоты)

# ## 3. Задание 0: считаем файл bmp
# Формат BMP (Bitmap) — один из самых простых графических форматов.
# Он состоит из:
# 1. **Файлового заголовка** (14 байт) — сигнатура "BM", размер файла, смещение к пикселям.
# 2. **Заголовка изображения** (обычно 40 байт — BITMAPINFOHEADER) — ширина, высота, бит на пиксель и т.д.
# 3. **Данных пикселей** — в формате BGR (не RGB!), с выравниванием до кратности 4 байтам по строке.

# Мы реализуем чтение простого 24-битного несжатого BMP.

def read_bmp_header(file_path):
    """
    Читает заголовки BMP-файла и возвращает метаданные.
    Поддерживает только 24-bit, uncompressed BMP.
    """
    with open(file_path, 'rb') as f:
        # --- Файловый заголовок (14 байт) ---
        signature = f.read(2)
        if signature != b'BM':
            raise ValueError("Файл не является BMP (неверная сигнатура).")

        file_size = int.from_bytes(f.read(4), 'little')
        f.read(4)  # зарезервировано (2x2 байта)
        pixel_data_offset = int.from_bytes(f.read(4), 'little')

        # --- Заголовок изображения (40 байт) ---
        header_size = int.from_bytes(f.read(4), 'little')
        if header_size != 40:
            raise ValueError("Поддерживаются только BITMAPINFOHEADER (40 байт).")

        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')
        planes = int.from_bytes(f.read(2), 'little')
        bit_count = int.from_bytes(f.read(2), 'little')
        compression = int.from_bytes(f.read(4), 'little')
        image_size = int.from_bytes(f.read(4), 'little')

        # Проверки
        if planes != 1:
            raise ValueError("Неподдерживаемое количество плоскостей.")
        if bit_count != 24:
            raise ValueError("Поддерживаются только 24-битные изображения.")
        if compression != 0:
            raise ValueError("Поддерживаются только несжатые BMP.")

        print(f"Ширина: {width}, Высота: {height}")
        print(f"Смещение данных пикселей: {pixel_data_offset} байт")
        print(f"Размер файла: {file_size} байт")

        return {
            'width': width,
            'height': height,
            'pixel_data_offset': pixel_data_offset,
            'file_size': file_size
        }


def read_bmp_pixels(file_path, width, height, pixel_data_offset):
    """
    Читает пиксели из BMP-файла и возвращает массив numpy в формате (H, W, 3) — RGB.
    В BMP пиксели хранятся снизу вверх и в порядке BGR!
    """
    with open(file_path, 'rb') as f:
        f.seek(pixel_data_offset)

        # В BMP каждая строка выравнивается до кратности 4 байтам
        bytes_per_pixel = 3
        row_bytes = width * bytes_per_pixel
        padding = (4 - (row_bytes % 4)) % 4  # 0, 1, 2 или 3 байта паддинга

        # Создаём массив для хранения изображения (в памяти будем хранить в RGB, сверху вниз)
        img = np.zeros((height, width, 3), dtype=np.uint8)
        print(img)

        # BMP хранит строки снизу вверх → читаем в обратном порядке
        for y in reversed(range(height)):
            row_data = f.read(row_bytes)
            # TODO: преобразуйте row_data в массив пикселей и запишите в img[y]
            # Помните: порядок байтов в BMP — BGR, а нам нужен RGB!
            # row_data — это bytes длиной row_bytes: [B0, G0, R0, B1, G1, R1, ...]
            # Подсказка: можно использовать np.frombuffer(row_data, dtype=np.uint8).reshape(-1, 3)
            # и затем поменять порядок каналов.
            row_data = np.frombuffer(row_data, dtype=np.uint8).reshape(-1, 3)
            img[y] = row_data[:, [2, 1, 0]]

            # Пропускаем паддинг (если есть)
            if padding > 0:
                f.read(padding)

        return img

test_bmp_path = "test_image.bmp"
if not os.path.exists(test_bmp_path):
    small_img = Image.fromarray(img_array[:448, :548], mode='L')
    small_img_rgb = small_img.convert('RGB')
    small_img_rgb.save(test_bmp_path)
    print(f"Создан тестовый файл: {test_bmp_path}")

# Прочитаем заголовок
meta = read_bmp_header(test_bmp_path)

bmp_img = read_bmp_pixels(test_bmp_path, meta['width'], meta['height'], meta['pixel_data_offset'])

# plt.figure(figsize=(6,6))
# plt.imshow(bmp_img)
# plt.title("Изображение, прочитанное вручную из BMP")
# plt.axis('off')
# plt.show()


## 3. Задание 1: реализуйте 2D ДКП

# ДКП в 2D можно выполнить построчно, а затем по столбцам (или наоборот).
# `scipy.fftpack.dct` по умолчанию работает с последним измерением.

def dct2(block):
    """
    Применяет 2D ДКП к блоку (например, 8x8).
    Подсказка: сначала по строкам (axis=1), потом по столбцам (axis=0).
    """
    # TODO: примените dct дважды — сначала по строкам, потом по столбцам
    # Используйте параметр norm='ortho' для ортонормированного ДКП (как в JPEG)
    return dct(dct(block, norm='ortho', axis=1), norm='ortho', axis=0)

def idct2(block):
    """
    Обратное 2D ДКП.
    """
    # TODO: аналогично, но с idct
    return idct(idct(block, norm='ortho', axis=1), norm='ortho', axis=0)

# Проверим на маленьком блоке 8x8
test_block = img_array[:8, :8].astype(np.float64)
dct_block = dct2(test_block)
idct_block = idct2(dct_block)

# Восстановленный блок должен быть почти равен исходному
print("Максимальная ошибка восстановления:", np.max(np.abs(test_block - idct_block)))


def apply_dct_to_image(img, block_size=8):
    H, W = img.shape
    img_dct = np.zeros_like(img, dtype=np.float64)

    for i in range(0, H, block_size):
        for j in range(0, W, block_size):
            block = img[i:i + block_size, j:j + block_size].astype(np.float64)
            # TODO: примените dct2 к block и сохраните результат в img_dct
            img_dct[i:i + block_size, j:j + block_size] = dct2(block)
    return img_dct


# Выполните ДКП
img_dct = apply_dct_to_image(img_array)

# Визуализируем коэффициенты ДКП (лог-масштаб для лучшей видимости)
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img_array, cmap='gray')
plt.title("Оригинал")
plt.axis('off')

plt.subplot(1, 2, 2)
# Применяем лог-масштаб, чтобы увидеть маленькие коэффициенты
plt.imshow(np.log(np.abs(img_dct) + 1), cmap='viridis')
plt.title("Коэффициенты ДКП (лог-шкала)")
plt.axis('off')

plt.tight_layout()
plt.show()


def apply_idct_to_image(img_dct, block_size=8):
    H, W = img_dct.shape
    img_rec = np.zeros_like(img_dct, dtype=np.float64)

    for i in range(0, H, block_size):
        for j in range(0, W, block_size):
            block_dct = img_dct[i:i + block_size, j:j + block_size]
            # TODO: примените idct2 и сохраните в img_rec
            img_rec[i:i + block_size, j:j + block_size] = idct2(block_dct)
    return img_rec


# Восстановим
img_reconstructed = apply_idct_to_image(img_dct)

# Сравним
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(img_array, cmap='gray')
plt.title("Оригинал")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(img_reconstructed, cmap='gray')
plt.title("Восстановлено из ДКП")
plt.axis('off')

plt.subplot(1, 3, 3)
diff = np.abs(img_array - img_reconstructed)
plt.imshow(diff, cmap='hot')
plt.title("Ошибка восстановления")
plt.axis('off')

plt.tight_layout()
plt.show()

print("Максимальная ошибка по всему изображению:", np.max(diff))

