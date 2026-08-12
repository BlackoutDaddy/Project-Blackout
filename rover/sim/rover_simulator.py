"""
Project Blackout - Rover Node

Rover Simulator

This module simulates Rover hardware so we can develop
and test Rover's software before connecting the actual
Raspberry Pi and radio hardware.
"""

import random
import time


# -------------------------------------------------
# SIMULATED SYSTEM
# -------------------------------------------------

def get_system_status():
    """
    Generate simulated Raspberry Pi system information.
    """

    cpu_temperature = random.uniform(40.0, 65.0)

    total_memory = 1024
    available_memory = random.randint(400, 900)

    total_storage = 32
    free_storage = random.uniform(10.0, 28.0)

    uptime = time.time()

    return {
        "cpu_temperature": cpu_temperature,

        "memory": {
            "total_mb": total_memory,
            "available_mb": available_memory
        },

        "storage": {
            "total_gb": total_storage,
            "free_gb": free_storage
        },

        "uptime": uptime
    }


# -------------------------------------------------
# SIMULATED GPS
# -------------------------------------------------

def get_gps_status():
    """
    Generate simulated GPS information.
    """

    latitude = 38.123456
    longitude = -85.123456

    altitude = random.uniform(200.0, 300.0)

    speed = random.uniform(0.0, 15.0)

    return {
        "available": True,
        "fix": True,
        "latitude": latitude,
        "longitude": longitude,
        "altitude": altitude,
        "speed": speed
    }


# -------------------------------------------------
# SIMULATED BATTERY
# -------------------------------------------------

def get_battery_status():
    """
    Generate simulated battery information.
    """

    voltage = random.uniform(3.6, 4.2)

    percentage = int(
        ((voltage - 3.6) / 0.6) * 100
    )

    return {
        "voltage": voltage,
        "percentage": percentage,
        "charging": False
    }


# -------------------------------------------------
# SIMULATED MESH
# -------------------------------------------------

def get_mesh_status():
    """
    Generate simulated Meshtastic network information.
    """

    return {
        "connected": True,
        "nodes": random.randint(1, 10),
        "messages_received": random.randint(0, 50),
        "messages_sent": random.randint(0, 50)
    }