import sqlite3
from modules.capture import DB_PATH

def analyze_logs():
    """Analyze logs and return a summary of events."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Count events by type
    cursor.execute("SELECT event_type, COUNT(*) as count FROM logs GROUP BY event_type")
    event_counts = cursor.fetchall()
    
    # Get recent suspicious events (example: app opens with unusual cmdline)
    cursor.execute("SELECT timestamp, details FROM logs WHERE event_type = 'App Opened' AND details LIKE '%cmd.exe%' LIMIT 5")
    suspicious_events = cursor.fetchall()
    
    conn.close()
    
    summary = "Event Summary:\n"
    for event_type, count in event_counts:
        summary += f"{event_type}: {count} occurrences\n"
    
    summary += "\nRecent Suspicious Events (cmd.exe related):\n"
    for timestamp, details in suspicious_events:
        summary += f"{timestamp} - {details}\n"
    
    return summary

def print_analysis():
    print(analyze_logs())