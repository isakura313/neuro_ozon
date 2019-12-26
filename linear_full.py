import numpy as nр
import matplotlib.pyplot as plt 

def estimate_coef(x, y):
	# метод наименьших квадратов
	# вставить проверку на нормальность распределение
	#  правильное мат ожидание
	#  можно было обучать!
	# количество элементов
	N = np.size(x)

	# здесь считается среднее x и y
	m_x, m_y = np.mean(x), np.mean(y)

	# сумма массивов - количество  элементов * среднее y и среднее x
	SS_xy = np.sum(y * x) - N * m_y * m_x

	# сумма массивов - количество элементов* среднее x и среднее x
	SS_xx = np.sum(x*x) - N * m_x * m_x

	b_1 = SS_xy /SS_xx 
	# b_1 коэфицент регрессии
	b_0 = m_y - b_1* m_x

	# нужны для расчета коэфицента регрессии
	return(b_0, b_1, m_x, m_y)

def plot_regression_line(x, y, b):
	plt.scatter(x, y, color="m", marker="o",
		s = 30)
	y_predict = b[0] + b[1]*x
	plt.plot(x, y_predict, color="g")

	plt.xlabel("контролируемая")
	plt.ylabel("свободная")

	plt.show()

def main():
	# данные приходят сюда
	x = np.array([181, 180, 183, 164, 192,180, 182, 181, 165, 190])
	y = np.array([81, 68, 69, 56, 87,80, 65, 67, 58, 89])
	#b это массив куда вернулись данные наших коэфицентов
	b = estimate_coef(x, y) 


	print(b[0])
	print(b[1])
	print(b[2])
	print(b[3])
	plot_regression_line(x, y, b)

if __name__ == "__main__":
	main()




