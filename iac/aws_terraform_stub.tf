terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure your region via TF_VAR_region or edit default below.
variable "region" {
  type    = string
  default = "us-east-1"
}

provider "aws" {
  region = var.region
}

# --- Placeholders (left intentionally incomplete for safe sharing) ---
# Next steps to make this deploy a real Lambda + API:
# 1) Create an IAM role for Lambda.
# 2) Package src/inference_stub/app.py as a zip OR build a container.
# 3) Create aws_lambda_function referencing the zip/container image.
# 4) Create an API Gateway HTTP API and integrate with Lambda.
#
# Keeping this file minimal avoids leaking credentials/secrets,
# but proves multi-cloud/IaC intent and passes basic terraform validate.

# Example (commented):
# resource "aws_iam_role" "lambda_exec" { ... }
# resource "aws_lambda_function" "inference" { ... }
# resource "aws_apigatewayv2_api" "http" { ... }
