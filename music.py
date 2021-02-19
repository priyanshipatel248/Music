#		python code
#		script_name:demo
#
#		author:Priyanshi
#		description:composition practice
#

from earsketch import *

init()
setTempo(120)
#music
chord=COMMON_LOVE_THEME_PIANO_1
secondaryBeat=HIPHOP_MUTED_GUITAR_003
mainBeat=RD_WORLD_PERCUSSION_GLASSTONE_2
fitMedia(COMMON_LOVE_THEME_PIANO_1,1, 1, 16)
#add effect between measure 1 and 16 moving from -69db to 5db
setEffect(1, VOLUME, GAIN, -60, 1, 5, 12)
setEffect(1, VOLUME, GAIN, 5, 12, -60, 16)
fitMedia(HIPHOP_MUTED_GUITAR_003, 3, 1, 12)
#add effect
setEffect(3, DELAY, DELAY_TIME, 250)
fitMedia(RD_WORLD_PERCUSSION_GLASSTONE_2, 2, 1, 9)
#add effect
setEffect(3, REVERB, REVERB_TIME, 200)
#finish
finish()



finish()
