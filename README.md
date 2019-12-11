# home_automation


## Troubleshooting
Still working on making system to automate several stuffs. 


## Problem. But solution? Not sure
- [How can I export DISPLAY from a Linux terminal to a Windows PC?](https://superuser.com/questions/325630/how-can-i-export-display-from-a-linux-terminal-to-a-windows-pc)
- [Open a window in a remote machine](https://askubuntu.com/questions/405916/open-a-window-in-a-remote-machine)
- The original problem was, when I access via SSH, what I'm controlling is not actually the Windows that I'm looking at.
  - SSH accessed Windows account
  - Windows in front of my head, in the monitor
  - Those two are acutally separated
  - Thus whatever I run in my SSH server, it doesn't appear at the monitor
  - I was trying to run seleinum remote server and control browsers inside the ssh account remotely
  - But this is not a root solution. It enables to open a browser, but can't turn on/off the monitor
- Solution in the link seems there is a way to get display in the monitor while accessing via SSH
- If it is, just simply acess and run script would be fine.

## Seems better solution
- [What's the easiest way to run GUI apps on Windows Subsystem for Linux as of 2018?](https://askubuntu.com/questions/993225/whats-the-easiest-way-to-run-gui-apps-on-windows-subsystem-for-linux-as-of-2018)
- [Launch GUI Application in WSL without XServer](https://github.com/Microsoft/WSL/issues/2356)
- [kpocza/LoWe](https://github.com/kpocza/LoWe)
- [Running Graphical Programs on Windows Subsystem on Linux](https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx)

## Hope this works and saves me
- [Turn off Win10 display(s) via OpenSSH](https://superuser.com/questions/1382319/turn-off-win10-displays-via-openssh)
- At least this guy is trying to do the same thing with me
