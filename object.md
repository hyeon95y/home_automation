# 1. 아침
- Trigger : iPhone Alarm (wake-up)
    - Shortcuts
        - 'Light alarm'
            - 조명 두개 단계적 점등 (미구현)
        - 'Today's weather'
        - 'Today's calendar, reminder'
        - 'Turn on the PC'
            - 윈도우 작업 스케줄러
                - powershell.exe / Start-Service sshd
        - 'Morning'
            - Run Script via SSH
            - 모든 세션을 돌면서 morning.py 실행
                - reminder, calendar 열기
                - Youtube Music 실행 (30분)
                - BBC News 실행 (2시간)
                - 어떻게 계속 켜놓을수 있을까?
        - 'Boil the water for coffee'
            - for 3 minutes
        
# 2. 집을 떠날때
- Trigger : When I leave home
    - Shortcuts
        - 'Turn off the PC'
            - Run Script via SSH
        - 'Turn off the light'
        - 'Turn off the heater'
        - 'Clean the room'
        - ...
 
 # 3. 집에 돌아올때
 - Trigger : When I get home
     - Shortcuts
         - 'Turn on the PC'
         - 'Turn on the light'
         - 'Get home'
             - Run Script via SSH
                 - reminder, calendar 열기
                 - Youtube Music 실행 (30분)
                 - 어떻게 계속 켜놓을수 있을까?
 
 # 4. 잘 시간
 - Trigger : Time 
     - Shortcuts
         - 'Turn on the heater'
         
 - Trigger : Time
     - Shortcuts
         - 'Turn off the light'
                 
              
 # 4. 그 외 음성 명령
 - Shortcuts
     - 'Boil the water'
         - for 3 minutes
     - 'Boil the water for coffee'
         - for 3 minutes
        
        
        
        
        
        
        
        
        
        
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
