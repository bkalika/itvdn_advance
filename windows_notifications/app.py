from win10toast import ToastNotifier
import time

# One-time initialization
toaster = ToastNotifier()

# Show notification whenever needed
toaster.show_toast("Notification! From Bohdan Kalika", "Hello, have a good day!",
                   threaded=True, icon_path=None, duration=5)


while toaster.notification_active():
    time.sleep(0.1)
