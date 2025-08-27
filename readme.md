# Pocketboard

### A Pocket-Friendly On-the-Go Keyboard (now with Bluetooth!)

![Photo of the keyboard #1](assets/photos/IMG_20250427_114951.jpg)
![Photo of the keyboard #2](assets/photos/1.jpg)

**Pocketboard** is a compact, versatile keyboard designed for IT technicians, tinkerers, and professionals who need a highly portable and efficient input device.

---

## 🚀 Project Status

- [x] Firmware: Home row mods
- [x] Firmware: Layer support
- [ ] Hardware & Firmware: LCD integration
- [ ] LCD: Battery percentage display
- [x] 3D: Case design finalized

---

## ✨ Features

- **USB Type-C Connector** – Reliable modern connection for seamless usage and charging.  
- **Miryoku Layout** – Optimized for productivity and efficient typing on a small form factor.  
- **Bluetooth (nRF52840)** – Wireless connectivity powered by the Nordic nRF52840 MCU.  
- **LCD Display (planned)** – Display keypresses and battery status.  
- **Battery Support** – Internal battery with charging circuit for true portability.  

---

## 🆕 What’s New in This Revision?

This revision builds upon the original **HandiPi** and **Pocketboard Rev. A** with major upgrades:

- **nRF52840 MCU** – Replaces RP2040 for enhanced performance and built-in Bluetooth LE.  
- **Battery Management** – Integrated charger and fuel gauge for real battery monitoring.  
- **USB-C Charging** – Power and charge with your everyday cable.  
- **LCD Support** – Hardware ready for display integration (testing in progress).  

---

## 🤔 Why Pocketboard?

Pocketboard is built for people on the move. Whether you’re debugging servers, configuring devices, or just need a minimal keyboard always at hand, Pocketboard fits right in your **cargo pocket, backpack, or car**.

---

## 📂 Repository Structure

- **`kicad/`** – PCB schematics and board files  
- **`gerbers/`** – Gerber files for PCB manufacturing  
- **`firmware/zmk-config/`** – ZMK firmware configuration and build files  

A schematic PDF is included in the `kicad/` directory for quick reference.

---

## 🙌 Credits

Pocketboard was inspired by the brilliant **[HandiPi](https://github.com/brickbots)** project by *brickbots*.

---

## 🤝 Contributing

We’d love your input! To contribute:

1. Open an issue to share your idea or improvement.  
2. After discussion, submit a pull request with your changes.  

Your feedback helps make Pocketboard even better.  

---
