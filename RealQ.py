import sys
import Kfactors
if __name__ == "__main__":


  Kfact = Kfactors._Const()
  g = open("tracklets_out_clean.dat","rb")
  outrl = open("tracklets_real.dat","w")
  oustb = open("stubpairs_real.dat","w")
  outrk = open("finaltracks_real.dat","w")
  
  
  for line in g:
    ln = line.split(" ")
    lstub1 =list( bin(int(ln[0],16)) )
    lstub2 =list( bin(int(ln[1],16)) )
    lstubpev = ln[3]
    ltracklet = list( bin(int(ln[5],16)) )
    ltrackletev = ln[7]
    lfit_unch = list(ln[9])
    trckfitstr = "".join(lfit_unch[16:len(lfit_unch)]) 
    lfittrack = list( bin(int(trckfitstr,16)) )
    lfittrackev = ln[11]

    #fixing strings lenghts 
    #Stubs
    mis = 38 - len(lstub1)
    lstub138 = []    
    for i in range (0,mis):
      lstub138 += "0"
    lstub138 += lstub1[2:len(lstub1)]
    
    
    mis = 38 - len(lstub2)
    lstub238 = []    
    for i in range (0,mis):
      lstub238 += "0"
    lstub238 += lstub2[2:len(lstub2)]


    #Tracklets
    mis = 58 - len(ltracklet)
    ltrl58 = []
    for i in range (0,mis):
      ltrl58 += "0"
    ltrl58 += ltracklet[2:len(ltracklet)]

    #Fittrack fix
    mis = 64 - len(lfittrack)
    lftrck62 = []
    for i in range (0,mis):
       lftrck62 +="0"   
    lftrck62 += lfittrack[5:len(lfittrack)]
    

    #Stub Pairs
    
    if( len(lstub138) == 36 and len(lstub238) == 36 ) :
      sb1pt = str(lstub138[0]) + str(lstub138[1]) + str(lstub138[2])
      sb2pt = str(lstub238[0]) + str(lstub238[1]) + str(lstub238[2])
      sb1r = ""
      sb2r = ""
      
      sb1z = ""
      sb2z = ""
    
      sb1phi = ""
      sb2phi = ""
    
      
  
      for i in range(3,10):
             sb1r += str(lstub138[i])
             sb2r += str(lstub238[i])
    
             
      for i in range(10,22):
             sb1z += str(lstub138[i])
             sb2z += str(lstub238[i])
           
      for i in range(22,len(lstub138)):
             sb1phi += str(lstub138[i])
             sb2phi += str(lstub238[i])

      #Conversion to reals. 

      sb1ptV =0     
      if(int(sb1pt,2) == 0 ): sb1ptV = 1/0.4 
      if(int(sb1pt,2) == 1 ): sb1ptV = 1/0.3 
      if(int(sb1pt,2) == 2 ): sb1ptV = 1/0.2 
      if(int(sb1pt,2) == 3 ): sb1ptV = 1/0.1 
      if(int(sb1pt,2) == 4 ): sb1ptV = -1/0.1 
      if(int(sb1pt,2) == 5 ): sb1ptV = -1/0.2 
      if(int(sb1pt,2) == 6 ): sb1ptV = -1/0.3 
      if(int(sb1pt,2) == 7 ): sb1ptV = -1/0.4 
      
      sb2ptV =0     
      if(int(sb2pt,2) == 0 ): sb2ptV = 1/0.4 
      if(int(sb2pt,2) == 1 ): sb2ptV = 1/0.3 
      if(int(sb2pt,2) == 2 ): sb2ptV = 1/0.2 
      if(int(sb2pt,2) == 3 ): sb2ptV = 1/0.1 
      if(int(sb2pt,2) == 4 ): sb2ptV = -1/0.1 
      if(int(sb2pt,2) == 5 ): sb2ptV = -1/0.2 
      if(int(sb2pt,2) == 6 ): sb2ptV = -1/0.3 
      if(int(sb2pt,2) == 7 ): sb2ptV = -1/0.4 
      
      ilphi_ = 1; 
      ilz = 1; 
      ilr = 2; 
      nbsr = 128.0; 
      nphibs = 16384; 
      rmean  = 1
 
      #sb1zV = sb1z*ilz*Kfact.kz;
      #sb2zV = sb2z*ilz*Kfact.kz;

      #sb1rV = sb1r/nbsr*() + rmean; 
      #sb2rV = sb2r/nbsr*() + rmean; 


    
      #Tracklets
      trlrinv  = ""
      trlphi0  = ""
      trlz     = ""
      trlt     = ""
      
      # print len(ltracklet)
      
     
      if(len(ltrl58) == 56 ):
        
        for i in range(0,14):
          trlrinv += ltrl58[i]
        for  i in range(14,32):
          trlphi0 += ltrl58[i]
        for i in range(32,42):
          trlz += ltrl58[i]
        for i in range(42,56):
          trlt += ltrl58[i]

          
    


      #Final Tracks 
      ftrkrinv  = ""
      ftrkphi0  = ""
      ftrkz     = ""
      ftrkt     = ""

      print len(lfittrack)," ",lfittrack," ",trckfitstr 
      
      if(len(lftrck62) == 59 ):
        
        for i in range(0,15):
          ftrkrinv += lftrck62[i]
        for  i in range(15,34):
          ftrkphi0 += lftrck62[i]
        for i in range(34,48):
          ftrkt += lftrck62[i]
        for i in range(48,59):
          ftrkz += lftrck62[i]

      

#      stubst = str(sb1ptV)+" "+str(sb1zV)+" "+str(sb2ptV)+" "+str(sb2zV)+"\n"
 #     oustb.write(stubst)

          
      #print "STUB full:", bin(int(ln[0],16)) ,"pt1: ",sb1ptV,"r1: ",sb1r," z:",sb1z," phi: ",sb1phi
      #print "TRACKLET full:", bin(int(ln[3],16)), "    ",ln[3]  ,"rinv: ",trlrinv,"phi0: ",trlphi0," z:",trlz," t: ",trlt
      #print "FinalTRACK full:", bin(int(ln[5],16)), "    ",ln[5]  ,"rinv: ",ftrkrinv,"phi0: ",ftrkphi0," z:",ftrkz," t: ",ftrkt
      #print Kfact.kphi0


      
      
      if(len(ltrl58) == 56):
          
        #making the signed ints to proper values and Calculating the proper quantities
        trlrinvV = (-1*(( int(trlrinv,2) ^ 16383   ) + 1 ) )*Kfact.krinvpars
        trlzV = int(trlz,2)*Kfact.kz
        trltV = int(trlt,2)*Kfact.kt
        trlphi0V = int(trlphi0,2)*Kfact.kphi0

        print "Converted"
        print "tracklet rinv: ",trlrinvV
        print "tracklet  z  : ",trlzV
        print "tracklet   t : ",trltV
        print "tracklet phi0: ",trlphi0V
      
        tracklett = str(trlrinvV)+" "+str(trlphi0V)+" "+str(trlzV)+" "+str(trltV)+" "+ltrackletev+"\n"
        outrl.write(tracklett)

      print " this one:" ,ftrkrinv  
      if(len(lftrck62) == 59):
        
        #making the signed ints to proper values and Calculating the proper quantities
        trkrinvV = (-1*(( int(ftrkrinv,2) ^ 32767) + 1))*Kfact.krinvpars
        trkzV = int(ftrkz,2)*Kfact.kz
        trktV = int(ftrkt,2)*Kfact.kt
        trkphi0V = int(ftrkphi0,2)*Kfact.kphi0
        
        print "Converted Final"
        print "tracklet rinv: ",trkrinvV
        print "tracklet  z  : ",trkzV
        print "tracklet   t : ",trktV
        print "tracklet phi0: ",trkphi0V
        
        finaltrackk = str(trkrinvV)+" "+str(trkzV)+" "+str(trktV)+" "+str(trkphi0V)+" "+lfittrackev+"\n"
        outrk.write(finaltrackk)
 
