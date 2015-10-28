import sys

if __name__ == "__main__":

  g = open("tracklets_out_clean.dat","rb")
  out = open("tracklets_out_Bin.dat","w")
  
  
  for line in g:
    ln = line.split(" ")
    lstub1 =list( bin(int(ln[0],16)) )
    lstub2 =list( bin(int(ln[1],16)) )
    
    ltracklet = list( bin(int(ln[3],16)) )
  
    lfittrack = list( bin(int(ln[5],16)) )
    

    #Stub Pairs

    if( len(lstub1) == 38 and len(lstub2) == 38 ) :
      sb1pt = str(lstub1[2]) + str(lstub1[3]) + str(lstub1[4])
      sb2pt = str(lstub2[2]) + str(lstub2[3]) + str(lstub2[4])
      sb1r = ""
      sb2r = ""
      
      sb1z = ""
      sb2z = ""
    
      sb1phi = ""
      sb2phi = ""
    
      
  
      for i in range(5,12):
             sb1r += str(lstub1[i])
             sb2r += str(lstub2[i])
    
             
      for i in range(12,24):
             sb1z += str(lstub1[i])
             sb2z += str(lstub2[i])
           
      for i in range(24,len(lstub1)):
             sb1phi += str(lstub1[i])
             sb2phi += str(lstub2[i])
    
      #Tracklets
      trlrinv  = ""
      trlphi0  = ""
      trlz     = ""
      trlt     = ""
      
      print len(ltracklet)
      if(len(ltracklet) == 58 ):
        
        for i in range(2,16):
          trlrinv += ltracklet[i]
        for  i in range(16,34):
          trlphi0 += ltracklet[i]
        for i in range(34,44):
          trlz += ltracklet[i]
        for i in range(44,58):
          trlt += ltracklet[i]

          
    


      #Final Tracks 
      ftrkrinv  = ""
      ftrkphi0  = ""
      ftrkz     = ""
      ftrkt     = ""

      print len(lfittrack)
      
      if(len(lfittrack) == 61 ):
        
        for i in range(2,17):
          ftrkrinv += lfittrack[i]
        for  i in range(17,36):
          ftrkphi0 += lfittrack[i]
        for i in range(36,47):
          ftrkt += lfittrack[i]
        for i in range(47,61):
          ftrkz += lfittrack[i]


          
      #print "STUB full:", bin(int(ln[0],16)) ,"pt1: ",sb1pt,"r1: ",sb1r," z:",sb1z," phi: ",sb1phi
      print "TRACKLET full:", bin(int(ln[3],16)), "    ",ln[3]  ,"rinv: ",trlrinv,"phi0: ",trlphi0," z:",trlz," t: ",trlt
      print "FinalTRACK full:", bin(int(ln[5],16)), "    ",ln[5]  ,"rinv: ",ftrkrinv,"phi0: ",ftrkphi0," z:",ftrkz," t: ",ftrkt
  
