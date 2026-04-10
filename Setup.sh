#!/bin/bash
# AWS EC2 Setup Script - Ubuntu
# Author: Harivasanth Arava

echo "================================="
echo "  AWS EC2 Cloud Setup"
echo "  Author: Harivasanth Arava"
echo "================================="

# Update system
echo "📦 Updating system packages..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
echo "🐳 Installing Docker..."
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | sudo apt-key add -

sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable"

sudo apt-get update -y
sudo apt-get install -y docker-ce

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Install Docker Compose
echo "📦 Installing Docker Compose..."
sudo curl -L \
"https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
-o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Install Git
echo "🐙 Installing Git..."
sudo apt-get install -y git

# Clone project
echo "📥 Cloning project from GitHub..."
git clone https://github.com/harivasantharava41-rgb/aws-cloud-project.git
cd aws-cloud-project

# Start containers
echo "🚀 Starting Docker containers..."
docker-compose up -d

echo "================================="
echo "✅ Setup Complete!"
echo "App running at: http://$(curl -s ifconfig.me):80"
echo "================================="
