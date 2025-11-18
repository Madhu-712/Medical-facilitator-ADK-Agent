# Medical-facilitator-ADK-Agent

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/4ec2b129-44e4-4943-960f-86094add1e12" />




# 🏥 Medical-Facilitator-ADK-Agent 
**Multi-Agent Medical Facilitation System using ADK + MCP**

---

## 📌 Overview  
**Medical-Facilitator-ADK-Agent** is an intelligent multi-agent system built using the **Agent Development Kit (ADK)** and the **Model Context Protocol (MCP)**.  

This project consists of **two core sub-agents**:  
1. **📄 Data Retriever Agent** – Extracts patient information from `patientsinfo.pdf` and answers related queries.
2. **🩺 Medical Facilitator Agent** – Acts as a comprehensive medical concierge facilitating treatment, logistics, administration, and generating a final treatment summary, which is then stored in the **Google Cloud Storage bucket (`report-summary`)**.

---

## 🔧 Architecture

```

```
             ┌──────────────────────────────┐
             │     patientsinfo.pdf         │
             └─────────────┬────────────────┘
                           │
                 (1) Data Retrieval
                           │
            ┌──────────────▼──────────────┐
            │   Data Retriever Agent      │
            │  - PDF parsing              │
            │  - Query answering          │
            └──────────────┬──────────────┘
                           │
           (2) Medical Liaison & Processing
                           │
            ┌──────────────▼──────────────┐
            │  Medical Facilitator Agent  │
            │  - Treatment guidance       │
            │  - Travel + logistics       │
            │  - Medical liaison          │
            │  - Report generation        │
            └──────────────┬──────────────┘
                           │
                 (3) Cloud Storage Export
                           │
            ┌──────────────▼──────────────┐
            │ GCS Bucket: report-summary  │
            │  - Stores final reports     │
            └─────────────────────────────┘
```

```

---

# 🤖 Agents

## 📄 Data Retriever Agent  
The **Data Retriever Agent** is responsible for:  
- Extracting information from `patientsinfo.pdf`  
- Structuring retrieved data  
- Answering user queries related to patient information  
- Providing context for downstream processing by the Medical Facilitator Agent  

---

## 🩺 Medical Facilitator Agent  
The **Medical Facilitator Agent** acts as a complete medical concierge and patient-care guide.  
It provides detailed, supportive, and actionable responses to all patient and user queries.

### 🎯 Core Responsibilities

1. **Patient Advocacy**  
   - Serve as the patient’s trusted guide  
   - Help them understand treatment plans, options, and processes  

2. **Logistics Coordination**  
   - Arrange/advise on flights, hotels, local transport  
   - Provide itinerary and scheduling guidance  

3. **Medical Liaison**  
   - Connect patients with doctors and specialists  
   - Assist with appointment coordination  
   - Provide clarity on medical procedures  

4. **Administrative Support**  
   - Help with medical record transfers  
   - Assist with paperwork, insurance, payments  
   - Communicate with hospitals on the patient's behalf  

5. **Personalized Support**  
   - Assist with language translation  
   - Guide post-treatment care and recovery planning  
   - Offer culturally appropriate recommendations  

6. **Package Creation**  
   - Create all-inclusive medical travel packages  
   - Include treatment, travel, lodging, cost breakdowns  
   - Provide transparent budgeting  

---

### 🧠 How the Medical Facilitator Agent Works

1. **Bridge Between Patient & Provider**  
   Acts as a key link between international patients and foreign healthcare providers ensuring smooth communication.

2. **Concierge-Level Support**  
   Works like a professional concierge, offering end-to-end medical travel guidance.

3. **Uses a Strong Provider Network**  
   Leverages hospitals, specialists, travel partners, translators, and care coordinators.

4. **Transparent Service Model**  
   Provides clear, ethical breakdowns of service fees, hospital charges, travel costs, and package inclusions.

---

### 📌 Output Requirements  
When responding to user queries, the Medical Facilitator Agent must:  

- Give **comprehensive**, **structured**, and **practical** guidance  
- Include actionable next steps  
- Offer alternative options when helpful  
- Be empathetic, clear, and culturally sensitive  
- Avoid unsafe or unverified medical advice  
- Produce a **final treatment summary report** stored in the **`report-summary` GCS bucket**

Example outputs include:  
- Treatment plan summaries  
- Doctor/hospital recommendations  
- Travel & logistics guidance  
- Administrative checklists  
- Post-treatment care plans  
- Full medical travel packages  

---

## 📁 Project Structure

Medical-facilitator-ADK-Agent/

├── agent.py                      # Main orchestrator for ADK agents

├── prompts.py                    # System prompts + agent instructions

├── tools.py                      # Utility functions, modular tools, helpers


├── .env                          # Environment variables

├── __init__.py                   # Package initializer

│

├── subagent/

│   ├── __init__.py               # Subagent module initializer

│   │

│   ├── data/                     # Internal test resource directory

│   │   └── patientsinfo.pdf      # Sample patient data used by retriever

│   │

│   ├── data_retriver_agent.py    # PDF & X-ray interpreter (multimodal extraction)

│   └── medical_facilitator_agent.py



│                                 # Medical summarization + concierge logic

│

├── Architecturediagrams/         # Architecture diagrams (PNG, SVG, PDF)

│   ├── architecture.png

│   ├── architecture.svg

│   ├── architecture.pdf

│   ├── multi_agent.png


│   ├── workflow.png
│   └── ...
│

├── reports/                      # Final generated medical summaries

│   ├── post-diagnosis-report-patient_summary.pdf


│   ├── patient_summary.pdf
│   └── ...
│

├── outputs/                      # (Optional: For intermediate data)
│

├── requirements.txt              # Python dependencies

└── README.md                     # Main documentation


## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Madhu-712/Medical-facilitator-ADK-Agent.git
cd Medical-facilitator-ADK-Agent
````

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file:

```env
GCS_BUCKET_NAME=report-summary
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```

### 5️⃣ Run the agent system

```bash
adk web --port 8080
```

---

## 🧠 How the System Works (End-to-End)

1. User uploads or queries information from `patientsinfo.pdf`
2. Data Retriever Agent extracts and prepares structured patient data
3. Medical Facilitator Agent analyzes, guides, and generates comprehensive treatment/logistics recommendations
4. Final summary or report is uploaded to the **GCS `report-summary` bucket**

---
## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

Clear commit messages & documentation updates are appreciated!

---

## 📄 License

Open-source under the **MIT License**.

---

## 📬 Contact

**Author:** Madhu
GitHub: [@Madhu-712](https://github.com/Madhu-712)

## Resources

## Youtube video
https://youtu.be/rHP1xBuwzxc

## Medium blog
https://medium.com/@madhu.712/how-an-adk-powered-multi-agent-system-is-transforming-medical-data-processing-patient-2b24822a572a

## App deployment link:
https://medical-facilitator-ai-demo-11279231310.us-west1.run.app/


---

> *A fully automated multi-agent workflow for international medical facilitation — from document analysis to travel planning to treatment coordination.*

