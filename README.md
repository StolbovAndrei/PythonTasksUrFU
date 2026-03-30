# PythonTasksUrFU

Here are all the assignments I solved for the 3rd and 4th semesters at UrFU. By completing these tasks, I earned an automatic pass.  
The repository contains solutions covering:

- **3rd semester:** decorators, generators, JPEG processing, working with `lxml`, `httpx`, `wikipediaapi`, `numpy`, `pandas`, `datetime`, `logging`, `argparse`, etc.  
- **4th semester:** three algorithmic tasks from Yandex Contest (graph connectivity, BFS in a labyrinth, and a Dijkstra variant for max‑min path).

---

## 3rd Semester

### 🎨 Decorators

- **`reverse_string`** – filters a string (keeps only letters and spaces) using regex, then reverses it; returns `None` if the result is not a string.  
- **`prime_fizz_buzz_modificator`** – replaces numbers in a list according to rules:  
  `42` → `"Answer!"`, prime → `"Prime"`, divisible by 3 and 5 → `"FizzBuzz"`, etc.  
- **`retry`** – retries a function on specified exceptions with exponential backoff.  
- **`my_saviour_decorator`** – manually copies `__name__` and `__doc__` (without `functools.wraps`).  
- **`logging_decorator`** – logs file reading with error handling.

### 🔁 Generators

- **`take(n)`** – limits the output of a generator to `n` items.  
- **`gen_prime()`** – infinite prime number generator, used with `take`.  
- **`business_days(start, end)`** – yields weekdays between two dates.  
- **`generate_dow(month, day, year)`** – yields the names of weekdays starting from a given date.  
- **`business_plus_generate()`** – combines the two above generators.  
- **`head_generator(filename, n)`** – reads the first `n` lines of a file, using a logging decorator.

### 🖼️ JPEG and Image Processing

- **BMP reader** – manually reads a 24‑bit uncompressed BMP file: file header, info header, and pixel data (BGR → RGB).  
- **2D DCT / IDCT** – implemented using `scipy.fftpack.dct` (applied first to rows, then columns).  
- **Block‑wise transform** – applied to an image in 8×8 blocks; visualised coefficients in log scale.  
- **Reconstruction** – used IDCT to recover the original image and computed the reconstruction error.

### 📊 NumPy Tasks

- **`nearest_value`** – finds the element closest to a given number; returns the smallest if multiple.  
- **`sort_evens`** – sorts only the even numbers in a 1D array (leaves odds unchanged).  
- **`tensor_mask`** – applies XOR between a 3D tensor and a 2D mask (broadcasting).  
- **`num_sum`** – computes the sum of digits for each number in an array.  
- **`replace_nans`** – replaces `NaN` values with the column median; columns that are all `NaN` become zeros.

### 🐼 Pandas Tasks

- **`ZOOtable`** – converts a nested dictionary into a DataFrame, handles missing features, sorts columns, and drops columns with `NaN`.  
- **`rus_feature`** – parses Russian dates (e.g., "10 июля 1856 г."), computes full years lived, adds a column with the result.  
- **`men_stat`** – calculates max, min, median, mean, and variance of ages for male victims on the Titanic.  
- **`age_stat`** – builds a pivot table of maximum age by sex and passenger class.  
- **`fename_stat`** – extracts first names from passengers with "Miss", counts popularity, and sorts by popularity (descending) then alphabetically.

### 🌐 Web & XML

- **Wikipedia links** – uses `httpx` and `lxml` to extract all `/wiki/` links from a Wikipedia page.  
- **Wikipedia BFS** – finds the shortest path between two Wikipedia pages using `wikipediaapi` and BFS.  
- **HTTP Cat** – downloads a random cat image from `http.cat` and displays it.  
- **XML to JSON** – parses `movies.xml` into a Python dictionary and writes it as JSON.  
- **BibTeX parser** – reads a `.bib` file and converts it to a structured JSON representation.

---

## 4th Semester – Yandex Contest Labs

Three algorithmic problems solved on the Yandex Contest platform. Each reads from `in.txt` and writes to `out.txt`.

### 1. Graph Connectivity (Connected Components)

Given an adjacency matrix (size `n × n`), find all connected components using **DFS**.  
- **Input:**  
  - First line: `n`  
  - Next `n` lines: adjacency matrix  
- **Output:**  
  - First line: number of components  
  - One line per component: space‑separated vertex numbers (1‑based) sorted ascending  
  - Components are sorted by their smallest vertex

### 2. BFS in a Labyrinth

Find the shortest path in a grid where `0` = free, `1` = wall.  
- **Input:**  
  - First line: number of rows  
  - Second line: number of columns  
  - Next `rows` lines: the grid  
  - Next line: start coordinates (1‑based)  
  - Next line: finish coordinates (1‑based)  
- **Output:**  
  - `"N"` if no path exists  
  - Otherwise `"Y"` followed by the path coordinates (one per line, 1‑based) in order from start to finish

### 3. Max‑Min Path (Widest Path)

Variant of Dijkstra: find a path from start to finish that maximises the minimum edge weight along the path (the *capacity*).  
- **Input:**  
  - First line: `n`  
  - Next `n` lines: adjacency matrix (`32767` means no edge)  
  - Next line: start vertex (1‑based)  
  - Next line: finish vertex (1‑based)  
- **Output:**  
  - `"N"` if no path exists  
  - Otherwise `"Y"` followed by the path (space‑separated vertices, 1‑based) and the capacity value (integer) on a new line

---

## 🚀 How to Run

Most scripts are self‑contained and can be run directly. For tasks that read/write files, place `in.txt` in the same directory and the output will be written to `out.txt`.  
The repository includes all necessary imports; install missing dependencies with:

```bash
pip install numpy pandas matplotlib scipy pillow httpx lxml wikipedia-api python-dateutil
```

---

## 📂 Repository Structure

```
PythonTasksUrFU/
├── labs/                 # Yandex Contest solutions (4th semester)
│   ├── a1/               # Graph connectivity
│   ├── b2/               # BFS labyrinth
│   └── c3/               # Max‑min Dijkstra
├── mini python tasks/    # 3rd semester topics
│   ├── decorators/
│   ├── generators/
│   ├── JPEG/
│   ├── numpy(1-5) and pandas(6-10)/
│   ├── resources/
│   ├── wiki/
│   └── xpath/
├── .gitignore
└── README.md
```

---

## 📝 Note

All code is my own work, solved during the course. The repository serves as both a portfolio and a reference for future students.  
For any questions or suggestions, feel free to open an issue or contact me.