"""
Project Blackout - Rover

Rover Brain

The brain collects information about Rover,
passes it through the health engine, and determines
what Rover should consider its current condition.
"""

import rover_simulator
import roverstatus
import roverevents

# -------------------------------------------------
# COLLECT ROVER DATA
# -------------------------------------------------

def collect_data():
    """
    Collect all simulated Rover information.
    """

    system = rover_simulator.get_system_status()
    gps = rover_simulator.get_gps_status()
    battery = rover_simulator.get_battery_status()
    mesh = rover_simulator.get_mesh_status()

    return {
        "system": system,
        "gps": gps,
        "battery": battery,
        "mesh": mesh
    }


# -------------------------------------------------
# ANALYZE ROVER
# -------------------------------------------------
def analyze_rover(data):
    """
    Analyze Rover's current condition and generate events.
    """

    cpu_temperature = data["system"]["cpu_temperature"]
    battery_percentage = data["battery"]["percentage"]

    cpu_status = roverstatus.check_cpu(
        cpu_temperature
    )

    battery_status = roverstatus.check_battery(
        battery_percentage
    )

    gps_status = roverstatus.check_gps(
        data["gps"]
    )

    mesh_status = roverstatus.check_mesh(
        data["mesh"]
    )

    statuses = [
        cpu_status,
        battery_status,
        gps_status,
        mesh_status
    ]

    overall_status = roverstatus.get_overall_status(
        statuses
    )

    events = []

    # ---------------------------------------------
    # CPU EVENTS
    # ---------------------------------------------

    if cpu_status == roverstatus.STATUS_CRITICAL:

        events.append(
            roverevents.create_event(
                roverevents.CRITICAL,
                "CPU",
                f"CPU temperature critical: "
                f"{cpu_temperature:.1f} C"
            )
        )

    elif cpu_status == roverstatus.STATUS_WARNING:

        events.append(
            roverevents.create_event(
                roverevents.WARNING,
                "CPU",
                f"CPU temperature elevated: "
                f"{cpu_temperature:.1f} C"
            )
        )

    # ---------------------------------------------
    # BATTERY EVENTS
    # ---------------------------------------------

    if battery_status == roverstatus.STATUS_CRITICAL:

        events.append(
            roverevents.create_event(
                roverevents.CRITICAL,
                "BATTERY",
                f"Battery critical: "
                f"{battery_percentage}%"
            )
        )

    elif battery_status == roverstatus.STATUS_WARNING:

        events.append(
            roverevents.create_event(
                roverevents.WARNING,
                "BATTERY",
                f"Battery low: "
                f"{battery_percentage}%"
            )
        )

    # ---------------------------------------------
    # GPS EVENTS
    # ---------------------------------------------

    if gps_status == roverstatus.STATUS_CRITICAL:

        events.append(
            roverevents.create_event(
                roverevents.CRITICAL,
                "GPS",
                "GPS service unavailable"
            )
        )

    elif gps_status == roverstatus.STATUS_WARNING:

        events.append(
            roverevents.create_event(
                roverevents.WARNING,
                "GPS",
                "GPS fix unavailable"
            )
        )

    # ---------------------------------------------
    # MESH EVENTS
    # ---------------------------------------------

    if mesh_status == roverstatus.STATUS_CRITICAL:

        events.append(
            roverevents.create_event(
                roverevents.CRITICAL,
                "MESH",
                "Mesh connection unavailable"
            )
        )

    elif mesh_status == roverstatus.STATUS_WARNING:

        events.append(
            roverevents.create_event(
                roverevents.WARNING,
                "MESH",
                f"Mesh has only "
                f"{data['mesh']['nodes']} node(s)"
            )
        )

    return {
        "cpu": cpu_status,
        "battery": battery_status,
        "gps": gps_status,
        "mesh": mesh_status,
        "overall": overall_status,
        "events": events
    }

# -------------------------------------------------
# DISPLAY ROVER BRAIN
# -------------------------------------------------

def display_analysis(data, analysis):
    """
    Display Rover's current condition and events.
    """

    print()
    print("=" * 40)
    print("ROVER BRAIN")
    print("=" * 40)

    print()
    print("CURRENT CONDITIONS")
    print("-" * 40)

    print(
        f"CPU: "
        f"{data['system']['cpu_temperature']:.1f} C"
    )

    print(
        f"Battery: "
        f"{data['battery']['percentage']}%"
    )

    print(
        f"GPS Fix: "
        f"{data['gps']['fix']}"
    )

    print(
        f"Mesh Nodes: "
        f"{data['mesh']['nodes']}"
    )

    print()
    print("HEALTH ANALYSIS")
    print("-" * 40)

    print(f"CPU: {analysis['cpu']}")
    print(f"Battery: {analysis['battery']}")
    print(f"GPS: {analysis['gps']}")
    print(f"Mesh: {analysis['mesh']}")

    print()
    print(
        f"OVERALL STATUS: "
        f"{analysis['overall']}"
    )

    # ---------------------------------------------
    # EVENTS
    # ---------------------------------------------

    if analysis["events"]:

        print()
        print("ROVER EVENTS")
        print("-" * 40)

        for event in analysis["events"]:
            roverevents.display_event(event)

    else:

        print()
        print("ROVER EVENTS")
        print("-" * 40)
        print("No active events.")

    print("=" * 40)


# -------------------------------------------------
# MAIN
# -------------------------------------------------

def main():

    data = collect_data()

    analysis = analyze_rover(data)

    display_analysis(
        data,
        analysis
    )


# -------------------------------------------------
# PROGRAM ENTRY POINT
# -------------------------------------------------

if __name__ == "__main__":
    main()