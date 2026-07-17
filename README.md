# CT-200 AI Test Case Generator

An AI-powered document analysis system built using **FastAPI**, **SQLite**, **SQLAlchemy**, and **Google Gemini**. The application parses CT-200 PDF manuals, extracts document hierarchy, stores multiple document versions, compares revisions, and generates software test cases using Generative AI.

---

## Features

- Parse CT-200 PDF manuals
- Extract document hierarchy (Headings & Sections)
- Store documents in SQLite
- Support multiple document versions
- Compare document versions
- Browse document hierarchy
- Search document sections
- AI-powered test case generation using Google Gemini
- REST APIs with FastAPI
- Interactive Swagger API documentation

---

## Tech Stack

### Backend
- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite

### AI
- Google Gemini API
- google-genai SDK

### PDF Processing
- PyMuPDF (fitz)
- pdfplumber

### Other Libraries
- Pydantic
- python-dotenv
- Uvicorn

---

## Project Structure

```
tri9t-ai-internship-assignment/
│
├── app/
│   ├── ai.py
│   ├── database.py
│   ├── models.py
│   ├── parser.py
│   ├── routes.py
│   ├── schemas.py
│   ├── utils.py
│   └── main.py
│
├── data/
│   ├── ct200_manual.pdf
│   └── ct200_manual_v2.pdf
│
├── tests/
│
├── ingest_manual.py
├── ingest_v2.py
├── init_db.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/NAGESHPATCHIPALA21/tri9t-ai-internship-assignment.git

cd tri9t-ai-internship-assignment
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Example:

```
GEMINI_API_KEY=AIzaSy..................................
```

---

## Initialize Database

```bash
python init_db.py
```

---

## Ingest Documents

Version 1

```bash
python ingest_manual.py
```

Version 2

```bash
python ingest_v2.py
```

---

## Run Application

```bash
python -m uvicorn app.main:app --reload
```

Application:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Documents

```
GET /documents
```

Returns all uploaded documents.

---

## Versions

```
GET /versions
```

Returns all document versions.

---

## Browse Nodes

```
GET /nodes
```

Returns all parsed document sections.

---

## Get Node

```
GET /nodes/{id}
```

Returns a specific document node.

---

## Search

```
GET /search?q=keyword
```

Search document content.

---

## Compare Versions

```
GET /compare?v1=v1&v2=v2
```

Compares two document versions and identifies:

- Added sections
- Removed sections
- Modified sections
- Unchanged sections

---

## Generate AI Test Cases

```
POST /generate
```

Example Request

```json
{
    "node_ids":[1,2,3]
}
```

Example Response

```json
{
    "generated_test_cases":"..."
}
```

---

## Database Schema

### Document

- id
- name

### DocumentVersion

- id
- version
- document_id

### Node

- id
- title
- body
- level
- page
- parent_id
- version_id
- content_hash

---

## AI Workflow

1. User selects document sections.
2. Node contents are fetched from SQLite.
3. Context is sent to Google Gemini.
4. Gemini generates structured software test cases.
5. Generated test cases are returned through the API.

---

## Future Improvements

- Save user selections
- Store generated test cases in SQLite
- Test case staleness detection
- Authentication
- Docker support
- CI/CD pipeline

---

## Author

**Nagesh Patchipala**

B.Tech CSE (IoT, Cyber Security & Blockchain)

Chaitanya Bharathi Institute of Technology

GitHub:
https://github.com/NAGESHPATCHIPALA21

---

## License

This project was developed as part of the **Tri9T AI Internship Assignment**.