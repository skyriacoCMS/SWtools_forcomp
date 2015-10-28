import os

def AllGlobal(layer,sector):
    f = open("../fpga_emulation/AllStubs_AS_L"+layer+"D3n1_"+sector+".dat", "rb")
    g = open("../fpga_emulation/AllStubs_AS_L"+layer+"D3n1_"+sector+"_hex.dat","w")
    for line in f:
        string = line.split(" ")
        if len(string) > 1 and not "Event" in line:
            #print hex(int(string[3],2))
            stub=string[1].replace("|","")
            g.write(string[0]+" "+hex(int(stub,2))+"\n")
        else:
            g.write(line)
def VM(layer,sector):
    if int(layer)%2 == 0:
        phi_max = 5
    else:
        phi_max = 4
    for i in range(1,phi_max):
        for j in range(1,3):
            f = open("../fpga_emulation/VMStubs_VMS_L"+layer+"D3PHI"+str(i)+"Z"+str(j)+"n1_"+sector+".dat", "rb")
            g = open("../fpga_emulation/VMStubs_VMS_L"+layer+"D3PHI"+str(i)+"Z"+str(j)+"n1_"+sector+"_hex.dat","w")
            for line in f:
                string = line.split(" ")
                if len(string) > 1 and not "Event" in line:
                    stub=string[1].replace("|","")
                    g.write(string[0]+" "+hex(int(stub,2))+"\n")
                else:
                    g.write(line)
def Raw(sector):
    f = open("../fpga_emulation/AllStubs_AS_L"+layer+"D3n1_04.dat", "rb")
    g = open("../fpga_emulation/AllStubs_AS_L"+layer+"D3n1_04_hex.dat","w")
    for line in f:
        string = line.split(" ")
        if len(string) > 1 and not "Event" in line:
            #print hex(int(string[3],2))
            stub=string[1].replace("|","")
            g.write(string[0]+" "+hex(int(stub,2))+"\n")
        else:
            g.write(line)
def Input(sector, region, link):
    f = open("../fpga_emulation/InputStubs_IL"+link+"_D3_"+sector+".dat", "rb")
    g = open("../fpga_emulation/InputStubs_IL"+link+"_D3_"+sector+"_hex.dat","w")
    #h = open('test.txt','r')
    for line in f:
        s = str(hex(int(line,2)))[2:]
        while len(s)<8:
            s = '0' + s
        g.write(s+"\n")
            
def Tracklet(sector):
    f = open("../fpga_emulation/TrackletParameters_TPAR_L1D3L2D3_"+sector+".dat", "rb")
    g = open("../fpga_emulation/TrackletParameters_TPAR_L1D3L2D3_"+sector+"_hex.dat","w")
    for line in f:
        string = line.split(" ")
        if len(string) > 1 and not "Event" in line:
            stub=string[1].replace("|","")
            g.write(string[0]+" "+hex(int(stub,2))+"\n")
        else:
            g.write(line)

def Projection(sector,layer):
    f = open("../fpga_emulation/TrackletProjections_TPROJ_L1D3L2D3_L"+layer+"D3_"+sector+".dat", "rb")
    g = open("../fpga_emulation/TrackletProjections_TPROJ_L1D3L2D3_L"+layer+"D3_"+sector+"_hex.dat","w")
    for line in f:
        if 'Event' not in line:
            string = line.split(" ")
            projection = string[1].replace("|","").replace("y","").replace('L','')
            g.write(string[0]+" "+hex(int(projection,2))+"\n")
        else:
            g.write(line)

def VMProj(sector):
    f = open("../fpga_emulation/VMProjections_"+sector+".txt", "rb")
    g = open("../fpga_emulation/VMProjections_"+sector+"_hex.txt","w")
    for line in f:
        if "xxxx" not in line:
            string = line.split(" ")
            vmproj = string[3].replace("|","")
            g.write(string[0]+" "+string[1]+" "+hex(int(vmproj.replace("x",""),2))+"\n")

def VMMatches(sector):
    f = open("../fpga_emulation/VMMatches_"+sector+".txt", "rb")
    g = open("../fpga_emulation/VMMatches_"+sector+"_hex.txt","w")
    for line in f:
        if "xxxxxxxxxxxx" not in line:
            string = line.split(" ")
            vmmatch = string[-1].replace("|","")
            g.write(string[0]+" "+string[1]+" "+hex(int(vmmatch.replace("x",""),2))+"\n")


def FullMatches(sector):
    f = open("../fpga_emulation/FullMatches_"+sector+".txt", "rb")
    g = open("../fpga_emulation/FullMatches_"+sector+"_hex.txt","w")
    for line in f:
        if "xxxxxxxxxxxx" not in line:
            string = line.split(" ")
            fmatch = string[-1].replace("|","")
            g.write(string[0]+" "+string[1]+" "+hex(int(fmatch.replace("y",""),2))+"\n")


def TrackletCands(sector):
    f = open("../fpga_emulation/TrackletCands_"+sector+".txt", "rb")
    g = open("../fpga_emulation/TrackletCands_"+sector+"_hex.txt","w")
    for line in f:
        if "xxxxxxxxxxxx" not in line:
            string = line.split(" ")
            cand = string[-1].replace("|","")
            g.write(string[0]+" "+string[1]+" "+hex(int(cand.replace("x",""),2))+"\n")



if __name__ == "__main__":
    layer = '1'
    link = '1'
    
    for s in range(1,5):
        for i in range(1,7):
            AllGlobal(str(i),'0'+str(s))
            VM(str(i),'0'+str(s))
            
        Tracklet('0'+str(s))
        Projection('0'+str(s),'3')
        Projection('0'+str(s),'4')
        Projection('0'+str(s),'5')
        Projection('0'+str(s),'6')
    #Raw(number)
    #Input('','','1')
    #Input('','','2')
    #Input('','','3')
    #Projection(number)
    #VMProj(number)
    #VMMatches(number)
    #FullMatches(number)
    #TrackletCands(number)
