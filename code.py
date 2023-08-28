import board
import digitalio
import socketpool
import wifi
import os
from adafruit_httpserver import Server, Request, FileResponse,Response, GET, POST, PUT, REQUEST_HANDLED_RESPONSE_SENT

ssid = os.getenv("WIFI_SSID")
password = os.getenv("WIFI_PASSWORD")

if wifi.radio.connected:
    print("Already connected to an AP")
else:
    print("Connecting to", ssid)
    wifi.radio.connect(ssid, password)
    print("Connected to", ssid)

# Configuración del LED
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT
led.value = False  # Inicialmente apagado

# Configuración del servidor
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, debug=True)

# Rutas del servidor
@server.route("/")
def index(request: Request):
    with open("/static/index.html", "r") as f:
        content = f.read()
        return Response(request, content, content_type="text/html")

@server.route("/<filename>")
def static_files(request: Request, filename: str):
    try:
        with open("/static/" + filename, "r") as f:
            content = f.read()
            if filename.endswith(".css"):
                content_type = "text/css"
            elif filename.endswith(".js"):
                content_type = "application/javascript"
            else:
                content_type = "text/plain"
            return Response(request, content, content_type=content_type)
    except FileNotFoundError:
        return Response(request, "File not found", content_type="text/plain", status_code=404)

@server.route("/on", POST)
def turn_on(request: Request):
    led.value = True
    print(request.form_data.get("accion"))
    return Response(request, "Led encendido", content_type="text/plain")

@server.route("/off", POST)
def turn_off(request: Request):
    led.value = False
    print(request.form_data.get("accion"))
    return Response(request, "Led apagado", content_type="text/plain")

@server.route("/infoLed", POST)
def getInfoLed(request: Request):
    message = "Led Encendido" if led.value else "Led Apagado"
    return Response(request, message, content_type="text/plain")

server.serve_forever(str(wifi.radio.ipv4_address))
