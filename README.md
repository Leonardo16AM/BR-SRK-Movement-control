# BR-SRK-Movement-Control

BR-SRK-Movement-Control is a comprehensive Raspberry Pi project designed to control a car equipped with two hacked servomotors. This project offers a user-friendly web app created with Flutter, enabling seamless control of the Raspberry Pi car remotely. 

The application includes a VLC-based camera streaming feature, providing real-time video feedback for enhanced user experience and control. A significant highlight of the project is its autonomous mode, which leverages an HC-SR04 ultrasonic sensor to prevent collisions, enabling the car to navigate without crashing into walls.

## Hardware Requirements

- Raspberry Pi
- Two hacked servomotors for movement control
- HC-SR04 ultrasonic sensor for distance measurement and autonomous conduction

## Pin Configuration

Ensure the following GPIO pin connections for the Raspberry Pi:

- Motor1: GPIO Pin 5
- Motor2: GPIO Pin 6
- HC-SR04 Echo: GPIO Pin 22
- HC-SR04 Trigger: GPIO Pin 23

## Usage

1. Clone the project repository to your Raspberry Pi.
2. Make sure to adjust the `host` value in `web_app` to match your Raspberry Pi's IP address. This adjustment makes the application visible on your local network.
3. Run `movement_control.py` to start the application.

```bash
python3 movement_control.py
```

If you face any issues with the camera streaming, please refer to our related project [BR-SRK-Camera-network-viewer](https://github.com/Leonardo16AM/BR-SRK-Camera-network-viewer) on GitHub for detailed instructions and troubleshooting.

## Notes

This project uses hacked servomotors for movement control. If you're using a different type of motor, you might need to adjust the control code accordingly.
