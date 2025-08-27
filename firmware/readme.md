# Pocketboard Firmware

This folder contains everything related to firmware and configuration for the Pocketboard.

---

## 🔥 Bootloader

Pocketboard is based on the **nRF52840** MCU and requires the **nice!nano bootloader** to be flashed before loading firmware.

### Flashing the Bootloader

1. **Requirements**
   - [pyOCD](https://github.com/pyocd/pyOCD) installed  
   - A **DAPLink** or other SWD-compatible programmer/debugger  
   - Access to the Pocketboard debug header  

2. **Steps**
   - Connect your DAPLink to the Pocketboard via the debug header.  
   - Use pyOCD to flash the nice!nano bootloader:  

     ```bash
     pyocd flash --target nrf52840 path/to/nice_nano_bootloader.hex
     ```

   - Once complete, the device should show up as a USB drive when plugged in over USB-C.

---

## ⚙️ ZMK Configuration

Firmware for Pocketboard is powered by [ZMK Firmware](https://zmk.dev/).  
The configuration files are located in the **`zmk-config/`** folder, which is also available as a separate GitHub project:

[Pocketboard ZMK Config Repo](https://github.com/sini6a/zmk-config)

---

### Submodule Setup

The `zmk-config` folder is included as a **Git submodule**.

To clone this repository with the config included, run:

```bash
git clone --recurse-submodules https://github.com/sini6a/pocketboard
```

If you already cloned without `--recurse-submodules`, initialize the submodule manually:

```bash
git submodule update --init --recursive
```

To pull the latest changes in the config:

```bash
cd firmware/zmk-config
git pull origin master
```

When updating the submodule reference, commit the new pointer in the main repo:

```bash
cd firmware/zmk-config
git pull origin main
cd ../..
git add firmware/zmk-config
git commit -m "Update zmk-config submodule"
```

---

## 🔧 Building the Firmware

You can build the firmware using the standard ZMK workflow:

```bash
west init -l firmware/zmk-config
west update
west build -b nice_nano_v2 -- -DSHIELD=pocketboard
```

Once built, copy the `.uf2` file to the Pocketboard’s USB drive (bootloader mode) to flash the firmware.

---

## 📌 Notes

- Make sure the bootloader is flashed **before** trying to load ZMK firmware.  
- The LCD support is still experimental and not yet fully integrated into the ZMK config.  
