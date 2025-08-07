#!/usr/bin/env python3
import time
import signal
import sys
import os

# Global flag to control the loop
running = True

def signal_handler(sig, frame):
    """Handle termination signals gracefully"""
    global running
    print(f"\n[!] Received signal {sig}. Shutting down keylogger...")
    running = False
    sys.exit(0)

def cleanup():
    """Cleanup function when exiting"""
    print("[+] Keylogger process terminated cleanly")

# Register signal handlers for graceful termination
signal.signal(signal.SIGTERM, signal_handler)  # Kill command
signal.signal(signal.SIGINT, signal_handler)   # Ctrl+C
signal.signal(signal.SIGQUIT, signal_handler)  # Quit signal

# Register cleanup function
import atexit
atexit.register(cleanup)

def main():
    global running
    
    print(f"[+] Starting keylogger with PID: {os.getpid()}")
    print("[+] Press Ctrl+C to stop or kill from another terminal")
    print("-" * 50)
    
    counter = 1
    try:
        while running:
            print(f"[{counter:04d}] Pretending to log keystrokes and intercept data...")
            time.sleep(5)  # Reduced sleep time for more activity
            counter += 1
            
            # Check if we should still be running
            if not running:
                break
                
    except KeyboardInterrupt:
        print("\n[!] KeyboardInterrupt received")
        running = False
    except Exception as e:
        print(f"[!] Error occurred: {e}")
        running = False
    finally:
        print("[+] Keylogger simulation stopped")

if __name__ == "__main__":
    main()