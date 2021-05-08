#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QMessageBox,QRadioButton,QGroupBox,QButtonGroup
from random import shuffle
from random import randint

app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle("Memory Card")
ask=QLabel("В чём измеряется вес?")
ans_1=QRadioButton("Н")
ans_2=QRadioButton("кг")
ans_3=QRadioButton("Дж")
ans_4=QRadioButton("Вт")
var=QGroupBox("Варианты ответов:")
btn=QPushButton("Ответить")

ans=QLabel("Правильно/Неправильно")
answ_1=QLabel("Правильный ответ")
answer=QGroupBox('Результат теста:')

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

question_list=[]
q1=Question('Год объединения Германии?','1990','1989','1993','1977')
q2=Question('Пальма-это...?','Трава','Дерево','Куст','-')
q3=Question('Сколько г в кг?','1000','100','10000','10')
q4=Question('Кто написал "Бесы"?','Достоевский','Гоголь','Булгаков','Лермонтов')
q5=Question('Сколько соседей у России?','16','14','19','20')
q6=Question('В чём измеряется магнитный поток?','Вб','Тл','А','Ом')
q7=Question('Основателем какого направления является Карамзин?','Сентиментализм','Классицизм','Романтизм','Реализм')
q8=Question('В какой стране французский не является официальным?','Дания','Швейцария','Канада','Бельгия')
question_list.append(q1)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
question_list.append(q6)
question_list.append(q7)
question_list.append(q8)

line_1=QVBoxLayout()
line_2=QVBoxLayout()
line_3=QHBoxLayout()
line_4=QVBoxLayout()

line_1.addWidget(ans_1)
line_1.addWidget(ans_2)
line_2.addWidget(ans_3)
line_2.addWidget(ans_4)
line_3.addLayout(line_1)
line_3.addLayout(line_2)
var.setLayout(line_3)

line_4.addWidget(ans)
line_4.addWidget(answ_1)
answer.setLayout(line_4)

main_layout=QVBoxLayout()
layout_1=QHBoxLayout()
layout_2=QHBoxLayout()
layout_3=QHBoxLayout()

layout_1.addWidget(ask, alignment=Qt.AlignVCenter)
layout_2.addWidget(var, alignment=Qt.AlignVCenter)
layout_2.addWidget(answer, alignment=Qt.AlignVCenter)
layout_3.addWidget(btn, alignment=Qt.AlignVCenter, stretch=2)

main_layout.addLayout(layout_1)
main_layout.addLayout(layout_2)
main_layout.addLayout(layout_3)

RadioGroup=QButtonGroup()
RadioGroup.addButton(ans_1)
RadioGroup.addButton(ans_2)
RadioGroup.addButton(ans_3)
RadioGroup.addButton(ans_4)
def show_result():
    var.hide()
    answer.show()
    btn.setText('Следующий вопрос')
def show_question():
    var.show()
    answer.hide()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    ans_1.setChecked(False)
    ans_2.setChecked(False)
    ans_3.setChecked(False)
    ans_4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if btn.text()=='Ответить':
       show_result()
    else:
       show_question()

answers=[ans_1,ans_2,ans_3,ans_4]
def asked(q):
    shuffle(answers)
    ask.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    answ_1.setText(q.right_answer)
    show_question()

def show_correct(r):
    ans.setText(r)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
        main_win.score+=1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct("Неправильно!")
main_win.cur_question= -1
def next_question():
    cur_question=randint(0,len(question_list)-1)
    q=question_list[cur_question]
    main_win.total+=1
    print('Статистика')
    print('Всего вопросов:', main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Рейтинг:',main_win.score/main_win.total*100)
    asked(q)

def click_ok():
    if btn.text()=="Ответить":
        check_answer()
    else:
        next_question()

main_win.total=0
main_win.score=0
btn.clicked.connect(click_ok)
main_win.setLayout(main_layout)
main_win.show()
answer.hide()
q=Question('Какой элемент обозначается буквой C?','Углерод','Водород','Гелий','Цинк')
asked(q)
app.exec_()
