# AI-Augmented, Cloud-Agnostic Serverless Healthcare Framework

Artifacts for the paper *"AI-Augmented, Cloud-Agnostic Serverless Framework for Intelligent Infectious Disease Response in Healthcare"*.

This repository contains **synthetic datasets**, **Infrastructure-as-Code (IaC) templates**, and **example AI/ML stubs** to help reproduce the concepts and experiments described in the paper.

---

## 📂 Contents

### `synthetic-data/`
Script to generate privacy-safe synthetic healthcare datasets:
- `health_events.csv` – Simulated daily test outcomes, vaccination flags, and exposure scores.
- `contact_edges.csv` – Example contact network for graph analytics.

### `iac/`
Multi-cloud Infrastructure-as-Code templates:
- AWS Terraform stub for Lambda-based inference.
- Knative manifest for Kubernetes-native deployment.

### `src/`
Minimal inference API stub for serverless environments.

### `notebooks/`
Example AI/ML workflows (to be expanded).

### `.github/workflows/`
CI pipeline to test synthetic data generation.

---

## 📜 Reproducibility

The operational dataset used in our deployment is **not public** due to HIPAA/GDPR requirements.  
This repo provides:
- Synthetic data with similar statistical characteristics to public WHO/CDC statistics.
- Minimal IaC templates to replicate multi-cloud serverless deployment patterns.

---

## 🚀 Quick Start

### Run Locally (No Docker)
```bash
# Clone the repo
git clone https://github.com/vvivek4ever/ai-augmented-serverless-healthcare.git
cd ai-augmented-serverless-healthcare

# Generate synthetic data
python synthetic-data/generate_synthetic.py

# Run the minimal inference API
cd src/inference_stub
python app.py


The server will start locally on port 8080.

Test API endpoints:

curl http://localhost:8080/           # Sample risk score
curl http://localhost:8080/health     # Health check

Press Ctrl + C to stop the server.

Run with Docker (Build Locally)

# Build the Docker image
docker build -t inference-api src/inference_stub/

# Run the container
docker run -p 8080:8080 inference-api

Test API endpoints:

curl http://localhost:8080/           # Sample risk score
curl http://localhost:8080/health     # Health check

Run with Prebuilt GHCR Image (Recommended)
You can skip the build step and pull the latest prebuilt image:

docker pull ghcr.io/vvivek4ever/inference-api:latest
docker run -p 8080:8080 ghcr.io/vvivek4ever/inference-api:latest

Test API endpoints:

curl http://localhost:8080/           # Sample risk score
curl http://localhost:8080/health     # Health check

### Download prebuilt synthetic CSVs (no local Python needed)
GitHub Actions generates and uploads the CSVs on each push.  
Go to **Actions → Generate Synthetic Data → latest run → Artifacts → `synthetic-csvs`** to download `health_events.csv` and `contact_edges.csv`.

To Stop the Container

docker ps            # Find your container ID
docker stop <id>
