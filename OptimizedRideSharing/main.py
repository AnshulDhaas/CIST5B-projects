import math
import pandas as pd
import tkinter as tk
from tkinter import Spinbox, filedialog, StringVar
from tkintermapview import TkinterMapView
from driver import Driver, Drivers
from passenger import Passenger, Passengers
from ridematchingsystem import RideMatchingSystem, Graph
from hash_table import HashTable


def main():
    # Tkinter map implmented by ChatGPT 4o
    root = tk.Tk()
    root.title("Map in Tkinter")
    root.geometry("800x1000")
    
    graph = Graph()
    ride_matching_system = RideMatchingSystem(graph) #initializing ride matching system

    map_widget = TkinterMapView(root, width=800, height=500, corner_radius=0)
    map_widget.pack(fill="both", expand=True)

    passengers = Passengers() #initializing passengers
    drivers = Drivers() #initializing drivers
    
    paths = {}
    
    map_widget.set_position(37.7749, -122.4194)
    map_widget.set_zoom(10)

    upload_frame = tk.Frame(root)
    upload_frame.pack(fill="x", padx=10, pady=10)

    # Entry widget for file path
    file_path_entry = tk.Entry(upload_frame, width=50)
    file_path_entry.pack(side="left", padx=5)
    # Tkinter map implmented by ChatGPT 4o
    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            file_path_entry.delete(0, tk.END)
            file_path_entry.insert(0, file_path)

    #The csv files I used were generated by ChatGPT 4o based on the attributes of the Passenger class and Driver class
    def load_csv(): #function to load the coordinates from the csv file
        file_path = file_path_entry.get()
        if file_path:
            try:
                df = pd.read_csv(file_path)
                
                if 'Latitude' in df.columns and 'Longitude' in df.columns: #check if the csv file contains the 'Latitude' and 'Longitude' columns
                    is_driver_file = 'DriverID' in df.columns
                    is_passenger_file = 'PassengerID' in df.columns

                    for _, row in df.iterrows(): #iterate through the rows of the csv file and read latitude and longitude values
                        lat, lon = row['Latitude'], row['Longitude']
                        
                        if is_driver_file:
                            driver = Driver(row["DriverID"], (lat, lon), row['Rating'], row['Capacity']) #initialize driver object for each value
                            drivers.add_driver(driver)  #add the driver to drivers linked list
                            ride_matching_system.add_driver(driver) #add the driver to the ride matching system
                            map_widget.set_marker(lat, lon, text=f"{row['DriverID']} ({lat}, {lon})") #map the driver's location on the map
                            
                        elif is_passenger_file:
                            passenger = Passenger(row['PassengerID'], (lat, lon), (37.6191, 122.3816), row['LuggageWeight_kg'], None) #initialize passenger object for each value
                            passengers.add_passenger(passenger)  #add the passenger to passengers linked list
                            ride_matching_system.add_passenger(passenger) #add the passenger to the ride matching system
                            closest_driver, dst = ride_matching_system.find_closest_driver(passenger.passenger_id) #find the closest driver to the passenger
                            
                            if closest_driver is not None: #if a driver is found, map the driver's location and draw the path between the passenger and the driver
                                map_widget.set_marker(lat, lon, text=f"{passenger.passenger_id} ({lat}, {lon})")
                                paths[passenger.passenger_id] = map_widget.set_path([(lat, lon), closest_driver.location], color="green")
                            else:
                                print(f"No available driver found for passenger {passenger.passenger_id}.")
                    
                    update_passenger_dropdown()
                else: #exception if the csv file does not contain the 'Latitude' and 'Longitude' columns
                    print("CSV file must contain 'Latitude' and 'Longitude' columns.")
            except Exception as e: #exception if the csv file cannot be loaded
                print(f"Error loading file: {e}")

    browse_button = tk.Button(upload_frame, text="Browse", command=browse_file) #browse button to select the csv file
    browse_button.pack(side="left", padx=5)

    load_button = tk.Button(upload_frame, text="Load Coordinates", command=load_csv) #load button to load the coordinates from the csv file
    load_button.pack(side="left", padx=5)

    filter_frame = tk.Frame(root) #frame for the filter options
    filter_frame.pack(fill="x", padx=10, pady=10)

    driver_list_label = tk.Label(filter_frame, text="Driver List:") #label for the driver list
    driver_list_label.grid(row=0, column=0, padx=5, sticky="w")

    driver_listbox = tk.Listbox(filter_frame, width=50, height=10) #listbox to display the drivers
    driver_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    rating_spinbox = Spinbox(filter_frame, from_=0, to=5, width=5) #spinbox to select the minimum rating
    rating_spinbox.grid(row=2, column=0, padx=5, pady=5)
    rating_label = tk.Label(filter_frame, text="Minimum Rating")
    rating_label.grid(row=2, column=1, padx=5)

    capacity_entry = Spinbox(filter_frame, from_=0, to=7, width=5) #spinbox to select the minimum capacity
    capacity_entry.grid(row=2, column=2, padx=5, pady=5)
    capacity_label = tk.Label(filter_frame, text="Min Capacity")
    capacity_label.grid(row=2, column=3, padx=5)
    
    def on_driver_select(event):
        selected_driver_idx = driver_listbox.curselection() #get the selected driver index
        if not selected_driver_idx:
            return
        driver_id = driver_listbox.get(selected_driver_idx[0]).split(",")[0].split(":")[1].strip() #get the driver ID

        #using LinkedList iteration to find the driver
        selected_driver = None
        for driver in drivers.drivers:
            if str(driver.driver_id) == driver_id:
                selected_driver = driver
                break

        selected_passenger_id = passenger_var.get()
        selected_passenger = None
        for passenger in passengers.passengers: #iterate through the passengers to find the selected passenger
            if passenger.passenger_id == selected_passenger_id:
                selected_passenger = passenger
                break

        if selected_driver and selected_passenger: #draw a connection between the passenger and the driver
            draw_connection(selected_passenger, selected_driver)
            
    driver_listbox.bind("<<ListboxSelect>>", on_driver_select) 
    def apply_filters(selected_passenger=None):
        if not selected_passenger:
            selected_passenger_id = passenger_var.get()
            selected_passenger = passengers.search_passenger(selected_passenger_id)  #search for the selected passenger by id
            if selected_passenger is None:
                print("No valid passenger selected for filtering.")
                return
        try:
            min_rating = float(rating_spinbox.get()) #get the minimum rating from the spinbox
        except ValueError:
            min_rating = 0

        try:
            min_capacity = int(capacity_entry.get()) #get the minimum capacity from the spinbox
        except ValueError:
            min_capacity = 0

        filtered_drivers = [
            driver for driver in drivers.drivers
            if driver.rating >= min_rating and driver.weight_capacity >= min_capacity
        ] #filter the drivers based on the minimum rating and capacity
        

        best_drivers = selected_passenger.rank_drivers(filtered_drivers) #rank the drivers based on the distance from the passenger and the driver's rating
        driver_listbox.delete(0, tk.END) #clear the driver listbox

        for driver in best_drivers:
            driver_info = (f"ID: {driver.driver_id}, Distance: {math.sqrt((driver.location[0] - selected_passenger.location[0]) ** 2 + (driver.location[1] - selected_passenger.location[1]) ** 2):.2f}, "
                        f"Rating: {driver.rating}, Capacity: {driver.weight_capacity}") #display the filtered drivers information
            print(driver)
            driver_listbox.insert(tk.END, driver_info)



    filter_button = tk.Button(filter_frame, text="Apply Filters", command=apply_filters) #button to apply the filters
    filter_button.grid(row=2, column=4, padx=5, pady=5)

    passenger_var = StringVar(root)
    passenger_dropdown = tk.OptionMenu(filter_frame, passenger_var, "Select Passenger", *[p.passenger_id for p in passengers.get_all_passengers()]) #dropdown to select the passenger
    passenger_dropdown.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    passenger_info_label = tk.Label(filter_frame, text="") #label to display the passenger information
    passenger_info_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def update_passenger_dropdown():
        menu = passenger_dropdown["menu"]
        menu.delete(0, "end")
        for passenger in passengers:
            menu.add_command(label=passenger.passenger_id, command=lambda p=passenger: passenger_var.set(p.passenger_id))
        first_passenger = next(iter(passengers), None)  #get the first passenger if available
        if first_passenger:
            passenger_var.set(first_passenger.passenger_id)

    def display_passenger_info(passenger): #function to display the passenger information
        passenger_info = (f"ID: {passenger.passenger_id}, "
                        f"Location: {passenger.location}, "
                        f"Destination: {passenger.destination}, "
                        f"Luggage: {passenger.luggage} kg, "
                        f"People: {passenger.people if passenger.people else 'N/A'}")
        passenger_info_label.config(text=passenger_info)
        
        apply_filters(selected_passenger=passenger)

    
    def draw_connection(passenger, driver): #function to draw the connection between the passenger and the driver
        path = map_widget.set_path([passenger.location, driver.location], color="red")
        remove_connection(passenger)
        paths[passenger.passenger_id] = path
        
    def remove_connection(passenger): #function to remove the connection between the passenger and the driver
        if passenger.passenger_id in paths:
            paths[passenger.passenger_id].delete()
            del paths[passenger.passenger_id]
    
    for driver in drivers.drivers:
        driver_listbox.insert(tk.END, driver.driver_id)
    
    root.mainloop()

main()
