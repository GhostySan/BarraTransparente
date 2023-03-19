import winreg
import subprocess

# Abrir la clave del registro
key_path = r'Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced'
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)

# Crear un nuevo valor DWORD con el nombre TaskbarAcrylicOpacity y valor 0
value_name = 'TaskbarAcrylicOpacity'
value_data = 0
winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, value_data)

# Cerrar la clave del registro
winreg.CloseKey(key)

# Reiniciar el explorador de archivos
subprocess.call(['taskkill', '/f', '/im', 'explorer.exe'])
subprocess.call(['explorer.exe'])
