import time
from pid_controller import PIDController
from imu_sensor import IMUSensor

class SelfBalancingRobot:
    def __init__(self):
        self.imu = IMUSensor()
        self.pid = PIDController(kp=1.2, ki=0.01, kd=0.5)
        self.setpoint = 0  # Upright position

    def balance(self):
        dt = 0.05
        while True:
            angle = self.imu.get_angle()
            correction = self.pid.compute(self.setpoint, angle, dt)
            self.apply_motor_torque(correction)
            print(f"Angle: {angle:.2f}, Correction: {correction:.2f}")
            time.sleep(dt)

    def apply_motor_torque(self, torque):
        # Send torque to motors (in Gazebo this would be via ROS topics)
        pass

if __name__ == "__main__":
    robot = SelfBalancingRobot()
    robot.balance()
