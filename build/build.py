import subprocess

cmd = [
    'python',
    '-m', 'PyInstaller',
    '../src/main.py',
    '--name', 'reptile',
    '--icon', '../favicon.ico',
    '--onefile',
    '--clean'
]
subprocess.call(cmd)
