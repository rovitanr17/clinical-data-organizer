# Clinical Data Organizer

**A Python-based web application for exploring structured clinical data, patient record retrieval, and the foundations of Clinical Natural Language Processing (NLP).**

## 1. Project Overview

Clinical Data Organizer is a personal learning and portfolio project that demonstrates how Python, FastAPI, and web technologies can work together to retrieve and display structured patient information.

The application currently allows users to search fictional patient records by ID and view information about documented asthma history.

The project is being developed incrementally, beginning with Python fundamentals and progressing toward clinical text extraction, automated testing, and Clinical NLP.

> **Disclaimer:** This is an educational prototype using synthetic patient data only. It is not intended for clinical use, medical diagnosis, or treatment decisions.

## 2. Problem Background

Clinical information can be incomplete, inconsistent, or distributed across different records.

A particularly important distinction is the difference between a documented negative finding and information that has not been documented.

For example:

- `True` — A history of asthma is documented.
- `False` — The record explicitly indicates no history of asthma.
- `None` — Asthma history is not documented.

These values should not be treated as equivalent.

This project explores how such distinctions can be represented, retrieved, and presented in a simple application.

## 3. Project Objectives

The main objectives are to:

1. Practice Python programming using functions, lists, dictionaries, and conditional statements.
2. Build a simple patient record search system.
3. Develop REST API endpoints using FastAPI.
4. Connect a browser-based frontend to a Python backend.
5. Present clinical information in a user-friendly interface.
6. Explore the foundations of clinical text extraction.
7. Gradually introduce software testing and Clinical NLP evaluation.

## 4. Current Features

### Patient Record Search

Users can enter a patient ID and retrieve an existing synthetic patient record.

Example:

**Input:** `P003`

**Output:**

```json
{
  "id": "P003",
  "asthma_history": null
}
```

### Asthma History Status

The interface converts raw values into understandable labels.

| Python value | JSON value | Display label |
|---|---|---|
| `True` | `true` | History Present |
| `False` | `false` | No History |
| `None` | `null` | Not Documented |

### Patient Not Found

When a patient ID does not exist, the API returns HTTP status `404`.

```json
{
  "detail": "Patient not found"
}
```

### Clinical Text Extraction — Initial Python Prototype

A basic rule-based extraction function is implemented in `extractor.py`.

It recognizes specific phrases related to asthma history:

| Clinical text | Extracted value |
|---|---|
| No history of asthma. | `False` |
| History of asthma. | `True` |
| Patient reports a headache. | `None` |

This is an early learning prototype. It does not yet provide comprehensive clinical language understanding.

The text extraction functionality is planned for integration into the web interface.

## 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and application logic |
| FastAPI | Backend API development |
| Uvicorn | Local ASGI web server |
| HTML | Web interface structure |
| CSS | Interface styling |
| JavaScript | User interaction and API communication |
| Git | Version control |
| GitHub | Source code hosting and documentation |

No external database or machine learning model is required for the current version.

## 6. Project Structure

```text
clinical-data-organizer/
│
├── main.py
├── README.md
├── .gitignore
│
└── clinical_ui_practice/
    ├── patient_data.py
    ├── extractor.py
    ├── api.py
    └── index.html
```

**File descriptions:**

- `main.py` — Initial Python exercises involving patient records.
- `patient_data.py` — Synthetic patient records and patient lookup function.
- `extractor.py` — Basic rule-based asthma history extraction.
- `api.py` — FastAPI application and patient search endpoint.
- `index.html` — Browser-based interface using HTML, CSS, and JavaScript.
- `.gitignore` — Excludes local environment files and Python cache from version control.

## 7. Installation and Setup

### Prerequisites

- Python installed
- Git installed
- VS Code or another code editor
- A modern web browser

### Step 1 — Clone the repository

```bash
git clone https://github.com/rovitanr17/clinical-data-organizer.git
cd clinical-data-organizer
```

### Step 2 — Create a virtual environment

```powershell
python -m venv .venv
```

### Step 3 — Install dependencies

For Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install fastapi uvicorn
```

### Step 4 — Navigate to the API directory

```powershell
cd clinical_ui_practice
```

### Step 5 — Start the application

```powershell
..\.venv\Scripts\python.exe -m uvicorn api:app --reload
```

The development server should be accessible at:

`http://127.0.0.1:8000/`

### Step 6 — Open the application

Open the following address in your browser:

**http://127.0.0.1:8000/**

Enter a patient ID such as `P003`, then click **Find Patient**.

To explore the automatically generated FastAPI documentation, open:

**http://127.0.0.1:8000/docs**

## 8. Application Architecture

The application follows a simple frontend–backend architecture.

```text
User
  |
  v
Web Browser
(HTML, CSS, JavaScript)
  |
  | HTTP GET request
  v
FastAPI (api.py)
  |
  v
Patient Lookup Function
(patient_data.py)
  |
  v
Synthetic Patient List
  |
  v
FastAPI JSON Response
  |
  v
Browser Displays Results
```

### Example Workflow

1. A user enters patient ID `P003`.
2. JavaScript reads the ID from the input field.
3. The browser sends a request to `/patients/P003`.
4. FastAPI receives the request.
5. The `find_patient_by_id()` function searches the patient list.
6. The matching patient record is returned.
7. FastAPI sends the result as JSON.
8. JavaScript displays the information in the interface.

## 9. API Documentation

### GET `/patients/{patient_id}`

Retrieves a synthetic patient record by ID.

**Example request:**

```http
GET /patients/P003
```

**Successful response — HTTP 200:**

```json
{
  "id": "P003",
  "asthma_history": null
}
```

**Unsuccessful response — HTTP 404:**

```json
{
  "detail": "Patient not found"
}
```

### GET `/`

Returns the application's HTML user interface.

## 10. Current Limitations

The prototype has several limitations:

- Patient records are stored in a Python list rather than a database.
- Patient records are synthetic.
- The current web interface supports patient lookup but not persistent record updates.
- Text extraction relies on exact phrase matching.
- The extraction logic does not reliably understand complex negation, clinical context, family history, or temporal relationships.
- The application does not include user authentication.
- Machine learning and LLM-based extraction have not yet been implemented.
- No clinical performance or safety validation has been completed.

The application is intended only for learning and technical demonstration.

## 11. Development Roadmap

- [x] Implement structured patient records using Python.
- [x] Create a patient lookup function.
- [x] Build a FastAPI patient search endpoint.
- [x] Develop a basic HTML and CSS interface.
- [x] Connect JavaScript to the API.
- [x] Display readable asthma history statuses.
- [x] Implement an initial rule-based extraction function.
- [ ] Connect clinical text extraction to a FastAPI endpoint.
- [ ] Add the Clinical Text Extractor interface.
- [ ] Improve responsive UI/UX design.
- [ ] Add automated tests using pytest.
- [ ] Introduce persistent storage using SQLite.
- [ ] Create labeled synthetic clinical notes for evaluation.
- [ ] Evaluate precision, recall, and F1-score.
- [ ] Explore pretrained NLP models and LLM-based extraction.

## 12. Learning Outcomes

This project provides practical experience in:

**Python programming**
- Working with lists and dictionaries.
- Defining and calling functions.
- Using loops and conditional statements.
- Handling missing values.

**Backend development**
- Designing REST API endpoints.
- Returning JSON responses.
- Handling HTTP errors.
- Organizing Python modules.

**Frontend development**
- Building HTML forms.
- Styling interfaces with CSS.
- Handling events using JavaScript.
- Fetching data asynchronously from an API.

**Software engineering**
- Separating application responsibilities.
- Debugging integration issues.
- Using Git and GitHub for version control.
- Documenting development decisions and limitations.

## 13. Future Research Direction

The longer-term goal is to explore **Clinical Context Integrity in Natural Language Processing**.

Potential research topics include:

- Clinical entity extraction
- Negation detection
- Temporal reasoning
- Uncertainty representation
- Evidence traceability
- Reliable structured information extraction
- Evaluation of LLM-generated clinical information

Future research extensions will build on the current software foundation while introducing appropriate datasets, baselines, quantitative evaluation, and systematic error analysis.

---

**Project Type:** Clinical Informatics Prototype

**Domain:** Medical Informatics / Clinical NLP / Software Development

**Status:** Prototype under active development

**Data:** Synthetic patient records only