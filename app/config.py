# app/config.py
"""
Application configuration.
NEVER commit real secrets to version control!
"""

import os

class Config:
    # These should come from environment variables in production
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///dev.db")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"

    # API Settings
    MAX_TASKS_PER_USER = 100
    VALID_PRIORITIES = ["low", "medium", "high", "critical"]
    VALID_STATUSES = ["pending", "in_progress", "completed"]
