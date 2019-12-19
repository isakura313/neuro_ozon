from tkinter import *
from ozon_neuro import assert_auto

class Assert_Ozon:
	def __init__(self, root, title, labelText, button_Text):
		self.root = root
		root.title = title

		self.label = Label(root, text=labelText)
		self.label.pack()

		#main_cond, second_cond, lr, accur, epoch

		self.main_cond = Entry()
		self.main_cond.pack()

		self.second_cond = Entry()
		self.second_cond.pack()

		self.lr = Entry()
		self.lr.pack()

		self.accur = Entry()
		self.accur.pack()

		self.epoch = Entry()
		self.epoch.pack()

		self.main_btn = Button(root, text= button_Text, command = self.assertation)
		self.main_btn.pack()

		self.label_result = Label(root, text='')
		self.label_result.pack()

	def assertation(self):
		result = assert_auto(int(self.main_cond.get()), int(self.second_cond.get()), float(self.lr.get()), float(self.accur.get()), int(self.epoch.get()))
		self.label_result["text"] = str(result)




root = Tk()

ozon_length = Assert_Ozon(root, "программа коэфицента длины", "Введите данные", "Вычислить")

root.geometry("400x400")
root.mainloop()




# прочитать про assert
# сделать в программе лого компании на заднем фоне ( и в классе!)
#пускай геометрия тоже задается в классе
# сделать лейблы к нашим entry





