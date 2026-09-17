# Time Complexity Visualizer

## Description

This project is a simple Python program that measures and visualizes the running time of different algorithms.

The program uses **Flask** to provide an API endpoint. It receives the algorithm name, input step, and maximum input size, then measures the running time and creates a graph.

The generated graphs are saved in the `snapshots/` folder.

## Algorithms

The project contains six algorithms:

| Algorithm | Time Complexity |
|---|---|
| Linear Search | O(n) |
| Binary Search | O(log n) |
| Bubble Sort | O(n²) |
| Nested Loops | O(n²) |
| Insertion Sort | O(n²) |
| Selection Sort | O(n²) |

## Requirements

- Python 3
- Flask
- Matplotlib
- NumPy

## Setup

Go to the project directory:

```bash


Create a virtual environment:

python3 -m venv venv

Activate it:

source venv/bin/activate

Install the required packages:

pip install flask matplotlib numpy
Run the Project

Start the Flask server:

python3 factorial.py

The server runs on:

http://localhost:8000
API Testing

The API endpoint is:

/analyze

It uses three parameters:

algo — algorithm to test
step — increase in input size
n_max — maximum input size
Linear Search
curl "http://localhost:8000/analyze?algo=linear_search&step=10&n_max=100"
Binary Search
curl "http://localhost:8000/analyze?algo=binary_search&step=10&n_max=100"
Bubble Sort
curl "http://localhost:8000/analyze?algo=bubble_sort&step=10&n_max=100"
Nested Loops
curl "http://localhost:8000/analyze?algo=nested_loops&step=10&n_max=100"
Insertion Sort
curl "http://localhost:8000/analyze?algo=insertion_sort&step=10&n_max=100"
Selection Sort
curl "http://localhost:8000/analyze?algo=selection_sort&step=10&n_max=100"
Output

For every request, the program:

Runs the selected algorithm.
Measures its running time.
Stores the input sizes and running times.
Creates a graph using Matplotlib.
Saves the graph in the snapshots/ folder.
Returns the results as JSON.
Includes the graph as a Base64 encoded image.
Snapshots

The project generates a separate image for each algorithm:

snapshots/
├── binary_search.png
├── bubble_sort.png
├── insertion_sort.png
├── linear_search.png
├── nested_loops.png
└── selection_sort.png
Project Structure
factorial.py
README.md
snapshots/
├── binary_search.png
├── bubble_sort.png
├── insertion_sort.png
├── linear_search.png
├── nested_loops.png
└── selection_sort.png
venv/
