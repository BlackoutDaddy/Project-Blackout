# Project Blackout Architecture

This document describes the intended architecture of the Project Blackout ecosystem.

The architecture is experimental and will change as hardware and software are developed and tested.

---

## 1. System Overview

Project Blackout is designed as a distributed field computing and communications ecosystem rather than a single device.

The system consists of three primary node types:

- Blackout — primary field computer and command node
- Scout — portable personal communications node
- Rover — vehicle-mounted communications node

The nodes are intended to remain useful independently while gaining additional capabilities when operating together.

---

## 2. Blackout

Blackout is the primary computing platform within the ecosystem.

Its responsibilities may include:

- Local computing
- Network and node monitoring
- Meshtastic integration
- Offline mapping
- GPS
- Local data storage
- System status
- Power monitoring
- User interface
- Future offline AI/LLM capabilities

Blackout is intended to provide capabilities that are impractical to place on smaller Scout or Rover hardware.

### Command Node

Blackout is currently envisioned as the primary command and management node.

However, the network should not depend entirely on Blackout remaining operational.

If Blackout becomes unavailable, other nodes should continue to provide their core communications functions.

This creates a distinction between:

Network participation

and

Network management.

---

## 3. Scout

Scout is the small, portable node within the Blackout ecosystem.

Its primary purpose is to provide an individual with access to the communications network without requiring them to carry the full Blackout computer.

Scout is intended to prioritize:

- Small size
- Low power consumption
- Portability
- Simple operation
- Reliable communications

Scout may eventually provide additional functionality, but communications are its primary purpose.

---

## 4. Rover

Rover is the vehicle-mounted node.

Its purpose is to provide a persistent communications node that can remain with a vehicle while users move away from it.

Potential Rover functions include:

- Meshtastic communications
- Network relay
- GPS/location information
- Vehicle-based power
- Extended antenna capability
- Persistent node availability

Rover may eventually serve as a bridge between mobile users and the wider Blackout network.

---

## 5. Communications

Meshtastic and LoRa are currently the primary communications technologies being investigated for Blackout.

The communications architecture is intended to operate without requiring:

- Cellular service
- Wi-Fi
- Internet access

Internet connectivity may provide additional capabilities when available, but it should not be considered a requirement for basic local communications.

---

## 6. Distributed Operation

A major design principle of Blackout is that the ecosystem should not have a single point of failure for basic communications.

Blackout provides additional computing and management capabilities, but the underlying communications network should remain functional when possible.

For example, if Blackout becomes unavailable, Scout and Rover should still be capable of participating in the underlying communications network.

---

## 7. Command vs. Autonomy

Blackout may eventually provide management functions for other nodes.

However, node management should be designed carefully so that loss of the Blackout command node does not unnecessarily disable the rest of the network.

The system should distinguish between:

- Configuration
- Monitoring
- Coordination
- Administrative control
- Core communications

Core communications should remain as independent as practical.

---

## 8. Power

Power is a major component of the Blackout architecture.

Each node should be capable of operating independently from the others.

Potential power sources include:

- Rechargeable batteries
- USB power banks
- Vehicle power
- Solar power
- Other field power sources

Power consumption, battery capacity, charging, and runtime will be documented as the hardware develops.

---

## 9. Offline-First Design

Blackout is intended to remain useful when conventional infrastructure is unavailable.

Where practical, important functions should be capable of operating locally.

Examples include:

- Maps
- Documentation
- System information
- Network information
- Stored data
- Local applications
- Future local AI/LLM services

Internet connectivity should enhance the system rather than define it.

---

## 10. Modularity

The Blackout ecosystem is intended to be modular.

Individual components should be replaceable or upgradeable without requiring the entire system to be redesigned.

Hardware and software interfaces should be documented as the system matures.

---

## 11. Current Development Status

This architecture represents the current direction of the project rather than a finalized specification.

Hardware choices, software architecture, communication methods, and node responsibilities may change based on testing.

Design decisions should be documented as the project evolves.

---

## 12. Design Goal

The ultimate goal is to create a system where:

The network remains useful even when individual components fail.

Blackout should provide additional capability without becoming an unnecessary single point of failure.

Build it. Test it. Break it. Learn from it. Improve it.
