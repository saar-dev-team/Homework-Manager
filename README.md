<div align="center">

# Homework Manager
# 📚

### A FastAPI service for homework records

Create a homework item, list every item, and open one by id. Records stay in memory for the current run.

<br>

# 👨‍💻 **SAAR Dev Team**

### *Sadra Hatami • Arashk Alizadeh Shahrivar*

<br>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-499848?style=for-the-badge)](https://www.uvicorn.org/)
[![REST](https://img.shields.io/badge/API-REST-2C3E50?style=for-the-badge)](https://restfulapi.net/)
[![JSON](https://img.shields.io/badge/Format-JSON-003B57?style=for-the-badge)](https://www.json.org/)
[![HTTP](https://img.shields.io/badge/HTTP-Methods-00599C?style=for-the-badge)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
[![Docs](https://img.shields.io/badge/Docs-Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://swagger.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)](https://opensource.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/saar-dev-team/Homework-Manager)

<br>

[🌐 Organization](https://github.com/saar-dev-team)
•
[👤 Sadra Hatami](https://github.com/sadra-hatami)
•
[👤 Arashk Alizadeh Shahrivar](https://github.com/AASHTheDeveLopEr)

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [Why This Project?](#-why-this-project)
- [Endpoints](#-endpoints)
- [Rules](#-rules)
- [Project Structure](#-project-structure)
- [Technologies](#️-technologies)
- [Installation](#-installation)
- [Usage](#️-usage)
- [Notes](#-notes)
- [FAQ](#-faq)
- [Contact](#-contact)
- [License](#-license)
- [Support](#-support)

---

# 📖 About

**Homework Manager** is a small FastAPI service for school homework.

It stores lesson, topic, deadline, and priority in an in-memory dictionary. A client can create an item, list every item, or fetch one by numeric id. An exam topic is forced to the highest priority.

This repository is a companion to [School Manager](https://github.com/saar-dev-team/School-Manager). It holds the homework API for that project, built by **SAAR Dev Team**.

> **Tagline:** *A FastAPI homework service for lesson, topic, deadline, and priority.*

---

# 🚀 Why This Project?

A homework desk needs a small, clear API before it needs a database.

This service keeps that first step:

- One file, one process
- Create, list, and read
- A priority range of 1 to 5
- A special rule for exams

Records live for the current run. Restarting the app clears them.

---

# 🔌 Endpoints

| Method | Path | Role |
|---|---|---|
| `GET` | `/all_homework` | Return every stored item |
| `POST` | `/new-homework` | Create one item |
| `GET` | `/homework/{homework_id}` | Return one item |

Create fields:

| Field | Role |
|---|---|
| `lesson` | Subject name |
| `topic` | Homework topic |
| `deadline` | Due text |
| `priority` | Integer from 1 to 5 |

A missing id returns `404`. A priority outside 1–5 returns `400`.

---

# 📏 Rules

- Priority must be between 1 and 5.
- If the topic is `exam`, priority is set to 1.
- Ids are `homework_1`, `homework_2`, and so on.
- Storage is a Python dictionary. There is no database file.

---

# 📁 Project Structure

```text
Homework-Manager/
├── main.py
├── LICENSE
└── README.md
```

`main.py` is the whole service.

---

# 🛠️ Technologies

- Python 3.10+
- FastAPI
- Uvicorn

---

# 🚀 Installation

```bash
git clone https://github.com/saar-dev-team/Homework-Manager.git
cd Homework-Manager
pip install fastapi uvicorn
```

---

# ▶️ Usage

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API page.

Create an item:

```bash
curl -X POST "http://127.0.0.1:8000/new-homework?lesson=Math&topic=Algebra&deadline=Friday&priority=2"
```

List items:

```bash
curl http://127.0.0.1:8000/all_homework
```

Read one item:

```bash
curl http://127.0.0.1:8000/homework/1
```

---

# 📝 Notes

- This is a supplementary repository for [School Manager](https://github.com/saar-dev-team/School-Manager).
- Data is in memory only.
- The MIT license is in [LICENSE](LICENSE).

---

# ❓ FAQ

### Does it save after restart?

No. The dictionary is cleared when the process stops.

### What does priority 1 mean?

It is the top of the 1–5 range. An `exam` topic is placed there automatically.

### Is there a frontend?

No. Use the docs page or any HTTP client.

### Where is the main school project?

The main project is [School Manager](https://github.com/saar-dev-team/School-Manager). This repository is the homework API for it.

---

# 📬 Contact

**Team:**

### SAAR Dev Team

[GitHub](https://github.com/saar-dev-team)

Developers:

### Sadra Hatami
*Co-Founder*

[GitHub](https://github.com/sadra-hatami)

📧 [Email](mailto:sadra.hatami.1732@gmail.com)

### Arashk Alizadeh Shahrivar
*Co-Founder • AASH.py*

[GitHub](https://github.com/AASHTheDeveLopEr)

---

# 📄 License

This project is licensed under the **[MIT License](LICENSE)**.

Copyright (c) 2026 [Sadra Hatami](https://github.com/sadra-hatami), [Arashk Alizadeh Shahrivar](https://github.com/AASHTheDeveLopEr), and [SAAR Dev Team](https://github.com/saar-dev-team)

---

# ⭐ Support

If this service is useful as a study sample, please consider giving it a ⭐ on GitHub.

---

<div align="center">

## Designed & Developed with ❤️ by Sadra Hatami and Arashk Alizadeh Shahrivar of SAAR Dev Team

</div>
