# foundation-recap-python

This repository contains practice examples that recap foundational skills essential for GenAI solutioning and building FastAPI microservices.

Each part focuses on a specific concept, and culminates in a mock FastAPI app that brings everything together.

---

## Directory Structure
```bash
foundation-recap-python/
├── fr-asyncio # Async IO example
├── fr-pydantic # Data validation and parsing
├── fr-os-uuid-datetime # Utility libraries - os, uuid, datetime
├── fr-dataclasses # Usage of Python dataclasses
├── fr-typing # Type hinting with typing module
├── mock-app/ # FastAPI mock app that brings all above into one combined example
└── fast-api-app/ # FastAPI app to revise basics - endpoints, requests
```

---

## How to run
1. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. To run individual files:
    ```bash
    python <filename.py>
    ```

3. To run the server:
    ```
    cd fr-mock-app
    uvicorn fr-app:app --reload
    ```
4. Test the endpoint:
    ```http
    POST http://127.0.0.1:8000/generate
    ```