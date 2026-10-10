# 🏠 HostelCare AI

### Intelligent Hostel Complaint Management & Escalation System

HostelCare AI is an AI-powered hostel support application that helps students report maintenance issues through a conversational interface, track complaint status, and enables hostel staff to manage, resolve, and escalate complaints systematically.

Built using **Python, Streamlit, SQLite, and Google Gemini**, the system combines conversational AI with structured complaint management and role-based access.

[View HostelCare AI Architecture](https://gitdiagram.com/haseebahsan-n/hostelcare-ai-agent)
## 🚀 Live Application

**Live Demo:** https://hostelcare-ai-agent.streamlit.app/

**GitHub Repository:** https://github.com/haseebahsan-n/HostelCare-AI-Agent


## 🎯 Project Objective

HostelCare AI aims to make hostel complaint handling more accessible, transparent, and organized by combining conversational AI, automated routing, ticket tracking, and structured escalation in one application.


## ✨ Features

### 🤖 Conversational AI Complaint Assistant
- Students describe hostel issues using natural language.
- Google Gemini helps understand complaints and collect relevant details.
- The assistant prepares a complaint summary, category, priority, and assignment.
- Students confirm before a complaint is submitted.
- Registered hostel block and room details are used automatically when available.

### 🔐 Role-Based Authentication
- Shared sign-in interface for registered users.
- Student self-registration.
- Separate Student, Warden, and Staff access.
- Registered student hostel details are displayed in the application header.

### 📋 Complaint Tracking
- Unique ticket IDs for submitted complaints.
- View complaint status and relevant ticket information.
- Filter tickets by status and category.
- Search tickets by ID, description, or block.
- Export filtered complaint records to CSV.

### 🛠️ Warden & Staff Dashboard
- View and inspect recorded complaints.
- Review complaint descriptions, categories, priorities, and statuses.
- Mark complaints as resolved.
- Manually escalate unresolved complaints.
- Review action logs for complaint handling and escalation.

### ⚡ Automated Routing & Escalation
- Complaints are assigned according to priority and routing rules.
- Critical complaints are initially routed to the Supervisor level.
- Other complaints are initially routed to the Technician level.
- Unresolved complaints can automatically escalate after 30 minutes at their current authority level.
- Each escalation is recorded in the audit log.

**Authority hierarchy:**

Technician → Supervisor → Warden → Director

### 📊 Analytics & Reporting
- Total complaint count.
- Open, escalated, and resolved complaint counts.
- Complaints grouped by category.
- Complaints grouped by priority.
- Searchable and filterable ticket records.

## 🧰 Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| User interface | Streamlit |
| Conversational AI | Google Gemini |
| Database | SQLite |
| Data processing | Pandas |
| Deployment | Streamlit Community Cloud |
| Version control | Git and GitHub |

## 🏗️ Project Structure

```text
HostelCare-AI-Agent/
├── app.py              # Streamlit interface and application workflow
├── agent.py            # Gemini-powered conversational complaint assistant
├── database.py         # Database operations and schema migrations
├── schema.sql          # SQLite database schema and initial records
├── routing.py          # Complaint routing and escalation logic
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from version control
└── README.md           # Project documentation
```

The SQLite database is initialized by the application. Database helper functions manage users, complaints, ticket updates, and audit logs.

## ⚙️ Run Locally

### 1. Prerequisites

Install Python and Git. A Google Gemini API key is required for Gemini-powered features.

### 2. Clone the repository

```bash
git clone https://github.com/haseebahsan-n/HostelCare-AI-Agent.git
cd HostelCare-AI-Agent
```

### 3. Install dependencies

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project directory and add your key:

```env
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
```

Use the exact environment variable expected by the application's Gemini integration. Never commit API keys or other secrets to GitHub.

### 5. Launch the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## 👤 Demo Accounts

The deployed demonstration includes the following pre-registered accounts.

**Student accounts**

| Name | Unique ID | Password | Block | Room |
|---|---|---|---|---|
| Haseeb | `23BME1191` | `hostel123` | A | 828 |
| Sam grason | `23BME1110` | `hostel123` | E | 1228 |
| Nigalyaa | `23BME1120` | `hostel123` | B | 416 |
| Balaji | `23BEE1144` | `hostel123` | A | 540 |
| Raja | `21BME1190` | `hostel123` | F | 1407 |

**Staff accounts**

| Role | Name | Unique ID | Password |
|---|---|---|---|
| Warden | Shanmugam | `53135` | `hostel123` |
| Technician / Staff | Kumar | `TECH01` | `hostel123` |

These are demonstration credentials, not production credentials. Change or replace them before any real deployment.

## 🔄 Complaint Workflow

1. A student signs in and describes a hostel issue.
2. The AI assistant gathers the necessary information and prepares a complaint summary.
3. The student reviews the details and confirms submission.
4. The application creates a ticket and assigns an initial authority.
5. The student tracks the ticket through the application.
6. Warden or Staff users inspect, resolve, or manually escalate the complaint.
7. Automatic escalation checks eligible unresolved complaints when the application executes.
8. Complaint actions and escalation events are recorded in the audit log.

## 🌐 Deployment

HostelCare AI is deployed using Streamlit Community Cloud.

To deploy your own instance:

1. Push the project to a GitHub repository.
2. Open Streamlit Community Cloud.
3. Create an app connected to the repository.
4. Set `app.py` as the application entry point.
5. Configure `GOOGLE_GEMINI_API_KEY` in the app's Secrets settings using the format required by the application.
6. Deploy the application.

**Deployment note:** Automatic escalation is checked during application execution and reruns; it is not a continuously running background scheduler. SQLite storage on cloud hosting should also be configured appropriately if persistent records are required across restarts or redeployments.

## 🔮 Future Improvements

- Notifications for assigned staff and students.
- Background scheduling for automatic escalation.
- More detailed complaint analytics and reports.
- Improved authentication and secure password storage.
- Administrative user and department management.
- Enhanced complaint history and resolution feedback.
- Support for multiple hostels and campuses.


---

**Built with Python, Streamlit, SQLite, and Google Gemini.**
