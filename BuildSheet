Project Blackout — Build Sheet

Project: Blackout
Purpose: Rugged, portable, self-contained communications and field-computing system
Status: Active development
Last Updated: August 13, 2026

⸻

1. Project Architecture

Project Blackout is being developed as a modular field system consisting of:

                         PROJECT BLACKOUT
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ▼                  ▼                  ▼
       MAIN BLACKOUT          ROVER             SCOUT
       Raspberry Pi 4       Raspberry Pi       Pico 2 W
             │                 Zero               │
             │                  │                 │
        SSD + UPS         18650 UPS HAT      SX1262 LoRa
             │                  │                 │
        Touchscreen        SX1262 LoRa          US915
        Keyboard             US915
        GPS
        Meshtastic
        Field Services

The system is intended to remain modular so individual nodes can operate independently while participating in the larger Blackout ecosystem.

⸻

2. Main Blackout Computer

Raspberry Pi 4 Model B — 2GB

Item	Specification
Quantity	1
Status	On hand
Assignment	Main Blackout
Processor	Raspberry Pi 4
RAM	2GB
Primary Storage	Lexar Portable SSD
Secondary Storage	128GB microSD
Power	Main UPS HAT
Display	5” IPS touchscreen
Input	Wireless keyboard/touchpad
GPS	USB GPS receiver
Radio	US915 LoRa hardware

Intended Functions

* Main Blackout computer
* Meshtastic services
* Offline maps
* GPS/location services
* Local network services
* Offline computing/LLM experimentation
* Field interface
* Data storage
* Node management
* Future Blackout applications

⸻

3. Main Storage

Lexar Portable SSD

Item	Specification
Quantity	1
Status	Arriving
Assignment	Main Blackout
Interface	USB
Role	Primary Blackout storage

Intended Use

The SSD is intended to provide the primary high-speed storage for the Raspberry Pi 4.

Potential uses include:

* Operating system
* Applications
* Offline maps
* Databases
* Logs
* Meshtastic-related data
* Local AI/LLM files
* Project files
* Future Blackout services

⸻

4. Backup / Boot Storage

SanDisk Ultra 128GB microSD

Item	Specification
Quantity	1
Status	On hand
Assignment	Raspberry Pi / Blackout
Capacity	128GB
Role	Boot, recovery, testing and backup

The microSD should remain available as a recovery/testing medium even after the primary system is moved to SSD storage.

⸻

5. Main Blackout Power

UPS HAT

Item	Specification
Quantity	1
Status	On hand
Assignment	Main Blackout
Host	Raspberry Pi 4
Role	Backup power / power management

Important

This UPS is NOT the Rover UPS.

The Blackout main computer has its own UPS system.

⸻

6. Rover Node

Raspberry Pi Zero

Item	Specification
Quantity	1
Status	On hand
Assignment	Blackout Rover
Role	Rover computer / communications node

⸻

Xicoolee Pi Zero UPS HUB HAT

Item	Specification
Quantity	1
Status	On hand
Assignment	Rover
Battery	18650
USB Expansion	3 × USB 2.0
Role	Rover power + USB expansion

Rover Power

The Rover uses an 18650-based UPS HAT.

This is separate from the UPS used by the Raspberry Pi 4.

⸻

MakerSpot Micro-USB OTG Hub

Item	Quantity	Assignment
Micro-USB OTG Hub	1	Rover

Role

Provides additional USB connectivity for the Raspberry Pi Zero Rover.

⸻

7. Rover LoRa Radio

Waveshare SX1262 LoRaWAN Node Module

Item	Specification
Quantity	1
Status	On hand
Frequency	US915 / 915 MHz
Assignment	Rover / Blackout
Radio	SX1262
Role	LoRa / Meshtastic communications

Notes

The Waveshare hardware purchased for Blackout has been confirmed as the US915 version.

⸻

8. Scout Node

Raspberry Pi Pico 2 W

Item	Specification
Quantity	1
Status	On hand
Assignment	Scout
Wireless	Wi-Fi / Bluetooth
Role	Low-power microcontroller

Scout Design Goal

The Scout is intended to be a small, low-power remote Blackout node rather than a full field computer.

⸻

Waveshare Pico SX1262 LoRa Node Module

Item	Specification
Quantity	1
Status	On hand
Frequency	US915 / 915 MHz
Assignment	Scout
Radio	SX1262
Host	Raspberry Pi Pico platform

Important

This is the US915 version.

⸻

9. RAK WisBlock Node

RAKwireless WisBlock Mini Meshtastic Starter Kit

US915 — RAK19003 Base

Item	Specification
Quantity	1 complete kit
Status	On hand
Frequency	US915
Base	RAK19003
Radio	RAK WisBlock LoRa module
Antenna	Included
Assignment	Blackout
Purchase Date	August 10, 2026
Purchase Price	$31.50

Role

This kit provides an additional complete Meshtastic-capable node platform for Blackout.

Inventory Rule

The kit is currently counted as one complete node kit.

The RAK base, radio and included antenna should not be counted as independent spare components unless the kit is intentionally disassembled.

⸻

10. RF / Antenna Hardware

915 MHz Antennas

Item	Quantity	Assignment
915 MHz antennas	2	Blackout / LoRa

Status

Limited inventory — 2 total shown.

⸻

SMA Bulkhead Adapters

Item	Quantity	Assignment
SMA bulkhead adapters	~2	Blackout enclosure

Role

Provides external antenna connections through the Blackout enclosure.

⸻

11. GPS

VFAN USB GPS Receiver

Item	Specification
Quantity	1
Status	On hand
Assignment	Main Blackout
Interface	USB
Role	GPS positioning

Intended Uses

* Position reporting
* Offline navigation
* Mapping
* Node location
* Future location-aware Blackout applications

⸻

12. User Interface

Hosyond 5” IPS Touchscreen

Item	Specification
Quantity	1
Resolution	800 × 480
Status	On hand
Assignment	Main Blackout
Role	Field display

⸻

Mini Wireless Keyboard + Touchpad

Item	Quantity	Assignment
Wireless keyboard/touchpad	1	Main Blackout

Role

Primary physical input device for field operation and configuration.

⸻

JSAUX Mini-HDMI → HDMI Adapter

Item	Quantity	Assignment
Mini-HDMI adapter	1	Main Blackout

Role

Display connectivity for the Raspberry Pi 4.

⸻

13. Enclosure Connectivity

Waterproof USB-C Bulkhead Connectors

Item	Quantity	Assignment
Waterproof USB-C bulkhead	~2	Main Blackout enclosure

Intended Uses

* External power
* External USB connectivity
* Weather-resistant enclosure interface

Final connector assignments will be determined during enclosure design.

⸻

14. Wiring

Fermerry 28 AWG Stranded Wire

Item	Quantity	Assignment
28 AWG wire assortment	1 set	General Blackout

Uses

* Signal wiring
* Low-current connections
* Internal electronics
* Sensors
* GPIO connections

⸻

BNTECHGO 30 AWG Silicone Wire

Item	Quantity	Assignment
30 AWG silicone wire kit	1 set	General Blackout

Uses

* PCB wiring
* Jumper wiring
* GPIO
* Sensors
* Low-current electronics

⸻

15. Batteries

3.7V LiPo Batteries

Item	Quantity	Status
3.7V LiPo batteries	6	On hand

Assignment

General Blackout node/electronics inventory.

Inventory Status

Limited — 6 total.

At least one battery has been considered for node use. Remaining batteries should be treated as available spares until specifically assigned.

⸻

18650 Battery

Rover

The Rover’s Xicoolee UPS HAT uses an 18650 battery.

Component	Quantity	Assignment
18650 battery system	1	Rover

The exact installed 18650 cell count should be documented once the actual cell is selected/installed.

⸻

16. Power Protection

Inline Fuse Holders

Item	Quantity	Assignment
12V inline fuse holders	6	Blackout power inventory

Role

Used for fused power distribution and protection.

Inventory Status

6 available.

These should be assigned as the final Blackout power architecture is designed.

⸻

17. Electronics Tools

These aren’t installed components, but are part of the available Blackout development equipment.

Soldering Iron Kit

Item	Quantity
60W soldering iron kit	1

Use

* Board assembly
* Wiring
* Connector installation
* Repairs
* Prototype construction

⸻

JOREST Precision Screwdriver Set

Item	Quantity
Precision screwdriver set	1

Use

* Electronics assembly
* Raspberry Pi work
* Enclosure assembly
* Small hardware

⸻

18. General USB / Adapter Inventory

USB → Micro-USB Adapters

Item	Quantity
USB/Micro-USB adapters	2

Status

Limited — 2 available.

⸻

19. Node Hardware Allocation

Hardware	Qty	Assigned To
Raspberry Pi 4 2GB	1	Main Blackout
Lexar SSD	1	Main Blackout
Main UPS HAT	1	Main Blackout
128GB microSD	1	Main Blackout / Pi
5” touchscreen	1	Main Blackout
Wireless keyboard/touchpad	1	Main Blackout
USB GPS	1	Main Blackout
Mini-HDMI adapter	1	Main Blackout
Raspberry Pi Zero	1	Rover
Xicoolee 18650 UPS HAT	1	Rover
MakerSpot OTG hub	1	Rover
SX1262 US915 LoRa module	1	Rover
Pico 2 W	1	Scout
Pico SX1262 US915	1	Scout
RAK WisBlock US915 Starter Kit	1	Blackout / additional node

⸻

20. Limited Components

The following components currently have little or no spare capacity:

Component	Available	Status
Raspberry Pi 4 2GB	1	Assigned
Raspberry Pi Pico 2 W	1	Assigned
Raspberry Pi Zero	1	Assigned
Main UPS HAT	1	Assigned
Rover UPS HAT	1	Assigned
Lexar SSD	1	Assigned
5” touchscreen	1	Assigned
Keyboard/touchpad	1	Assigned
USB GPS	1	Assigned
Pico SX1262	1	Assigned
SX1262 US915	1	Assigned
RAK WisBlock kit	1	Available node
915 MHz antennas	2	Limited
SMA bulkheads	~2	Limited
USB-C bulkheads	~2	Limited
128GB microSD	1	Limited
LiPo batteries	6	Limited
USB/Micro-USB adapters	2	Limited

⸻

21. Current Build Status

Main Blackout

Hardware acquisition: 🟢 In progress

* Raspberry Pi 4
* Main UPS HAT
* SSD
* microSD
* Touchscreen
* Keyboard/touchpad
* GPS
* LoRa hardware
* Final enclosure
* Internal mounting system
* Final power distribution
* Final cooling solution
* Final wiring
* Software deployment
* Full system testing

⸻

Rover

Hardware acquisition: 🟢 In progress

* Raspberry Pi Zero
* Xicoolee 18650 UPS HAT
* MakerSpot OTG hub
* US915 LoRa hardware
* Final rover chassis
* Motor/control electronics
* Battery selection
* Antenna mounting
* Final enclosure
* Software integration
* Field testing

⸻

Scout

Hardware acquisition: 🟢 In progress

* Raspberry Pi Pico 2 W
* Waveshare Pico SX1262 US915
* Final power system
* Enclosure
* Antenna mounting
* Firmware configuration
* Field testing

⸻

22. Future Procurement

Items not yet confirmed as purchased should be tracked separately from the current inventory.

Main Blackout

* Final rugged enclosure
* Internal mounting hardware
* Power distribution hardware
* Appropriate DC/DC conversion hardware if required
* Cooling/fan solution if required
* Additional storage/backup media
* Additional RF antennas if required
* Connectors/cabling required after enclosure layout

Rover

* 18650 cell
* Motor controller
* Motors
* Rover chassis/mechanical components
* Wheels
* Additional sensors as required
* Final antenna solution

Scout

* Battery/power solution
* Compact enclosure
* Final antenna solution
* Mounting hardware

⸻

23. Design Philosophy

Project Blackout is being built around several principles:

Modular

Each node should be capable of operating independently where practical.

Portable

The system should be capable of being removed from a fixed location and deployed elsewhere.

Rugged

Final hardware should be protected against normal field use, transportation and weather exposure.

Repairable

Components should remain accessible and replaceable rather than being permanently sealed whenever practical.

Offline Capable

Core functions should not depend entirely on an Internet connection.

Expandable

The system should allow additional nodes, sensors, storage, radios and computing hardware to be added later.

⸻

24. Hardware Inventory Rules

1. US915 is the confirmed operating frequency for the Blackout Waveshare LoRa hardware.
2. The main Raspberry Pi 4 UPS and Rover Pi Zero UPS are separate systems.
3. The RAK WisBlock kit is counted as one complete node kit.
4. Components assigned to a node should not be counted as available spares.
5. Limited components should be tracked by quantity.
6. Returned or cancelled purchases are excluded from inventory.
7. New purchases should be added to this document as soon as they are confirmed.
8. Component assignments can change as the architecture evolves.
9. Final quantities should be verified against physical inventory before assembly.
10. This document is the authoritative hardware build sheet for Project Blackout.

⸻

25. Revision History

v0.1 — August 13, 2026

Initial consolidated hardware build sheet created from Amazon purchase history and confirmed project discussions.

Confirmed in v0.1

* Raspberry Pi 4 2GB identified as Main Blackout computer
* Raspberry Pi Zero identified as Rover computer
* Pico 2 W identified as Scout controller
* Waveshare SX1262 hardware confirmed as US915
* RAK WisBlock Mini Meshtastic Starter Kit confirmed as US915
* RAK19003 base confirmed
* Xicoolee 18650 UPS HAT assigned specifically to Rover
* Main UPS HAT retained for Raspberry Pi 4
* SSD assigned as primary Blackout storage
* GPS assigned to Main Blackout
* 5” touchscreen assigned to Main Blackout
* Blackout/Rover/Scout hardware allocations established

⸻

Project Blackout — Build Sheet

This document should be updated whenever hardware is purchased, assigned, replaced, consumed, or removed from the project.