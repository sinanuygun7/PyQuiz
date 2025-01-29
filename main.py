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
    
    def getQuestionRandom(self)->Question:
        self.questionIndex=random.randint(0, len(self.questions)-1)
        return self.questions[self.questionIndex]
    
    def getQuestion(self)->Question:
        return self.questions[self.questionIndex]
    
    def getScore(self)->int:
        return self.score
    
    def getName(self)-> str:
        return self.name
    
    def getSurname(self)->str:
        return self.surname
    
    def createQuestionDictionery(self,quest:Question)-> dict:
        return {
                'text': quest.text,
                'A':f'{quest.choices[0]}',
                'B':f'{quest.choices[1]}',
                'C':f'{quest.choices[2]}',
                'D':f'{quest.choices[3]}',
                'E':f'{quest.choices[4]}',
            }
        
    def controlAnswer(self,answer: str,dic: dict,quest: Question)-> bool:
        correct=False
        if(answer.lower() in ['a','b','c','d','e']):
            answ=dic.get(answer.upper())
            if(answ!=None):
                answer=answ
        if(quest.checkanswer(answer)):
            self.questions.remove(quest)
            correct=True
        else:
            self.questions.remove(quest)
            correct=False
        return correct
    
    def controlScore(self,correct:bool)->None:
        if(correct):
            self.score+=1
        else:
            pass
    
    def display(self)->None:
        print(f'Merhaba {self.getName()} {self.getSurname()},')
        selection=input('Rastgele Sırala Evet(E) Hayır(H): ')
        print(f'Quiz Başlıyor...')
        
        for i in range(len(self.questions)):
            if(selection.upper()=='E'):
                quest=self.getQuestionRandom()
            else:
                quest=self.getQuestion()
            dic=self.createQuestionDictionery(quest)
            answer=input(
                f'{quest.text}'+'\n'+
                f'A-) {quest.choices[0]}'+'\n'+
                f'B-) {quest.choices[1]}'+'\n'+
                f'C-) {quest.choices[2]}'+'\n'+
                f'D-) {quest.choices[3]}'+'\n'+
                f'E-) {quest.choices[4]}'+'\n'+
                'Cevap: '
            )
            correct=self.controlAnswer(answer=answer,dic=dic,quest=quest)
            self.controlScore(correct=correct)
                
        print(f'İsim: {self.name} Soyad: {self.surname} Score: {self.score}')
    
question1=Question(text='Hangisi bir yazılım dilidir?',choices=['S','R','K','N','Ç'],answer='R')
question2=Question(text='Yılan sembolü kullanan yazılım dili nedir?',choices=['R','Dart','C++','C#','Python'],answer='Python')
question3=Question(text='Hangi Yazılım dili daha eskidir?',choices=['C#','BASIC','Java','Python','Dart'],answer='BASIC')
question4=Question(text='Hangi Yazılım dili daha kolay yazım şekline sahiptir?',choices=['C++','Python','Java','C','Ruby'],answer='Python')

questions=[question1,question2,question3,question4]

            
quiz=Quiz(questions=questions,name='Sinan', surname='Uyğun')

quiz.display()
