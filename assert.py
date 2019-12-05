mili = 62.37
kilometri = 100

# enter = input()
# coef = float(enter)

def assort(coef):
	Error = mili - (kilometri * coef)
	print("Your error")
	print(Error)

# assort(coef)


def assert_auto(main_dep, second_dep, learning_rate, coef, epoch):
	for i in range(epoch):
		error = second_dep - ( main_dep * coef)
		coef += learning_rate
		print(error)
		print(coef)
		if error < 0.02:
			print("our final score")
			print(coef)
			return

enter_lr = input("enter the learning_rate")
lr = float(enter_lr)
enter_coef = input("enter coef")
coef = float(enter_coef)
enter_epoch = input("enter epoch")
epoch = int(enter_epoch)


assert_auto(kilometri, mili, lr, coef, epoch)

#адаптиовать функцию assert_auto на слишким выский коэфицент
# пишем дополнительный if
# найти в документации стандартную функцию, что питон коэфицент генерировал от 0 до 1
# потестить на дюймах и сантиметрах
# любая валюта






