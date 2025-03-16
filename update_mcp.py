#!/usr/bin/env python3
"""
Script to restart the MCP server with our changes.
"""
import os
import signal
import subprocess
import time
import sys

def main():
    # Kill any existing MCP server
    try:
        subprocess.run("pkill -f main.py", shell=True)
        print("Killed existing MCP server")
    except Exception as e:
        print(f"Error killing MCP server: {e}")
    
    # Wait a moment for the process to terminate
    time.sleep(1)
    
    # Start the MCP server
    try:
        process = subprocess.Popen(["python", "main.py"])
        print(f"Started MCP server with PID {process.pid}")
        print("MCP server is now running with the updated code")
    except Exception as e:
        print(f"Error starting MCP server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 