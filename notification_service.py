import datetime
import winsound
import os
from plyer import notification
import numpy as np

class NotificationService:
    def __init__(self):
        self.log_file = "emergency_log.txt"
        
    def send_emergency_notifications(self, confidence_score):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Desktop notification
        notification.notify(
            title='⚠️ EMERGENCY - Scream Detected!',
            message=f'Confidence Score: {confidence_score:.2f}\nTime: {timestamp}',
            app_icon=None,
            timeout=10,
        )
        
        # Play alarm sound
        winsound.Beep(1000, 1000)  # frequency=1000Hz, duration=1000ms
        
        # Console output
        alert_message = f"\n{'!'*50}\nSCREAM DETECTED at {timestamp}\nConfidence: {confidence_score:.2f}\n{'!'*50}\n"
        print(alert_message)
        
        # Log to file
        try:
            with open(self.log_file, "a") as f:
                f.write(alert_message)
        except Exception as e:
            print(f"Failed to write to log file: {str(e)}")