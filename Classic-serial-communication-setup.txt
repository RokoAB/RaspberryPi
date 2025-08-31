import serial

# === SETUP SERIAL FOR ARDUINO ===
try:
    arduino = serial.Serial('/dev/ttyACM0', 9600)  #Linux version because Pi
    time.sleep(2)  # Wait for Arduino to initialize
    print("Connected to Arduino.")
except Exception as e:
    print("Could not connect to Arduino:", e)
    arduino = None