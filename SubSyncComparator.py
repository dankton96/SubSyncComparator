import platform, os
import easygui
os.system("python -m pip install -r requirements.txt")
from charset_normalizer import CharsetNormalizerMatches as CnM
##################################################################
if platform.system()=="Linux":
    os.system("xrdb -load /dev/null")
    os.system("xrdb -query")

nums=['0','1','2','3','4','5','6','7','8','9']
numsPos=[0,1,3,4,6,7,9,10,11,17,18,20,21,23,24,26,27,28]
ColonsPos=[2,5,19,22]
CommasPos=[8,25]
##################################################################
def IsSubTimeLine(strP):
        if len(strP)!=30:
            return False
        else:
            numst=[]
            for p in numsPos:
                if strP[p] not in nums:
                    return False
            for n in ColonsPos:
                if strP[n]!=':':
                    return False
            for n1 in CommasPos:
                if strP[n1]!=',':
                    return False
            if strP[13:16]!='-->':
                return False
        return True
######################################################################################
def ClearScreen():
    if platform.system()=="Windows":
        os.system("cls")
    if platform.system()=="Linux":
        os.system("clear")
######################################################################################
ClearScreen()
ModelPath=easygui.fileopenbox("Selecione a legenda modelo:")
TargetPath=easygui.fileopenbox("Selecione a legenda alvo:")
######################################################################################
ModelCoding=CnM.from_path(ModelPath).best().first().encoding
TargetCoding=CnM.from_path(TargetPath).best().first().encoding
######################################################################################

ModelSub=open(ModelPath,encoding=ModelCoding)
TargetSub=open(TargetPath,encoding=TargetCoding)
ModelContent=ModelSub.readlines()
TargetContent=TargetSub.readlines()
i=0
ModelTimesPos=[]
for l in ModelContent:
    if IsSubTimeLine(l):
        ModelTimesPos.append(i)
    i+=1
i=0
TargetTimesPos=[]
for l in TargetContent:
    if IsSubTimeLine(l):
        TargetTimesPos.append(i)
    i+=1
ModelTimesPos.sort()
TargetTimesPos.sort()
if(ModelTimesPos==TargetTimesPos):
    print("Legendas sincronizadas:\n")
    print(ModelPath,TargetPath,sep='\n')
else:
    print("A legenda alvo está dessincronizada em relação a legenda modelo")
input("\n\n\n\nPressione enter para encerrar o programa")
ClearScreen()
ModelSub.close()
TargetSub.close()