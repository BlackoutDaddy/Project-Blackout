"""
Project Blackout - Rover

Rover Command Console

Allows a user to interact with the Rover software
through a simple command-line interface.
"""

import rover_simulator
import roverstatus


# -------------------------------------------------
# DISPLAY STATUS
# -------------------------------------------------

def show_status():

    system = rover_simulator.get_system_status()
    battery = rover_simulator.get_battery_status()
    gps = rover_simulator.get_gps_status()
    mesh = rover_simulator.get_mesh_status()

    print()
    print("=" * 40)
    print("ROVER STATUS")
    print("=" * 40)

    print(
        f"CPU: "
        f"{system['cpu_temperature']:.1f} C"
    )

    print(
        f"Battery: "
        f"{battery['percentage']}%"
    )

    print(
        f"GPS: "
        f"{'FIX' if gps['fix'] else 'NO FIX'}"
    )

    print(
        f"Mesh: "
        f"{'CONNECTED' if mesh['connected'] else 'OFFLINE'}"
    )

    print(
        f"Mesh Nodes: "
        f"{mesh['nodes']}"
    )

    print("=" * 40)


# -------------------------------------------------
# DISPLAY GPS
# -------------------------------------------------

def show_gps():

    gps = rover_simulator.get_gps_status()

    print()
    print("GPS STATUS")
    print("-" * 40)

    if gps["fix"]:

        print("Fix: YES")
        print(f"Latitude: {gps['latitude']}")
        print(f"Longitude: {gps['longitude']}")
        print(f"Altitude: {gps['altitude']:.1f} m")
        print(f"Speed: {gps['speed']:.1f} m/s")

    else:

        print("Fix: NO")


# -------------------------------------------------
# DISPLAY BATTERY
# -------------------------------------------------

def show_battery():

    battery = rover_simulator.get_battery_status()

    print()
    print("BATTERY STATUS")
    print("-" * 40)

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
# DISPLAY MESH
# -------------------------------------------------

def show_mesh():

    mesh = rover_simulator.get_mesh_status()

    print()
    print("MESH STATUS")
    print("-" * 40)

    print(
        f"Connected: "
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
# HELP
# -------------------------------------------------

def show_help():

    print()
    print("ROVER COMMANDS")
    print("-" * 40)

    print("status   - Show overall Rover status")
    print("gps      - Show GPS information")
    print("battery  - Show battery information")
    print("mesh     - Show mesh information")
    print("help     - Show available commands")
    print("exit     - Exit Rover console")


# -------------------------------------------------
# COMMAND PROCESSOR
# -------------------------------------------------

def process_command(command):

    if command == "status":

        show_status()

    elif command == "gps":

        show_gps()

    elif command == "battery":

        show_battery()

    elif command == "mesh":

        show_mesh()

    elif command == "help":

        show_help()

    elif command == "exit":

        return False

    else:

        print(
            "Unknown command. "
            "Type 'help' for commands."
        )

    return True


# -------------------------------------------------
# MAIN CONSOLE
# -------------------------------------------------

def main():

    print("=" * 40)
    print("PROJECT BLACKOUT")
    print("ROVER COMMAND CONSOLE")
    print("=" * 40)

    print()
    print("Type 'help' for available commands.")
    print()

    running = True

    while running:

        command = input("ROVER > ")

        command = command.strip().lower()

        running = process_command(command)

    print()
    print("Rover console closed.")


# -------------------------------------------------
# PROGRAM ENTRY POINT
# -------------------------------------------------

if __name__ == "__main__":
    main()