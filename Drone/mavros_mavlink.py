import rospy
import time
from mavros_msgs.srv import CommandLong
from mavros_msgs.srv import ParamGet
from mavros_msgs.msg import State
from pymavlink.dialects.v20 import common as mavlink

send_command_long = rospy.ServiceProxy('/mavros/cmd/command', CommandLong)
get_param = rospy.ServiceProxy('/mavros/param/get', ParamGet)
system_status = -1
heartbeat_sub = None
heartbeat_sub_status = None

def state_callback(data):
    global system_status
    system_status = data.system_status

def check_state_topic():
    global system_status, heartbeat_sub, heartbeat_sub_status
    # Check subscriber
    if (not heartbeat_sub) or (not heartbeat_sub_status):
        rospy.loginfo('Not subscribed to topic')
        return False
    # Wait for heartbeat
    start_time = time.time()
    while system_status == -1:
        if time.time() - start_time > 3.:
            rospy.loginfo("Not connected to fcu. Check connection.")
            return False
        rospy.sleep(0.1)
    # print(system_status)
    return True

def reboot_fcu():
    if check_state_topic():
        rospy.loginfo("Send reboot message to fcu")
        send_command_long(False, mavlink.MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN, 0, 1, 0, 0, 0, 0, 0, 0)
        return True
    return False

def calibration_msg(sensor):
    mavlink_message = [0,0,0,0,0,0,0]
    index, value = {
        'gyro': (0,1),
        'level':(4,2)
    }.get(sensor, (0,0))
    mavlink_message[index]=value
    return mavlink_message

def calibrate(sensor):
    global system_status
    if check_state_topic():
        # Check system_status
        if system_status > mavlink.MAV_STATE_STANDBY:
            rospy.loginfo("System status is incorrect for calibration")
            return False
        # Make calibration message
        calibration_message = calibration_msg(sensor)
        # Send mavlink calibration command 
        send_command_long(False, mavlink.MAV_CMD_PREFLIGHT_CALIBRATION, 0, *calibration_message)
        rospy.loginfo('Send {} calibration message'.format(sensor))
        # Wait until system status to uninit (during calibration on px4)
        while system_status != mavlink.MAV_STATE_UNINIT:
            rospy.sleep(0.1)
        rospy.loginfo("Start {} calibration. Please, don't move the drone!".format(sensor))
        # Wait until the end of the calibration
        while system_status != mavlink.MAV_STATE_STANDBY:
            rospy.sleep(0.1)
        rospy.loginfo("Calibration is finished!")
        return True
    return False

def get_calibration_status():
    gyro_status = get_param('CAL_GYRO0_ID')
    mag_status = get_param('CAL_MAG0_ID')
    acc_status = get_param('CAL_ACC0_ID')
    status_text = ""
    if gyro_status.success == False:
        status_text += "gyro: wrong_param; "
    elif gyro_status.value.integer == 0:
        status_text += "gyro: uncalibrated; "
    if mag_status.success == False:
        status_text += "mag: wrong_param; "
    elif mag_status.value.integer == 0:
        status_text += "mag: uncalibrated; "
    if acc_status.success == False:
        status_text += "acc: wrong_param; "
    elif acc_status.value.integer == 0:
        status_text += "acc: uncalibrated; "    
    if status_text == "":
        status_text = "OK"
    else:
        status_text = status_text[:-2]
    return status_text

def get_sys_status():
    global system_status
    if check_state_topic():
        status_text = {
            mavlink.MAV_STATE_UNINIT: "MAV_STATE_UNINIT",
            mavlink.MAV_STATE_BOOT: "MAV_STATE_BOOT",
            mavlink.MAV_STATE_CALIBRATING: "MAV_STATE_CALIBRATING",
            mavlink.MAV_STATE_STANDBY: "MAV_STATE_STANDBY",
            mavlink.MAV_STATE_ACTIVE: "MAV_STATE_ACTIVE",
            mavlink.MAV_STATE_CRITICAL: "MAV_STATE_CRITICAL",
            mavlink.MAV_STATE_EMERGENCY: "MAV_STATE_EMERGENCY",
            mavlink.MAV_STATE_POWEROFF: "MAV_STATE_POWEROFF",
            mavlink.MAV_STATE_FLIGHT_TERMINATION: "MAV_STATE_FLIGHT_TERMINATION"
        }.get(system_status, "NOT_CONNECTED_TO_FCU")
        return status_text
    return "NOT_CONNECTED_TO_FCU"

def start_subscriber():
    global heartbeat_sub, heartbeat_sub_status
    heartbeat_sub = rospy.Subscriber('/mavros/state', State, state_callback)
    heartbeat_sub_status = True
    # print(not heartbeat_sub)
    # print(not heartbeat_sub_status)

def stop_subscriber():
    global heartbeat_sub, heartbeat_sub_status
    if heartbeat_sub:
        heartbeat_sub.unregister()
        heartbeat_sub_status = False

