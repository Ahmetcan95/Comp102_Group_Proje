class Microcontroller:
    def check_device_status(self):
        print("[Microcontroller] cihaz durumu kontrol ediliyor...")
        return "Device is ON"



class Cloud:
    def __init__(self, microcontroller):
        self.microcontroller = microcontroller
    
    def send_signal_to_microcontroller(self):
        print("[Cloud] Mikrodenetleyici sinyal gönderilir.")
        return self.microcontroller.check_device_status()
    
    def receive_status(self,status):
        print(f"[Cloud] Durum alındı: {status}")
        return status



class Database:
    def __init__(self,cloud):
        self.cloud = cloud
        self.stored_status = None
    
    def forward_signal_to_cloud(self):
        print("[Database] sinyal buluta veritabanına iletildi.")
        status = self.cloud.send_signal_to_microcontroller()
        return self.cloud.receive_status(status)
    
    def store_status(self, status):
        self.stored_status = status
        print(f"[Database] Durum veritabanına kaydedildi: {status}")
       
       

class MobileApp:
    def __init__(self, database):
        self.database = database
        
    def user_login(self):
        print("[App] kullanıcı giriş yaptı.")
        self.send_signal_to_database("request_device_status")
        
    def send_signal_to_database(self,signal):
        print(f"[App] veritabanına sinyal gönderildi: {signal}")
        status = self.database.forward_signal_to_cloud()
        self.database.store_status(status)
        self.display_status_to_user(status)
        
    def display_status_to_user(self, status):
        print(f"[App] kullanıcıya cihaz durumu gösteriliyor: {status}")
    
    
# kullanım örneği
micro = Microcontroller()
cloud = Cloud(micro)
database = Database(cloud)
app = MobileApp(database)

# Simulate
app.user_login()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    