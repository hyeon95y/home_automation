# 1. 아침
- BIOS Setting
    - 윈도우 부팅
- 윈도우 작업 스케줄러
    - SSH Server 실행
    - morning.py
        - reminder, calendar 열기
        - Youtube Music 실행 (30분)
        - BBC News 실행 (2시간)
        - 마지막 작업 후 스크립트 종료
        
# 2. 집을 떠날때
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