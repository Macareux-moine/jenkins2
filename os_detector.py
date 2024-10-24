import platform
import os
import subprocess
def obtenir_sys_info():
os_info = platform.uname()
type_systeme = os_info.system
node_name = os_info.node
release = os_info.release
version = os_info.version
machine = os_info.machine
processor = os_info.processor
system_info = {
'System Type': type_systeme,
'Node Name': node_name,
'Release': release,
'Version': version,
'Machine': machine,
'Processor': processor
}
return system_info
def get_windows_hardware_info():
try:
cpu_info = subprocess.check_output("wmic cpu get
name", shell=True).decode().strip().split('\n')[1].strip()
mem_info = subprocess.check_output("wmic memorychip
get capacity", shell=True).decode().strip().split('\n')[1:]
total_memory = sum(int(mem.strip()) for mem in
mem_info) / (1024**3) # Convertis les octets en Go
except Exception as e:
cpu_info = "Impossible d'obtenir les informations
CPU"
total_memory = "Impossible d'obtenir les
informations Mémoire vive"
