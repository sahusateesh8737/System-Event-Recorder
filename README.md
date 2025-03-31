Security Event Recorder
Overview
A Python-based security monitoring tool that tracks file system changes, login attempts, and system processes on Windows systems.

Features
Real-time file system monitoring
Windows Event Log tracking
Process creation/termination monitoring
GUI interface for event visualization
SQLite database for event storage
Statistical analysis and reporting
Prerequisites
Python 3.13 or higher
Windows Operating System
Administrator privileges




nstallation
1.Clone the Repository

git clone https://github.com/yourusername/SecurityEventRecorder.git
cd SecurityEventRecorder

2.Create Virtual Environment

python -m venv venv
.\venv\Scripts\activate

3.Install Dependencies

pip install -r requirements.txt


SecurityEventRecorder/
├── main.py
├── requirements.txt
├── README.md
├── modules/
│   ├── __init__.py
│   ├── capture.py
│   ├── analysis.py
│   └── ui.py
└── data/
    └── security_events.db



Module Details
1. Capture Module (modules/capture.py)
Handles system event monitoring through:

File system monitoring using watchdog
Windows Event Log monitoring via pywin32
Process monitoring using psutil
2. Analysis Module (modules/analysis.py)
Provides data analysis features:

Event pattern analysis
Statistical reporting
Data visualization
Threat detection
3. UI Module (modules/ui.py)
Implements the graphical interface:

Real-time event display
Event filtering
Control panel
Visual analytics


Usage
1.Run as Administrator

python main.py


2.Interface Controls
Create/Delete test files using buttons
Monitor real-time events in TreeView
Filter events by type
View statistical analysis
Database Schema

CREATE TABLE security_events (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    event_type TEXT,
    details TEXT
);



Dependencies

psutil>=5.9.8
pywin32>=306
watchdog>=3.0.0
pandas>=2.2.1
numpy>=1.26.4
python-dateutil>=2.8.2
matplotlib>=3.8.3



<------------------------------------------------------>
Troubleshooting
Common Issues
1.Permission Denied

Run VS Code as Administrator
Check Windows Security settings
2.Module Import Errors


pip install -r requirements.txt --upgrade

3.Event Log Access
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser




Contributing
1.Fork the repository
2.Create feature branch
3.Commit changes
4.Push to branch
5.Create Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Python community
Windows API documentation
Open source contributors
Version History
v1.0.0 - Initial release
Basic monitoring features
GUI implementation
Event logging system


Future Enhancements
Network traffic monitoring
Advanced threat detection
Remote monitoring capabilities
Cloud integration
Custom alert system
