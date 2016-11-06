from subprocess import call
from multiprocessing import Process
import os, sys

pList = sys.argv[1]

#hostList = ["tayodroid0","tayodroid1"]

nextAvHost = 0
allProcs = []

hostList = ["tayodroid0","tayodroid1","tayodroid2","tayodroid3","servi_01","servi_02"
,"servi_03","servi_04","servi_05","servi_06","servi_07","servi_08","servi_09","servi_10"
,"servi_11","servi_12","servi_13","servi_14","servi_15","servi_16"];





def GenNgram_parallel(host,dir,trainingDir,testingFile):
	#print(dir)
	call(["ssh",host,"python3 "+dir+"trainNGram.py",trainingDir,testingFile])
	#call(["ssh",host,"ls","-l"])
	

def GetNextAvHost():
	hostToUse = "";
	global nextAvHost;
	while(hostToUse == ""):
		#if os.system("ping -c 1 " + hostList[nextAvHost]) == 0:
		hostToUse = hostList[nextAvHost]
		nextAvHost = (nextAvHost + 1)%len(hostList)
	return hostToUse
	
def SetupGramThreads(argsList):
	
	for i in range(len(argList)):
		currHost = GetNextAvHost()
		if(i > 0 and i%2 == 0):
			#print("i: %d, %s,%s, %s" i argList[i-2] argList[i-1] argList[i])
			allProcs.append(Process(target=GenNgram_parallel, args=(currHost,argList[i-2],argList[i-1],argList[i])))
			
	for i in range(len(allProcs)):
		print("proc: " + str(i))
		allProcs[i].start()
		allProcs[i].join()

if __name__ == '__main__':
	argList = [];
	#Get all arguments in for the n-gram development
	with open(pList, 'r') as f:
		for line in f:
			for s in line.split(' '):
				argList.append(s)
	#print(argList[5])
	#SetupGramThreads(argList)
	p1 = Process(target=GenNgram_parallel, args=("tayodroid0",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p2 = Process(target=GenNgram_parallel, args=("tayodroid1",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p3 = Process(target=GenNgram_parallel, args=("tayodroid2",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p4 = Process(target=GenNgram_parallel, args=("tayodroid3",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p5 = Process(target=GenNgram_parallel, args=("servi_01",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p6 = Process(target=GenNgram_parallel, args=("servi_02",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p7 = Process(target=GenNgram_parallel, args=("servi_03",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p8 = Process(target=GenNgram_parallel, args=("servi_04",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p9 = Process(target=GenNgram_parallel, args=("servi_05",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p10 = Process(target=GenNgram_parallel, args=("servi_06",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p11 = Process(target=GenNgram_parallel, args=("servi_07",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p12 = Process(target=GenNgram_parallel, args=("servi_08",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p13 = Process(target=GenNgram_parallel, args=("servi_09",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p14 = Process(target=GenNgram_parallel, args=("servi_10",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p15 = Process(target=GenNgram_parallel, args=("servi_11",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p16 = Process(target=GenNgram_parallel, args=("servi_12",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p17 = Process(target=GenNgram_parallel, args=("servi_13",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p18 = Process(target=GenNgram_parallel, args=("servi_14",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	p19 = Process(target=GenNgram_parallel, args=("servi_15",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))
	#p20 = Process(target=GenNgram_parallel, args=("servi_16",'/home/odroid/Documents/', '/home/odroid/Documents/nGramData/', '/home/odroid/Documents/nGramData/out_23.txt'))

	
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p5.start()
	p6.start()
	p7.start()
	p8.start()
	p9.start()
	p10.start()
	p11.start()
	p12.start()
	p13.start()
	p14.start()
	p15.start()
	p16.start()
	p17.start()
	p18.start()
	p19.start()
	#p20.start()
	
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	p7.join()
	p8.join()
	p9.join()
	p10.join()
	p11.join()
	p12.join()
	p13.join()
	p14.join()
	p15.join()
	p16.join()
	p17.join()
	p18.join()
	p19.join()
	#p20.join()
	