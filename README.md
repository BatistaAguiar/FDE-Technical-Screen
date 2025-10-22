# 📦 FDE Technical Screen — Package Sorter

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🧭 Overview

This repository was developed as part of the **FDE Technical Screening** challenge.  
It implements a **deterministic classification algorithm** that sorts packages into three categories — `STANDARD`, `SPECIAL`, or `REJECTED` — based on physical characteristics such as volume and mass.

The solution emphasizes **data validation**, **robust logic**, and **unit-test coverage** to ensure operational reliability in logistics and warehouse automation contexts.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Logic & Classification Rules](#-logic--classification-rules)
- [Validation & Error Handling](#-validation--error-handling)
- [API Specification](#-api-specification)
- [Examples](#-examples)
- [Setup & Execution](#-setup--execution)
- [Testing](#-testing)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## ⚙️ Logic & Classification Rules

Packages are automatically sorted into predefined stacks according to the following criteria:

| Condition | Classification |
|------------|----------------|
| Volume ≥ 1,000,000 cm³ OR any dimension ≥ 150 cm | Bulky |
| Mass ≥ 20 kg | Heavy |
| Bulky **and** Heavy | **REJECTED** |
| Bulky **or** Heavy (but not both) | **SPECIAL** |
| Neither bulky nor heavy | **STANDARD** |

**Decision Matrix:**

| Bulky | Heavy | Result |
|:------:|:------:|:------:|
| ❌ | ❌ | STANDARD |
| ✅ | ❌ | SPECIAL |
| ❌ | ✅ | SPECIAL |
| ✅ | ✅ | REJECTED |

---

## 🧩 Validation & Error Handling

The system enforces strict input validation to ensure consistent performance and data integrity.

### Input Constraints
- All parameters (`width`, `height`, `length`, `mass`) **must be numeric** (`int` or `float`).
- All parameters **must be positive (> 0)**.

### Exceptions
| Error Type | Trigger Condition |
|-------------|-------------------|
| `TypeError` | Non-numeric input |
| `ValueError` | Zero or negative values |

---

## 🧠 API Specification

**Function Signature**

```python
sort(width: float, height: float, length: float, mass: float) -> str
```

**Return Values**
- `"STANDARD"`
- `"SPECIAL"`
- `"REJECTED"`

---

## 🚀 Examples

```python
from src.sorter import sort

print(sort(10, 10, 10, 1))        # STANDARD
print(sort(100, 100, 100, 1))     # SPECIAL (volume == 1_000_000 → bulky)
print(sort(150, 10, 10, 1))       # SPECIAL (dimension >= 150 → bulky)
print(sort(10, 10, 10, 20))       # SPECIAL (mass >= 20 → heavy)
print(sort(200, 200, 200, 20))    # REJECTED (both bulky and heavy)
```

---

## 🧱 Setup & Execution

### Optional: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

---

## 🧪 Testing

Run all unit tests with:
```bash
python -m unittest discover -s tests -v
```

Expected output:
```
OK
```

---

## 🔭 Future Enhancements

To scale this module into production-grade logistics software, the following roadmap items are envisioned:

- ✅ **CLI Support** – Enable command-line sorting of multiple packages via CSV import.
- 🌐 **REST API Integration** – Expose the classification service through a Flask/FastAPI endpoint.
- 🧾 **Batch Analytics** – Aggregate package classifications for operational dashboards.
- 🧠 **Machine Learning Extension** – Predict classification anomalies using empirical distribution data.
- 🧍 **User Interface** – Add a lightweight web dashboard for visual monitoring.

---

## 🤝 Contributing

I welcome collaborative innovation. To contribute:

1. **Fork** the repository.
2. **Create** a feature branch:  
   `git checkout -b feature/your-feature`
3. **Commit** your changes:  
   `git commit -m "Add new feature"`
4. **Push** to your branch:  
   `git push origin feature/your-feature`
5. **Open a Pull Request** describing your enhancement.

Ensure all unit tests pass and new code is covered by tests.  
Follow PEP 8 conventions for Python style consistency.

---

## ⚖️ License

This project is released under the [MIT License](LICENSE).  
Use freely with attribution.
