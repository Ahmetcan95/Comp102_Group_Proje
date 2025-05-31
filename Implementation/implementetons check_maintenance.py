import time as t
class Methods:

    maintenance_counter = 0

    @classmethod
    def update_monthly(update):

        t.sleep(30 * 24 * 60 * 60)
        update.maintenance_counter += 1
    
    @classmethod
    def get_current_maintenance(value):
         
         return value.maintenance_counter
    
    @staticmethod
    def send_notification_to_app(value):
        print("sending notification to app...")
        t.sleep(5)
        print(value)
    
for i in range(6):
    Methods.update_monthly()

maintenance_counter = Methods.get_current_maintenance()

if maintenance_counter >= 6:
    message = "maintenance time has been reached please see a service"
    Methods.send_notification_to_app(message)
    print("User notified")
else:
    print("No maintenance needed")    
         