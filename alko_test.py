from tkinter import *
import tkinter.messagebox
import alko_questions
from alko_questions import *


root = Tk()
root.geometry('750x500+0+0')
root.title('Тест на алкогольную зависимость')

#-----------------------------------начало вступление-------------------------------------------------------


begining = False





def dalshe():
    def begintest():
        BeginText.place_forget()
        BeginFrame.place_forget()
        OkButton.place_forget()
        begining_true()

    BeginFrame = Frame(root, width=750, height=300, relief=RIDGE)
    BeginFrame.grid(row=0, column=0)
    BeginText = Label(BeginFrame, font=('arial', 12, 'bold'), text=Instruction, justify=LEFT)
    BeginText.place(x=50, y=50)

    OkButton = Button(BeginFrame, text = 'Начать тест', height = 3, width = 10, command = lambda : begintest())
    OkButton.place(x=300, y=220)


if begining == False:
    BeginFrame = Frame(root, width = 750, height = 300, relief = RIDGE)
    BeginFrame.grid(row=0, column=0)
    BeginText = Label(BeginFrame, font = ('arial', 12, 'bold'), text = Introduction, justify = LEFT)
    BeginText.place(x=50, y= 50)

    DalsheButton = Button(BeginFrame, text= 'Дальше>>>', height = 3, width = 10, command = lambda : dalshe())
    DalsheButton.place(x=300, y=220)



#-----------------------------------тест--------------------------------------------------------------------
def begining_true():
    global question_number
    global score
    score = 0
    question_number = 0

    def test_finished():
        #tkinter.messagebox.showinfo('Тест пройден','Вы набрали {score} очков')
        if score < 5:
            result = 'У вас нет алкогольной зависимости'
        if score >= 5 and score <= 8:
            result = 'У вас ранняя стадия алкоголизма'
        if score >= 9 and score <= 15:
            result = 'У вас начальная средняя стадия алкоголизма'
        if score >=16 and score <=21:
            result = 'У вас средняя стадия алкоголизма'
        if score >=22 and score <=27:
            result = 'У вас поздняя средняя стадия алкоголизма'
        if score >= 28:
            result = 'У вас поздняя стадия алкоголизма'

        if question_number == 27:
            tkinter.messagebox.showinfo(f"Вы набрали {score} баллов", result)

            """
            От 5 до 8 баллов — Ранняя стадия алкоголизма
            От 9 до 15 баллов — Начальная средняя стадия алкоголизма
            От 16 до 21 балла — Средняя стадия алкоголизма
            От 22 до 27 баллов — Поздняя средняя стадия алкоголизма.
            От 28 и выше — Поздняя стадия алкоголизма.
            """



    def nobutton():
        global question_number

        question_number +=1
        QuestionsText.config(text=list_of_questions[question_number])

        if question_number == 27:
            test_finished()




    def yesbutton():
        global question_number
        global score

        question_number +=1
        QuestionsText.configure(text=list_of_questions[question_number])



        if question_number <=9:
            score += 1
            #print(score)
        if question_number >= 9 and question_number <=18:
            score += 2
            #print(score)
        if question_number >= 19 and question_number <27:
            score += 3
            #print(score)
        if question_number == 27:
            test_finished()


    list_of_questions = (question_1, question_2, question_3, question_4, question_5, question_6, question_7,
                         question_8, question_9, question_10, question_11, question_12, question_13, question_14,
                         question_15, question_16, question_17, question_18, question_19, question_20,
                         question_21, question_22, question_23, question_24, question_25, question_26, question_27, question_28)



    TopFrame = Frame(root, padx=8, pady=8, width=750, height=300, relief=RIDGE)
    TopFrame.grid(row=0, column=0)

    #lblQuestions = Label(TopFrame, font=('arial', 30, 'bold'), text='Вопросы:', fg='maroon', justify=CENTER)
    #lblQuestions.place(x=0, y=-100)



    QuestionsText = Label(TopFrame, font = ('arial', 12), text = list_of_questions[question_number], justify=CENTER)
    QuestionsText.grid(row=1, column=0)

    ButtonsFrameLeft = Frame(root,  padx=8, pady=8, width=375, height=200, relief=RIDGE)
    ButtonsFrameLeft.place(x=0, y=300)

    ButtonsFrameRight = Frame(root, padx=8, pady=8, width=375, height= 200, relief=RIDGE)
    ButtonsFrameRight.place(x=325, y=300)

    YesButton = Button(ButtonsFrameLeft, text = 'Да', font = ('arial', 30, 'bold'), height = 1, width = 5, justify = CENTER,
                       padx=5, pady=5, bg = 'gainsboro', command = lambda : yesbutton())
    YesButton.place(x=150,y=0)
    NoButton = Button(ButtonsFrameRight, text = 'Нет', font = ('arial', 30, 'bold'), height = 1, width = 5, justify = RIGHT,
                      padx=5, pady=5, bg= 'gainsboro', command = lambda : nobutton())
    NoButton.place(x=100, y=0)






"""
От 5 до 8 баллов — Ранняя стадия алкоголизма
От 9 до 15 баллов — Начальная средняя стадия алкоголизма
От 16 до 21 балла — Средняя стадия алкоголизма
От 22 до 27 баллов — Поздняя средняя стадия алкоголизма.
От 28 и выше — Поздняя стадия алкоголизма.
"""









# логика - по нажатию кнопки НЕТ текст вопроса меняется на элемент +1, по нажатию да - так же меняется на элемент +1
# и засчитывается очко for вопросы in range 1-9: 1 очко, 10-..: 2 очка и тд.
# красивые кнопки сделать потом




score = IntVar()
score.set(0)












root.mainloop()