import sys
from tkinter import Tk, filedialog
from tkintermapview import TkinterMapView
from network import Graph
from system import System
import pandas as pd
import tkinter as tk
from car import Car

#Implmented by ChatGPT 4o

class TextRedirector:
    """Redirects stdout to a Tkinter Text widget."""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert("end", text)  # Append the text to the widget
        self.text_widget.see("end")  # Scroll to the end of the widget
        
    def flush(self):
        pass
    
#Implmented by ChatGPT 4o

def main():
    graph = Graph() #Graph Declaration
    system = System(graph=graph) #System Declaration, initialized with the graph

    #Note; GUI Code was scrapped from my last project and modified to fit this project
    
    root = Tk()
    root.title("Traffic and Map System")
    root.geometry("1200x800")

    map_widget = TkinterMapView(root, width=800, height=400, corner_radius=0)
    map_widget.pack(fill="both", expand=True)
    map_widget.set_position(37.7749, -122.4194)  # Default to San Francisco
    map_widget.set_zoom(10)

    # Frame for controls
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=10, pady=10)

    # Terminal-style output text widget
    text_frame = tk.Frame(root)
    text_frame.pack(fill="both", expand=True, padx=10, pady=5)
    output_text = tk.Text(text_frame, wrap="word", state="normal", height=15, bg="black", fg="white")
    output_text.pack(fill="both", expand=True)
    
    # Redirect stdout to the Text widget
    sys.stdout = TextRedirector(output_text)

    # Dropdown menus for intersections
    start_var = tk.StringVar(value="Select Intersection")
    end_var = tk.StringVar(value="Select Intersection")
    start_dropdown = tk.OptionMenu(frame, start_var, "")
    end_dropdown = tk.OptionMenu(frame, end_var, "")
    start_dropdown.pack(side="left", padx=5)
    end_dropdown.pack(side="left", padx=5)

    def update_dropdowns():
        """Update dropdown menus with intersection names."""
        options = list(graph.intersections.keys())
        start_dropdown['menu'].delete(0, 'end')
        end_dropdown['menu'].delete(0, 'end')
        for option in options:
            start_dropdown['menu'].add_command(label=option, command=tk._setit(start_var, option))
            end_dropdown['menu'].add_command(label=option, command=tk._setit(end_var, option))

    def browse_and_load_intersections():
        """Load intersections from a CSV file and display them on the map."""
        file_path = filedialog.askopenfilename(title="Select Intersections CSV File", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            # File reading
            df = pd.read_csv(file_path)
            # Initializing the intersections
            for _, row in df.iterrows():
                intersection_name = row['name'].strip()
                latitude = float(row['latitude'])
                longitude = float(row['longitude'])
                graph.add_intersection(intersection_name, latitude, longitude) 
                # Add a marker for the intersection
                map_widget.set_marker(latitude, longitude, text=intersection_name)
            print("Intersections loaded successfully.")
            update_dropdowns()
        except Exception as e:
            print(f"Error loading intersections: {e}")

    def browse_and_load_roads():
        """Load roads from a CSV file and display them on the map."""
        file_path = filedialog.askopenfilename(title="Select Roads CSV File", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            df = pd.read_csv(file_path)
            for _, row in df.iterrows():
                start = row['start'].strip()
                end = row['end'].strip()
                distance = float(row['distance'])
                speed_limit = float(row['speed_limit']) if not pd.isna(row['speed_limit']) else None
                lanes = int(row['lanes'])
                graph.add_road(start, end, distance, speed_limit, lanes)

                # Get the coordinates of the start and end intersections
                start_intersection = graph.get_intersection(start)
                end_intersection = graph.get_intersection(end)
                if start_intersection and end_intersection:
                    # Draw a path between the two intersections
                    start_coords = (start_intersection.latitude, start_intersection.longitude)
                    end_coords = (end_intersection.latitude, end_intersection.longitude)
                    map_widget.set_path([start_coords, end_coords])
            print("Roads loaded successfully.")
        except Exception as e:
            print(f"Error loading roads: {e}")

    def browse_and_load_cars():
        file_path = filedialog.askopenfilename(title="Select Cars CSV File", filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            car = Car(
                graph=graph,
                car_id=int(row['id']), current_location=row['current_location'].strip(),
                destination=row['destination'].strip()
            )
            system.cars.append(car)
        print(f"{len(system.cars)} cars loaded successfully.")

    current_route_path = None
    
    
    
    def find_fastest_route():
        """Find the fastest route between two intersections and display it on the map."""
        nonlocal current_route_path # Use the current route path to update the path on the map
        start, end = start_var.get(), end_var.get()
        
        if start == "Select Intersection" or end == "Select Intersection":
            print("Select both start and end intersections.")
            return

        distance, path = system.find_shortest_path(start, end) # Finding the shortest path, using the system object
        print(f"Route from {start} to {end}: {path}, Weight: {distance:.2f}")
        
        if distance == float('inf') or len(path) < 2: # If no path is found
            print("No valid path found.")
            return

        coordinates = [
            (graph.get_intersection(node).latitude, graph.get_intersection(node).longitude) # Get the coordinates
            for node in path
        ]
        # Set the path on the map
        if current_route_path:
            current_route_path.delete()

        current_route_path = map_widget.set_path(coordinates, color="red", width=3)
    #Simulate Traffic Event
    def simulate_traffic_event():
        system.simulate_traffic()
        print("Traffic simulation completed.")


    tk.Button(frame, text="Load Intersections", command=browse_and_load_intersections).pack(side="left", padx=5)
    tk.Button(frame, text="Load Roads", command=browse_and_load_roads).pack(side="left", padx=5)
    tk.Button(frame, text="Load Cars", command=browse_and_load_cars).pack(side="left", padx=5)
    tk.Button(frame, text="Find Route", command=find_fastest_route).pack(side="left", padx=5)
    tk.Button(frame, text="Simulate Traffic", command=simulate_traffic_event).pack(side="left", padx=5)

    root.mainloop()

main()