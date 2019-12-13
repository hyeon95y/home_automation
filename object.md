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
        - '?'
            - 오늘 날씨, 일정 읽어주기
        
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
        
        
        
# 5. 여러 명령 묶어서 애플홈킷 Favorites Scenes로 구현
- Get Home, Leave Home 정도만 지원하고 (이마저도 위치 센서로 동작하는지는 모름)
- 나머지 모드는 그냥 이름만 설정할수 있고 조건은 걸 수 없음.
        
        
        
        
   
