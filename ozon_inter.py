from tkinter import *
from ozon_neuro import assert_auto
# from PIL import Image


class Assert_Ozon:
	def __init__(self, root, img_path, main_cond, second_cond, lr, accur, epoch, NameProg, button_Text):
		self.root = root
		# root.title = title

		self.label = Label(root, text=NameProg, font=("Helvetica", 32))
		self.label.grid(row = 0, column = 2, columnspan = 3, pady=10)

		#main_cond, second_cond, lr, accur, epoch
		self.label = Label(root, text = main_cond, font=("Helvetica", 24))
		self.label.grid(row = 1, column = 1, columnspan = 1)

		self.main_cond = Entry(font=("Helvetica", 24))
		self.main_cond.grid(row = 1, column = 2, columnspan = 2)

		self.label = Label(root, text = second_cond, font=("Helvetica", 24))
		self.label.grid(row = 2, column = 1, columnspan = 1)

		self.second_cond = Entry(font=("Helvetica", 24))
		self.second_cond.grid(row = 2, column = 2, columnspan = 2)

		self.label = Label(root, text = lr, font=("Helvetica", 24))
		self.label.grid(row = 3, column = 1, columnspan = 1)

		self.lr = Entry(font=("Helvetica", 24))
		self.lr.grid(row = 3, column = 2, columnspan = 2)

		self.label = Label(root, text = accur, font=("Helvetica", 24))
		self.label.grid(row = 4, column = 1, columnspan = 1)

		self.accur = Entry(font=("Helvetica", 24))
		self.accur.grid(row = 4, column = 2, columnspan = 2)

		self.label = Label(root, text = epoch, font=("Helvetica", 24))
		self.label.grid(row = 5, column = 1, columnspan = 1)

		self.epoch = Entry(font=("Helvetica", 24))
		self.epoch.grid(row = 5, column = 2, columnspan = 2)

		self.main_btn = Button(root, text= button_Text, command = self.assertation, font=("Helvetica", 24))
		self.main_btn.grid(row = 6, column = 2, columnspan = 1)

		self.label_result = Label(root, text='', font=("Helvetica", 24))
		self.label_result.grid(row = 7, column = 2, columnspan = 3)

		self.img_src = PhotoImage(file=(img_path))
		self.labl_image = Label(image = self.img_src, bd=2, bg="red", padx=10, pady=10)
		self.labl_image.image = self.img_src
		self.labl_image.grid(row = 8, column = 2, columnspan=10)

	def assertation(self):
		result = assert_auto(int(self.main_cond.get()), int(self.second_cond.get()), float(self.lr.get()), float(self.accur.get()), int(self.epoch.get()))
		self.label_result["text"] = str(result)




root = Tk()

ozon_length = Assert_Ozon(root,"ozon_logo.gif","километры", "мили", "шаг обучения", "точность", "эпохи","программа коэфицента длины", "Вычислить")

root.geometry("800x800")
root.mainloop()




# прочитать про assert
# сделать в программе лого компании на заднем фоне ( и в классе!)
#пускай геометрия тоже задается в классе
# сделать лейблы к нашим entry





