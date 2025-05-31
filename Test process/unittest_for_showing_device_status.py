import sys

from implementations_showing_device_status import Microcontroller, Cloud, Database, MobileApp

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    

micro = Microcontroller()
cloud = Cloud(micro)
database = Database(cloud)
app = MobileApp(database)

status = micro.check_device_status()
test(status == "Device is ON")

status_from_cloud = cloud.send_signal_to_microcontroller()
test(status_from_cloud == "Device is ON")

app.user_login()
test(database.stored_status == "Device is ON")
