# Project Blackout — Rover

Rover is the mobile node of Project Blackout.

It is designed to function as a rugged, portable communications and computing node capable of operating independently while participating in the larger Blackout network.

The long-term goal is for Rover to provide:

- Meshtastic / LoRa communications
- GPS and location reporting
- System health monitoring
- Battery and power monitoring
- Mesh node awareness
- Local event detection
- Remote status reporting
- Command processing
- Autonomous operation when Blackout is unavailable

## Current Development Status

**Software prototype / simulation phase**

Rover's software architecture is currently being developed and tested without the physical Raspberry Pi and LoRa hardware.

The simulator allows development to continue before hardware integration.

### Currently implemented

- Rover configuration
- System monitoring architecture
- GPS interface architecture
- Simulated hardware
- Rover health/status engine
- Event generation
- Rover decision/analysis layer
- Interactive command console
- Simulation test environment

### Not yet implemented

- Physical Raspberry Pi integration
- Physical GPS receiver
- Physical battery/UPS monitoring
- SX1262 LoRa hardware integration
- Meshtastic integration
- Blackout-to-Rover communications
- Persistent event logging
- Remote command execution

## Architecture

Rover is being developed as a modular system.

The basic software flow is:

ROVER
|
v
rover.py
|
+----------------+----------------+
|                |                |
v                v                v
SYSTEM           GPS              MESH
|                |                |
+----------------+----------------+
|
v
ROVER STATUS
|
v
ROVER BRAIN
|
+----------------+----------------+
|                                 |
v                                 v
EVENTS                         COMMANDS
|                                 |
+----------------+----------------+
|
v
BLACKOUT NETWORK

The goal is to keep hardware interfaces separate from Rover's decision-making logic.

This allows simulated hardware to be replaced with real hardware without requiring the entire Rover software system to be rewritten.

## Core Software

### rover.py

The primary Rover program.

Responsibilities include:

- Starting Rover
- Loading configuration
- Running the primary program loop
- Coordinating Rover subsystems

### rovernodeconfig.py

Central Rover configuration.

Contains settings such as:

- Node identity
- Blackout node identity
- GPS configuration
- Meshtastic configuration
- System monitoring intervals
- Debug settings

Hardware-specific configuration will eventually be expanded here.

### roversystem.py

System monitoring module.

Designed to monitor the Raspberry Pi itself.

Current monitoring includes:

- CPU temperature
- Memory
- Storage
- System uptime

Future monitoring will include:

- CPU load
- Power state
- Battery voltage
- Charging state
- UPS status
- Network connectivity

### rovergps.py

GPS interface module.

The current design uses gpsd as the Linux interface between Rover software and the physical GPS receiver.

Rover is designed to work with GPS information including:

- Fix status
- Latitude
- Longitude
- Altitude
- Speed

### roverstatus.py

Rover health evaluation engine.

This module evaluates individual subsystems and assigns a status:

NOMINAL
WARNING
CRITICAL

The overall Rover status is determined by the most severe active condition.

Example:

CPU: WARNING
Battery: NOMINAL
GPS: NOMINAL
Mesh: NOMINAL

Overall: WARNING

### roverbrain.py

Rover's decision and analysis layer.

The brain collects information from Rover's subsystems and passes that information through the health engine.

It is responsible for:

- Collecting subsystem data
- Evaluating Rover's condition
- Determining overall health
- Generating events
- Preparing information for future automated actions

The brain is intentionally separated from hardware interfaces.

### roverevents.py

Rover event system.

Provides a standardized structure for important events.

Events contain:

- Timestamp
- Severity
- Source
- Message

Example:

[WARNING] CPU: CPU temperature elevated
[WARNING] BATTERY: Battery low

The event system will eventually allow events to be:

- Displayed locally
- Logged
- Stored
- Sent over the mesh
- Forwarded to Blackout
- Used to trigger automated actions

### roverconsole.py

Interactive Rover command console.

Currently supports commands such as:

status
gps
battery
mesh
help
exit

The console is currently connected to simulated Rover data.

The long-term goal is for the same command architecture to operate through local access, a Blackout command interface, or the Meshtastic network.

## Simulation Environment

The sim directory contains development and testing software.

The simulator allows Rover software to be developed without physical hardware.

Simulation files:

- rover_simulator.py — simulated Rover hardware
- rover_loop.py — continuous Rover simulation
- test_rover.py — simulator test program

### rover_simulator.py

Provides simulated Rover hardware.

Currently simulates:

- CPU temperature
- Memory
- Storage
- GPS
- Battery
- Mesh connectivity
- Mesh nodes
- Messages sent and received

Randomized values are used to simulate changing conditions.

### test_rover.py

Basic simulator test program.

Used to verify that the simulated Rover subsystems can be accessed and that their data can be processed correctly.

### rover_loop.py

Continuous Rover simulation.

Runs repeated system checks to simulate Rover operating continuously.

This is useful for testing Rover's response to changing conditions.

## Development Philosophy

Rover is being developed using a modular architecture.

The basic development principle is:

REAL HARDWARE
|
v
HARDWARE INTERFACE
|
v
ROVER SOFTWARE
|
v
DECISION / HEALTH ENGINE
|
v
EVENT SYSTEM
|
v
COMMUNICATIONS
|
v
BLACKOUT

During development, simulated hardware can replace physical hardware:

SIMULATED HARDWARE
|
v
HARDWARE INTERFACE
|
v
ROVER SOFTWARE
|
v
DECISION / HEALTH ENGINE

This allows software development and testing to continue independently of hardware availability.

## Planned Communications Architecture

Rover is intended to operate as a participant in the Project Blackout mesh.

The planned architecture is:

BLACKOUT
|
v
LoRa Mesh
|
+----------------+
|                |
v                v
ROVER           SCOUT
|
v
Mobile Node

Rover should not depend completely on Blackout to remain operational.

If Blackout becomes unavailable, Rover should continue to:

- Monitor itself
- Maintain mesh participation
- Track its location
- Process local events
- Store important information
- Resume communication when Blackout becomes available again

This is a core design principle of Project Blackout.

## Future Development

### Phase 1 — Software Prototype

- [x] Rover configuration
- [x] System monitoring architecture
- [x] GPS architecture
- [x] Simulated hardware
- [x] Health engine
- [x] Event system
- [x] Interactive console

### Phase 2 — Software Integration

- [ ] Connect command console to Rover Brain
- [ ] Standardize Rover command protocol
- [ ] Persistent event logging
- [ ] Simulated Blackout command node
- [ ] Simulated mesh messaging
- [ ] Node identification
- [ ] Message prioritization

### Phase 3 — Hardware Integration

- [ ] Raspberry Pi integration
- [ ] GPS hardware
- [ ] UPS/power monitoring
- [ ] SX1262 integration
- [ ] SPI configuration
- [ ] Meshtastic integration
- [ ] Antenna configuration
- [ ] Physical field testing

### Phase 4 — Blackout Integration

- [ ] Blackout to Rover communication
- [ ] Remote status requests
- [ ] Remote GPS requests
- [ ] Mesh health reporting
- [ ] Event forwarding
- [ ] Command authentication
- [ ] Offline operation
- [ ] Recovery after Blackout reconnects

## Development Environment

Initial Rover software development is being performed on an iPad using Python and Textastic.

The simulator allows development to continue without the physical Raspberry Pi.

The eventual deployment target is a Raspberry Pi-based mobile node.

## Project

Rover is a subsystem of Project Blackout.

Project Blackout is a rugged, modular survival computing and communications platform designed to provide resilient local computing, communications, information, and network capabilities.
