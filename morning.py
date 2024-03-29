from home import open_icloud, play_youtube, play_bbc, monitor_turn_on, monitor_turn_off
from info import get_email_passwd
    
def main() : 
    # these files are loaded under the path of cron (why?)
    # C:/Program Files (x86)/cron
    # chromedriver.exe also should be under the path of cron
    email, password = get_email_passwd() # plain text
    
    monitor_turn_off()

    # open reminder
    # at 7:00
    link = 'https://icloud.com/reminders'
    positions = [2550, 220]
    sizes = [900, 1030]
    reminders = open_icloud(link, 1, positions, sizes, email, password)
    
    # open calendar
    link = 'https://icloud.com/calendar'
    positions = [3430, 220]
    sizes = [850, 1030]
    calendar = open_icloud(link, 2, positions, sizes, email, password)
    
    monitor_turn_on()
    
    # play youtube
    # from 7:00 ~ 7:30
    link = 'https://www.youtube.com/watch?v=Suy_dHz8Ojg'
    minutes_music = 1
    volume_music = 20
    play_youtube(link, minutes_music, volume_music)
    
    # play bbc
    # from 7:30 ~ 9:30
    link = 'https://www.livenewsmag.com/bbc-news-uk-live-stream/'
    minutes_bbc = 120 # don't quit
    volume_bbc = 50
    play_bbc(link, minutes_bbc, volume_bbc)
    
    #reminders.quit()
    #calendar.quit()
    
    return
    
if __name__ == "__main__":
    main()

