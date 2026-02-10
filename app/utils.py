# app/utils.py
"""
Utility functions for the task management API.
WARNING: This file contains bugs that need to be found and fixed!
"""

import re
from datetime import datetime


def validate_email(email: str) -> bool:
    """
    Validate email format.
    Returns True if valid, False otherwise.

    BUG #1: This regex is too permissive - it accepts invalid emails
    """
    # This pattern has a bug - can you find it?
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def calculate_priority_score(priority: str, days_until_due: int) -> int:
    """
    Calculate a numeric priority score for sorting tasks.
    Higher score = more urgent.

    Priority weights:
    - critical: 100
    - high: 75
    - medium: 50
    - low: 25

    Days until due modifier:
    - Overdue (negative days): +50
    - Due today (0 days): +30
    - Due within 3 days: +20
    - Due within 7 days: +10

    BUG #2: There's an off-by-one error and missing case
    """
    priority_weights = {
        "critical": 100,
        "high": 75,
        "medium": 50,
        "low": 25
    }

    if priority not in priority_weights:
        raise ValueError(f"Invalid priority: {priority}")

    # Bug: What if priority is not in the dict?
    base_score = priority_weights[priority]

    # Bug: Off-by-one error in the conditions
    if days_until_due < 0:
        urgency_bonus = 50
    elif days_until_due == 0:
        urgency_bonus = 30
    elif days_until_due <= 3:  # Should be <= 3
        urgency_bonus = 20
    elif days_until_due <= 7:  # Should be <= 7
        urgency_bonus = 10
    else:
        urgency_bonus = 0

    return base_score + urgency_bonus


def sanitize_input(text: str) -> str:
    """
    Sanitize user input to prevent XSS attacks.

    BUG #3: This function is dangerously incomplete!
    It only handles a few cases and misses critical ones.
    """
    if not text:
        return ""

    # This is NOT sufficient sanitization!
    sanitized = text.replace("<script>", "")
    sanitized = sanitized.replace("</script>", "")

    return sanitized


def parse_date(date_string: str) -> datetime:
    """
    Parse a date string in format YYYY-MM-DD.

    BUG #4: No error handling for invalid dates
    """
    # What happens if the format is wrong?
    return datetime.strptime(date_string, "%Y-%m-%d")


def get_days_until_due(due_date_str: str) -> int:
    """
    Calculate days until a task is due.
    Negative number means overdue.
    """
    due_date = parse_date(due_date_str)
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    delta = due_date - today
    return delta.days
