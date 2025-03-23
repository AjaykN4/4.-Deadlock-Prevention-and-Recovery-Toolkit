import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class DeadlockToolkit:
    def __init__(self, num_processes, num_resources):
        self.num_processes = num_processes
        self.num_resources = num_resources
        self.allocation = np.zeros((num_processes, num_resources), dtype=int)
        self.max_demand = np.zeros((num_processes, num_resources), dtype=int)
        self.available = np.zeros(num_resources, dtype=int)
        self.graph = nx.DiGraph()

    def set_resources(self, available):
        if len(available) != self.num_resources:
            raise ValueError(f"❌ Expected {self.num_resources} resource values, but got {len(available)}.")
        self.available = np.array(available, dtype=int)

    def set_allocation(self, allocation):
        if len(allocation) != self.num_processes or any(len(row) != self.num_resources for row in allocation):
            raise ValueError(f"❌ Allocation matrix must be {self.num_processes}×{self.num_resources}.")
        self.allocation = np.array(allocation, dtype=int)

    def set_max_demand(self, max_demand):
        if len(max_demand) != self.num_processes or any(len(row) != self.num_resources for row in max_demand):
            raise ValueError(f"❌ Max demand matrix must be {self.num_processes}×{self.num_resources}.")
        self.max_demand = np.array(max_demand, dtype=int)

    def is_safe_state(self):
        work = np.copy(self.available)
        finish = np.array([False] * self.num_processes)

        while True:
            allocated = False
            for i in range(self.num_processes):
                if not finish[i] and all(self.max_demand[i] - self.allocation[i] <= work):
                    work += self.allocation[i]
                    finish[i] = True
                    allocated = True
            if not allocated:
                break
        return all(finish)

    def detect_deadlock(self):
        self.build_resource_allocation_graph()
        try:
            cycle = nx.find_cycle(self.graph, orientation='original')
            return True, cycle
        except:
            return False, []

    def build_resource_allocation_graph(self):
        self.graph.clear()
        for p in range(self.num_processes):
            self.graph.add_node(f'P{p}', color='blue')
        for r in range(self.num_resources):
            self.graph.add_node(f'R{r}', color='red')

        for p in range(self.num_processes):
            for r in range(self.num_resources):
                if self.allocation[p][r] > 0:
                    self.graph.add_edge(f'R{r}', f'P{p}')
                if self.max_demand[p][r] - self.allocation[p][r] > 0:
                    self.graph.add_edge(f'P{p}', f'R{r}')

    def visualize_graph(self):
        color_map = [self.graph.nodes[node]['color'] for node in self.graph.nodes()]
        plt.figure(figsize=(8, 6))
        nx.draw(self.graph, with_labels=True, node_color=color_map, node_size=2000, font_size=12)
        plt.show()

    def simulate_scenario(self, allocation, max_demand, available):
        self.set_allocation(allocation)
        self.set_max_demand(max_demand)
        self.set_resources(available)

        print("\n🔹 Allocation Matrix:\n", self.allocation)
        print("🔹 Max Demand Matrix:\n", self.max_demand)
        print("🔹 Available Resources:\n", self.available)

        safe = self.is_safe_state()
        deadlock, cycle = self.detect_deadlock()

        self.visualize_graph()
        return {'safe': safe, 'deadlock_detected': deadlock, 'cycle': cycle}

def get_user_input():
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of resources: "))

    def get_matrix_input(name):
        print(f"\nEnter {name} matrix row by row (space-separated values):")
        matrix = []
        for i in range(num_processes):
            while True:
                try:
                    row = list(map(int, input(f"Row {i + 1}: ").split()))
                    if len(row) != num_resources:
                        raise ValueError(f"❌ Expected {num_resources} values, got {len(row)}.")
                    matrix.append(row)
                    break
                except ValueError as e:
                    print(e)
        return matrix

    available = list(map(int, input("\nEnter available resources (space-separated): ").split()))
    while len(available) != num_resources:
        print(f"❌ Expected {num_resources} values for available resources.")
        available = list(map(int, input("Re-enter available resources: ").split()))

    allocation = get_matrix_input("allocation")
    max_demand = get_matrix_input("max demand")

    return num_processes, num_resources, allocation, max_demand, available

if __name__ == "__main__":
    try:
        num_processes, num_resources, allocation, max_demand, available = get_user_input()
        toolkit = DeadlockToolkit(num_processes, num_resources)

        result = toolkit.simulate_scenario(allocation, max_demand, available)
        print("\n🔍 **Results:**")
        if result['safe']:
            print("✅ System is in a SAFE STATE.")
        else:
            print("❌ Deadlock detected!")

        if result['deadlock_detected']:
            print("🔴 Deadlock Cycle Found:", result['cycle'])

    except Exception as e:
        print(f"\n⚠️ Error: {e}")
