import serial
import csv
import time
import os

# Configure Serial port
arduino_port = "COM8"  # Adjust to match your Arduino's COM port
baud_rate = 9600  # Ensure this matches the baud rate in your Arduino code
output_file = os.path.join(os.path.dirname(os.path.abspath(r"C:\Users\SWAPNIL JAIN\Desktop\dataset\Sign-language\testing.csv")), "testing.csv")

# Open Serial connection
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Allow some time for the connection to stabilize

file_exists = os.path.exists(output_file)

with open(output_file, mode='a', newline='') as file:
    writer = csv.writer(file)

    # Write header row only if the file is new
    if not file_exists:
        writer.writerow(["Timestamp", "RateRoll1", "RatePitch1", "RateYaw1", "KalmanRoll1", "KalmanPitch1", "KalmanYaw1",
                         "RateRoll2", "RatePitch2", "RateYaw2", "KalmanRoll2", "KalmanPitch2", "KalmanYaw2",
                         "RateRoll3", "RatePitch3", "RateYaw3", "KalmanRoll3", "KalmanPitch3", "KalmanYaw3",
                         "RateRoll4", "RatePitch4", "RateYaw4", "KalmanRoll4", "KalmanPitch4", "KalmanYaw4",
                         "RateRoll5", "RatePitch5", "RateYaw5", "KalmanRoll5", "KalmanPitch5", "KalmanYaw5"])

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

            # Check if the line matches the expected format
            if line.startswith("Timestamp:") and all(keyword in line for keyword in [
                "RateRoll1:", "RatePitch1:", "RateYaw1:", "KalmanRoll1:", "KalmanPitch1:", "KalmanYaw1:",
                "RateRoll2:", "RatePitch2:", "RateYaw2:", "KalmanRoll2:", "KalmanPitch2:", "KalmanYaw2:",
                "RateRoll3:", "RatePitch3:", "RateYaw3:", "KalmanRoll3:", "KalmanPitch3:", "KalmanYaw3:",
                "RateRoll4:", "RatePitch4:", "RateYaw4:", "KalmanRoll4:", "KalmanPitch4:", "KalmanYaw4:",
                "RateRoll5:", "RatePitch5:", "RateYaw5:", "KalmanRoll5:", "KalmanPitch5:", "KalmanYaw5:"]):

                try:
                    parts = line.split(", ")

                    # Extract values
                    data = {}
                    for part in parts:
                        key, value = part.split(":")
                        data[key.strip()] = float(value.strip())

                    # Print the parsed data
                    timestamp = time.time()
                    print(f"Timestamp: {timestamp}, Data: {data}")

                    # Write to CSV
                    writer.writerow([timestamp, data["RateRoll1"], data["RatePitch1"], data["RateYaw1"], data["KalmanRoll1"], data["KalmanPitch1"], data["KalmanYaw1"],
                                     data["RateRoll2"], data["RatePitch2"], data["RateYaw2"], data["KalmanRoll2"], data["KalmanPitch2"], data["KalmanYaw2"],
                                     data["RateRoll3"], data["RatePitch3"], data["RateYaw3"], data["KalmanRoll3"], data["KalmanPitch3"], data["KalmanYaw3"],
                                     data["RateRoll4"], data["RatePitch4"], data["RateYaw4"], data["KalmanRoll4"], data["KalmanPitch4"], data["KalmanYaw4"],
                                     data["RateRoll5"], data["RatePitch5"], data["RateYaw5"], data["KalmanRoll5"], data["KalmanPitch5"], data["KalmanYaw5"]])

                except (ValueError, KeyError) as e:
                    print(f"Error parsing data: {e}, Line: {line}")

    except KeyboardInterrupt:
        print("Data collection stopped by user.")
    finally:
        ser.close()
