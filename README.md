# Uploading Local CSV Files to Amazon S3 Using Python (boto3)

This repository contains a simple, focused Python script for uploading local CSV files to an Amazon S3 bucket.

The purpose of this project is to demonstrate a clear understanding of **data movement fundamentals** and **Amazon S3’s object storage model**, rather than to showcase complex application logic.

---

## 📌 Overview

The script performs the following steps:

1. Scans a local directory for `.csv` files
2. Constructs S3 object keys using a configurable prefix
3. Uploads each file to an Amazon S3 bucket using `boto3.upload_file()`
4. Logs success or failure for each upload

The implementation prioritizes clarity, correctness, and safe defaults.

---

## 🧠 Key Concepts

- **Amazon S3 is object storage**, not a filesystem  
- “Folders” in S3 are logical prefixes in the object key
- Object location is determined entirely by the key (e.g. `csv_uploads/orders.csv`)
- `upload_file()` is used instead of lower-level APIs for reliability and multipart handling

---

## 📂 Script Responsibilities

- Validate that the local source directory exists
- Discover CSV files using pattern matching
- Normalize S3 prefixes to avoid malformed object keys
- Upload files individually with basic error handling

---

## ⚙️ Prerequisites

- Python 3.9+
- An existing Amazon S3 bucket
- AWS credentials configured locally (AWS CLI, environment variables, or IAM role)
- Python dependency:
  - `boto3`

Install dependency:

```bash
pip install boto3
