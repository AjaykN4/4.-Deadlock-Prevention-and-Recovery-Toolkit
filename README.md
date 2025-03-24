# 4.-Deadlock-Prevention-and-Recovery-Toolkit
# **Deadlock Detection & Prevention Toolkit** 🚀  

This Python program helps in **detecting and preventing deadlocks** in a system using the **Banker's Algorithm** and **Resource Allocation Graphs (RAGs)**. It checks for safe states, detects deadlocks, and visualizes the resource allocation graph.

---

## **📌 Features**  
✅ **Detects Deadlock** using Resource Allocation Graphs  
✅ **Checks Safe State** with Banker's Algorithm  
✅ **Finds Deadlock Cycles** if present  
✅ **Visualizes Resource Allocation Graph** with NetworkX  
✅ **Handles Edge Cases** like incorrect input sizes  

---

## **📥 Installation**  

### **1️⃣ Install Required Libraries**  
Ensure you have Python installed and run:  
```sh
pip install numpy networkx matplotlib
```

### **2️⃣ Clone or Download the Repository**  
```sh
git clone https://github.com/your-username/deadlock-toolkit.git
cd deadlock-toolkit
```

---

## **🚀 Usage**  

Run the script in a terminal:  
```sh
python deadlock_toolkit.py
```

### **💡 Input Format**  
1️⃣ **Enter Number of Processes & Resources**  
2️⃣ **Enter Available Resources** (space-separated)  
3️⃣ **Enter Allocation Matrix** (row by row)  
4️⃣ **Enter Max Demand Matrix** (row by row)  

### **📌 Example Input**
```
Enter the number of processes: 3
Enter the number of resources: 2

Enter available resources (space-separated):
1 1

Enter allocation matrix row by row (space-separated values):
Row 1: 0 1
Row 2: 2 0
Row 3: 3 2

Enter max demand matrix row by row (space-separated values):
Row 1: 3 2
Row 2: 2 2
Row 3: 4 3
```

---

## **📊 Example Output**
```
🔹 Allocation Matrix:
 [[0 1]
 [2 0]
 [3 2]]
🔹 Max Demand Matrix:
 [[3 2]
 [2 2]
 [4 3]]
🔹 Available Resources:
 [1 1]

✅ System is in a SAFE STATE.
```
*(A graph visualization of the resource allocation is also displayed.)*

---

## **🛠 How It Works**  

### **1️⃣ Deadlock Detection**  
- Builds a **Resource Allocation Graph (RAG)**
- Uses **cycle detection** to identify deadlocks

### **2️⃣ Safe State Checking**  
- Uses the **Banker’s Algorithm**  
- Tries to find a **safe sequence** of process execution  
- If a **safe sequence exists**, the system is safe ✅  
- If not, **deadlock exists** ❌  

### **3️⃣ Graph Visualization**  
- Uses **NetworkX & Matplotlib**  
- **Processes → Blue nodes**  
- **Resources → Red nodes**  
- **Edges show dependencies**  

---

## **📜 Code Structure**  

- **`DeadlockToolkit`**: Core class for deadlock detection  
- **`simulate_scenario()`**: Runs the entire deadlock detection process  
- **`is_safe_state()`**: Checks if system is in a safe state  
- **`detect_deadlock()`**: Detects cycles in RAG  
- **`visualize_graph()`**: Displays resource allocation graph  
- **`get_user_input()`**: Handles user input  

---

## **💡 Notes**  
- If **no safe sequence** is found → **Deadlock is present!**  
- **Graph visualization helps** in understanding the allocation & dependencies  
- Proper **input validation ensures** no incorrect data is entered  

---

## **📜 License**  
This project is **open-source**. Feel free to use, modify, and improve it. ⭐  

---

## **📬 Contributing**  
Found a bug? Have an improvement idea?  
- **Fork this repo**  
- **Make changes & test**  
- **Submit a Pull Request!** 🚀  

---
