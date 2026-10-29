"""
One-click Python Dashboard Launcher
Finds an available local port, starts a lightweight server, and automatically opens the browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

def launch():
    dashboard_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dashboard')
    os.chdir(dashboard_dir)
    
    # Try finding an open port starting from 5500
    handler = http.server.SimpleHTTPRequestHandler
    server = None
    port_to_use = None
    
    for port in [5500, 5000, 8000, 8888, 3000, 8081]:
        try:
            server = socketserver.TCPServer(("", port), handler)
            port_to_use = port
            break
        except Exception:
            continue
            
    if not server:
        # Fallback to direct file opening in default browser
        print("Starting direct file in browser...")
        index_file = os.path.join(dashboard_dir, 'index.html')
        webbrowser.open(f'file:///{index_file}')
        return

    url = f"http://localhost:{port_to_use}"
    print("=" * 60)
    print(f"Marketing Funnel Dashboard is live at: {url}")
    print("Opening browser automatically...")
    print("Press Ctrl+C to stop the dashboard server.")
    print("=" * 60)
    
    webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDashboard server stopped.")

if __name__ == '__main__':
    launch()
