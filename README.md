Steam Analytics Cloud Engine 🚀

Steam Analytics Cloud Engine is a Data Engineering and Web Development project that integrates a Lakehouse data architecture in Google Cloud with a Django backend dashboard for interactive analytics.

The project demonstrates how large-scale datasets can be processed in a modern cloud data stack and then exposed through a web application for real-time insights.

Architecture
Steam Dataset
     │
     ▼
BigQuery (Lakehouse Layers)
Bronze → Silver → Gold
     │
     ▼
Django Backend (Python)
     │
     ▼
Web Dashboard / Analytics Panel

This architecture follows the Medallion Lakehouse pattern, ensuring:

Data reliability

Layered transformations

Scalable analytics pipelines

Technologies
Backend

Python

Django

Django Templates

Data Engineering

SQL

ETL Pipelines

Medallion Architecture

Cloud

Google Cloud Platform

BigQuery

Service Accounts Authentication

Other Tools

Git

GitHub

Data Visualization

Features

Real-time connection between Django and BigQuery

Secure authentication using Google Cloud Service Accounts

Professional and scalable project structure

Data pipeline designed with Lakehouse principles

Visualization of Steam popularity and review metrics

Data Pipeline

The dataset is processed using a Lakehouse architecture:

Bronze Layer

Raw data ingestion from the Steam dataset.

Silver Layer

Data cleaning, normalization, and transformation.

Gold Layer

Aggregated datasets optimized for analytics and dashboard queries.

Project Structure
steam-analytics-cloud-engine
│
├── dashboard
│   ├── templates
│   ├── views.py
│   ├── models.py
│
├── steam_project
│   ├── settings.py
│   ├── urls.py
│
├── services
│   ├── bigquery_client.py
│
├── requirements.txt
├── README.md
Example Use Case

The platform allows analysis of:

Most popular Steam games

Review trends

Player engagement

Market trends in gaming

Future Improvements

API endpoints with Django REST Framework

Data orchestration with Airflow

Real-time streaming ingestion

Advanced analytics dashboards

Author

Mauricio Velez Rengifo

Data Engineer | Backend Developer

GitHub
https://github.com/Mvelezrengifo

LinkedIn
https://linkedin.com/in/mauricio-velez-5162a7152
