a={}
dc={}
ref={'A':8.167,'B':1.492,'C':2.782,'D':4.253,'E':12.702,'F':2.228,'G':2.015,'H':6.094,'I':6.966,'J':0.153,'K':0.772,'L':4.025,'M':2.406,'N':6.749,'O':7.507,'P':1.929,'Q':0.095,'R':5.987,'S':6.327,'T':9.056,'U':2.758,'V':0.978,'W':2.360,'X':0.150,'Y':1.974,'Z':0.074}
import operator
ref= sorted(ref.iteritems(), key=operator.itemgetter(1))
ref=ref[-1::-1]
for i in range(0,26):
    a[chr(65+i)]=0
fob=open('text.txt','r')
i=0
j=0
k=list(fob.read())
while(j<len(k)):
    o=ord(k[j])
    if(o>96 and o<123):
        o-=32
    if(o>64 and o<91):
        i+=1
        a[chr(o)]+=1
    j+=1
j+=0.0
for i in range(0,26):
    a[chr(65+i)]=(a[chr(65+i)]*100)/j
import operator
a= sorted(a.iteritems(), key=operator.itemgetter(1))
a=a[-1::-1]
for i in range(0,26):
    dc[a[i][0]]=ref[i][0]
fob.close()
fob=open('text.txt','r')
i=0
j=0
k=list(fob.read())
while(j<len(k)-1):
    o=ord(k[j])
    if(o>96 and o<123):
        k[j]=chr(o-32)
        o-=32
    if(o>64 and o<91):
        k[j]=dc[k[j]]
    j+=1
k=''.join(k)
fout=open('output.txt','w')
fout.write(k)
fout.close()

    
    
