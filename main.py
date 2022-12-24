import random
import sys
class cell_auto:
    def __init__(self,X,Y,percent):
        self.__X=X
        self.__Y=Y
        self.__percent=percent
        field=[[0]*X for i in range(Y)]
        self.__field=field
    @property
    def field(self):
        return self.__field
    @property
    def X(self):
        return self.__X
    @X.setter
    def X(self,val):
        if val<0:
            print('ОШИБКА')
        else:
            self.__X=val
    @property
    def Y(self):
        return self.__Y
    @Y.setter
    def Y(self,val):
        if val<0:
            print('ОШИБКА')
        else:
            self.__Y=val
    @property
    def percent(self):
        return self.__percent
    @percent.setter
    def percent(self,val):
        if val<0 or val>100:
            print('ОШИБКА')
        else:
            self.__percent=val
    def updating(self,cell_auto):
        for i in range(0,self.__X):
            for j in range(0,self.__Y):
                if random.randint(1,100)<=self.__percent:
                    self.__field[j][i]=1
        display(self.__field)
        while True:
            move=input('НАЖМИТЕ ЛЮБУЮ КЛАВИШУ ДЛЯ ПРОДОЛЖЕНИЯ ИЛИ ВВЕДИТЕ (off) ДЛЯ ЗАВЕРШЕНИЯ ОПЕРАЦИИ: ')
            self.__buffer=[[0]*self.__X for i in range(self.__Y)]
            cell_auto.neighbors()
            display(self.__buffer)
            self.__field=self.__buffer
            if move=='off':
                break
    def neighbors(self):
        for i in range(0,self.__X):
            for j in range(0,self.__Y):
                k=0
                for p in range(i-1,i+2):
                    for r in range(j-1,j+2):
                        if (p==i and r==j) or p==-1 or r==-1 or p==self.__X or r==self.__Y:
                            continue
                        elif self.__field[r][p]==1:
                            k+=1
                if self.__field[j][i]==1:
                    if k==2 or k==3:
                        self.__buffer[j][i]=1
                    else:
                        self.__buffer[j][i]=0
                elif self.__field[j][i]==0:
                    if k==3:
                        self.__buffer[j][i]=1
                    else:
                        self.__buffer[j][i]=0
def display(field):
        for i in range(0,len(field)):
            for j in range(0,len(field[i])):
                print(field[i][j],end=' ')
            print()
        print()
def main():
    cell_auto1 = cell_auto(7,7,50)
    cell_auto1.updating(cell_auto1)
main()
