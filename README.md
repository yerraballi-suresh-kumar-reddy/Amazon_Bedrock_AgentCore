# Amazon_Bedrock_AgentCore

Credits - https://strandsagents.com/latest/documentation/docs/user-guide/deploy/deploy_to_bedrock_agentcore/

# Launch EC2 – Ubuntu and add IAM role to access services such as Amazon Bedrock, ECS, etc 

# Run these commands

✅ Step 1: Update System
sudo apt update
sudo apt upgrade -y

✅ Step 2: Add Deadsnakes PPA (contains newer Python versions)
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

✅ Step 3: Install Python 3.11
sudo apt install -y python3.11 python3.11-venv python3.11-dev

✅ Step 4: Verify Version
python3.11 --version


You should see:

Python 3.11.x

🎯 (Optional) Set Python 3.11 as Default Python
Check available Python versions
ls /usr/bin/python*

Set Python alternative
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
sudo update-alternatives --config python3


Choose Python 3.11 from the list.

Once choosen check for python version

Now create virtual environment

python3 -m venv agentenv

source agentenv/bin/activate

Install Docker on Ubuntu

🚀  1. Add Docker’s official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

🚀 2. Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

🚀 3. Update again & Install Docker Engine
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

🚀 4. Start & Enable Docker
sudo systemctl enable docker
sudo systemctl start docker

🚀 5. Check Docker Version
docker --version


# Upload the given files on Ubuntu

 - requirements.txt
 - docker
 - build.sh

Note: Add these details in 

- ACCOUNT=""
- REGION="ap-south-1"
- REPO="agentcoredemo"

REPO name should be same as ECR created name


