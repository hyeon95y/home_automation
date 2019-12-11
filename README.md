# home_automation




## Control other session via SSH in Windows10 OpenSSH server
- [Turn off Win10 display(s) via OpenSSH](https://superuser.com/questions/1382319/turn-off-win10-displays-via-openssh)
- At least this guy is trying to do the same thing with me
- Install PsTools and set environment variable

Turn off the screen (in the PATH)
```bash
FOR /F "usebackq tokens=4" %s IN (`tasklist /nh /fo table /fi "imagename eq explorer.exe"`) DO psexec -accepteula -nobanner -d -i %s -w "%windir%" powershell (Add-Type '[DllImport(\"user32.dll\")]^public static extern int SendMessage(int hWnd, int hMsg, int wParam, int lParam);' -Name a -Pas)::SendMessage(-1,0x0112,0xF170,2)
```

Turn off the screen (outside of PATH)
```bash
FOR /F "usebackq tokens=4" %s IN (`tasklist /nh /fo table /fi "imagename eq explorer.exe"`) DO C:\PSTools\psexec -accepteula -nobanner -d -i %s -w "%windir%" powershell (Add-Type '[DllImport(\"user32.dll\")]^public static extern int SendMessage(int hWnd, int hMsg, int wParam, int lParam);' -Name a -Pas)::SendMessage(-1,0x0112,0xF170,2)
```

Run Python Script
```bash
FOR /F "usebackq tokens=4" %s IN (`task
list /nh /fo table /fi "imagename eq explorer.exe"`) DO psexec -accepteula -nobanner -d -i %s -w "%wi
ndir%" C:\Users\Hyeonwoo\AppData\Local\Programs\Python\Python36\python.exe C:\Users\Hyeonwoo\Document
s\GitHub\home_automation\morning.py
```

Other commands
```
FOR /F "usebackq tokens=4" %s IN (`task
list /nh /fo table /fi "imagename eq explorer.exe"`) DO psexec -accepteula -nobanner -d -i %s -w "%wi
ndir%" command
```

**this works. yeaaaaaaaaah!**
