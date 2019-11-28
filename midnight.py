from home import open_icloud, play_youtube, play_bbc
from info import get_email_passwd
    
def main() : 
    # these files are loaded under the path of cron (why?)
    # C:/Program Files (x86)/cron
    # chromedriver.exe also should be under the path of cron
    email, password = get_email_passwd() # plain text
    
    return
    
if __name__ == "__main__":
    main()


