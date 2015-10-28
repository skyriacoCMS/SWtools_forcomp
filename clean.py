import sys
from collections import OrderedDict

def AllGlobal(fname):
  fin = open(fname+".dat","r")
  fout = open(fname+"_clean.dat","w")
  n_stub = 0
  n_tracklet = 0
  n_track = 0
  n_tracklets = []
  n_tracks = []
  stubs = []
  tracklets = []
  tracks = []
  stubs_keys = []
  tracklets_keys = []
  tracks_keys = []
  n_stub_values = []
  n_tracklet_values = []
  n_track_values = []
  for line in fin:
    line = line.strip()
    string = line.split(" ")
    if string[0] != "000000000" and string[1] != "000000000":
      stub = string[0]+" "+string[1]
      stubs.append(stub)
    if string[2] != "00000000000000":
      tracklet = string[2]
      tracklets.append(tracklet)
    if string[3] != "00000000000000000Xxxxxxxxxxxxxxx" and string[3] != "00000000000000000000000000000000":
      track = string[3]
      tracks.append(track)


  #nstubs = OrderedDict((i, stubs.count(i)) for i in stubs)
  #ntracklets = OrderedDict((i, tracklets.count(i)) for i in tracklets)
  #ntracks = OrderedDict((i, tracks.count(i)) for i in tracks)
  #num = [len(nstubs), len(ntracklets), len(ntracks)]

  num = [len(stubs), len(tracklets), len(tracks)]
  num.sort()
  #print(num)

  stub = stubs[0]
  n_stub = 0
  tracklet = tracklets[0]
  n_tracklet = 0
  track = tracks[0]
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
      n_stub_values.append(str(n_stub))
      stub = stubs[i]
      n_stub = 1
    else:
      n_stub += 1
    
  for i in range(0, len(tracklets)):
    if(tracklet != tracklets[i]):
      tracklets_keys.append(tracklet)
      n_tracklet_values.append(str(n_tracklet))
      tracklet = tracklets[i]
      n_tracklet = 1
    else:
      n_tracklet += 1
    
  for i in range(0, len(tracks)):
    if(track != tracks[i]):
      tracks_keys.append(track)
      n_track_values.append(str(n_track))
      track = tracks[i]
      n_track = 1
    else:
      n_track += 1

  num = [len(stubs_keys), len(tracklets_keys), len(tracks_keys)]
  num.sort()
  for i in range(0, num[2]):
    if len(stubs_keys) < i+1:
      stub = "000000000 000000000"
      n_stub = 0
    else:
      stub = stubs_keys[i]
      n_stub = n_stub_values[i]
    fout.write(stub)
    fout.write(" ")
    if(int(n_stub) < 10): fout.write("0")
    fout.write(str(n_stub))
    fout.write(" ")
    
    if len(tracklets_keys) < i+1:
      tracklet = "00000000000000"
      n_tracklet = 0
    else:
      tracklet = tracklets_keys[i]
      n_tracklet = n_tracklet_values[i]
    fout.write(tracklet)
    fout.write(" ")
    if(int(n_tracklet) < 10): fout.write("0")
    fout.write(str(n_tracklet))
    fout.write(" ")

    if len(tracks_keys) < i+1:
      track = "00000000000000000000000000000000"
      n_track = 0
    else:
      track = tracks_keys[i]
      n_track = n_track_values[i]
    fout.write(track)
    fout.write(" ")
    if(int(n_track) < 10): fout.write("0")
    fout.write(str(n_track))
    fout.write(" ")

    fout.write('\n')


if __name__ == "__main__":
  AllGlobal(sys.argv[1])
