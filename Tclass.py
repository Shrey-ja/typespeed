import random as rand
class typer:
    @staticmethod
    def give_words():
        s=['Hi,How are you','hello, im a guy','no i do not want your juice','help this nigga is chasing me ','haha imagine dying']
        return rand.choice(s)
    @staticmethod
    def type_speed():
        import time as t
        start=t.time()
        inp=input("type=>")
        end=t.time()
        total=end-start
        print(f" answered in:{total:.2f}sec")
        return total,inp
    @staticmethod
    def valid(inp,sentence):
        counter=0
        for word1,wordinp in zip(sentence.split(),inp.split()):
            if word1 == wordinp:
                counter+=1
            else:
                continue
        return counter
    @staticmethod
    def accuracy(counter,sen):
        total=len(sen.split())
        return (counter/total)*100 if total > 0 else 0
    
    @staticmethod
    def wpm(inp,sentence):
        total=len(sentence)
        correct=0
        for i,ch in enumerate(inp):
            if i<total and ch==sentence[i]:
                correct+=1
        return correct/total if total > 0 else 0