#!/usr/bin/python3
##!/usr/bin/env python

from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT 
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive
from datetime import datetime
import subprocess
import re

colour="red"
padding=0
inky_display = InkyPHAT(colour)
inky_display.set_border(inky_display.BLACK)

date_format = "%m/%d/%Y"
dead = datetime.strptime('01/01/2020', date_format)
now = datetime.today()
tt = now.timetuple()
hour = tt.tm_hour
delta = dead - now 
numbdays = delta.days # that's it
#print ("Number of days = %i " % numbdays)
shiftdays = int(round(numbdays/8.0))

# Load the fonts
scale_size = 1
term_font = ImageFont.truetype("/usr/share/fonts/opentype/3270/3270Medium.otf", 10)
tiny_term_font = ImageFont.truetype("/usr/share/fonts/opentype/3270/3270Medium.otf", 8)
hanken_bold_font = ImageFont.truetype(HankenGroteskBold, int(16 * scale_size))
hanken_banner_font = ImageFont.truetype(HankenGroteskBold, int(26 * scale_size))
hanken_medium_font = ImageFont.truetype(HankenGroteskMedium, int(16 * scale_size))


if (numbdays < 0):
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, inky_display.WIDTH, inky_display.HEIGHT), fill=inky_display.BLACK, outline=inky_display.WHITE)
    #draw.rectangle((0, 0, inky_display.WIDTH, inky_display.HEIGHT), fill=inky_display.BLACK, outline=inky_display.BLACK)
    uptime = subprocess.Popen('uptime', shell=True, stdout=subprocess.PIPE)
    uptime_output = uptime.stdout.read().decode("utf-8")
#    print ("%s" % uptime_output)
    numbdays_string = ("Ruling %s days," % abs(numbdays))
    uptime_output = re.sub(r"up\s+\S+", numbdays_string, uptime_output)
    uptime_output = re.sub(r"^\s+", "", uptime_output)
#    print ("%s" % uptime_output)
    term1 = ("darkstar:/root # whoami;uptime" )
    term2 = ("darthsciuridae")
    shift_message = ("%i days of rule under" % abs(numbdays))
    draw.text((10, 10), term1, inky_display.WHITE, font=term_font)
    draw.text((10, 20), term2, inky_display.RED, font=term_font)
    draw.text((10, 30), uptime_output, inky_display.WHITE, font=term_font)
    draw.text((10, 40), uptime_output, inky_display.BLACK, font=term_font)
    if ( hour < 8 ):
        bob_name = "resources/Bobdobbs3_3.png"
        bob_image = Image.open(bob_name)
        img.paste(bob_image, (170, 46))
    logo_name = "resources/imperial_logo2.png"
    logo_image = Image.open(logo_name)
    img.paste(logo_image, (0, 50))
elif (numbdays > 0):
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, inky_display.WIDTH, inky_display.HEIGHT), fill=inky_display.WHITE, outline=inky_display.BLACK)
    banner = ("Nightshift B-team")
    message = ("%i days until" % numbdays)
    shift_message = ("%i shift sets until" % shiftdays)
    draw.text((3, 10), banner, inky_display.BLACK, font=hanken_banner_font)
    draw.text((30, 60), shift_message, inky_display.RED, font=hanken_bold_font)
    draw.text((30, 80), message, inky_display.BLACK, font=hanken_bold_font)
    logo_name = "resources/tombstone_2colour2.png"
    logo_image = Image.open(logo_name)
    img.paste(logo_image, (170, 55))
else:
    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)
    message = ("Happy New Year")
    shift_message = ("Love You All")
    draw.text((10, 5), message, inky_display.BLACK, font=hanken_banner_font)
    draw.text((60, 30), shift_message, inky_display.RED, font=hanken_bold_font)
    bob_name = "resources/Bobdobbs3_3.png"
    bob_image = Image.open(bob_name)
    img.paste(bob_image, (80, 45))

inky_display.set_image(img)
inky_display.show()
