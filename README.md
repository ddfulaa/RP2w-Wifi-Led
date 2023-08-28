
# Raspberry Pi Pico WiFi LED Controller
Control an LED wirelessly using a Raspberry Pi Pico and CircuitPython. The project demonstrates how to create a web server on the Raspberry Pi Pico that allows you to turn an LED on and off via WiFi connection. The Pico itself acts as an Access Point (AP) and serves a web interface to control the LED.
## Introduction

The Raspberry Pi Pico WiFi LED Controller project showcases how to control an LED remotely using WiFi and a web interface. This is achieved by creating a simple web server on the Pico that serves a web page for controlling the LED.

## Features
Turn on and off an LED wirelessly.
Serve a static web page for controlling the LED.
Display the LED's current status.
## Getting Started
### Prerequisites
Raspberry Pi Pico with CircuitPython installed.
Adafruit CircuitPython library.
### Installation
1. Clone this repository:
```
git clone https://github.com/yourusername/raspberry-pico-wifi-led.git
```
2. Put files in memory

### Configuration
Edit the settings.toml file to set up your WiFi Access Point (AP) credentials:
WIFI_SSID = "Put here SSID"
WIFI_PASSWORD = "Put here the password"

### Usage

Open a web browser and navigate to the address indicated in the serial port to access the control interface.

### API Endpoints
GET /: Serve the main HTML page.

GET /<filename>: Serve static files like CSS and JavaScript.

POST /on: Turn on the LED.

POST /off: Turn off the LED.

POST /infoLed: Get information about the LED's current state.

## Contributing
Contributions are welcome! Feel free to open issues and pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
