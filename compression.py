fname = input("Enter the file name to compress: ")          #압축할 파일이름을 입력 받는다
f=open(fname+".txt",'r+')                                   #압축할 파일이름을 연다
r=open("compress_"+fname+".txt",'w+')                       #압축될 파일이름을 만든어 파일을 만든다

if(f==-1):                                                  #만약 파일이 없다면 파일을 열수없다고 출렧하고 프로그램을 종료한다
    print ("File cannot be opened: ", fname)
    exit()

data=f.readlines()                                          #파일을 리스트로 줄단위로 읽어온다
count=1                                                     #읽는 숫자에 대해서 숫자의 량을 측정할 변수를 생성한다

for i in data:                                              #리스트로 읽어온 데이터를 줄단위로 끊어서 읽는다
    for j in range(len(i)):                                 #문자 단위로 끊어서 읽어간다
        if(j+1<len(i) and i[j]==i[j+1]):                    #만약 문자가 끝이아니고 문자가 다음 문자와 같다고 판단되면
            count+=1                                        #숫자의 측정을 증가시킨다
        elif(count>=5):                                     #만약 문자가 다음문자가 같지않고 5이상이라면
            r.write(i[j]+"("+str(count)+")")                #문자와 괄호를 치고 숫자의 량만큼 적은다음 괄호를 닫아준다
            count=1                                         #숫자의 량를 1로 초기화 한다
        else:                                               #만약 문자가 5미만이고 만자가 같지않다면
            r.write(i[j]*(count))                           #문자의 량만큼 문자를 출력한고
            count=1                                         #숫자의 량을 1로 초기화한다
print("compress_"+fname)                                    #그리고 압축된 파일의 이름을 출력하여 준다
