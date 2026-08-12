"""
Project Blackout - Rover Node
System Monitoring Module
This module provides information about the Raspberry Pi
and the operating system running Rover.
"""
import os
import shutil
# -------------------------------------------------
# CPU TEMPERATURE
# -------------------------------------------------
def get_cpu_temperature():
    """
    Read the Raspberry Pi CPU temperature.
    Returns:
        float: CPU temperature in degrees Celsius.
        None if the temperature cannot be read.
    """
    temperature_file = "/sys/class/thermal/thermal_zone0/temp"
    try:
        with open(temperature_file, "r") as file:
            temperature = int(file.read().strip())
        return temperature / 1000
    except (FileNotFoundError, ValueError):
        return None
# -------------------------------------------------
# MEMORY
# -------------------------------------------------
def get_memory():
    """
    Read system memory information.
    Returns:
        dict containing total and available memory.
    """
    memory = {}
    try:
        with open("/proc/meminfo", "r") as file:
            for line in file:
                if line.startswith("MemTotal:"):
                    memory["total_kb"] = int(
                        line.split()[1]
                    )
                elif line.startswith("MemAvailable:"):
                    memory["available_kb"] = int(
                        line.split()[1]
                    )
    except FileNotFoundError:
        return {}
    return memory
# -------------------------------------------------
# STORAGE
# -------------------------------------------------
def get_storage():
    """
    Check available storage on the Raspberry Pi.
    Returns:
        dict containing total and available storage.
    """
    storage = shutil.disk_usage("/")
    return {
        "total": storage.total,
        "used": storage.used,
        "free": storage.free
    }
# -------------------------------------------------
# SYSTEM UPTIME
# -------------------------------------------------
def get_uptime():
    """
    Return the amount of time Rover has been running.
    Returns:
        float: uptime in seconds.
    """
    try:
        with open("/proc/uptime", "r") as file:
            uptime = float(file.read().split()[0])
        return uptime
    except FileNotFoundError:
        return 0
# -------------------------------------------------
# SYSTEM STATUS
# -------------------------------------------------
def get_system_status():
    """
    Collect Rover's basic system information.
    Returns:
        dict containing current system status.
    """
    return {
        "cpu_temperature": get_cpu_temperature(),
        "memory": get_memory(),
        "storage": get_storage(),
        "uptime": get_uptime()
    }
