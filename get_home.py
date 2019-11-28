from home import open_icloud, play_youtube, play_bbc
from info import get_email_passwd
    
def main() : 
    # these files are loaded under the path of cron (why?)
    # C:/Program Files (x86)/cron
    # chromedriver.exe also should be under the path of cron
    email, password = get_email_passwd() # plain text

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
    
    return
    
if __name__ == "__main__":
    main()


