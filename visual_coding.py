from tkinter import *

from my_algorithm import NeedlemanWunsch


def do_algorithm():
    first_string = first_input_spot.get()
    second_string = second_input_spot.get()

    my_object = NeedlemanWunsch(first_string, second_string)
    result_matrix = my_object.get_result_matrix()
    result_lsc = my_object.get_lcs()

    score_matrix_window = Tk()
    score_matrix_window.geometry('400x300')
    score_matrix_window.title('Результат:')

    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[i])):
            label = Label(score_matrix_window, text=result_matrix[i][j])
            label.grid(column=j, row=i)

    result_lsc = Label(score_matrix_window, text=f'Наибольшая общая подпоследовательность: {result_lsc}')
    result_lsc.grid(row=len(result_matrix)+2, column=90)

    score_matrix_window.mainloop()


window = Tk()
window.title('Нахождение максимальной общей подпоследовательности')
window.geometry('400x300')

first_text = Label(window, text='Введите первую строку:')
first_text.grid(column=0, row=0)

first_input_spot = Entry(window)
first_input_spot.grid(column=1, row=0)

second_text = Label(window, text='Введите вторую строку:')
second_text.grid(column=0, row=1)

second_input_spot = Entry(window)
second_input_spot.grid(column=1, row=1)

button = Button(window, text='Обработать', command=do_algorithm)
button.grid(row=2, column=0)

window.mainloop()