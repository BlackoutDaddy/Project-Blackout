"""
Project Blackout - Rover Node
Configuration
This file contains Rover's basic configuration.
Keep hardware-specific settings here so the main
program doesn't need to be changed every time we
modify the node.
"""
# -------------------------------------------------
# NODE IDENTITY
# -------------------------------------------------
NODE_NAME = "ROVER"
NODE_DESCRIPTION = "Project Blackout Mobile Node"
# -------------------------------------------------
# BLACKOUT NETWORK
# -------------------------------------------------
# Blackout's primary node name.
# This will be used later when we establish
# communication between Rover and Blackout.
BLACKOUT_NODE = "BLACKOUT"
# -------------------------------------------------
# GPS
# -------------------------------------------------
GPS_ENABLED = True
# -------------------------------------------------
# SYSTEM
# -------------------------------------------------
# How often Rover checks its systems.
# Value is in seconds.
SYSTEM_CHECK_INTERVAL = 30
# -------------------------------------------------
# MESH
# -------------------------------------------------
# Enable Meshtastic functionality.
MESHTASTIC_ENABLED = True
# -------------------------------------------------
# DEBUGGING
# -------------------------------------------------
# Set this to False when we eventually deploy
# Rover as a finished node.
DEBUG = True
