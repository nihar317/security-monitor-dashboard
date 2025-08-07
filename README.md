# Security Monitor Dashboard

**Real-time Process Monitoring & Threat Detection System**

---

## Project Overview

A sophisticated security monitoring dashboard built with Flask that provides real-time detection of suspicious processes, keyloggers, and potential security threats. Features a modern web interface with comprehensive threat analysis capabilities.

### Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Data Layer    │────│  Analysis Layer  │────│ Interface Layer │
│                 │    │                  │    │                 │
│ • Process Data  │    │ • Real-time Scan │    │ • Web Dashboard │
│ • Safe Registry │    │ • Classification │    │ • Terminal UI   │
│ • Threat Sigs   │    │ • Pattern Match  │    │ • Real-time WS  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

## Quick Start Guide

### Prerequisites
- Python 3.11
- Web Browser
- Administrative privileges (optional)

### Installation & Setup

```bash
# 1. Clone or create project directory
git clone https://github.com/nihar317/security-monitor-dashboard/
cd security-monitor-dashboard

# 2. Create virtual environment
python -m venv monitor_env

# 3. Activate environment
# Windows:
monitor_env\Scripts\activate
# Linux/Mac:
source monitor_env/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python monitor_snooping_web.py
```

### Access Dashboard
Open browser to: **http://localhost:5000**

---

## Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Backend** | Python 3.8+ | Core application logic |
| **Web Framework** | Flask | HTTP server & routing |
| **Real-time** | Socket.IO | WebSocket communication |
| **System Monitoring** | psutil | Process & system data |
| **Frontend** | HTML5/CSS3/JS | User interface |
| **Data Format** | JSON | API communication |
| **Styling** | CSS Variables | Theme system |

---

## Project Structure

```
security-monitor-dashboard/
├── monitor_snooping_web.py     # Main Flask application
├── test_keylogger.py           # Threat simulation tool
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git exclusions
├── README.md                   # Project documentation
└── templates/
    └── dashboard.html          # Web interface template
```

---

## Feature Matrix

| Feature | Status | Description |
|---------|--------|-------------|
| **Real-time Monitoring** | Active | Scans processes every 10 seconds |
| **Threat Classification** | Active | High/Medium/Low priority system |
| **Web Dashboard** | Active | Modern responsive interface |
| **Theme Support** | Active | Dark/Light mode toggle |
| **Process Termination** | Active | Kill suspicious processes |
| **Terminal Integration** | Active | Dual interface support |
| **Documentation** | Active | Built-in FAQ & manual |
| **Mobile Responsive** | Active | Works on all devices |

---

## Threat Detection Logic

### Classification System

```python
THREAT_PRIORITIES = {
    "HIGH": {
        "triggers": ["keylog", "logger", "intercept", "keystroke"],
        "risk": "Direct data theft",
        "action": "Immediate attention required"
    },
    "MEDIUM": {
        "triggers": ["mic", "audio", "bluetooth", "camera"],
        "risk": "Hardware surveillance",
        "action": "Monitor regularly"
    },
    "LOW": {
        "triggers": ["system", "kernel", "service"],
        "risk": "Normal operations",
        "action": "Routine monitoring"
    }
}
```

### Detection Workflow

1. **Process Enumeration** → List all active processes
2. **Safe List Filtering** → Exclude whitelisted processes  
3. **Pattern Matching** → Check against threat signatures
4. **Priority Assignment** → Classify by risk level
5. **Real-time Update** → Push to dashboard via WebSocket

---

## Interface Components

### Navigation Structure
```
├── Dashboard (Main monitoring interface)
├── User Manual (System documentation)
└── FAQ (Troubleshooting guide)
```

### Dashboard Elements
- **Statistics Cards**: Real-time threat counters
- **Process Table**: Detailed threat information
- **Control Panel**: Start/Stop monitoring
- **Theme Toggle**: Dark/Light mode switch

---

## Configuration Options

### Command Line Arguments
```bash
python monitor_snooping_web.py [OPTIONS]

Options:
  --port INTEGER     Port number (default: 5000)
  --strict          Enable strict mode with kill prompts
  --help            Show help message
```

### Safe Processes Configuration
Create `safe_processes.txt` to exclude known safe processes:
```
systemd
NetworkManager
pulseaudio
gnome-session
chrome.exe
```

---

## Testing & Development

### Test Threat Simulation
```bash
# Run in separate terminal
python test_keylogger.py

# This creates a fake keylogger process that will be detected
```

### Development Mode
```bash
# Enable Flask debug mode
export FLASK_DEBUG=1
python monitor_snooping_web.py
```

### API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Serve main dashboard |
| `/start_monitoring` | POST | Begin threat scanning |
| `/stop_monitoring` | POST | Stop threat scanning |
| `/kill_process` | POST | Terminate specific process |

---

## Performance Metrics

### System Requirements
- **Memory**: ~50MB base + process data
- **CPU**: <5% during scanning
- **Disk**: ~10MB installation
- **Network**: Minimal (local WebSocket only)

### Scan Performance
- **Process Enumeration**: ~100ms
- **Pattern Matching**: ~50ms per process
- **Dashboard Update**: ~10ms
- **Total Cycle**: ~1-2 seconds

---

## Troubleshooting Guide

### Common Issues

#### "No module named 'psutil'"
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

#### "Port 5000 already in use"
```bash
# Solution: Use different port
python monitor_snooping_web.py --port 8080
```

#### "No threats detected"
```bash
# Solution: Run test keylogger
python test_keylogger.py
```

#### "Dashboard won't load"
```bash
# Check if server is running
netstat -an | findstr :5000

# Restart with debug mode
set FLASK_DEBUG=1
python monitor_snooping_web.py
```

---

## Security Considerations

### Permissions
- **Process Enumeration**: Usually requires admin privileges
- **Process Termination**: Requires elevated permissions
- **Safe Mode**: Run without admin for read-only monitoring

### Data Privacy
- **Local Only**: No external network connections
- **No Data Storage**: Information not persisted
- **Real-time Only**: Data exists only during active session

---

## Contributing

### Development Workflow
1. **Fork** the repository
2. **Create** feature branch: `git checkout -b feature-name`
3. **Implement** changes with tests
4. **Commit** with clear messages
5. **Submit** pull request

### Code Style
- **Python**: PEP 8 compliance
- **JavaScript**: ES6+ standards
- **CSS**: BEM methodology
- **Documentation**: Markdown format

---

## Future Enhancements

### Planned Features
- [ ] **Historical Logging** - Store threat detection history
- [ ] **Email Alerts** - Notification system for critical threats
- [ ] **Machine Learning** - AI-based anomaly detection
- [ ] **Network Monitoring** - Track network connections
- [ ] **Plugin System** - Extensible detection modules
- [ ] **Multi-user Support** - Role-based access control

---

## Acknowledgments

### Technologies Used
- **Flask** - Python web framework
- **Socket.IO** - Real-time communication
- **psutil** - System monitoring
- **CSS Grid/Flexbox** - Responsive layouts

### Inspiration
- Security best practices from NIST Framework
- Modern web application design patterns
- Real-time monitoring methodologies

---

### Getting Help
1. **Check FAQ** - Built into dashboard interface
2. **Review Documentation** - User manual in dashboard  
3. **Test Environment** - Use test_keylogger.py for validation
4. **Issue Tracking** - GitHub issues for bug reports

### Version Information
- **Current Version**: 1.0.0
- **Python Support**: 3.8+
- **Last Updated**: 2024
- **Compatibility**: Windows, Linux, macOS

---
