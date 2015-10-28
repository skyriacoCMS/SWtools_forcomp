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
    f = open("../fpga_emulation/StubPairs_SP_"+sector+".dat", "rb")
    
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
                strl.append(line)
#                print strl, "inside the function"
    return strl


def TrackletPars(sector,ev):
    f = open("../fpga_emulation/TrackletParameters_TPAR_"+sector+".dat", "rb")
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
                strl.append(line)
    return strl

def TrackFitpEv(sector,ev):
    f = open("../fpga_emulation/TrackFit_TF_"+sector+".dat", "rb")
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
                strl.append(line)
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
    gstub = open("../fpga_emulation/Stubs_Pairs_all.txt","w") 
    gtrackl = open("../fpga_emulation/Tracklets_all.txt","w") 
    gfitt = open("../fpga_emulation/FinalTracks_all.txt","w") 
    
    for ev in range (1,101):   
        print "event" ,ev
        SPnames = open("../fpga_emulation/SPnames.txt","rb")
        TPnames = open("../fpga_emulation/TPnames.txt","rb")
        TFnames = open("../fpga_emulation/TFnames.txt","rb")
       
        for line in SPnames:
            fn = line.rstrip('\n')
            for sect in range (1,5):
                sector = fn+"_0"+str(sect)
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
      
