#!/usr/bin/python
import os

##################################################################################################
#
#
#
#
#
#    Functions for Data extraction from memories
#
#                                                                     -Savvas K
##################################################################################################
            





            
def StubPairs(sector,ev):
    f = open("StubPairs_SP_"+sector+".dat", "rb")
    
    strl = []

    i = 0
    for line in f:
        string = line.split(" ")
        if ( len(string) == 6 and string[3] == "Event" and string[5] == str(ev)+"\n" ):
            i = 1
        elif "Event : " in line:
            i = 0
        else :
            if i == 1 : 
                wriout = string[0]+" "+hex(int(string[1],2))+" "+hex(int(string[2],2)) 
                strl.append(wriout)
#                print strl, "inside the function"
    return strl


def TrackletPars(sector,ev):
    f = open("TrackletParameters_TPAR_"+sector+".dat", "rb")
    strl = []

    i = 0
    for line in f:
        string = line.split(" ")
        if ( len(string) == 6 and string[3] == "Event" and string[5] == str(ev)+"\n" ):
            i = 1
        elif "Event : " in line:
            i = 0
        else :
            if i == 1 : 
                stub=string[1].replace("|","")
                hexified =(string[0]+" "+hex(int(stub,2)))
                strl.append(hexified)
    return strl

def TrackFitpEv(sector,ev):
    f = open("TrackFit_TF_"+sector+".dat", "rb")
    strl = []
    
    i = 0
    for line in f:
        string = line.split(" ")
        if ( len(string) == 6 and string[3] == "Event" and string[5] == str(ev)+"\n" ):
            i = 1
        elif "Event : " in line:
            i = 0
        else :
            if i == 1 : 
                second = string[1].split("|")
                #writout = string[0]+" "+second[0]+" "+second[1]+" "+second[2]+" "+second[3]
                tohex = second[0]+second[1]+second[2]+second[3]
                writout = string[0]+" "+hex(int(tohex,2))
                #print writout
                strl.append(writout)
    return strl
            

##################################################################################################
#
#
#
#
#
#    Main Script
#
#                                                                                  -Savvas K
##################################################################################################

if __name__ == "__main__":
    gstub = open("Stubs_Pairs_all.txt","w") 
    gtrackl = open("Tracklets_all.txt","w") 
    gfitt = open("FinalTracks_all.txt","w") 
    
    for ev in range (1,101):   
        print "event" ,ev
        SPnames = open("SPnames.txt","rb")
        TPnames = open("TPnames.txt","rb")
        TFnames = open("TFnames.txt","rb")
       
        for line in SPnames:
            fn = line.rstrip('\n')

            sector = fn
                #print sector
            strl = []
            strl = StubPairs(sector,ev)
            if(len(strl) > 0 ):
                for it in strl: 
                    writeout = it.rstrip("\n")+"  "+sector+" "+str(ev)+"\n" 
                    print writeout
                    gstub.write(writeout)
                
       
       
        for line in TPnames:
            fn = line.rstrip('\n')
            sector = fn
                #print sector
            strl = []
            strl = TrackletPars(sector,ev)
            if(len(strl) > 0 ):
                for it in strl: 
                    writeout = it.rstrip("\n")+"  "+sector+" "+str(ev)+"\n" 
                    print writeout
                    gtrackl.write(writeout)
                    
                
        for line in TFnames:
            fn = line.rstrip('\n')
            sector = fn
            strl = []
            strl = TrackFitpEv(sector,ev)
            if(len(strl) > 0 ):
                for it in strl: 
                    writeout = it.rstrip("\n")+"  "+sector+" "+str(ev)+"\n" 
                    print writeout
                    gfitt.write(writeout)
      
