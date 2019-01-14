#!/usr/bin/env python
import sys, rospy
from std_msgs.msg import Int16, Bool

class Led_Liner:
    def __init__(self):
        self.devfile = "/dev/myled0"
        self.subint = rospy.Subscriber("key_command", Int16, self._int_callback)
        self.subbool = rospy.Subscriber("key_console", Bool, self._bool_callback)

        self.flash = False
        self.senddevfile = "N\n"
        self.key_cmd = "0"
        self.key_con = True

    def _write_devfile(self, input_str):
        with open(self.devfile, mode="w") as dev:
            dev.write(str(input_str) + "\n")

    def _int_callback(self, msg):
        self.key_cmd = msg.data

    def _bool_callback(self, msg):
        self.key_con = msg.data

    def _action(self):
        if self.key_con:
            self.flash = True
            self.senddevfile = str(self.key_cmd) + "\n"
        else:
            if self.flash:
                self.senddevfile = "A\n"
                self.flash = False
            else:
                self.senddevfile = "4\n"

    def run(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            self._action()
            self._write_devfile(self.senddevfile)
            rate.sleep()

if __name__ == "__main__":
    rospy.init_node("led_liner")
    led = Led_Liner()
    led.run()
