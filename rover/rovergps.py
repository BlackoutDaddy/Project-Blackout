"""
Project Blackout - Rover Node
GPS Module

This module provides GPS information to Rover.

Rover will use gpsd as the interface between Linux
and the physical GPS receiver.
"""

import json
import subprocess


# -------------------------------------------------
# GPS STATUS
# -------------------------------------------------

def get_gps_status():
    """
    Get the current GPS status from gpsd.

    Returns:
        dict containing GPS information.
    """

    try:
        result = subprocess.run(
            ["gpspipe", "-w", "-n", "1"],
            capture_output=True,
            text=True,
            timeout=5
        )

    except (FileNotFoundError, subprocess.TimeoutExpired):
        return {
            "available": False,
            "fix": False,
            "latitude": None,
            "longitude": None,
            "altitude": None,
            "speed": None
        }

    if result.returncode != 0:
        return {
            "available": False,
            "fix": False,
            "latitude": None,
            "longitude": None,
            "altitude": None,
            "speed": None
        }

    try:
        data = json.loads(result.stdout)

    except json.JSONDecodeError:
        return {
            "available": False,
            "fix": False,
            "latitude": None,
            "longitude": None,
            "altitude": None,
            "speed": None
        }

    # gpsd TPV messages contain position information.
    if data.get("class") != "TPV":
        return {
            "available": True,
            "fix": False,
            "latitude": None,
            "longitude": None,
            "altitude": None,
            "speed": None
        }

    mode = data.get("mode", 0)

    return {
        "available": True,
        "fix": mode >= 2,
        "latitude": data.get("lat"),
        "longitude": data.get("lon"),
        "altitude": data.get("alt"),
        "speed": data.get("speed")
    }


# -------------------------------------------------
# GPS DISPLAY
# -------------------------------------------------

def display_gps_status():
    """
    Display the current GPS information.
    """

    gps = get_gps_status()

    if not gps["available"]:
        print("[GPS] GPS service unavailable.")
        return

    if not gps["fix"]:
        print("[GPS] No GPS fix.")
        return

    print("[GPS] GPS fix acquired.")

    print(
        f"[GPS] Latitude: "
        f"{gps['latitude']}"
    )

    print(
        f"[GPS] Longitude: "
        f"{gps['longitude']}"
    )

    if gps["altitude"] is not None:
        print(
            f"[GPS] Altitude: "
            f"{gps['altitude']:.1f} m"
        )

    if gps["speed"] is not None:
        print(
            f"[GPS] Speed: "
            f"{gps['speed']:.1f} m/s"
        )
