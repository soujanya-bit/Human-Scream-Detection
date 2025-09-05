from audio_processor import AudioProcessor
from scream_detector import ScreamDetector
from ml_detector import MLScreamDetector
import time
import numpy as np
from colorama import init, Fore, Back
import datetime
import wave
import os

def display_meter(value, threshold=0.85):
    bars = int(value * 20)
    meter = '█' * bars + '░' * (20 - bars)
    color = Fore.GREEN if value < threshold else Fore.RED
    return f"{color}{meter} {value:.2f}{Fore.RESET}"

def save_detection_event(audio_data, sample_rate, ml_confidence, energy_level):
    # Create directories if they don't exist
    os.makedirs("detections/audio", exist_ok=True)
    os.makedirs("detections/logs", exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save audio file
    audio_path = f"detections/audio/scream_{timestamp}.wav"
    with wave.open(audio_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())
    
    # Log detection details
    log_path = "detections/logs/detection_log.txt"
    with open(log_path, 'a') as f:
        f.write(f"\nDetection at {timestamp}")
        f.write(f"\nML Confidence: {ml_confidence:.2f}")
        f.write(f"\nEnergy Level: {energy_level:.2f}")
        f.write("\n" + "-"*50)

def main():
    init()  # Initialize colorama
    audio_processor = AudioProcessor()
    traditional_detector = ScreamDetector()
    ml_detector = MLScreamDetector()
    
    print("Loading trained model...")
    ml_detector.load_model()
    print("Starting enhanced scream detection system...")
    print("\nPress Ctrl+C to stop monitoring")
    
    try:
        while True:
            print("\033[H\033[J")  # Clear screen
            print("🎤 Monitoring Audio...")
            audio_data = audio_processor.record_audio(duration=3)
            
            traditional_result, traditional_energy = traditional_detector.detect_scream(
                audio_data, 
                audio_processor.rate
            )
            
            ml_result, ml_confidence = ml_detector.predict(
                audio_data, 
                audio_processor.rate
            )
            
            print("\nDetection Levels:")
            print(f"ML Confidence:    {display_meter(ml_confidence)}")
            print(f"Energy Level:     {display_meter(traditional_energy)}")
            
            if traditional_result and ml_result:
                print(f"\n{Back.RED}⚠️ SCREAM DETECTED!{Back.RESET}")
                save_detection_event(audio_data, audio_processor.rate, ml_confidence, traditional_energy)
                print("\nDetection saved!")
            
            time.sleep(0.5)
    
    except KeyboardInterrupt:
        print("\nStopping scream detection system...")

if __name__ == "__main__":
    main()