from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QApplication, QButtonGroup, QGroupBox, QHBoxLayout, QWidget, QRadioButton, QPushButton, QLabel, QVBoxLayout)
from random import shuffle 


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("Какие штаны НЕ носили строители?", "Jnco", "Dickies", "Charhartt", "TrueReligeans"))
question_list.append(Question("Какие штаны НЕ носили строители?", "Jnco", "Dickies", "Charhartt", "TrueReligeans"))
question_list.append(Question("Какие штаны НЕ носили строители?", "Jnco", "Dickies", "Charhartt", "TrueReligeans"))

shuffle(question_list)
print(question_list)

msg = QMessageBox()
msg.setIcon(QMessageBox.Critical)
msg.setText("Error")
msg.setInformativeText('More information')
msg.setWindowTitle('Error')
msg.exec_()

app = QApplication([])
main_win = QWidget()
main_win.resize(400,400)
main_win.setWindowTitle('Вопрос от учителя')

btn_OK = QPushButton('Ответить')
question = QLabel('Какой национальности не существет?')

RadioGroupBox = QGroupBox("Варианты ответов:")

rbnt_1 = QRadioButton("1) Энцы")
rbnt_2 = QRadioButton("2) Смурфы")
rbnt_3 = QRadioButton("3) Чулымцы") 
rbnt_4 = QRadioButton("4) Алеуты")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbnt_1)
RadioGroup.addButton(rbnt_2)
RadioGroup.addButton(rbnt_3)
RadioGroup.addButton(rbnt_4)

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbnt_1)
layout_ans2.addWidget(rbnt_2)
layout_ans3.addWidget(rbnt_3)
layout_ans3.addWidget(rbnt_4) 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результаты теста")
lb_result = QLabel("Ты прав или нет?")
lb_correct = QLabel("Ответ будет тут")
layout_ans4 = QVBoxLayout()
layout_ans4.addWidget(lb_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_ans4.addWidget(lb_correct, alignment = Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_ans4)

layout_line = QVBoxLayout()
layout_line.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignHCenter))
layout_line.addWidget(RadioGroupBox)
layout_line.addWidget(AnsGroupBox)
AnsGroupBox.hide() 
layout_line.addWidget(btn_OK, stretch=2)
main_win.setLayout(layout_line) 

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Продолжить")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbnt_1.setChecked(False)
    rbnt_2.setChecked(False)
    rbnt_3.setChecked(False)
    rbnt_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbnt_1, rbnt_2, rbnt_3, rbnt_4]
def ask (q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked() :
            show_correct("Неверно!")

def next_question():
    main_win.cur_question +=1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    q = question_list[main_win.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


main_win.cur_question = -1
btn_OK.clicked.connect(click_OK)
next_question()
      
main_win.show() 
app.exec()