# 🧪 ADMET Risk Flagging Assistant

## 📌 Overview
The ADMET Risk Flagging Assistant is a Python-based command-line tool designed to simulate a lightweight pre-screening system used in AI-driven drug discovery workflows.

It evaluates molecules using rule-based logic to identify potential risks before they proceed to expensive computational pipelines such as:
- ADMET prediction
- Virtual screening
- Retrosynthesis
- Generative AI pipelines

---

## 🚀 Features

### 🔍 Molecule Search
- Accepts molecule input (name)
- Fetches data from PubChem API
- Retrieves:
  - CID
  - Molecular Formula
  - Molecular Weight
  - Canonical SMILES
  - IUPAC Name (Scientific Name)

---

### ⚠️ Risk Flagging Engine
Applies rule-based logic to detect:
- High molecular weight
- Small molecule fragments
- Missing structure
- Invalid or incomplete data
- Complex structures

---

### 📊 Risk Classification
Classifies molecules into:
- Low Risk
- Medium Risk
- High Risk
- Insufficient Data

---

### 💡 Workflow Recommendation
Suggests next steps:
- Ready for Virtual Screening
- Requires Manual Review
- Reject Molecule
- Retry Input

---

### 🧠 Smart Features
- Input normalization (case-insensitive)
- Retry logic (lowercase + capitalized input)
- Auto-correction (e.g., "asprin" → "aspirin")
- Error handling for API failures and invalid inputs

---

### 🎨 User Interface
- Colored terminal output
- Structured report display
- Risk score visualization (0–10 scale)

---

## 🛠️ Installation

```bash
pip install requests
 
---

 ▶️ How to Run
python main.py

---

## 📸 Sample Outputs
See the `screenshots/` folder for example runs.

---

 🧪 Example Inputs
Aspirin
asprin
Caffeine
Ibuprofen
xyz

---
 📂 Project Structure
project/
│
├── main.py               # Entry point
├── api_utils.py          # API interaction logic
├── risk_engine.py        # Risk analysis engine
├── report_generator.py   # Output formatting
├── README.md
└── RISK_ENGINE_NOTES.md

---

 ⚠️ Assumptions
Input is a valid molecule name

PubChem API returns correct data

Focus is on lightweight screening (not deep chemistry)

---

 🚧 Limitations
No deep ADMET prediction

No SMILES validation engine

Does not support complex polymers or mixtures

Dependent on PubChem API availability

---

 🔧 Technologies Used
Python

Requests library
 📸 Sample Outputs
See the `screenshots/` folder for example runs.

PubChem PUG REST API

---

 👨‍💻 Author
Akarsh Srivatsav Pappala
