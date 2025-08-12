AI-Augmented, Cloud-Agnostic Serverless Healthcare Framework
Artifacts for the paper "AI-Augmented, Cloud-Agnostic Serverless Framework for Intelligent Infectious Disease Response in Healthcare".

This repository contains synthetic datasets, Infrastructure-as-Code (IaC) templates, and example AI/ML stubs to help reproduce the concepts and experiments described in the paper.

Contents
synthetic-data/ – Script to generate privacy-safe synthetic healthcare datasets:

health_events.csv – Simulated daily test outcomes, vaccination flags, and exposure scores.

contact_edges.csv – Example contact network for graph analytics.

iac/ – Multi-cloud Infrastructure-as-Code templates:

AWS Terraform stub for Lambda-based inference.

Knative manifest for Kubernetes-native deployment.

src/ – Minimal inference API stub for serverless environments.

notebooks/ – Example AI/ML workflows (to be expanded).

.github/workflows/ – CI pipeline to test synthetic data generation.

Reproducibility
The operational dataset used in our deployment is not public due to HIPAA/GDPR requirements.
This repo provides:

Synthetic data with similar statistical characteristics to public WHO/CDC statistics.

Minimal IaC templates to replicate multi-cloud serverless deployment patterns.

Quick Start
bash
Copy
Edit
# Clone the repo
git clone https://github.com/vvivek4ever/ai-augmented-serverless-healthcare.git
cd ai-augmented-serverless-healthcare

# Generate synthetic data
python synthetic-data/generate_synthetic.py
License
This project is licensed under the MIT License – see the LICENSE file for details.
