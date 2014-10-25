import sys
import random 
def Costos():
    a=0
    suma=0
    while a<m:
        xi=xs[a]
        val=0
        i=0
        while i<len(xi):
	        val=val+xi[i]*tethas[i]
	        i=i+1
        val=val-ys[a]
        val=val*val
        #print str(a)+":"+str(val)
        suma=suma+val
        #print 'suma('+str(a)+"):"+str(suma)
        a=a+1
    return (1/float(2*m))*suma
def Optimizar():
    nt=0
    newtethas=[]
    while nt<len(tethas):
        tetha=0
        a=0
        suma=0
        while a<m:
            xi=xs[a]
            val=0
            i=0
            while i<len(xi):
    	        val=val+xi[i]*tethas[i]
    	        i=i+1
            val=val-ys[a]
            val=val*xi[nt]
            #print str(a)+":"+str(val)
            suma=suma+val
            #print 'suma('+str(a)+"):"+str(suma)
            a=a+1
        tetha= tethas[nt]-(alfa/float(m))*suma
        newtethas.append(tetha)
        nt=nt+1
    return newtethas
f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'r')
xs=[]
ys=[]
l1 = f1.readline().replace('\n','')
l2 = f2.readline().replace('\n','')
while l1 and l2:
    xsl=[]
    for num in l1.split(','):
        xsl.append(float(num))
    xs.append(xsl)
    ys.append(float(l2))
    l1 = f1.readline().replace('\n','')
    l2 = f2.readline().replace('\n','')
n=len(xs[0])
m=len(ys)
alfa=float(sys.argv[3])
iteraciones=int(sys.argv[4])
tolerancia=float(sys.argv[5])
tethas=[]
for val in xs[0]:
    tethas.append(random.uniform(-10,10))
print ('n:'+str(n))
print ('m:'+str(m))
print ('alpha:'+str(alfa))
print ('iteraciones:'+str(iteraciones))
print ('tolerancia:'+str(tolerancia))
print ('tethas iniciales:'+str(tethas))
print ('Costos Inicial:'+str(Costos()))
rep=0
f=open("costos.txt","w")
f.write(str(Costos())+"\n")
while rep<iteraciones and Costos()>=tolerancia:
    tethas=Optimizar()
    f.write(str(Costos())+"\n")
    rep=rep+1
f.close()
print ('Tethas Finales:'+str(tethas))