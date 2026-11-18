# Assignment 4.0 - MLOps Automation

## Project Overview
This project demonstrates an automated MLOps workflow using
GitHub Actions, TensorFlow, Docker, GitHub Container Registry,
FastAPI, and Kubernetes.

## Implemented Features
- Python code validation in GitHub Actions
- Automated preprocessing and dataset splitting
- CNN model training using TensorFlow
- Configurable training epochs through workflow_dispatch
- Optional training through the run_training input
- Model artifacts stored in GitHub Actions
- Docker image build with the trained model
- Automated publishing to GitHub Container Registry
- Automated Kubernetes deployment using a self-hosted runner
- Commit SHA and run ID based image versioning

## Testing
A synthetic dataset was used to validate the technical pipeline.
The dataset contains 60 generated images across three classes:
cats, dogs, and pandas.

The model is not intended for real animal classification.
The test verifies that the entire automation pipeline works.

## Kubernetes
Cluster: k3d-mlops
Namespace: rares
Deployment: animals-api
Container port: 8000

## Limitations
- Azure subscription is currently disabled.
- Azure Blob and Container Apps deployment could not be completed.
- Kubeflow Pipelines and MLflow are not yet integrated.
- Real training data is not included.

## Evidence
See the evidence/ directory for Kubernetes deployment information.
