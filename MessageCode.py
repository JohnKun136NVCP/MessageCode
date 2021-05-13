import numpy as np
import os
import time
def Main():
    flag=True
    while flag:
        print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮")
        print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃")
        print("╭╮╭┳━━┳━━┳━━┳━━┳━━┳━━╮╭━━┳━╮╭━━┳━━┳━╯┣━━┳━╮")
        print("┃╰╯┃┃━┫━━┫━━┫╭╮┃╭╮┃┃━┫┃┃━┫╭╮┫╭━┫╭╮┃╭╮┃┃━┫╭╯")
        print("┃┃┃┃┃━╋━━┣━━┃╭╮┃╰╯┃┃━┫┃┃━┫┃┃┃╰━┫╰╯┃╰╯┃┃━┫┣╮")
        print("╰┻┻┻━━┻━━┻━━┻╯╰┻━╮┣━━╯╰━━┻╯╰┻━━┻━━┻━━┻━━┻┻╯")
        print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃")
        print("╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯")
        print("")
        print("Cretor:")
        print("╭━┳━┳━┳━━┳━┳━┳━╮")
        print("┃╋┃╋┃┃┣╮╭┫┳┫╭┫┃┃")
        print("┃╭┫╮┫┃┃┃┃┃┻┫╰┫┃┃")
        print("╰╯╰┻┻━╯╰╯╰━┻━┻━╯")
        print("Choose an option: ")
        print("1. Code")
        print("2. Decode")
        print("3. Quit")
        try:
            op=int(input("====> "))
            if op==1:
                word=input("Write your message: ")
                clw=Cleankey(word)
                ma=Matrixcoord(clw)
                Encryptcode(word,ma)
                time.sleep(3)
                flag=False
                break
            elif op==2:
                code=input("Type your code: ")
                mat=Matrix_Inverse(code)
                cmat=Clean_Matrix(mat)
                Decoded_Word(code,cmat)
                time.sleep(3)
                flag=False
                break
            elif op==3:
                quit()
                break
            elif op!=1 or op!=2:
                print("Not valid option")
        except ValueError:
            print("You typed other key")
            time.sleep(1.5)
            if os.name=="posix":
                os.system('clear')
            elif os. name=="ce" or os.name=="nt" or os.name=="dos":
                os.system("cls")
def Cleankey(key):
    key=key.replace(' ','')
    key=key.upper()
    key_1=list()
    for i in key:
        key_1.append(i)
    for k in range(len(key_1)):
        if key_1[k]=='J' or key_1[k]=='I':
            key_1[k]='I/J'
    return key_1

def Matrixcoord(woldkey):
    cordination=list()
    coord=np.array([['A','B','C','D','E'],['F','G','H','I/J','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']])    
    for i in range(len(woldkey)):
        for x, row in enumerate(coord):
            for y, elemment in enumerate(row):
                if elemment==woldkey[i]:
                    cordination.append(9-x)
                    cordination.append(y)
    matrix_code=[str(x) for x in cordination]
    matrix_code=''.join(matrix_code)
    return matrix_code

def Encryptcode(message,matrix_not_null):
    print("Your original message: ",''.join(message))
    print("Your message has been coded: ",matrix_not_null)

def Matrix_Inverse(ls):
	coord=np.array([['A','B','C','D','E'],['F','G','H','I/J','K'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z'] ])
	tem_a=list()
	tem_c=list()
	tem_d=list()
	prueba=list()
	prueba3=list()
	for i in range(len(ls)):
		tem_a.append(int(ls[i]))
	flag1=0
	flag2=0
	for flag1, i in enumerate(tem_a):
		if flag1%2==1:
			tem_c.append(i)
	for flag2, i in enumerate(tem_a):
		if flag2%2==0:
			tem_d.append(i)

	for x in zip(tem_d,tem_c):
		prueba.append((x[0],x[1]))
	
	for x in (prueba):
		if x==(9,0):
			prueba3.append(coord[0][0])
		elif x==(9,1):
			prueba3.append(coord[0][1])
		elif x==(9,2):
			prueba3.append(coord[0][2])
		elif x==(9,3):
			prueba3.append(coord[0][3])
		elif x==(9,4):
			prueba3.append(coord[0][4])
		elif x==(8,0):
			prueba3.append(coord[1][0])
		elif x==(8,1):
			prueba3.append(coord[1][1])
		elif x==(8,2):
			prueba3.append(coord[1][2])
		elif x==(8,3):
			prueba3.append(coord[1][3])
		elif x==(8,4):
			prueba3.append(coord[1][4])
		elif x==(7,0):
			prueba3.append(coord[2][0])
		elif x==(7,1):
			prueba3.append(coord[2][1])
		elif x==(7,2):
			prueba3.append(coord[2][2])
		elif x==(7,3):
			prueba3.append(coord[2][3])
		elif x==(7,4):
			prueba3.append(coord[2][4])
		elif x==(6,0):
			prueba3.append(coord[3][0])
		elif x==(6,1):
			prueba3.append(coord[3][1])
		elif x==(6,2):
			prueba3.append(coord[3][2])
		elif x==(6,3):
			prueba3.append(coord[3][3])
		elif x==(6,4):
			prueba3.append(coord[3][4])
		elif x==(5,0):
			prueba3.append(coord[4][0])
		elif x==(5,1):
			prueba3.append(coord[4][1])
		elif x==(5,2):
			prueba3.append(coord[4][2])
		elif x==(5,3):
			prueba3.append(coord[4][3])
		elif x==(5,4):
			prueba3.append(coord[4][4])
	return prueba3

    
def Clean_Matrix(codeword):
	codeword=''.join(codeword)
	return codeword

def Decoded_Word(code,decode):
	print("Your code word is: ",code)
	print("Your decode word is: ",decode)

Main()

