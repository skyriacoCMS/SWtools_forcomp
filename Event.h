//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Oct 28 02:24:39 2015 by ROOT version 5.34/03
// from TTree event_tree/
// found on file: Event_tree.root
//////////////////////////////////////////////////////////

#ifndef Event_h
#define Event_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <cstdlib>
#include <iostream>
#include <iomanip>

// Header file for the classes stored in the TTree if any.
#include <vector>

// Fixed size dimensions of array or collections stored in the TTree if any.

class Event {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   vector<float>   *stubpt1;
   vector<float>   *stubr1;
   vector<float>   *stubz1;
   vector<float>   *stubphi1;
   vector<float>   *stubpt2;
   vector<float>   *stubr2;
   vector<float>   *stubz2;
   vector<float>   *stubphi2;
   vector<float>   *trackletpt;
   vector<float>   *trackletrinv;
   vector<float>   *trackletphi0;
   vector<float>   *trackletz0;
   vector<float>   *tracklett;
   vector<float>   *vivtrackletrinv;
   vector<float>   *vivtrackletphi0;
   vector<float>   *vivtrackletz0;
   vector<float>   *vivtracklett;
   vector<float>   *fittrackpt;
   vector<float>   *fittrackrinv;
   vector<float>   *fittrackphi0;
   vector<float>   *fittrackt;
   vector<float>   *fittrackz0;
   vector<float>   *vivfittrackrinv;
   vector<float>   *vivfittrackphi0;
   vector<float>   *vivfittrackt;
   vector<float>   *vivfittrackz0;

   // List of branches
   TBranch        *b_stubpt1;   //!
   TBranch        *b_stubr1;   //!
   TBranch        *b_stubz1;   //!
   TBranch        *b_stubphi1;   //!
   TBranch        *b_stubpt2;   //!
   TBranch        *b_stubr2;   //!
   TBranch        *b_stubz2;   //!
   TBranch        *b_stubphi2;   //!
   TBranch        *b_trackletpt;   //!
   TBranch        *b_trackletrinv;   //!
   TBranch        *b_trackletphi0;   //!
   TBranch        *b_trackletz0;   //!
   TBranch        *b_tracklett;   //!
   TBranch        *b_vivtrackletrinv;   //!
   TBranch        *b_vivtrackletphi0;   //!
   TBranch        *b_vivtrackletz0;   //!
   TBranch        *b_vivtracklett;   //!
   TBranch        *b_fittrackpt;   //!
   TBranch        *b_fittrackrinv;   //!
   TBranch        *b_fittrackphi0;   //!
   TBranch        *b_fittrackt;   //!
   TBranch        *b_fittrackz0;   //!
   TBranch        *b_vivfittrackrinv;   //!
   TBranch        *b_vivfittrackphi0;   //!
   TBranch        *b_vivfittrackt;   //!
   TBranch        *b_vivfittrackz0;   //!

   Event(TTree *tree=0);
   virtual ~Event();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef Event_cxx
Event::Event(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("Event_tree.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("Event_tree.root");
      }
      f->GetObject("event_tree",tree);

   }
   Init(tree);
}

Event::~Event()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t Event::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t Event::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void Event::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   stubpt1 = 0;
   stubr1 = 0;
   stubz1 = 0;
   stubphi1 = 0;
   stubpt2 = 0;
   stubr2 = 0;
   stubz2 = 0;
   stubphi2 = 0;
   trackletpt = 0;
   trackletrinv = 0;
   trackletphi0 = 0;
   trackletz0 = 0;
   tracklett = 0;
   vivtrackletrinv = 0;
   vivtrackletphi0 = 0;
   vivtrackletz0 = 0;
   vivtracklett = 0;
   fittrackpt = 0;
   fittrackrinv = 0;
   fittrackphi0 = 0;
   fittrackt = 0;
   fittrackz0 = 0;
   vivfittrackrinv = 0;
   vivfittrackphi0 = 0;
   vivfittrackt = 0;
   vivfittrackz0 = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("stubpt1", &stubpt1, &b_stubpt1);
   fChain->SetBranchAddress("stubr1", &stubr1, &b_stubr1);
   fChain->SetBranchAddress("stubz1", &stubz1, &b_stubz1);
   fChain->SetBranchAddress("stubphi1", &stubphi1, &b_stubphi1);
   fChain->SetBranchAddress("stubpt2", &stubpt2, &b_stubpt2);
   fChain->SetBranchAddress("stubr2", &stubr2, &b_stubr2);
   fChain->SetBranchAddress("stubz2", &stubz2, &b_stubz2);
   fChain->SetBranchAddress("stubphi2", &stubphi2, &b_stubphi2);
   fChain->SetBranchAddress("trackletpt", &trackletpt, &b_trackletpt);
   fChain->SetBranchAddress("trackletrinv", &trackletrinv, &b_trackletrinv);
   fChain->SetBranchAddress("trackletphi0", &trackletphi0, &b_trackletphi0);
   fChain->SetBranchAddress("trackletz0", &trackletz0, &b_trackletz0);
   fChain->SetBranchAddress("tracklett", &tracklett, &b_tracklett);
   fChain->SetBranchAddress("vivtrackletrinv", &vivtrackletrinv, &b_vivtrackletrinv);
   fChain->SetBranchAddress("vivtrackletphi0", &vivtrackletphi0, &b_vivtrackletphi0);
   fChain->SetBranchAddress("vivtrackletz0", &vivtrackletz0, &b_vivtrackletz0);
   fChain->SetBranchAddress("vivtracklett", &vivtracklett, &b_vivtracklett);
   fChain->SetBranchAddress("fittrackpt", &fittrackpt, &b_fittrackpt);
   fChain->SetBranchAddress("fittrackrinv", &fittrackrinv, &b_fittrackrinv);
   fChain->SetBranchAddress("fittrackphi0", &fittrackphi0, &b_fittrackphi0);
   fChain->SetBranchAddress("fittrackt", &fittrackt, &b_fittrackt);
   fChain->SetBranchAddress("fittrackz0", &fittrackz0, &b_fittrackz0);
   fChain->SetBranchAddress("vivfittrackrinv", &vivfittrackrinv, &b_vivfittrackrinv);
   fChain->SetBranchAddress("vivfittrackphi0", &vivfittrackphi0, &b_vivfittrackphi0);
   fChain->SetBranchAddress("vivfittrackt", &vivfittrackt, &b_vivfittrackt);
   fChain->SetBranchAddress("vivfittrackz0", &vivfittrackz0, &b_vivfittrackz0);
   Notify();
}

Bool_t Event::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void Event::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t Event::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef Event_cxx
