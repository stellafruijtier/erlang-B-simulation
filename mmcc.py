import math
import random
import heapq
import statistics
from typing import List, Tuple

def erlang_b(load: float, servers: int) -> float:
    """Calculate Erlang-B blocking probability"""
    numerator = (load ** servers) / math.factorial(servers)
    denominator = sum((load ** k) / math.factorial(k) for k in range(servers + 1))
    return numerator / denominator

def find_servers(load: float, target_blocking: float) -> int:
    """Find minimum servers needed to achieve target blocking probability"""
    low = 1
    high = 2 * int(load) 
    
    # find an upper bound
    while erlang_b(load, high) > target_blocking:
        high *= 2
    
    # binary search between low and high
    while low < high:
        mid = (low + high) // 2
        if erlang_b(load, mid) > target_blocking:
            low = mid + 1
        else:
            high = mid
    
    return low

class MMccSimulator:
    """Discrete-event simulator for M/M/c/c queueing system"""
    
    def __init__(self, arrival_rate: float, avg_service_time: float, num_servers: int):
        self.arrival_rate = arrival_rate
        self.avg_service_time = avg_service_time
        self.num_servers = num_servers
        self.time = 0.0
        self.event_queue = []
        self.current_customers = 0
        self.total_arrivals = 0
        self.blocked_arrivals = 0
        
    def run(self, max_time: float) -> float:
        """Run simulation until max_time is reached"""
        # schedule first arrival
        heapq.heappush(self.event_queue, (self.time + random.expovariate(self.arrival_rate), 'arrival'))
        
        while self.time < max_time and self.event_queue:
            time, event_type = heapq.heappop(self.event_queue)
            self.time = time
            
            if event_type == 'arrival':
                self._handle_arrival()
            elif event_type == 'departure':
                self._handle_departure()
                
        blocking_prob = self.blocked_arrivals / self.total_arrivals if self.total_arrivals > 0 else 0
        return blocking_prob
    
    def _handle_arrival(self):
        """Process an arrival event"""
        self.total_arrivals += 1
        # schedule next arrival
        heapq.heappush(self.event_queue, (self.time + random.expovariate(self.arrival_rate), 'arrival'))
        
        if self.current_customers < self.num_servers:
            self.current_customers += 1
            # schedule departure
            service_time = random.expovariate(1/self.avg_service_time)
            heapq.heappush(self.event_queue, (self.time + service_time, 'departure'))
        else:
            self.blocked_arrivals += 1
    
    def _handle_departure(self):
        """Process a departure event"""
        self.current_customers -= 1

class MMccErlangSimulator(MMccSimulator):
    """Simulator with Erlang-2 distributed service times"""
    
    def _handle_arrival(self):
        """Process an arrival event with Erlang-2 service times"""
        self.total_arrivals += 1
        # schedule next arrival
        heapq.heappush(self.event_queue, (self.time + random.expovariate(self.arrival_rate), 'arrival'))
        
        if self.current_customers < self.num_servers:
            self.current_customers += 1
            # generate Erlang-2 service time (sum of two exponentials with mean 0.5)
            service_time = random.expovariate(1/0.5) + random.expovariate(1/0.5)
            heapq.heappush(self.event_queue, (self.time + service_time, 'departure'))
        else:
            self.blocked_arrivals += 1

def run_simulation_trials(
    simulator_class,
    arrival_rate: float,
    avg_service_time: float,
    num_servers: int,
    max_time: float = 10000,
    trials: int = 5
) -> Tuple[float, List[float]]:
    """Run multiple simulation trials and return average and individual results"""
    blocking_probs = []
    for _ in range(trials):
        sim = simulator_class(arrival_rate, avg_service_time, num_servers)
        blocking_probs.append(sim.run(max_time))
    return statistics.mean(blocking_probs), blocking_probs

def main():
    # System parameters
    arrival_rate = 10.0
    avg_service_time = 1.0
    offered_load = arrival_rate * avg_service_time
    
    print("=== Part 1: Erlang-B Formula Calculations ===")
    print(f"For offered load E = {offered_load}:")
    for target in [0.1, 0.01, 0.001]:
        servers = find_servers(offered_load, target)
        blocking = erlang_b(offered_load, servers)
        print(f"  Servers needed for <{target*100:.1f}% blocking: {servers} "
              f"(actual blocking: {blocking*100:.4f}%)")
    
    print("\n=== Part 2: Simulation Verification ===")
    test_cases = [
        (13, 0.1),
        (18, 0.01),
        (21, 0.001)
    ]
    
    for servers, target in test_cases:
        avg_blocking, all_results = run_simulation_trials(
            MMccSimulator, arrival_rate, avg_service_time, servers)
        print(f"\nWith {servers} servers (target <{target*100:.1f}% blocking):")
        print(f"  Simulated blocking: {avg_blocking*100:.4f}%")
        print(f"  Individual trial results: {[f'{x*100:.4f}%' for x in all_results]}")
        print(f"  Erlang-B prediction: {erlang_b(offered_load, servers)*100:.4f}%")
    
    print("\n=== Part 3: Erlang-2 Service Times ===")
    # for Erlang-2, the average service time is still 1.0 (0.5 + 0.5)
    servers_erlang = find_servers(offered_load, 0.01)
    avg_blocking, _ = run_simulation_trials(
        MMccErlangSimulator, arrival_rate, avg_service_time, servers_erlang)
    
    # find actual servers needed for Erlang-2 case
    print("\nFinding servers needed for <1% blocking with Erlang-2 service times...")
    current_servers = servers_erlang
    while True:
        avg_blocking, _ = run_simulation_trials(
            MMccErlangSimulator, arrival_rate, avg_service_time, current_servers)
        if avg_blocking < 0.01:
            break
        current_servers += 1
    
    print(f"Servers needed for <1% blocking with Erlang-2 service: {current_servers}")
    print(f"  (Compared to {servers_erlang} servers for exponential service times)")

if __name__ == "__main__":
    main()