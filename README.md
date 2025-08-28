# Self-Balancing-Two-Wheel-Robot-Program
## 📌 Objective
A simulated robot that balances itself like a **Segway** using **PID control**.

---

## 🛠 Tools & Technologies
- **ROS** (Robot Operating System)
- **Gazebo** (Simulation environment)
- **Python** (Control & PID implementation)

---

## ⚙️ Features
- PID control for **balancing** and movement  
- Simulated **IMU sensor fusion**  
- Basic **user-controlled navigation**  

---

## 🚀 How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/Starky-16/Self-Balancing-Two-Wheel-Robot-Program.git
   cd Self-Balancing-Two-Wheel-Robot-Program
##Install requirements:

bash
Copy code
pip install -r requirements.txt

##Launch simulation:
bash
Copy code
roslaunch launch/robot_sim.launch

##Run the control program:

bash
Copy code
python3 src/robot_control.py
