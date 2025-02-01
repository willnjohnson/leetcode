class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Initializations
        total_gas = 0   # Total amount of gas available at all stations
        total_cost = 0  # Total cost to travel between all stations
        
        current_gas = 0  # Gas in current tank while attempting from a specific station
        start_index = 0  # The candidate starting station
        
        # Iterate through each gas station to calculate total gas and total cost
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            
            current_gas += gas[i] - cost[i]
            
            # Current gas is negative (constraint), so reset start index and current_gas
            if current_gas < 0:
                start_index = i + 1  # Set the next station as the new candidate starting point
                current_gas = 0  # Reset current_gas
        
        # Check if the circuit can be completed
        if total_gas < total_cost:
            return -1  # Not enough gas to complete circuit
        
        # Otherwise, valid starting point exists, so return start_index
        return start_index
