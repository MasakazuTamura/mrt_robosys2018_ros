#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

class Callback:
    def __init__(self):
        self._pub = rospy.Publisher("twice", Int32, queue_size=1)

    def callback(self, message):
        data = message.data * 2
        self._pub.publish(data)

if __name__ == "__main__":
    rospy.init_node("twice")
    cb = Callback()
    sub = rospy.Subscriber("count_up", Int32, cb.callback)
    rospy.spin()
