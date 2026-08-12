"""
Project Blackout - Rover

Rover Simulator Test Bench

This program tests the simulated Rover hardware.
"""

import rover_simulator


# -------------------------------------------------
# SYSTEM TEST
# -------------------------------------------------

print("=" * 40)
print("PROJECT BLACKOUT")
print("ROVER SIMULATOR")
print("=" * 40)

print()
print("SYSTEM STATUS")
print("-" * 40)

system = rover_simulator.get_system_status()

print(
    f"CPU Temperature: "
    f"{system['cpu_temperature']:.1f} C"
)

print(
    f"Memory Available: "
    f"{system['memory']['available_mb']} MB"
)

print(
    f"Storage Free: "
    f"{system['storage']['free_gb']:.1f} GB"
)


# -------------------------------------------------
# GPS TEST
# -------------------------------------------------

print()
print("GPS STATUS")
print("-" * 40)

gps = rover_simulator.get_gps_status()

print(
    f"GPS Fix: "
    f"{gps['fix']}"
)

print(
    f"Latitude: "
    f"{gps['latitude']}"
)

print(
    f"Longitude: "
    f"{gps['longitude']}"
)

print(
    f"Altitude: "
    f"{gps['altitude']:.1f} m"
)

print(
    f"Speed: "
    f"{gps['speed']:.1f} m/s"
)


# -------------------------------------------------
# BATTERY TEST
# -------------------------------------------------

print()
print("BATTERY STATUS")
print("-" * 40)

battery = rover_simulator.get_battery_status()

print(
    f"Voltage: "
    f"{battery['voltage']:.2f} V"
)

print(
    f"Battery: "
    f"{battery['percentage']}%"
)

print(
    f"Charging: "
    f"{battery['charging']}"
)


# -------------------------------------------------
# MESH TEST
# -------------------------------------------------

print()
print("MESH STATUS")
print("-" * 40)

mesh = rover_simulator.get_mesh_status()

print(
    f"Mesh Connected: "
    f"{mesh['connected']}"
)

print(
    f"Nodes: "
    f"{mesh['nodes']}"
)

print(
    f"Messages Received: "
    f"{mesh['messages_received']}"
)

print(
    f"Messages Sent: "
    f"{mesh['messages_sent']}"
)


# -------------------------------------------------
# COMPLETE
# -------------------------------------------------

print()
print("=" * 40)
print("ROVER SIMULATION COMPLETE")
print("=" * 40)