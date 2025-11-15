import subprocess
import json
import sys

def test_mcp_server():
    try:
        # Start the MCP server
        process = subprocess.Popen(
            [sys.executable, "weather.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd="e:\\mcp_server\\weather"
        )
        
        # Send initialize request
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test-client", "version": "1.0.0"}
            }
        }
        
        # Send the request
        request_str = json.dumps(init_request) + "\n"
        stdout, stderr = process.communicate(input=request_str, timeout=10)
        
        print("STDOUT:", stdout)
        print("STDERR:", stderr)
        print("Return code:", process.returncode)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_mcp_server()