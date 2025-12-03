# Amazon_Bedrock_AgentCore

Credits - https://strandsagents.com/latest/documentation/docs/user-guide/deploy/deploy_to_bedrock_agentcore/

# Launch EC2 – Ubuntu 

- Take higher machine size as docker takes time if the size of the ubuntu is small
- Add IAM role to access services such as Amazon Bedrock, ECS, etc 

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

# Now Install AWS CLI v2 (not installed currently)

Run these EXACT commands depending on CPU architecture.

👉 For x86_64 machine (most EC2 instances):
cd /tmp
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

Try to check if it has the access

aws s3 ls 

# Upload the given files on Ubuntu

 - requirements.txt
 - docker
 - build.sh

Note: Add these details in 

- ACCOUNT=""
- REGION="ap-south-1"
- REPO="agentcoredemo"

REPO name should be same as ECR created name


Now run this for Streamlit App to get the response

pip install fastapi uvicorn boto3 streamlit

To run

streamlit run invoke_agent.py --server.address 0.0.0.0 --server.port 8501

On web browser

http://<EC2_PUBLIC_IP>:8501


# Agent-1 call for product recommendation

<img width="940" height="449" alt="image" src="https://github.com/user-attachments/assets/5848d9aa-386f-4863-8791-aaf500ac7b08" />

# Agent-2 call for trip recommendation

<img width="940" height="465" alt="image" src="https://github.com/user-attachments/assets/a287f55e-d15e-4089-af43-c6cd66cd2d68" />

# Direct basic Arithmetic question to see if it goes to agents

<img width="940" height="637" alt="image" src="https://github.com/user-attachments/assets/761f960c-12c1-4b03-a077-c483f58fa9da" />





