# Homestuck Captcha Dowel Calculator

This just-for-fun script translates [Homestuck's](https://www.homestuck.com) captchalogue codes into segment widths of a carved dowel.

## What is Homestuck?

Broadly, Homestuck is a multi-media webcomic, primarily written and drawn Andrew Hussie. It is the fourth entry in a series of "MS Paint Adventures" which mimick the look and feel of yesteryear's text-based adventure games. Readers "played" MSPA by submitting commands as forum replies. Then, Andrew would select a batch of commands turn them into new comic pages. A page of MSPA typically consists of one or more panels, sometimes accompanied by a narrative caption or dialogue.

Homestuck incorporates simple programming concepts into its parody of text-based adventure games. Notably, player characters' inventory systems are constrained by simple data structures:

| <img src="https://storage.homestuck.com/story/homestuck/media/images/panels/act-1/00010.gif" alt="John expresses frustration at being unable to access the card containing his prop arms, because they are 'below' the card containing his smoke pellets." width="50%"/> |
| :---: |
| "Unfortunately, you cannot access the FAKE ARMS! Their card is underneath the one you just used to captchalogue the SMOKE PELLETS. You will have to use the pellets first in order to access the arms... Your SYLLADEX'S FETCH MODUS is currently dictated by the logic of a STACK DATA STRUCTURE. You were never all that great with data structures and you find the concept puzzling and mildly irritating." |

## What are "Captcha Dowels"?

"Captcha Dowels" is a descriptive term I prescribed to one of Homestuck's important in-game items: Totems. Totems are a crucial ingredient for punch card alchemy, a system enabling players to fabricate (alchemize) new items by combining those in their inventory.

Items are stored on "captchalogue cards". Storing an item in a captchalogue card generates an eight character captcha code on the card's back. 

| <img src="https://storage.homestuck.com/story/homestuck/media/images/panels/act-2/00523.gif" alt="John expresses frustration at being unable to access the card containing his prop arms, because they are 'below' the card containing his smoke pellets." width="50%"/> |
| :---: |
| "You flip over the top card containing your POGO RIDE. Any time you captchalogue something, a new code appears on the back of the card. You've always wondered what the code was for." |

Inputting the code into a Punch Designix machine allows players to punch their cards with a corresponding pattern of holes. To alchemize the item on the card, the player punches it using the Punch Designix, and slots it into the card-reader on another machine, the Totem Lathe. The Totem Lathe carves Cruxite Dowels into Totems based on the pattern of punched holes on the card.

| <img src="https://storage.homestuck.com/story/homestuck/media/images/panels/act-1/00205.gif" alt="John slots a punched card into the Totem Lathe, activating the machine."/> | <img src="https://storage.homestuck.com/story/homestuck/media/images/panels/act-1/00210_1.gif" alt="The Totem Lathe carves a cylindrical dowel into an oddly-shaped Totem."/> | 
| :---: | :---: |
| "You slip the PRE-PUNCHED CARD into a slot on the TOTEM LATHE." | "The lathe carves ONE (1) TOTEM." |

Then, the player brings the Totem to the Alchemiter, which scans the Totem and alchemizes the item on the card. Players can alchemize new items by punching a single card with two codes, or by inserting two punched cards into the Totem Lathe.

| <img src="https://storage.homestuck.com/story/homestuck/media/images/panels/act-2/00631_2.gif" alt="John overlaps two punched cards, creating a new pattern of punched holes"/> | <img src="https://storage.homestuck.com/story/homestuck/media/images/panels/act-2/00632.gif" alt="John carves a new Totem, with a different shape than the one previous"/> | <img src="https://storage.homestuck.com/story/homestuck/media/images/panels/act-2/00635.gif" alt="John poses triumphantly with his newly-alchemized weapon. It has elements of both the Claw Hammer and Pogo Ride."/> |
| :---: | :---: | :---: |
| "You overlap two of the punched cards. They mask each other's hole patterns." | "You carve another TOTEM using the new combined hole pattern." | "You got the POGO HAMMER" |