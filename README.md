# Variant Quality Assessor

## Overview

The **Variant Quality Assessor** is a Python-based tool designed to evaluate the quality of genetic variants from Variant Call Format (VCF) files. It marks variants as "PASS" or "FAIL" based on the following quality metrics:
- **Depth (DP)**: Should be ≥ 400.
- **Allele Frequency (AF)**: Should be between 0.001 and 0.2 (inclusive).

The tool is implemented using Python, with features like object-oriented programming, automated tests using `pytest`, Docker support, and CI/CD integration with GitHub Actions.

---

## Features

- **VCF Parsing**: Reads and processes VCF files into structured data.
- **Quality Assessment**: Evaluates each variant against defined thresholds.
- **Automated Testing**: Comes with comprehensive test coverage using `pytest`.
- **Containerization**: Docker support for consistent environments.
- **CI/CD Integration**: GitHub Actions workflow for automated testing.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.9 or higher
- `pip` package manager
- `pytest` for testing
- Docker (optional, for containerization)
- GitHub Actions (optional, for CI/CD)

---

## Installation
- pip install -r requirements.txt



