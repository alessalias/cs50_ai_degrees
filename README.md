# 🧠 AI movie-graph pathfinder

![Python](https://img.shields.io/badge/Python-3.11-blue)
![CS50 AI](https://img.shields.io/badge/CS50-AI_Project-orange)
![Logic](https://img.shields.io/badge/Search%20AI-✓-brightgreen)
![Status](https://img.shields.io/badge/Status-Complete-success)

A command-line tool that computes the **shortest path between two actors** based on shared movies — the classic “Six Degrees of Kevin Bacon” problem.  
It loads IMDb-style data, builds a graph of actors and movies, and uses **Breadth-First Search (BFS)** to find the minimum connection.

This project focuses on **clean architecture**, **explicit reasoning**, and **highly commented code** to make the decision-making process traceable — something recruiters appreciate when reviewing technical work.

---

## 📁 Project Structure

```
.
├── degrees.py      # Main program: loads data, handles input, BFS search
├── util.py         # Node class + stack/queue frontier implementations
├── large/          # Large IMDb-like dataset (people, movies, stars)
├── small/          # Small dataset for easier debugging
└── __pycache__/    # Python cache files
```

---

## 🧭 Overview

This project builds a **graph of actors** connected through **movies** they starred in.

- **Nodes** → actors  
- **Edges** → movies (actor A acted with actor B in movie X)  
- **Goal** → find the shortest chain from actor X to actor Y  
- **Algorithm** → *Breadth-First Search (BFS) over the actor graph*  
- **Output** → sequence of `(movie_id, person_id)` tuples describing the connection

```
[Actor A]
    │
    ├──(Movie X)──>[Actor B]
    │                 │
    └──(Movie Y)──>[Actor C]──(Movie Z)──>[Actor D]
```

BFS ensures you always discover the shortest chain first.

---

## 🧩 How the AI Works

At the core, the AI system solves a **graph shortest-path problem**.

### 1. Build the Knowledge Graph  
The program parses three CSVs:

- `people.csv` → actors  
- `movies.csv` → movies  
- `stars.csv` → links actor ↔ movie  

These populate:

```python
names = {}   # name → set(person_ids)
people = {}  # person_id → {name, birth, movies}
movies = {}  # movie_id → {title, year, stars}
```

### 2. Generate Neighbors

For a given actor:

```
neighbors_for_person(person_id)
→ returns { (movie_id, co_star_id), ... }
```

This becomes your action/state graph for BFS.

### 3. Run Breadth-First Search (BFS)

Basic BFS cycle:

```
Initialize queue with starting actor
Loop:
    Pop from frontier
    If actor == target → reconstruct path
    Else add all unexplored neighbors
```

Because BFS expands *level by level*, the first time you reach the target you have the **shortest** path.

###  Example Interaction

```
$ python degrees.py
Loading data...
Data loaded.
Name: Natalie Portman
Name: Tom Hanks

2 degrees of separation.
1: Natalie Portman and John Hurt starred in V for Vendetta
2: John Hurt and Tom Hanks starred in The Da Vinci Code
```

---

## ▶️ Running the Project

### **1. Install Python (3.10 recommended)**  
Any recent Python version works, but BFS performance improves with 3.10+.

### **2. Run using the large dataset (default):**

```
python degrees.py
```

### **3. Or specify a dataset:**

```
python degrees.py small
```

### **4. Follow the prompts:**

- Enter two actor names  
- The AI calculates the connection and prints it  

---

## 📘 Concepts Covered

This project demonstrates mastery of:

### 🔹 AI Search Algorithms  
- Breadth-First Search (BFS)  
- Frontier queues  
- Node state tracing  
- Path reconstruction  

### 🔹 Data Structures  
- Graph modeling  
- Dictionaries as hash maps  
- Sets for O(1) membership checking  

### 🔹 Software Engineering Practices  
- Modular architecture (`degrees.py` vs `util.py`)  
- Comment-driven development  
- Clean, methodical BFS implementation  
- Robust input handling  
- Debug-friendly structure (`small/` dataset)  

### 🔹 Algorithmic Thinking  
- State modeling  
- Action/state transitions  
- Avoiding cycles with explored sets  
- Complexity reasoning of BFS on large datasets  

---

## 📄 License

This project is open-source and available under the MIT License.
