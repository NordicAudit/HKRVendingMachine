# HKRVendingMachine
System Engineering Project

# Raspberry Pi Vending Machine

This is a basic vending machine project made using a Raspberry Pi 5  
It includes:

- 2 physical buttons for product selection  
- 2 motors to release products  
- An I2C LCD screen for user feedback  
- A 3D-printed case to hold all components  

---

## 🧠 Features

- Press Button 1 → Dispense Product 1  
- Press Button 2 → Dispense Product 2  
- LCD shows messages like "Select Product" and "Dispensing"  
- Easy to use no payment system required  

---

## 🛠️ Hardware Used

- Raspberry Pi 5  
- 2 Push buttons  
- 2 DC motors or stepper motors (with drivers)  
- I2C 16x2 LCD  
- Jumper wires  
- Breadboard or custom PCB  
- 3D printed enclosure  

---

## 📦 Wiring

| Component | GPIO Pin (BCM) |
|----------|----------------|
| Button 1 | 17             |
| Button 2 | 27             |
| Motor 1  | 22             |
| Motor 2  | 23             |
| LCD SDA  | GPIO 2 (Pin 3) |
| LCD SCL  | GPIO 3 (Pin 5) |

Make sure to connect GND and 5V where needed

---

## 🚀 Setup

1. Clone this repo to your Raspberry Pi  
2. Make sure your `lcd_i2c.py` file is present  
3. Run the main script:

```bash
python3 vending.py
