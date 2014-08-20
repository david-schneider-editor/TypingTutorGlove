#
# Tactile-glove typing tutor v.0.0 (April 2014)
#
#
import serial
import time
import random
import winsound


#
# Open a serial port (note that the port number = COM number minus one).
#
ser = serial.Serial(13, 9600, timeout=1)  	# open first serial port
time.sleep(2)								# need to sleep for a bit after opening the port or Arduino can't handle things
#
#
#
import Tkinter as tk
import time

vocab = ['the', 'be','to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would',
'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time',
'no', 'just', 'him', 'no', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'then', 'see', 'other', 'then', 'than',
'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well',
'way', 'even', 'new', 'want', 'because', 'these', 'give', 'day', 'most', 'us']

word = (random.choice(vocab))
typed_word = ''
chars_typed = 0		#Number of characters in typed_word that have been typed so far
newFlag = False
counter = -1
delay = 1000		#mS delay between letters of the target word

def say_word(word):
	soundfile = word + '.wav'
	winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)


def change_word():
	global word
	global newFlag
	global vocab
	global counter
	global typed_word
	global chars_typed
	
	chars_typed = 0
	newFlag = True
	label1.config(text='')
	typed_word = ''
	counter = -1
	word = (random.choice(vocab))
	word_label(label)
	
def erase():
	global typed_word
	label1.config(text='')
	typed_word = ''
	

def word_label(label):
	def count():
		global counter
		global newFlag
		global word
		counter += 1
		if (counter>len(word)):
			counter = 0
			say_word(word)	
		if (newFlag):
			newFlag = False
			return
		label.config(text=word[:counter])
		vibrate(word[counter-1:counter])   					# write current character to Arduino so that it vibrates the correct finger
		label.after(delay, count)

	label.config(text=word)
	label.after(2000, count)
	
def key(event):
	global typed_word
	global chars_typed
	
	if event.char == event.keysym:
		typed_word = typed_word + event.char
		chars_typed = chars_typed + 1

	elif len(event.char) == 1:
		msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
	else:
		msg = 'Special Key %r' % event.keysym
		
	if (chars_typed > len(word)):
		chars_typed = 1
		typed_word = typed_word[-1:]
	label1.config(text=typed_word)
	
def hscale_cb(value):
	global delay
	delay = int(value)
	
def vibrate(letter):
	if (letter == 'a') or (letter == 'A'):
		ser.write('1')      						#Vibrate "finger 1" (left pinky)
	elif (letter == 'b') or (letter == 'B'):
		ser.write('4')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'c') or (letter == 'C'):
		ser.write('3')								#Vibrate "finger 3" (left middle)
	elif (letter == 'd') or (letter == 'D'):
		ser.write('3')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'e') or (letter == 'E'):
		ser.write('3')								#Vibrate "finger 3" (left middle)
	elif (letter == 'f') or (letter == 'F'):
		ser.write('4')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'g') or (letter == 'G'):
		ser.write('4')								#Vibrate "finger 3" (left middle)
	elif (letter == 'h') or (letter == 'H'):
		ser.write('7')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'i') or (letter == 'I'):
		ser.write('8')								#Vibrate "finger 3" (left middle)
	elif (letter == 'j') or (letter == 'J'):
		ser.write('7')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'k') or (letter == 'K'):
		ser.write('8')								#Vibrate "finger 3" (left middle)
	elif (letter == 'l') or (letter == 'L'):
		ser.write('9')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'm') or (letter == 'M'):
		ser.write('7')								#Vibrate "finger 3" (left middle)
	elif (letter == 'n') or (letter == 'N'):
		ser.write('7')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'o') or (letter == 'O'):
		ser.write('9')								#Vibrate "finger 3" (left middle)
	elif (letter == 'p') or (letter == 'P'):
		ser.write('A')								#Vibrate "finger 4" (left pointer) hop
	elif (letter == 'q') or (letter == 'Q'):
		ser.write('1')								#Vibrate "finger 3" (left middle)
	elif (letter == 'r') or (letter == 'R'):
		ser.write('4')								#Vibrate "finger 4" (left pointer)
	elif (letter == 's') or (letter == 'S'):
		ser.write('2')								#Vibrate "finger 3" (left middle)
	elif (letter == 't') or (letter == 'T'):
		ser.write('4')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'u') or (letter == 'U'):
		ser.write('7')								#Vibrate "finger 3" (left middle)
	elif (letter == 'v') or (letter == 'V'):
		ser.write('4')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'w') or (letter == 'W'):
		ser.write('2')								#Vibrate "finger 3" (left middle)
	elif (letter == 'x') or (letter == 'X'):
		ser.write('2')								#Vibrate "finger 4" (left pointer)
	elif (letter == 'y') or (letter == 'Y'):
		ser.write('7')								#Vibrate "finger 3" (left middle)
	elif (letter == 'z') or (letter == 'Z'):
		ser.write('1')								#Vibrate "finger 4" (left pointer)

	
root = tk.Tk()
root.title("Tactile Tutor")
root.bind_all('<Key>', key)	
label = tk.Label(root, fg="red", font="Helvetica 64 bold")
label.pack()

word_label(label)

label1 = tk.Label(root, text="", fg="black", font="Helvetica 64 bold")
label1.pack()

changeButton = tk.Button(root, text='TRY NEW WORD', width=60, font="Helvetica 12 bold", command=change_word)
changeButton.pack()

newButton = tk.Button(root, text='ERASE TYPED WORD', width=60, font="Helvetica 12 bold", command=erase)
newButton.pack()

stopButton = tk.Button(root, text='QUIT', width=60, font="Helvetica 12 bold", command=root.destroy)
stopButton.pack()

w = tk.Scale(root, from_=1000, to=100, font="Helvetica 10 bold", label='<< SLOW                                                                                                                      FAST >>', length=600, width=25, orient=tk.HORIZONTAL, showvalue=0, command=hscale_cb)
w.set(550)
w.pack()

root.mainloop()

ser.close()             # close port