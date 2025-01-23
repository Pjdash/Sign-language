import serial
import csv
import time
import os

# Configure Serial port
arduino_port = "COM8"  # Adjust to match your Arduino's COM port
baud_rate = 9600  # Ensure this matches the baud rate in your Arduino code
output_file = os.path.join(os.path.dirname(os.path.abspath(r"C:\Users\SWAPNIL JAIN\Desktop\dataset\Sign-language\testing_new.csv")), "testing_new.csv")

# Open Serial connection
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Allow some time for the connection to stabilize

file_exists = os.path.exists(output_file)

with open(output_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write header row only if the file is new
    if not file_exists:
        writer.writerow(["Timestamp", "Pitch", "Roll", "Yaw"])  # Header row

    try:
        while True:
            # Read line from Serial
            raw_line = ser.readline()
            try:
                line = raw_line.decode('utf-8').strip()  # Decode and strip whitespace
                print("Raw Data:", line)  # Print the raw data
            except UnicodeDecodeError as e:
                print(f"Decode error: {e}, Raw Data: {raw_line}")
                continue

            # Parse data
            if line.startswith("Pitch:") and "Roll:" in line and "Yaw:" in line:
                try:
                    parts = line.split(", ")
                    pitch = float(parts[0].split(":")[1].strip())
                    roll = float(parts[1].split(":")[1].strip())
                    yaw = float(parts[2].split(":")[1].strip())

                    # Print the parsed data
                    timestamp = time.time()
                    print(f"Timestamp: {timestamp}, Pitch: {pitch}, Roll: {roll}, Yaw: {yaw}")

                    # Write to CSV
                    writer.writerow([timestamp, pitch, roll, yaw])
                except (ValueError, IndexError) as e:
                    print(f"Error parsing data: {e}, Line: {line}")
    except KeyboardInterrupt:
        print("Data collection stopped by user.")
    finally:
        ser.close()
