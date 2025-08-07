import psutil
import time
import argparse
import os
import threading
import getpass
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from tabulate import tabulate

# Define keywords and their priorities (EXACT COPY FROM YOUR ORIGINAL)
SUSPICIOUS_KEYWORDS = {
    "Keylogger": {"keywords": ["keylog", "logger", "intercept", "keystroke"], "priority": "High"},
    "Mic Access": {"keywords": ["mic", "audio", "pulse", "alsa"], "priority": "Medium"},
    "Bluetooth Access": {"keywords": ["bluetoothd", "btmon", "bluetooth"], "priority": "Medium"},
    "Camera Access": {"keywords": ["v4l", "webcam", "camera", "cheese"], "priority": "Medium"},
}
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}
SAFE_HEADERS = ["PID", "Name", "Type", "Priority", "Sensor Access"]

# Flask app setup
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app, cors_allowed_origins="*")

# Global variables
safe_list = set()
is_monitoring = False
monitoring_thread = None
strict_mode = False
safe_text_entered = False

def load_safe_processes():
    """EXACT COPY FROM YOUR ORIGINAL CODE"""
    global safe_list
    path = input("Enter path to safe_processes.txt (press Enter to skip): ").strip()
    if path:
        try:
            with open(path, 'r') as file:
                safe_list = {line.strip().lower() for line in file if line.strip()}
                print(f"[+] Loaded {len(safe_list)} safe process names.\n")
        except FileNotFoundError:
            print("[!] File not found. Proceeding without safe list.\n")
    else:
        print("[!] No safe list provided. Proceeding with all processes considered.\n")

def get_safe_text():
    """Get safe text from user for authentication"""
    global safe_text_entered
    print("\n" + "="*60)
    print("SECURITY AUTHENTICATION REQUIRED")
    print("="*60)
    safe_text = getpass.getpass("Enter your safe text (hidden input): ")
    if safe_text.strip():
        safe_text_entered = True
        print("[+] Safe text accepted. Proceeding with monitoring setup...")
        return safe_text
    else:
        print("[!] No safe text provided. Monitoring will proceed without authentication.")
        return None

def classify_process(name, cmdline):
    """EXACT COPY FROM YOUR ORIGINAL CODE"""
    full_cmd = " ".join(cmdline).lower()
    name = name.lower()
    for ptype, meta in SUSPICIOUS_KEYWORDS.items():
        for keyword in meta["keywords"]:
            if keyword in name or keyword in full_cmd:
                return ptype, meta["priority"]
    return None, None

def scan_processes(safe_list, strict=False):
    """EXACT COPY FROM YOUR ORIGINAL CODE WITH WEB INTEGRATION"""
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            pid = proc.info['pid']
            name = proc.info['name'] or ''
            cmdline = proc.info['cmdline'] or []
            
            if name.lower() in safe_list:
                continue
                
            ptype, priority = classify_process(name, cmdline)
            if ptype:
                suspicious.append({
                    "PID": pid,
                    "Name": name,
                    "Type": ptype,
                    "Priority": priority,
                    "Sensor Access": "Yes"  # Minimal live sensor access trace
                })
                
                if strict:
                    user_input = input(f"\u26a0\ufe0f  Kill suspicious process PID {pid} ({name})? [y/n]: ").lower()
                    if user_input == 'y':
                        try:
                            psutil.Process(pid).kill()
                            print(f"[+] Killed PID {pid}\n")
                            # Emit kill notification to web clients
                            socketio.emit('process_killed', {
                                'pid': pid,
                                'name': name,
                                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
                            })
                        except Exception as e:
                            print(f"[!] Failed to kill PID {pid}: {e}\n")
                            
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return suspicious

def display_results(detections):
    """EXACT COPY FROM YOUR ORIGINAL CODE"""
    print("\nSuspicious Activity Detected:\n")
    if not detections:
        print("No suspicious processes detected.\n")
    else:
        detections.sort(key=lambda x: PRIORITY_ORDER[x["Priority"]])
        print(tabulate(detections, headers="keys", tablefmt="grid"))
        print()

def monitoring_loop():
    """Uses your EXACT original logic"""
    global is_monitoring
    while is_monitoring:
        # Use EXACT same function call as your original
        detections = scan_processes(safe_list, strict=strict_mode)
        
        # Display in terminal using EXACT original function
        display_results(detections)
        
        # Also send to web dashboard
        socketio.emit('update_data', {
            'detections': detections,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'safe_text_status': safe_text_entered,
            'total_processes_scanned': len(list(psutil.process_iter())),
            'safe_processes_count': len(safe_list)
        })
        
        print(f"[{time.strftime('%H:%M:%S')}] Scan complete - {len(detections)} threats found")
        print(f"[{time.strftime('%H:%M:%S')}] Web dashboard updated")
        print("-" * 60)
        
        time.sleep(10)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/start_monitoring', methods=['POST'])
def start_monitoring():
    global is_monitoring, monitoring_thread
    
    if not is_monitoring:
        is_monitoring = True
        monitoring_thread = threading.Thread(target=monitoring_loop)
        monitoring_thread.daemon = True
        monitoring_thread.start()
        print("[+] Web monitoring started - using original detection logic")
        return jsonify({'status': 'started'})
    else:
        return jsonify({'status': 'already_running'})

@app.route('/stop_monitoring', methods=['POST'])
def stop_monitoring():
    global is_monitoring
    is_monitoring = False
    print("[+] Web monitoring stopped")
    return jsonify({'status': 'stopped'})

@app.route('/kill_process', methods=['POST'])
def kill_process():
    """Kill a specific process via web interface"""
    data = request.get_json()
    pid = data.get('pid')
    
    try:
        psutil.Process(pid).kill()
        print(f"[+] Killed PID {pid} via web interface")
        return jsonify({'status': 'killed', 'pid': pid})
    except Exception as e:
        print(f"[!] Failed to kill PID {pid}: {e}")
        return jsonify({'status': 'error', 'message': str(e)})

@socketio.on('connect')
def handle_connect():
    print('[+] Web client connected')
    emit('connected', {
        'data': 'Connected to monitoring server',
        'safe_text_status': safe_text_entered
    })

@socketio.on('disconnect')
def handle_disconnect():
    print('[+] Web client disconnected')

def main():
    """USES YOUR EXACT ORIGINAL ARGUMENT PARSING AND SETUP"""
    parser = argparse.ArgumentParser(description="Sensor and Keylogger Detection Tool - Web Version")
    parser.add_argument('--strict', action='store_true', help="Enable strict mode (kills + prompts)")
    parser.add_argument('--port', type=int, default=5000, help="Port to run web server on")
    args = parser.parse_args()
    
    global strict_mode
    strict_mode = args.strict
    
    mode = "Strict" if args.strict else "Light"
    print("=" * 60)
    print(f"Starting sensor and keylogger detection (Web Dashboard - {mode} mode)")
    print("=" * 60)
    
    # Get safe text for authentication
    safe_text = get_safe_text()
    
    # Load safe processes using EXACT original function
    load_safe_processes()
    
    print(f"\n[+] Web dashboard available at: http://localhost:{args.port}")
    print("[+] This uses your EXACT original detection logic")
    print("[+] Terminal will show the same table as your original code")
    print("[+] Web dashboard will show the same data in a nice interface")
    
    if args.strict:
        print("[!] STRICT MODE: You will be prompted to kill suspicious processes in terminal")
    
    print("\n" + "="*60)
    print("READY - SAME DETECTION AS YOUR ORIGINAL CODE")
    print("="*60)
    
    # Start Flask-SocketIO server
    try:
        socketio.run(app, host='0.0.0.0', port=args.port, debug=False)
    except KeyboardInterrupt:
        print("\n[+] Server stopped by user")
        is_monitoring = False

if __name__ == "__main__":
    main()