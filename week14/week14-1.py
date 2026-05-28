#week14-1.py CPE 2026-05-26
t=1
while True: #step1
	M,N=list(map(int,input().split()))#step
	if M==0 and N==0:break#step1:input
	a=[]
	for i in range(M):
		a.append(list(input()))#step3:list()

	for i in range(M):
		for j in range(N):
			if a[i][j]=='*':continue#step6
			a[i][j]=0 #step6
			for ii in range(i-1,i+2): #step4
				for jj in range(j-1,j+2):
					if ii<0 or jj<0 or ii>=M or jj>=N:
						continue #step5
					if a[ii][jj]=='*':#step6
						a[i][j]+=1#step6

	if t>1:print()	#step2:Output
	print(f'Field #{t}:') #step2:Output
	for i in range(M): #step2:Outp
		#print(a[i])
		for j in range(N):
			print(a[i][j],end='')
		print()
	t+=1
