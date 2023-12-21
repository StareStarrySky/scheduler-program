import subprocess

cmd = [
    'python',
    '-m', 'PyInstaller',
    '../src/main.py',
    '--name', 'scheduler',
    '--icon', '../favicon.ico',
    '--onefile',
    '--clean'
]
subprocess.call(cmd)
