EMERGENCY_CONTACTS = {
    "local_alert": {
        "sound_duration": 3,  # seconds
        "alert_sound_frequency": 1000,  # Hz
        "volume": 0.8  # 0.0 to 1.0
    },
    "logging": {
        "log_file": "emergency_log.txt",
        "save_recordings": True
    }
}

# Twilio credentials
TWILIO_ACCOUNT_SID = "your sid number"
TWILIO_AUTH_TOKEN = "your auth token"
TWILIO_PHONE_NUMBER = "your_twilio_phone"

# Email configuration
EMAIL_SENDER = "your_email@example.com"
EMAIL_PASSWORD = "your_app_specific_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587