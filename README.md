# inkyphat_countdown_nightshifts

## Intallation

Install Pimoroni's Inkyphat software first:
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat

Clone this repo:
    
     git clone https://github.com/tommybobbins/inkyphat_countdown_nightshifts

Edit the countdown date in countdown.py

     dead = datetime.strptime('01/01/2020', date_format)

Run it via cron :
 
     pi@raspberrypi:~/$ crontab -e
     23 * * * * ( cd /home/pi/inkyphat_countdown_nightshifts ; ./countdown.py >/var/tmp/output.txt 2>&1 )

