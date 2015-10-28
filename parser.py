import os,math
import ROOT
from bitstring import Bits

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def in_A_notin_B(A,B):
    l = []
    for a in A:
        if a not in B:
            l.append(a) 
    return l


in_stubs = []
out_stubs = []
tracklets = []
proj_1 = []
proj_2 = []
proj_3 = []
proj_4 = []
tracks = []
e_in_stubs = []
e_out_stubs = []
e_tracklets = []
e_proj_1 = []
e_proj_2 = []
e_proj_3 = []
e_proj_4 = []
e_tracks = []

f = open('tracklets_out.dat')

for line in f:
	in_stubs.append(line.split(' ')[0])
	out_stubs.append(line.split(' ')[1])
	tracklets.append(line.split(' ')[2])
#	proj_1.append(line.split(' ')[3])
#	proj_2.append(line.split(' ')[4])
#	proj_3.append(line.split(' ')[5])
#	proj_4.append(line.split(' ')[6])
	tracks.append(line.split(' ')[3])

g1 = open('AllStubs_AS_L1D3n1_02_hex.dat')
g2 = open('AllStubs_AS_L2D3n1_02_hex.dat')
g3 = open('TrackletParameters_TPAR_L1D3L2D3_02_hex.dat')

for line in g1:
	if 'Event' not in line:
		e_in_stubs.append(line.split(' ')[1].strip().replace('0x',''))
for line in g2:
	if 'Event' not in line:
		e_out_stubs.append(line.split(' ')[1].strip().replace('0x',''))
for line in g3:
	if 'Event' not in line:
		e_tracklets.append(line.split(' ')[1].strip().replace('0x',''))
        
f_in_stubs = f7(in_stubs)
f_out_stubs = f7(out_stubs)
f_tracklets = f7(tracklets)

'''
print 'Inner Stub:'
print 'In E not in F:',in_A_notin_B(e_in_stubs,f_in_stubs)
print 'In F not in E:',in_A_notin_B(f_in_stubs,e_in_stubs)
print 'Outer Stub:'
print 'In E not in F:',in_A_notin_B(e_out_stubs,f_out_stubs)
print 'In F not in E:',in_A_notin_B(f_out_stubs,e_out_stubs)
print 'Tracklets:'
print 'In E not in F:',in_A_notin_B(e_tracklets,f_tracklets)
print 'In F not in E:',in_A_notin_B(f_tracklets,e_tracklets)
'''

verbose = False
compare = True
k = 0
g = open('par.txt','w')
for e in e_tracklets:
    if verbose:
        print e
    for t in f_tracklets:
        if int(t,16) == 0:
            continue
        #print t,bin(int(t,16))[:-42]
        bin_irinv_h = bin(int(t,16))[:-42]
        while len(bin_irinv_h) < 14:
            bin_irinv_h = '0'+bin_irinv_h
        irinv_h = Bits(bin=(bin_irinv_h))
        irinv_s = Bits(bin=(bin(int(e,16)))[:-42])
        iphi0_h = int((bin(int(t,16)))[-42:-24],2)
        iphi0_s = int(bin(int(e,16))[-42:-24],2)
        iz0_h = Bits(bin=(bin(int(t,16)))[-24:-14])
        iz0_s = Bits(bin=(bin(int(e,16)))[-24:-14])
        it_h = Bits(bin=(bin(int(t,16)))[-14:])
        it_s = Bits(bin=(bin(int(e,16)))[-14:])
        #print irinv_h,irinv_s,iphi0_h,iphi0_s
        if math.fabs(iz0_h.int-iz0_s.int) < 1 and math.fabs(iphi0_h-iphi0_s) < 1 and math.fabs(irinv_h.int-irinv_s.int) < 10 and math.fabs(it_h.int-it_s.int) < 1:
            k = k + 1
            if verbose:
                    print t
            if compare:
                g.write('z0= '+str(iz0_h.int)+' '+str(iz0_s.int)+' '+str(iz0_h.int-iz0_s.int)+'\n')
                g.write('phi0= '+str(iphi0_h)+' '+str(iphi0_s)+' '+str(iphi0_h-iphi0_s)+'\n')
                g.write('r_inv= '+str(irinv_h.int)+' '+str(irinv_s.int)+' '+str(irinv_h.int-irinv_s.int)+'\n')
                g.write('t= '+str(it_h.int)+' '+str(it_s.int)+' '+str(it_h.int-it_s.int)+'\n')

g.close()

m = open('par.txt')                    
h_0 = ROOT.TH1F("h_0","Bitwise difference z_{0}",20,-10,10)
h_1 = ROOT.TH1F("h_1","Bitwise difference phi_{0}",20,-10,10)
h_2 = ROOT.TH1F("h_2","Bitwise difference rho^{-1}",20,-10,10)
h_3 = ROOT.TH1F("h_3","Bitwise difference tracklet parameters",20,-10,10)
for line in m:
    #print line
    if 'z0=' in line or 'Phi=' in line:
        h_0.Fill(int(line.strip().split(' ')[-1]))
    if 'phi0=' in line or 'Z=' in line:
        h_1.Fill(int(line.strip().split(' ')[-1]))
    if 'r_inv=' in line or 'dphi=' in line:
        h_2.Fill(int(line.strip().split(' ')[-1]))
    if 't=' in line or 'dz=' in line:
        h_3.Fill(int(line.strip().split(' ')[-1]))
    
c1 = ROOT.TCanvas("c1","Canvas",400,300)
   
#h_0.GetYaxis().SetRangeUser(0,(max([h_0.GetMaximum(),h_1.GetMaximum(),h_2.GetMaximum(),h_3.GetMaximum()])) + 10)
#   h_1.GetYaxis().SetRangeUser(0,(max([h_0.GetMaximum(),h_1.GetMaximum(),h_2.GetMaximum(),h_3.GetMaximum()])) + 10)
#   h_2.GetYaxis().SetRangeUser(0,(max([h_0.GetMaximum(),h_1.GetMaximum(),h_2.GetMaximum(),h_3.GetMaximum()])) + 10)
#   h_3.GetYaxis().SetRangeUser(0,(max([h_0.GetMaximum(),h_1.GetMaximum(),h_2.GetMaximum(),h_3.GetMaximum()])) + 10)
#print max([h_0.GetMaximum(),h_1.GetMaximum(),h_2.GetMaximum(),h_3.GetMaximum()])

h_1.SetLineColor(2)
h_2.SetLineColor(6)
h_3.SetLineColor(3)
histos = sorted([h_0,h_1,h_2,h_3], key=lambda x:x.GetMaximum())

histos[3].Draw()
histos[1].Draw('same')
histos[2].Draw('same')
histos[0].Draw('same')

leg = ROOT.TLegend( 0.78, 0.50, 0.98, 0.65 ) ;
leg.AddEntry( h_0, "#Delta z_{0}" ) ;
leg.AddEntry( h_1, "#Delta #phi_{0}" ) ;
leg.AddEntry( h_2, "#Delta #rho^{-1}" ) ;
leg.AddEntry( h_3, "#Delta tan(#theta)" ) ;
#Float_t sizeleg = leg->GetTextSize()*1.2;
#leg->SetTextSize( sizeleg ) ;
leg.SetFillColor( ROOT.kWhite ) ;
leg.Draw();
