# 🚀 GenAI RAG Chatbot

A production-ready Generative AI chatbot built using FastAPI, Streamlit, Docker, Google Gemini, and Retrieval-Augmented Generation (RAG).

The application allows users to upload documents, process them through a RAG pipeline, and interact with an AI assistant capable of answering questions based on uploaded knowledge sources.

---

## 🌟 Features

### AI Capabilities

* Google Gemini LLM Integration
* Retrieval-Augmented Generation (RAG)
* Context-Aware Question Answering
* Multi-Turn Chat Interface
* Document-Based Knowledge Retrieval

### Backend

* FastAPI REST API
* Modular Service Architecture
* Environment Variable Management
* API Documentation with Swagger

### Frontend

* Streamlit User Interface
* Interactive Chat Experience
* File Upload Support
* Real-Time Response Streaming Ready

### DevOps

* Dockerized Backend
* Dockerized Frontend
* Docker Compose Orchestration
* Easy Deployment Workflow

---

## 🏗️ Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ├── Gemini LLM
 │
 ├── RAG Service
 │
 └── Document Processing
       │
       ▼
   Uploaded Files
```

---

## 📂 Project Structure

```text
GENAI-PRO
│
├── backend
│   ├── core
│   ├── routes
│   ├── services
│   │   ├── rag_service.py
│   │   ├── gemini.py
│   │   └── utils.py
│   │
│   ├── data
│   └── app.py
│
├── frontend
│   └── app.py
│
├── data
│   └── uploads
│
├── .env
├── requirements.txt
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Tech Stack

### Languages

* Python

### AI & LLM

* Google Gemini
* LangChain
* RAG

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Deployment

* Docker
* Docker Compose

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd GENAI-PRO
```

### Create Environment

```bash
python -m venv .venv
```

### Activate

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

---

## 🐳 Run With Docker

Build Containers

```bash
docker compose build
```

Start Application

```bash
docker compose up
```

Run In Background

```bash
docker compose up -d
```

Stop Containers

```bash
docker compose down
```

---

## 🌐 Access Application

Frontend

```text
http://localhost:8501
```

Backend

```text
http://localhost:8000
```

API Documentation

```text
http://localhost:8000/docs
```

---

## 🎯 Future Improvements

* PDF Processing
* FAISS Vector Database
* ChromaDB Integration
* Chat Memory
* Authentication
* Multi-User Support
* Cloud Deployment
* CI/CD Pipeline

---

## 📸 Screenshots

(Add screenshots after deployment)

---

## 📈 Skills Demonstrated

* Generative AI
* RAG Systems
* LLM Integration
* FastAPI
* Streamlit
* Docker
* Backend Engineering
* AI Application Deployment

---

## 👨‍💻 Author

Built as part of an AI Engineering Portfolio showcasing practical Generative AI and Retrieval-Augmented Generation applications.

