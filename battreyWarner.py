import psutil #pip install psutill in cmd if u did not installed it before 
from win10toast import ToastNotifier  # pip install win10toast in cmd for installing win10toast package 


while True:
    toaster = ToastNotifier()
    battery = psutil.sensors_battery()
    percent = str(battery.percent)
    plugged = battery.power_plugged
    print(percent)
    if plugged==False: plugged="Not Plugged In"
    else: plugged="Plugged In"
    if percent=="100":
        
        toaster.show_toast(percent+'% | '+plugged,"Fully Charged ",None,99999)
        
        break
    elif percent=="12":
        toaster.show_toast(percent+'% | '+plugged,"please Charge ",None,10000)
        break


"""
PLEASE CONTACT FOR ANY QUERIES :-
Vinay Kumar Gudi
+918146399973

vnaykumr0@gmail.com
vinay.11611373@lpu.in

@juniorAk47
#saveBattries

"""
