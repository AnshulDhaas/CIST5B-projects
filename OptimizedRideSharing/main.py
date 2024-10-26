import heapq
from collections import defaultdict
import math
import pandas as pd
import numpy as np
from collections import deque
import tkinter as tk
from tkinter import filedialog
from tkintermapview import TkinterMapView
from driver import Driver, Drivers
from passenger import Passenger, Passengers
from ridematchingsystem import RideMatchingSystem, Graph
def main():
    # Initialize Tkinter
    root = tk.Tk()
    root.title("Map in Tkinter")
    root.geometry("800x600")

    # Create a Map Widget
    map_widget = TkinterMapView(root, width=800, height=500, corner_radius=0)
    map_widget.pack(fill="both", expand=True)

    passengers = Passengers()
    drivers = Drivers()
    
    # Set starting location (latitude, longitude) and zoom level
    map_widget.set_position(37.7749, -122.4194)  # Example: San Francisco
    map_widget.set_zoom(10)

    # Frame for file upload interface
    upload_frame = tk.Frame(root)
    upload_frame.pack(fill="x", padx=10, pady=10)

    # Entry widget for file path
    file_path_entry = tk.Entry(upload_frame, width=50)
    file_path_entry.pack(side="left", padx=5)

    # Function to browse and select a CSV file
    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            file_path_entry.delete(0, tk.END)  # Clear any existing text
            file_path_entry.insert(0, file_path)  # Insert the new file path

    # Function to load and display markers from the entered file path
    def load_csv():
        file_path = file_path_entry.get()  # Get the file path from the entry widget
        if file_path:
            # Read the CSV file
            try:
                df = pd.read_csv(file_path)
                
                # Check if necessary columns are present
                if 'Latitude' in df.columns and 'Longitude' in df.columns:
                    # Determine if it's a driver or passenger CSV based on the columns
                    is_driver_file = 'DriverID' in df.columns
                    is_passenger_file = 'PassengerID' in df.columns

                    # Add markers for each coordinate
                    for _, row in df.iterrows():
                        lat, lon = row['Latitude'], row['Longitude']
                        
                        if is_driver_file:
                            driver = Driver(row["DriverID"], (lat, lon), row['Rating'], row['Capacity'])
                            drivers.add_driver(driver)
                            map_widget.set_marker(lat, lon, text=f"{row['DriverID']} ({lat}, {lon})")
                        
                        elif is_passenger_file:
                            passenger = Passenger(row['PassengerID'], (lat, lon), (37.6191, 122.3816), row['LuggageWeight_kg'], None)
                            passengers.add_passenger(passenger)
                            map_widget.set_marker(lat, lon, text=f"{passenger.passenger_id} ({lat}, {lon})")
                else:
                    print("CSV file must contain 'Latitude' and 'Longitude' columns.")
            except Exception as e:
                print(f"Error loading file: {e}")

    # Button to browse files
    browse_button = tk.Button(upload_frame, text="Browse", command=browse_file)
    browse_button.pack(side="left", padx=5)

    # Button to load the CSV file
    load_button = tk.Button(upload_frame, text="Load Coordinates", command=load_csv)
    load_button.pack(side="left", padx=5)

    # Run the Tkinter main loop
    root.mainloop()
main()



