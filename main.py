import random

class Question():
    def __init__(self,text:str,choices:list,answer:str)->None:
        self.text=text
        self.choices=choices
        self.answer=answer
        
    def checkanswer(self,answer:str)->bool:
        return self.answer.lower()==answer.lower()
    


class Quiz():
    def __init__(self,name:str,surname:str,questions:list)->None:
        self.score=0
        self.name=name
        self.surname=surname
        self.questions=questions
        self.questionIndex=0
    
    def getQuestion(self):
        self.questionIndex=random.randint(0, len(self.questions)-1)
        return self.questions[self.questionIndex]
    
    def start(self):
        print(f'Merhaba {self.name} {self.surname},')
        print(f'Quiz Başlıyor...')
        
        for i in range(len(self.questions)):
            quest=self.getQuestion()
            dic={
                'text': quest.text,
                'A':f'{quest.choices[0]}',
                'B':f'{quest.choices[1]}',
                'C':f'{quest.choices[2]}',
                'D':f'{quest.choices[3]}',
                'E':f'{quest.choices[4]}',
            }
            answer=input(
                f'{quest.text}'+'\n'+
                f'A-) {quest.choices[0]}'+'\n'+
                f'B-) {quest.choices[1]}'+'\n'+
                f'C-) {quest.choices[2]}'+'\n'+
                f'D-) {quest.choices[3]}'+'\n'+
                f'E-) {quest.choices[4]}'+'\n'+
                'Cevap: '
            )
            if(answer.lower() in ['a','b','c','d','e']):
                answ=dic.get(answer.upper())
                if(answ!=None):
                    answer=answ
            if(quest.checkanswer(answer)):
                self.questions.remove(quest)
                self.score+=1
            else:
                self.questions.remove(quest)
        print(f'İsim: {self.name} Soyad: {self.surname} Score: {self.score}')
    
question1=Question(text='Hangisi bir yazılım dilidir?',choices=['S','R','K','N','Ç'],answer='R')
question2=Question(text='Yılan sembolü kullanan yazılım dili nedir?',choices=['R','Dart','C++','C#','Python'],answer='Python')
question3=Question(text='Hangi Yazılım dili daha eskidir?',choices=['C#','BASIC','Java','Python','Dart'],answer='BASIC')
question4=Question(text='Hangi Yazılım dili daha kolay yazım şekline sahiptir?',choices=['C++','Python','Java','C','Ruby'],answer='Python')

questions=[question1,question2,question3,question4]

            
quiz=Quiz(questions=questions,name='Sinan', surname='Uyğun')
quiz.start()
