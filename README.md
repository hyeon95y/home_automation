# home_automation


## Troubleshooting
Still working on making system to automate several stuffs. 


## Solution to all problems, finally found
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
