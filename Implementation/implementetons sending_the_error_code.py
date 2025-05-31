class Methods:

    def __init__(self,code,device):

        self.code = code
        self.device = device
        

    @staticmethod
    def get_error_from_database():
        
        error_code = " "
        print("The error code has been get from database")
        return error_code
    
    def send_via_Wİ_FI(massage):
    
         message_sent = print("sending via WI-FI: ", message)
         return message_sent
    
    check_sent = lambda: True

error_data = Methods.get_error_from_database()

if error_data != None:
    
    device = error_data.device
    code = error_data.code
    message = print(f"The error code{code} has been send {device}")
    Methods.send_via_Wİ_FI(message)
if Methods.check_sent == True:
    print("The message has been sent successfully")
elif Methods.check_sent == False:
    print("message failed to sent")

else:
    print("message failed to found in database")
    


         