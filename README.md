
markdown

# Vehicle Search System

A simple semantic search demo built with [Chroma](https://www.trychroma.com/), a vector database. It lets you ask natural-language questions and returns the most relevant vehicle descriptions using embedding-based similarity search — not keyword matching.

## Features

- In-memory vector store (no setup required)
- Semantic search over short vehicle descriptions
- Interactive command-line query loop
- Returns top-N matches ranked by similarity distance

## Requirements

- Python 3.8+
- `chromadb`

## Installation

```bash
pip install chromadb
```

## Usage

Run the script:

```bash
python vehicle_search.py
```

Then type natural-language questions when prompted:

```
Vehicle Search System
Type 'exit' to quit.

Ask a question: what travels underwater?

Top Matches:
- submarine1 (distance: 0.3421): A submarine is a vehicle that travels underwater, used for naval operations, research, or exploration beneath the sea.
- boat1 (distance: 0.6127): A boat is a watercraft that travels on rivers, lakes, or the sea, used for fishing, transport, or leisure on water.

Ask a question: exit
Goodbye!
```

Type `exit` at any prompt to quit.

## How It Works

1. **Collection setup** — A Chroma collection named `vehicles` is created (or reused if it already exists).
2. **Adding documents** — Descriptive text about each vehicle is added along with a unique ID. Chroma automatically embeds each document using its default embedding function.
3. **Querying** — Each question you type is embedded the same way, and Chroma returns the documents whose embeddings are closest in vector space — i.e., the most semantically similar matches.
4. **Results** — The top matches are printed along with their document ID and similarity distance (lower = more similar).

## Customization

- **Add more vehicles**: extend the `documents` and `ids` lists in the script (make sure they stay the same length and IDs remain unique).
- **Change result count**: adjust `n_results` in the `collection.query(...)` call.
- **Persist data across runs**: swap `chromadb.Client()` for `chromadb.PersistentClient(path="./chroma_db")` to save the collection to disk instead of keeping it in memory.
- **Use a different embedding model**: pass a custom `embedding_function` when creating the collection (e.g., OpenAI, Sentence Transformers).

## Project Structure

```
.
├── vehicle_search.py   # Main script
└── README.md           # This file
```

## License

Free to use and modify for personal or educational purposes.