#!/usr/bin/env python
import sys,tty,termios
import rospy
from std_msgs.msg import Int16, Bool

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
#            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get1():
    inkey = _Getch()

    k = inkey()
    # ^[A, ^[B, ^[C, or ^[D
    if k == "\x1b":
        for i in range(0, 2):
            k += inkey()
        if k == "\x1b[A":
            print("up")
            key_num = 0
        elif k == "\x1b[B":
            print("down")
            key_num = 1
        elif k == "\x1b[C":
            print("right")
            key_num = 2
        elif k == "\x1b[D":
            print("left")
            key_num = 3
        else:
            print(k)
            key_num = -1
    # ^C
    elif k == "\x03":
        print("ctrl+c key down")
        key_num = -1
    # ^R
    elif k == "\x12":
        print("ctrl+r key down")
        key_num = -1
    # ^S
    elif k == "\x13":
        print("ctrl+s key down")
        key_num = -1
    else:
        print("unknown command")
        print("note: arrow key only")
        key_num = -1
    return k, key_num

if __name__ == '__main__':
    rospy.init_node("key_input")
    pubint = rospy.Publisher("key_command", Int16, queue_size=1)
    pubbool = rospy.Publisher("key_console", Bool, queue_size=1)

    rate = rospy.Rate(10)
    key_cmd = Int16()
    key_con = Bool()
    while not rospy.is_shutdown():
        keyevent, key_cmd.data = get1()
        # ^C
        if keyevent == "\x03":
            rospy.signal_shutdown("ctrl+c")
        # ^R
        elif keyevent == "\x12":
            key_con = True
            pubbool.publish(key_con)
        # ^S
        elif keyevent == "\x13":
            key_con = False
            pubbool.publish(key_con)
        # ^[A, ^[B, ^[C, or ^[D
        elif not key_cmd.data < 0:
            pubint.publish(key_cmd)

        rate.sleep()

