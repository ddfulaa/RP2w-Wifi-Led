
# Raspberry Pi Pico WiFi LED Controller
Control an LED wirelessly using a Raspberry Pi Pico and CircuitPython. The project demonstrates how to create a web server on the Raspberry Pi Pico that allows you to turn an LED on and off via WiFi connection. The Pico connects to an Access Point (AP) and serves a web interface to control the LED.
## Introduction

The Raspberry Pi Pico WiFi LED Controller project showcases how to control an LED remotely using WiFi and a web interface. This is achieved by creating a simple web server on the Pico that serves a web page for controlling the LED.

## Features
* Turn on and off an LED wirelessly.
* Serve a static web page for controlling the LED.
* Display the LED's current status. (Optional)
## Getting Started
### Prerequisites
* Raspberry Pi Pico with CircuitPython installed.
* Adafruit CircuitPython 8.2.3.
* adafruit_httpserver library
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


### Raspberry Pi Pico W as Access Point
You can configure the board to act as an AP. All you need is to change the configuration.
```
wifi.radio.start_station()
if not wifi.radio.ap_active:
    wifi.radio.start_ap(os.getenv("WIFI_SSID"), os.getenv("WIFI_PW"))
print(wifi.radio.ipv4_address_ap)
```
In my case, I cannot stop the AP station. The only way is rebooting.
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
