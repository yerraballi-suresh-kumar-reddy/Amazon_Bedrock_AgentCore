#!/bin/bash
 
ACCOUNT="AWS_ACC_ID"
REGION="ap-south-1"
REPO="agentcoredemo"
 
echo "🚀 Building and pushing Ubuntu-based agent image..."
 
# Ensure Docker Buildx exists (Ubuntu EC2 needs this)
docker buildx create --use || true
 
# Create ECR repository if not exists
aws ecr create-repository \
    --repository-name $REPO \
    --region $REGION || true
 
# Login to ECR
aws ecr get-login-password --region $REGION \
    | docker login --username AWS --password-stdin \
      $ACCOUNT.dkr.ecr.$REGION.amazonaws.com
 
echo "🧪 Building Ubuntu-based MCQ Agent (ARM64)..."
 
docker buildx build \
    --platform linux/arm64 \
    -f docker \
    -t $ACCOUNT.dkr.ecr.$REGION.amazonaws.com/$REPO:mcq-agent \
    --push .
