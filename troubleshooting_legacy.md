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


     
        
        
  ----- legacy

- Apple Automation :  Run Script via SSH
    - 모니터 끄기
        - (Add-Type '[DllImport("user32.dll")]public static extern int SendMessage(int hWnd, int hMsg, int wParam, int lParam);' -Name a -Pas)::SendMessage(-1,0x0112,0xF170,2)
    - 돌고 있는 모든 python script 종료
        - taskkill /F /IM python.exe /T
    - ~~leave_home.py~~
        - 아래(3.)과 마찬가지의 이유로 파이썬 스크립트를 실행시킬수 없었음
        
# 3. 집에 돌아올때
- Apple Automation : Run Script via SSH
    - ~~get_home.py~~
    - 내가 접속한 kernel(혹은 계정?)에서 .py가 실행되어, 윈도우 데스크탑에 selenium browser가 뜨지 않음
    - (추측) selenium이 내가 접속한 계정에 할당된 디스플레이(no-display)를 잡는듯, 그래서 코드는 돌지만 윈도우 데스크탑에 창이 뜨지 않음
    
## Troubleshooting
- [python selenium remote - 원격 PC 크롬 실행](https://myinbox.tistory.com/125)
- 원격에서 selenium을 실행시키려면, local에서 selenium server가 돌아가고 selenium server를 통해서 명령을 내려야 하는듯
- (추측) selenium 자체는 local 사용을 가정하고 만든 것이라 ssh를 통해서 접속했을 경우 접속 계정에서 selenium이 돌아감
- (추측) 따라서 local monitor에 browser를 띄워주지 않아 의도한대로 사용할 수 없음
