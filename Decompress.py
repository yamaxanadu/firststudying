fname = input("Enter the file name to decompress: ")    #압축풀 파일이름을 입력 받는다
f=open(fname+".txt",'r+')                               #압축풀 파일이름을 연다
r=open("decompress_"+fname+".txt",'w+')                 #압축풀 파일이름을 만든어 파일을 만든다
if(f==-1):                                              #
    print ("File cannot be opened: ", fname)            #만약 파일이 없다면 파일을 열수없다고 출렧하고 프로그램을 종료한다
    exit()

#파일을 리스트로 줄단위로 읽어온다
data=f.readlines()

for i in data:
    k=0
    j=0
    #리스트로 읽어온 데이터를 줄단위로 끊어서 읽는다
    while(j<len(i)):
        #문자 단위로 끊어서 읽는다
        if(j+1<len(i) and i[j+1]=="("):
            tmp=i[j]
            j+=2
            while(i[j]!=")"):
                k=(k*10+int(i[j]))
                j+=1
                #문자열을 숫자로 바꿔주는 역활을 한다
            r.write(tmp*k)
            k=0
            #닫힌 괄호를 만난다면 문자를 문자열을 숫자로 바꾼만큼 곱해서 출력한다
        else:
            r.write(i[j])
            #괄호를 만나지 않는다면 문자를 그대로 출력하여준다
        j+=1
        #문장을 문자로 인덱싱을 하면서순서대로 읽기위하여 index j를 증가시켜 다음 문자를 읽게 만든다
