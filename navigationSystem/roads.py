class Road:
    """Road class to represent a road segment in the map"""
    def __init__(self, start, end, distance, speed_limit, lanes):
        self.start = start # Starting intersection
        self.end = end # Ending intersection
        # Traffic/physical factors on the road
        self.distance = distance
        self.speed_limit = speed_limit
        self.lanes = lanes
        self.current_traffic = 0  # Number of cars on this road
        # Weight of the road based on traffic and other factors
        self.base_weight = self.calculate_base_weight()
        self.traffic_score = 0.0  # Score based on traffic congestion
    
    def calculate_base_weight(self):
        """Calculate the base weight of the road"""
        if self.speed_limit and self.distance > 0:
            return self.distance / self.speed_limit  # Simple base weight calculation
        return self.distance  # Default to distance if speed limit is missing
    
    def update_traffic(self, cars_added=0, cars_removed=0):
        """Update the traffic on the road"""
        self.current_traffic += cars_added - cars_removed
        self.current_traffic = max(0, self.current_traffic)
        self.calculate_traffic_score()
    
    def calculate_traffic_score(self):
        """Calculate traffic score based on current traffic density"""
        density = self.current_traffic / (self.lanes * 10)  # Based off of lane capacity
        self.traffic_score = density * 0.1  # Basic congestion score
        return self.traffic_score
    #Weight calculation by ChatGPT 4o
    def calculate_weight(self):
        """Weight Calculation"""
        base_weight = self.distance / self.speed_limit if self.speed_limit > 0 else float('inf')

        lane_capacity = self.lanes * 10  # Assuming each lane supports 10 cars efficiently
        traffic_factor = self.current_traffic / lane_capacity if lane_capacity > 0 else 0

        congestion_penalty = 1 + (traffic_factor ** 2)

        weight = base_weight * congestion_penalty

        decay_factor = 0.95 if self.current_traffic < lane_capacity else 1.0
        weight *= decay_factor

        self.weight = weight
        return self.weight
    
    def update_weight(self): # Update the weight of the road
        self.base_weight = self.calculate_weight()
