import subprocess

print("--- Command Output ---")
result = subprocess.run('dir', shell=True, capture_output=True, text=True, check=True)
    
print(result.stdout)