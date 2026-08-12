"""
Project Blackout - Rover

Rover Health and Status Engine

This module evaluates Rover's sensor information
and determines the overall health of the node.
"""


# -------------------------------------------------
# STATUS LEVELS
# -------------------------------------------------

STATUS_NOMINAL = "NOMINAL"
STATUS_WARNING = "WARNING"
STATUS_CRITICAL = "CRITICAL"


# -------------------------------------------------
# CHECK CPU
# -------------------------------------------------

def check_cpu(temperature):

    if temperature >= 75:
        return STATUS_CRITICAL

    elif temperature >= 60:
        return STATUS_WARNING

    else:
        return STATUS_NOMINAL


# -------------------------------------------------
# CHECK BATTERY
# -------------------------------------------------

def check_battery(percentage):

    if percentage <= 10:
        return STATUS_CRITICAL

    elif percentage <= 25:
        return STATUS_WARNING

    else:
        return STATUS_NOMINAL


# -------------------------------------------------
# CHECK GPS
# -------------------------------------------------

def check_gps(gps):

    if not gps["available"]:
        return STATUS_CRITICAL

    elif not gps["fix"]:
        return STATUS_WARNING

    else:
        return STATUS_NOMINAL


# -------------------------------------------------
# CHECK MESH
# -------------------------------------------------

def check_mesh(mesh):

    if not mesh["connected"]:
        return STATUS_CRITICAL

    elif mesh["nodes"] <= 1:
        return STATUS_WARNING

    else:
        return STATUS_NOMINAL


# -------------------------------------------------
# DETERMINE OVERALL STATUS
# -------------------------------------------------

def get_overall_status(statuses):

    if STATUS_CRITICAL in statuses:
        return STATUS_CRITICAL

    elif STATUS_WARNING in statuses:
        return STATUS_WARNING

    else:
        return STATUS_NOMINAL