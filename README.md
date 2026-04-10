# AWS-Cloud-Project
Python web application deployed on AWS EC2 using Docker containers and MySQL database. Cloud infrastructure setup with Linux Ubuntu, Docker Compose, and GitHub for source control.

<div align="center">

# ☁️ Cloud Infrastructure Setup using AWS and Docker

### Python Web App Deployed on AWS EC2 with Docker and MySQL



![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)




![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)




![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)




![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)




![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)




![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)



</div>

---

## 📌 Project Overview
Python web application deployed on AWS EC2 using
Docker containers and MySQL database on Linux Ubuntu.

---

## 🏗️ Architecture
Developer → GitHub → AWS EC2 (Ubuntu)
↓
Docker Engine
↙              ↘
Python Flask          MySQL 8.0
(Port 80)             (Port 3306)
---

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| ☁️ AWS EC2 | Cloud virtual server |
| 🐧 Linux Ubuntu | Server operating system |
| 🐳 Docker | Application containerization |
| 🐍 Python Flask | Web application framework |
| 🗄️ MySQL | Relational database |
| 🐙 GitHub | Source code management |
| 💻 Git Bash | Command-line operations |

---

## 📁 Project Structure
aws-cloud-project/
├── app.py                # Python Flask web app
├── Dockerfile            # Docker image config
├── docker-compose.yml    # Multi-container setup
├── requirements.txt      # Python dependencies
├── setup.sh              # EC2 auto-setup script
└── README.md
---

## 🚀 How to Deploy on AWS EC2

### Step 1 — Launch EC2 Instance
- Go to AWS Console → EC2 → Launch Instance
- Choose Ubuntu 22.04 LTS (Free Tier)
- Select t2.micro instance type
- Open ports 22, 80, 3306 in Security Group

### Step 2 — Connect via SSH
```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
Step 3 — Run Setup Script
chmod +x setup.sh
./setup.sh
Step 4 — Access Application
Open browser: http://your-ec2-public-ip
💻 Local Testing
git clone https://github.com/harivasantharava41-rgb/aws-cloud-project.git
cd aws-cloud-project
docker-compose up -d
# Open http://localhost
👨‍💻 Author
Harivasanth Arava
📧 hariarava41@gmail.com
🔗 LinkedIn
🎓 MCA Cloud Computing — Jain University, Bengaluru
---

**Steps:**
1. Click **README.md** in your repo
2. Click **pencil ✏️ edit**
3. Delete everything
4. Paste above content
5. Click **Preview** to check ✅
6. Click **Commit changes** ✅

That's all 6 files done! Your second
