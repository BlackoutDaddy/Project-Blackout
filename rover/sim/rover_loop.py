"""
Project Blackout - Rover

Rover Simulator Loop

This simulates Rover continuously monitoring itself.
"""

import time
import rover_simulator


# -------------------------------------------------
# SETTINGS
# -------------------------------------------------

CHECK_INTERVAL = 3


# -------------------------------------------------
# ROVER CHECK
# -------------------------------------------------

def check_rover():

    system = rover_simulator.get_system_status()
    battery = rover_simulator.get_battery_status()
    gps = rover_simulator.get_gps_status()
    mesh = rover_simulator.get_mesh_status()

    print()
    print("=" * 40)
    print("ROVER STATUS")
    print("=" * 40)

    # CPU
    temperature = system["cpu_temperature"]

    print(f"CPU Temperature: {temperature:.1f} C")

    if temperature >= 60:
        print("WARNING: CPU temperature is high!")

    else:
        print("CPU temperature is normal.")

    # Battery
    percentage = battery["percentage"]

    print(f"Battery: {percentage}%")

    if percentage <= 25:
        print("WARNING: Battery is low!")

    else:
        print("Battery level is normal.")

    # GPS
    if gps["fix"]:
        print("GPS: FIX")

    else:
        print("GPS: NO FIX")

    # Mesh
    if mesh["connected"]:
        print(
            f"Mesh: CONNECTED "
            f"({mesh['nodes']} nodes)"
        )

    else:
        print("Mesh: DISCONNECTED")


# -------------------------------------------------
# MAIN LOOP
# -------------------------------------------------

print("Starting Rover simulator...")
print("Press Ctrl+C to stop.")

while True:

    check_rover()

    time.sleep(CHECK_INTERVAL)
	
print()
print("Rover simulation complete")