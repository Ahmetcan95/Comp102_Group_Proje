class SmartDevice:
    def __init__(self, device_id, device_type, sensor_data):
        self.device_id = device_id
        self.device_type = device_type
        self.sensor_data = sensor_data
        
    def get_error_code(self):
        # Some error examples
        if self.sensor_data.get("temperature", 0) > 80:
            return "E01" # High temperature
        elif self.sensor_data.get("voltage", 0) < 180:
            return "E02" # High voltage
        else:
            return None
        
    def send_to_database(self,error_code):
        print(f"{self.device_id} - Hata kodu: {error_code} >>> veritabanına gönderildi.")

#fake devices
devices = [
    SmartDevice("fridge_01", "fridge",{"temperature":75, "voltage":220}),
    SmartDevice("washer_02", "washer",{"temperature":90, "voltage":220}),
    SmartDevice("vacuum_05", "vacuum",{"temperature":70, "voltage":170})
    ]

for device in devices:
    error= device.get_error_code()
    if error:
        device.send_to_database(error)
        
print("Taramalar tamamlandı")
    
    
    
    
    
    





        