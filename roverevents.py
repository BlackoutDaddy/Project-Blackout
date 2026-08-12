"""
Project Blackout - Rover

Rover Event System

Provides a standardized way for Rover to record
and communicate important events.
"""

import time


# -------------------------------------------------
# EVENT LEVELS
# -------------------------------------------------

INFO = "INFO"
WARNING = "WARNING"
CRITICAL = "CRITICAL"


# -------------------------------------------------
# CREATE EVENT
# -------------------------------------------------

def create_event(level, source, message):
    """
    Create a Rover event.

    Returns:
        dict containing event information.
    """

    return {
        "timestamp": time.time(),
        "level": level,
        "source": source,
        "message": message
    }


# -------------------------------------------------
# DISPLAY EVENT
# -------------------------------------------------

def display_event(event):
    """
    Display a Rover event.
    """

    timestamp = event["timestamp"]
    level = event["level"]
    source = event["source"]
    message = event["message"]

    print(
        f"[{level}] "
        f"{source}: "
        f"{message}"
    )