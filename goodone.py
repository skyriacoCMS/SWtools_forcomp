import sys
from collections import OrderedDict

def AllGlobal(fname):
  fin = open(fname,"r")
  fout = open(fname[:-4]+"_clean.dat","w")
  n_stub = 0
  n_tracklet = 0
  n_track = 0
  n_tracklets = []
  n_tracks = []

  stubs = []
  tracklets = []
  tracks = []

  ### UGLY MANUAL HACK TO GET STARTING POINT RIGHT 
  stub_evtcount = -2
  tracklet_evtcount = -4
  track_evtcount = -8
  
  stubs_bx = []
  tracklets_bx = []
  tracks_bx = []
  stubs_evt = []
  tracklets_evt = []
  tracks_evt = []

  stubs_keys = []
  tracklets_keys = []
  tracks_keys = []

  stubs_bx_keys = []
  tracklets_bx_keys = []
  tracks_bx_keys = []
  stubs_evt_keys = []
  tracklets_evt_keys = []
  tracks_evt_keys = []

  n_stub_values = []
  n_tracklet_values = []
  n_track_values = []
  
  tmp_stub = "X"
  tmp_tracklet = "X"
  tmp_track = "X"
  
  for line in fin:
    line = line.strip()
    string = line.split(" ")

    if string[1] != tmp_stub :
        stub_evtcount += 1
        tmp_stub = string[1]
    if string[7] != tmp_tracklet :
        tracklet_evtcount += 1
        tmp_tracklet = string[7]
    if string[10] != tmp_track :
        track_evtcount += 1
        tmp_track = string[10]
    
    if string[0] == "1" and string[2] != "000000000" and string[3] == "1" and string[5] != "000000000":
      stub = string[2]+" "+string[5]
      stubs.append(stub)
      stub_bx = int(string[1], 16)
      while (stub_bx > 7) :
          stub_bx -= 8
      stubs_bx.append(stub_bx)
      stubs_evt.append(stub_evtcount)

    if string[6] == "1" and string[8] != "00000000000000":
      tracklet = string[8]
      tracklets.append(tracklet)
      tracklets_bx.append(string[7])
      tracklets_evt.append(tracklet_evtcount)
    
    if string[9] == "1" and string[11] != "00000000000000000Xxxxxxxxxxxxxxx" and string[11] != "00000000000000000000000000000000":
      track = string[11]
      tracks.append(track)
      tracks_bx.append(string[10])
      tracks_evt.append(track_evtcount)


  #nstubs = OrderedDict((i, stubs.count(i)) for i in stubs)
  #ntracklets = OrderedDict((i, tracklets.count(i)) for i in tracklets)
  #ntracks = OrderedDict((i, tracks.count(i)) for i in tracks)
  #num = [len(nstubs), len(ntracklets), len(ntracks)]

  num = [len(stubs), len(tracklets), len(tracks)]
  print(num)

  stub = stubs[0]
  stub_bx = stubs_bx[0]
  stub_evt = stubs_evt[0]
  n_stub = 0
  tracklet = tracklets[0]
  tracklet_bx = tracklets_bx[0]
  tracklet_evt = tracklets_evt[0]
  n_tracklet = 0
  track = tracks[0]
  track_bx = tracks_bx[0]
  track_evt = tracks_evt[0]
  n_track = 0
    #stub_keys = nstubs.keys()
    #n_stub_values = nstubs.values()
    #tracklet_keys = ntracklets.keys()
    #n_tracklet_values = ntracklets.values()
    #track_keys = ntracks.keys()
    #n_track_values = ntracks.values()
    
  for i in range(0, len(stubs)):
    if(stub != stubs[i]):
      stubs_keys.append(stub)
      stubs_bx_keys.append(stub_bx)
      stubs_evt_keys.append(stub_evt)
      n_stub_values.append(str(n_stub))
      stub = stubs[i]
      stub_bx = stubs_bx[i]
      stub_evt = stubs_evt[i]
      n_stub = 1
    else:
      n_stub += 1
    
  for i in range(0, len(tracklets)):
    if(tracklet != tracklets[i]):
      tracklets_keys.append(tracklet)
      tracklets_bx_keys.append(tracklet_bx)
      tracklets_evt_keys.append(tracklet_evt)
      n_tracklet_values.append(str(n_tracklet))
      tracklet = tracklets[i]
      tracklet_bx = tracklets_bx[i]
      tracklet_evt = tracklets_evt[i]
      n_tracklet = 1
    else:
      n_tracklet += 1
    
  for i in range(0, len(tracks)):
    if(track != tracks[i]):
      tracks_keys.append(track)
      tracks_bx_keys.append(track_bx)
      tracks_evt_keys.append(track_evt)
      n_track_values.append(str(n_track))
      track = tracks[i]
      track_bx = tracks_bx[i]
      track_evt = tracks_evt[i]
      n_track = 1
    else:
      n_track += 1

  num = [len(stubs_keys), len(tracklets_keys), len(tracks_keys)]
  print num
  num.sort()
  for i in range(0, num[2]):
    if len(stubs_keys) < i+1:
      stub = "000000000 000000000"
      stub_bx = 0
      stub_evt = 0
      n_stub = 0
    else:
      stub = stubs_keys[i]
      stub_bx = stubs_bx_keys[i]
      stub_evt = stubs_evt_keys[i]
      n_stub = n_stub_values[i]
    fout.write(stub)
    fout.write(" ")
    fout.write(str(stub_bx))
    fout.write(" ")
    if(int(stub_evt) < 10): fout.write("0")
    fout.write(str(stub_evt))
    fout.write(" ")
    if(int(n_stub) < 10): fout.write("0")
    fout.write(str(n_stub))
    fout.write(" ")
    
    if len(tracklets_keys) < i+1:
      tracklet = "00000000000000"
      tracklet_bx = 0
      tracklet_evt = 0
      n_tracklet = 0
    else:
      tracklet = tracklets_keys[i]
      tracklet_bx = tracklets_bx_keys[i]
      tracklet_evt = tracklets_evt_keys[i]
      n_tracklet = n_tracklet_values[i]
    fout.write(tracklet)
    fout.write(" ")
    fout.write(str(tracklet_bx))
    fout.write(" ")
    fout.write(str(tracklet_evt))
    fout.write(" ")
    if(int(n_tracklet) < 10): fout.write("0")
    fout.write(str(n_tracklet))
    fout.write(" ")

    if len(tracks_keys) < i+1:
      track = "00000000000000000000000000000000"
      track_bx = 0
      track_evt = 0
      n_track = 0
    else:
      track = tracks_keys[i]
      track_bx = tracks_bx_keys[i]
      track_evt = tracks_evt_keys[i]
      n_track = n_track_values[i]
    fout.write(track)
    fout.write(" ")
    fout.write(str(track_bx))
    fout.write(" ")
    if(int(track_evt) < 10): fout.write("0")
    fout.write(str(track_evt))
    fout.write(" ")
    if(int(n_track) < 10): fout.write("0")
    fout.write(str(n_track))
    fout.write(" ")

    fout.write('\n')


if __name__ == "__main__":
  AllGlobal(sys.argv[1])
