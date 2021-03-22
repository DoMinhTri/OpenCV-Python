
import jetbot_driver.robot as jetbot
import  time

robot = jetbot.JetRobot()
robot.left(0.3)

while True:
    time.sleep(2)
    robot.stop()