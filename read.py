import serial
import csv
import time
import os

# Configure Serial port
arduino_port = "COM8"  
baud_rate = 9600
output_file = os.path.join(os.path.dirname(os.path.abspath(r"C:\Users\SWAPNIL JAIN\Desktop\dataset\testing.csv")), "testing.csv")

# Open Serial connection
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  

file_exists = os.path.exists(output_file)

with open(output_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write header row only if the file is new
    if not file_exists:
        writer.writerow(["Time", "Pitch", "Roll"])  # Header row

    try:
        while True:
            # Read line from Serial
            line = ser.readline().decode('utf-8').strip()  
            print("Raw Data:", line)  # Print the raw data
            
            # Extract data
            if "Pitch:" in line and "Roll:" in line:
               
                parts = line.split(", ")
                try:
                    pitch = float(parts[0].split(":")[1].strip()) 
                    roll = float(parts[1].split(":")[1].strip())   

                    # Print the data being written
                    print(f"Time: {time.time()}, Pitch: {pitch}, Roll: {roll}")
                    
                    # Write to CSV
                    writer.writerow([time.time(), pitch, roll])
                except ValueError as e:
                    print(f"Error parsing data: {e}")
    except KeyboardInterrupt:
        print("Data collection stopped.")
    finally:
        ser.close()
