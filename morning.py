import pickle
from home import open_icloud, play_youtube, play_bbc
from info import get_email_passwd
import os
    
def main() : 
    # these files are loaded under the path of cron
    # C:/Program Files (x86)/cron
    # chromedriver.exe also should be under the path of cron
    email, password = get_email_passwd() # plain text
    
    # open reminder
    # at 6:55
    link = 'https://icloud.com/reminders'
    positions = [2550, 220]
    sizes = [900, 1030]
    reminders = open_icloud(link, 1, positions, sizes, email, password)
    
    # open calendar
    link = 'https://icloud.com/calendar'
    positions = [3430, 220]
    sizes = [850, 1030]
    reminders = open_icloud(link, 2, positions, sizes, email, password)
    
    # play youtube
    # from 7:00 ~ 7:30
    link = 'https://www.youtube.com/watch?v=Suy_dHz8Ojg'
    minutes_music = 30
    volume_music = 70
    play_youtube(link, minutes_music, volume_music)
    
    # play bbc
    # from 7:30 ~ 9:30
    link = 'https://www.livenewsmag.com/bbc-news-uk-live-stream/'
    minutes_bbc = 120
    volume_bbc = 15
    play_bbc(link, minutes_bbc, volume_bbc)
    
    return
    
if __name__ == "__main__":
    # execute only if run as a script
    logf = open("C:\error.txt", "w")
    try : 
        main()
    except Exception as e :
        with open('C:\error.txt', 'wb') as handle:
            logf.write(str(e))

