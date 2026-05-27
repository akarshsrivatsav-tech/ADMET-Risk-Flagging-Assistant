
# 🧠 Risk Engine Design Notes

## 📌 Objective
The risk engine is designed to simulate a simplified molecular screening system used in early-stage drug discovery pipelines.

It identifies potential risks using rule-based logic and provides workflow recommendations.

---

## ⚙️ Risk Rules

### 1. Molecular Weight Rules
- > 500 → High Molecular Weight (potential bioavailability issues)
- 150–500 → Moderate Molecular Weight (acceptable but monitored)
- < 100 → Small Fragment Molecule (may lack functional relevance)

---

### 2. Structural Rules
- Missing SMILES → Missing Structure
- SMILES length > 100 → Complex Structure (possible synthesis difficulty)

---

### 3. Data Integrity Rules
- Missing molecular formula → Incomplete Data
- Molecular weight = 0 → Invalid Data

---

## 📊 Risk Classification Logic

| Condition | Risk Level |
|----------|----------|
| No flags | Low Risk |
| 1 flag | Medium Risk |
| ≥2 flags | High Risk |
| Missing key data | Insufficient Data |

---

## 📈 Risk Scoring System
- Each risk flag = 2 points
- Score range: 0–10
- Capped at 10

---

## 🔄 Workflow Recommendation Logic

| Risk Level | Recommendation |
|-----------|---------------|
| Low Risk | Ready for Virtual Screening |
| Medium Risk | Requires Manual Review |
| High Risk | Reject Molecule |
| Insufficient Data | Retry Input |

---

## 🧠 Smart Behavior Implemented

### 1. Reflection Logic (Retry Mechanism)
- Initial attempt with user input
- Retry using lowercase
- Retry using capitalized input

---

### 2. Adaptive Logic
- Automatically corrects common spelling mistakes
  - Example: "asprin" → "aspirin"

---

### 3. Input Normalization
- Handles case-insensitive inputs
  - Example: "aSpIrIn" → "Aspirin"

---

## ⚠️ Edge Cases Handled
- Invalid molecule names
- Empty API responses
- Network/API failures
- Missing fields in API response
- Unsupported inputs (e.g., polymers like "Polyethylene")

---

## 🧪 Limitations
- No chemical validation engine
- No stereochemistry handling
- No real ADMET prediction
- Simplified rule-based approach

---

## 🤖 AI Assistance
- ChatGPT used for:
  - Code structuring
  - Debugging
  - Designing modular architecture

---

## 📌 Assumptions
- PubChem API provides accurate molecular data
- Molecule names are sufficient for identification
- Rule-based screening is acceptable for this simulation

---

## 💡 Design Philosophy
The system prioritizes:
- Simplicity
- Robust error handling
- Clear workflow decision-making
- Readability and modular design