"""
Project Blackout - Rover Node
Rover is the mobile/vehicle-mounted node in the
Project Blackout network.
Its job is to provide:
    - Meshtastic / LoRa communications
    - GPS/location information
    - System and power monitoring
    - A persistent mesh presence
    - Communication with Blackout when available
Rover should remain useful even when Blackout is offline.
"""
import time
import rovernodeconfig as config
import roversystem as system
# -------------------------------------------------
# STARTUP
# -------------------------------------------------
def startup():
    """
    Start Rover and display its basic configuration.
    """
    print("=" * 40)
    print("PROJECT BLACKOUT")
    print("ROVER NODE")
    print("=" * 40)
    print(f"Node: {config.NODE_NAME}")
    print(f"Description: {config.NODE_DESCRIPTION}")
    print(f"Blackout node: {config.BLACKOUT_NODE}")
    print(f"GPS enabled: {config.GPS_ENABLED}")
    print(f"Meshtastic enabled: {config.MESHTASTIC_ENABLED}")
    print("=" * 40)
    print("Rover startup complete.")
    print()
# -------------------------------------------------
# SYSTEM CHECK
# -------------------------------------------------
def system_check():
    """
    Collect and display Rover's current system status.
    """

    print("[SYSTEM] Rover system check")

    status = system.get_system_status()

    # CPU temperature
    temperature = status["cpu_temperature"]

    if temperature is not None:
        print(f"[SYSTEM] CPU temperature: {temperature:.1f}°C")
    else:
        print("[SYSTEM] CPU temperature: unavailable")

    # Memory
    memory = status["memory"]

    if memory:
        total_mb = memory["total_kb"] / 1024
        available_mb = memory["available_kb"] / 1024

        print(
            f"[SYSTEM] Memory: "
            f"{available_mb:.0f} MB available / "
            f"{total_mb:.0f} MB total"
        )
    else:
        print("[SYSTEM] Memory: unavailable")

    # Storage
    storage = status["storage"]

    total_gb = storage["total"] / (1024 ** 3)
    free_gb = storage["free"] / (1024 ** 3)

    print(
        f"[SYSTEM] Storage: "
        f"{free_gb:.1f} GB free / "
        f"{total_gb:.1f} GB total"
    )

    # Uptime
    uptime = status["uptime"]

    uptime_hours = uptime / 3600

    print(f"[SYSTEM] Uptime: {uptime_hours:.1f} hours")

    print("[SYSTEM] Check complete.")
    print()
# -------------------------------------------------
# MAIN PROGRAM LOOP
# -------------------------------------------------
def main():
    """
    Main Rover program.
    """
    startup()
    while True:
        system_check()
        print(
            f"[SYSTEM] Waiting "
            f"{config.SYSTEM_CHECK_INTERVAL} seconds..."
        )
        time.sleep(config.SYSTEM_CHECK_INTERVAL)
# -------------------------------------------------
# PROGRAM ENTRY POINT
# -------------------------------------------------
if __name__ == "__main__":
    main()
