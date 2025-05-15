# 🗽 Heart of New York

**Heart of New York** is a web-based application designed to enrich visitors' experiences at the Center for Technology & Innovation building's map of New York State. By scanning uniquely generated QR codes for each county, users can access detailed information about local historical societies.

---

## 🌟 Features

- Physical map of New York State with scannable QR codes
- QR code-based access to historical society content
- Integrated PostgreSQL database hosted on Neon
- Flask-powered backend served from AWS EC2
- JavaScript integration with SquareSpace for seamless UX

---

## 🛠 Technologies Used

- **Python 3**  
- **Flask Framework**  
- **PostgreSQL**, managed via **pgAdmin4**, hosted on **Neon**
- **AWS EC2** (Ubuntu) for deployment  
- **nginx** reverse proxy to resolve HTTP/HTTPS routing issues  
- **SquareSpace + JavaScript** for frontend integration  
- QR Code generation libraries

---

## 🧠 System Design Overview

By scanning QR codes placed on a physical map, users are directed to county-specific pages containing historical society information — all powered by a lightweight backend system designed for efficiency and maintainability.

### 🧩 System Components

#### 1. Physical Interaction & QR Routing
- A large physical map of New York State is installed on-site.
- Each county has a unique QR code sticker affixed to its location.
- Scanning a QR code with a smartphone leads to a dynamic county-specific endpoint served by the backend.

#### 2. Backend Application
- Developed in **Python Flask**, hosted on an **AWS EC2** instance.
- Each county QR code maps to a Flask route that queries the database and renders content for the user.
- API endpoints serve data in real-time using a simple RESTful architecture.

#### 3. Database Layer
- A centralized **PostgreSQL** database stores county information:
  - County name
  - Historical society contact info
  - URLs and responsible staff
- Hosted on [Neon](https://neon.tech), a serverless PostgreSQL platform chosen to **minimize infrastructure costs** due to the modest data volume.
- Administered using **pgAdmin4** during development.

#### 4. Hosting & Infrastructure
- Application is hosted on an **AWS EC2 (Ubuntu)** instance.
- **nginx** is used as a reverse proxy to resolve **HTTP/HTTPS compatibility issues** between the Flask server and domain-level requests.
- Environment configuration and deployment handled via secure SSH.

#### 5. Frontend Integration
- The system is embedded into a **SquareSpace** site using custom **JavaScript** that connects dynamic content to the API.
- When a QR code is scanned, the JavaScript retrieves and displays the relevant information without requiring user input.

---

## 🚀 Getting Started

> ⚠️ **Note**: This project is not designed for public deployment or local development due to privacy restrictions and private infrastructure dependencies.

This system is securely deployed on a private AWS EC2 instance and designed exclusively for use within the [Center for Technology & Innovation](https://ctandi.org/) environment. All QR code links and content are integrated into internal systems and cannot be accessed publicly.

### Prerequisites (For Educational Reference Only)

- Python 3.x
- PostgreSQL
- AWS EC2 access
- nginx (if replicating deployment setup)

### Installation

```bash
git clone https://github.com/eylulkadioglu/HeartOfNY.git
cd HeartOfNY
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
## 📄 License

This project is licensed under the [MIT License](./LICENSE).

