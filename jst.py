# AND GATE
# 1 1 1
# 1 0 0
# 0 1 0
# 0 0 0

# OR GATE
# 1 1 1
# 1 0 1
# 0 1 1
# 0 0 0

# while(epoch menggasilkan error)
# err=T-O
# if Err<>0 then
#   Wj=Wj+LR*Ij*Err
# endif
# end

# Ij = input dari neuron
# Wj = bobot dari input neuron (Ij) ke output neuron
# LR = Learning rate
# T  = nilai training
# Err= nilai error

import random
import time

class singleperceptron:
    def __init__(self):
        self.w1=1
        self.w2=1
        self.x1=1
        self.x2=1
        self.output=1
        self.learningrate=1/5
        
    def hitung(self,x1,x2):
        output=x1*self.w1+x2*self.w2
        return self.linear(output)
    
    def linear(self,x):
        if(x>=2):
            return 1
        return 0

    def training(self,dataset):
        self.w1=round(random.uniform(-1,1),2)
        self.w2=round(random.uniform(-1,1),2)
        iserror=True
        while(iserror):
            iserror=False
            print(f'\nw1 old -> {self.w1}')
            print(f'w2 old -> {self.w2}')
            for i in range(len(dataset)):
                hasil=self.hitung(dataset[i][0],dataset[i][1])
                error=dataset[i][2]-hasil
                if(error):
                    iserror=True
                    self.w1+=self.learningrate+dataset[i][0]*error
                    self.w2+=self.learningrate+dataset[i][1]*error
                    self.w1=round(self.w1,2)
                    self.w2=round(self.w2,2)
                print(f'{dataset[i][0]} {dataset[i][1]} {dataset[i][2]} {hasil} error = {error}')
            print(f'\nw1 new -> {self.w1}')
            print(f'w2 new -> {self.w2}\n')

class doubleperceptron:
    def __init__(self):
        self.w13=1
        self.w23=1
        self.w14=1
        self.w24=1
        self.w35=1
        self.w45=1
        self.x1=1
        self.x2=1
        self.h1=1
        self.h2=1
        self.output=1
        self.learningrate=1/5
        
    def hitung(self,x1,x2,w1,w2,bias):
        output=x1*w1+x2*w2+bias
        return self.linear(output)
    
    def linear(self,x):
        if(x>=1):
            return 1
        return 0

    def training(self,dataset):
        self.w13=round(random.uniform(-1,1),2)
        self.w23=round(random.uniform(-1,1),2)
        self.w14=round(random.uniform(-1,1),2)
        self.w24=round(random.uniform(-1,1),2)
        self.w35=round(random.uniform(-1,1),2)
        self.w45=round(random.uniform(-1,1),2)
        # self.w13=20
        # self.w23=20
        # self.w14=-20
        # self.w24=-20
        # self.w35=20
        # self.w45=20
        iserror=True
        k=0
        while(iserror):
            iserror=False
            print(f'\nw13 old -> {self.w13}')
            print(f'w23 old -> {self.w23}')
            print(f'w14 old -> {self.w14}')
            print(f'w24 old -> {self.w24}')
            print(f'w35 old -> {self.w35}')
            print(f'w45 old -> {self.w45}')
            for i in range(len(dataset)):
                h1=self.hitung(dataset[i][0],dataset[i][1],self.w13,self.w23,-10)
                h2=self.hitung(dataset[i][0],dataset[i][1],self.w14,self.w24,30)
                hasil=self.hitung(h1,h2,self.w35,self.w45,-30)
                error=dataset[i][2]-hasil
                if(error):
                    iserror=True

                    self.w13=round(self.w13+self.learningrate+dataset[i][0]*error,2)
                    self.w23=round(self.w23+self.learningrate+dataset[i][1]*error,2)
                    self.w14=round(self.w14-self.learningrate+dataset[i][0]*error,2)
                    self.w24=round(self.w24-self.learningrate+dataset[i][1]*error,2)
                    self.w35=round(self.w35+self.learningrate+h1*error,2)
                    self.w45=round(self.w45+self.learningrate+h2*error,2)

                print(f'{dataset[i][0]} {dataset[i][1]} {dataset[i][2]} {hasil} error = {error}')
            print('')
            print(f'w13 new -> {self.w13}')
            print(f'w23 new -> {self.w23}')
            print(f'w14 new -> {self.w14}')
            print(f'w24 new -> {self.w24}')
            print(f'w35 new -> {self.w35}')
            print(f'w45 new -> {self.w45}')
            print('')
            k+=1
            if k==1 and False:
                break

def main():
    dataset_and=((1,1,1),(1,0,0),(0,1,0),(0,0,0))
    dataset_or=((1,1,1),(1,0,1),(0,1,1),(0,0,0))
    dataset_xor=((1,1,0),(1,0,1),(0,1,1),(0,0,0))
    gate=singleperceptron()
    gatexor=doubleperceptron()
    while True:
        print('===========================')
        print('===========================')
        print('===========================')
        print('===========================')
        print('1. AND gate')
        print('2. OR gate')
        print('3. XOR gate')
        print('4. exit')
        menu=input('menu: ')
        if menu == '1':
            gate.training(dataset_and)
        elif menu == '2':
            gate.training(dataset_or)
        elif menu == '3':
            gatexor.training(dataset_xor)
        elif menu == '4':
            break

    

if(__name__=='__main__'):
    main()