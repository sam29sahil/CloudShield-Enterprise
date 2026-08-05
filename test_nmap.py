from app.security.tools.network.nmap import NmapTool

print("1. Import successful")

tool = NmapTool()

print("2. Tool created")

print("Installed:", tool.installed())
print("Version:", tool.version())

print("3. Starting scan...")

result = tool.scan("127.0.0.1")

print("4. Scan finished")

print(result)