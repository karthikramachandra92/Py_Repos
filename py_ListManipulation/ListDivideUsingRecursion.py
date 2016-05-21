import sys
from pprint import pprint

class ListReduce(object):
    
    def __init__(self,list_input):
        self.mainList = list_input
        self.dividedList_dict = {}
        self.gb_Counter = 0
        
    def recursive_half(self,inList):

        if(len(inList) < 2):
            return inList
        if(len(inList) == 2):
            self.dividedList_dict[self.gb_Counter] = inList
            self.gb_Counter = self.gb_Counter + 1
            #print inList
            return inList
        if(len(inList) > 2):
            #Calling Left Recursive
            inList_L = self.recursive_half(inList[:abs(len(inList)/2)])
            #Calling Right Recursive
            inList_R = self.recursive_half(inList[abs(len(inList)/2):])
            if(len(inList_L) != 0 and len(inList_R) != 0):
                # Adding two lists
                inList_L = inList_L + inList_R
            elif(len(inList_L) == 0 and len(inList_R) != 0):
                # Adding two lists
                inList_L = inList_R
            else:
                pass
            self.dividedList_dict[self.gb_Counter] = inList_L
            self.gb_Counter = self.gb_Counter + 1
            #print inList_L
            return inList_L
        return inList
            
    def getOrganizedDict(self):
        retList = self.recursive_half(self.mainList)
        if(retList == self.mainList):
            pprint(self.dividedList_dict)
            print "List Reduction Successful!!"
        else:
            pprint(self.dividedList_dict)
            print "Reduction Failed"

def main():
    if(len(sys.argv) == 2):
        ListReduce_Obj = ListReduce(sys.argv[1])
    else:
        mList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        ListReduce_Obj = ListReduce(mList)
    ListReduce_Obj.getOrganizedDict()    
    
def usage():
    print "\n Please provide correct Input parameters. \n Usage: vivek.py <LIST_TO_BE_REDUCED>"
    
if __name__ == "__main__":
    if(len(sys.argv) <= 2):
        main()
    else:
        usage()