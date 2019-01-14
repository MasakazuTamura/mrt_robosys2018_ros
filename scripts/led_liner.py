#!/usr/bin/env python
import sys, rospy
from std_msgs.msg import Int16, Bool

class Led_Liner:
    def __init__(self):
        self.devfile = "/dev/myled0"
        self.subint = rospy.Subscriber("key_command", Int16, _int_callback)
        self.subbool = rospy.Subscriber("key_console", Bool, _bool_callback)

        self.pos = 0.0
        self.vel = 1
        self.direction = 1
        self.done = True
        self.flash = False

    def _write_devfile(self, input_str):
        with open(self.devfile, mode="w") as dev:
            dev.write(str(input_str)) + "\n")

    def _int_callback(self, msg):
        self.key_cmd = msg.data
        if self.key_cmd == 0:
            if not self.vel == 0:
                self.vel += self.direction
        elif self.key_cmd == 1:
            if not self.vel == 0:
                self.vel -= self.direction
        elif self.key_cmd == 2:
            if not self.vel == 0:
                self.vel = abs(self.vel)
            else:
                self.vel = 1
        elif self.key_cmd == 3:
            if not self.vel == 0:
                self.vel = abs(self.vel) * -1
            else:
                self.vel = -1

    def _bool_callback(self, msg):
        self.key_con = msg.data
        if self.done == self.key_con:
            self.key_con = self.key_con

    def _action():
        if self.done == True:
            self.pos += self.vel * 0.1
            if self.pos > 8.0:
                self.pos -= 8.0
            elif self.pos < 0.0:
                self.pos += 8.0
            self.senddevfile = str(round(self.pos))
        else:
            if self.flash = True:
                self.senddevfile = "A"
                self.flash = False

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self._action()
            self._write_devfile(self.senddevfile)
            rate.sleep()

if __name__ == "__main__":
    rospy.init_node("led_liner")
    led = Led_Liner()
    led.run()
