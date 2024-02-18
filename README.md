# Celery_Email_Sender

# Celery Email Sender: Automate Email Sending with Celery and Python

This repository contains a simple Celery task to send emails periodically using Celery Beat.

## Introduction

The Celery Email Sender automates the process of sending emails at regular intervals, making it ideal for tasks like sending newsletters, notifications, or reminders.

## Installation

To get started, install Celery and other necessary libraries using pip:

```bash
pip install celery redis
```
### SMTP Server Configuration
Before running the Celery task, ensure you have access to an SMTP server for sending emails. If you're using Gmail, you can configure it with the following settings:

SMTP Server: smtp.gmail.com
Port: 587
Username: Your Gmail email address
Password: Your Gmail password or an App Password if Two-Factor Authentication is enabled

### Running Celery Worker and Celery Beat
Run the Celery worker with the following command:
```bash
celery -A celery_tasks worker --loglevel=info
```
In another terminal, run Celery Beat to schedule the task:
```bash
celery -A celery_tasks beat --loglevel=info
```
