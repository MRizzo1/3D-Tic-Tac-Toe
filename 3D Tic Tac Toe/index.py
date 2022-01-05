from tkinter import *
from tkinter import ttk, font
from data import *
import game

class Application():
	def __init__(self):
		#Defining root static per object
		self.root = Tk()
		#Window
		self.root.resizable(False, False)
		self.root.title("N-In-Line Game")
		self.root.iconbitmap("img/ico.ico")
		#Root Config
		self.root.config(width="800", height="800")

		#Header with logo
		header_image = PhotoImage(file = "img/Logo3.png")
		self.header_image = ttk.Label(self.root,image = header_image)
		self.header_image.pack()
		#Flag Variable init
		self.flag = -1
		#Body Frame
		self.body = Frame()
		#Buttons style
		self.style = ttk.Style()
		self.style.configure('W.TButton', font=("Courier New", 15))
		self.body.pack(fill ="x")
		self.main_menu()

		self.root.mainloop()


	#Methods
	def clear_body(self):
		#Do not be afraid of those who kill the body but cannot kill the sould.
		#Rather, be afraid of the One who can destroy both sould and body in hell.
		#Matthew 10:28 New International Bible Version
		self.body.destroy() # :'(

		#Jesus said to her. I am the resurrection and the life.
		#The one who believes in me will live, even though they die
		#John 11:25
		self.body = Frame() # :)

		self.body.pack(fill ="x")

	def main_menu(self):
		#Clear Body Conditional
		if self.flag == 1:
			self.clear_body()
		#Buttons
		self.nw_game = ttk.Button(self.body, style ='W.TButton' ,text="New Game", command= self.colect_users_data)

		self.exit = ttk.Button(self.body, style ='W.TButton' ,text="Exit", command =quit)

		#Packing
		self.body.pack(fill ="x")
		self.nw_game.pack(fill ="x", ipadx=7, ipady=7,  padx=35, pady=2)
		self.exit.pack(fill ="x", ipadx=7, ipady=7,  padx=35, pady=2)

		#Flag Variable change
		self.flag = 1


	def colect_users_data(self):
		#Clear Body
		self.clear_body()
		#Declares 2 variables, type string, for the users
		self.user_one = StringVar()
		self.user_two = StringVar()
		self.n = StringVar()
		self.user_one.set("Player 1")
		self.user_two.set("Player 2")
		self.n.set("3")

		#fields of text
		self.ctext1 = ttk.Entry(self.body, textvariable=self.user_one, width=30)
		self.ctext2 = ttk.Entry(self.body, textvariable=self.user_two, width=30)
		self.ctext3 = ttk.Entry(self.body, textvariable=self.n, width=30)
		self.separ1 = ttk.Separator(self.body, orient=HORIZONTAL) #Separator

		#Buttons
		self.back = ttk.Button(self.body, style ='W.TButton' ,text="Back", command= self.main_menu)
		self.Start = ttk.Button(self.body, style ='W.TButton' ,text="Start", command= self.start)
		self.exit = ttk.Button(self.body, style ='W.TButton' ,text="Exit", command =quit)
		#Packing
		#Info Users
		Label(self.body, text="Insert User Names", font=('Courier New', 15,'italic')).pack()
		self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
		self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
		#Info Table
		Label(self.body, text="Insert Width (N's Value)", font=('Courier New', 15,'italic')).pack()
		self.ctext3.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
		self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
		self.back.pack(side =LEFT, padx=3, pady=5)
		self.Start.pack(side =LEFT, padx=3, pady=5)
		self.exit.pack(side =LEFT, padx=3, pady=5)

		#print(self.ctext1.get())
		#print(self.ctext2.get())
		#print(self.ctext3.get())


	def start(self):
		user_one = self.ctext1.get()
		user_two = self.ctext2.get()
		try: table_with = int(self.ctext3.get())
		except:
			self.error

		#Start Game
		game.main(table_with,user_one,user_two)

	def error(self):
		pass

def main():
	app = Application()
	return 0

if __name__ == '__main__':
	main()
