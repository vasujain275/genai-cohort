# Basic Ollama Chat API using FastAPI

- To run this code, you need to have Ollama installed and running on your machine.

- Actiate uv env

```bash
source .venv/bin/activate
```

- Install the required packages from `requirements.txt`

```bash
uv pip install -r requirements.txt
```

- Run the FastAPI server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- Open your browser and go to `http://localhost:8000/docs` to see the API documentation and test the endpoints.
