#define Event_cxx
#include "Event.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void Event::Loop()
{
//   In a ROOT session, you can do:
//      Root > .L Event.C
//      Root > Event t
//      Root > t.GetEntry(12); // Fill t data members with entry number 12
//      Root > t.Show();       // Show values of entry 12
//      Root > t.Show(16);     // Read and show values of entry 16
//      Root > t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch

  TH1F *Ntlev = new TH1F("Ntlev","",5,0,5);
  TH1F *Ntlevviv = new TH1F("Ntlevviv","",5,0,5);

  TH1F *NFtev = new TH1F("NFtev","",5,0,5);
  TH1F *NFtevviv = new TH1F("NFtevviv","",5,0,5);

  TH1F *NFtdif = new TH1F("NFtdif","",5,0,5);

  
  TH1F *Dphi  = new TH1F("Dphi","",1000,-0.5,0.5);
  TH1F *Drinv = new TH1F("Drinv","",1000,-0.5,0.5);
  TH1F *Dz   = new TH1F("Dz","",20000,-100,100);
  TH1F *Dt   = new TH1F("Dt","",1000,-0.05,0.05);

  TH2F *DphiDrinv  = new TH2F("DphivsDrinv","",1000,-0.5,0.5,1000,-0.5,0.5);






   if (fChain == 0) return;
   Long64_t nentries = fChain->GetEntriesFast();
   Long64_t nbytes = 0, nb = 0;
   int allfinemu = 0; 
   int allfinemuV = 0; 
   
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
      //  cout<<"Event"<< jentry<<endl;

      allfinemu += (*fittrackz0).size();
      allfinemuV += (*vivfittrackz0).size();
      
      if((*fittrackz0).size() > 1 ) cout<<jentry<<"  "<<(*fittrackz0).size()<<endl; 
      if((*fittrackz0).size()  == 1 ) cout<<jentry<<"  "<<(*fittrackz0).size()<<endl; 

      Ntlev->Fill((*trackletz0).size());
      Ntlevviv->Fill((*vivtrackletz0).size());
      NFtev->Fill((*fittrackz0).size());
      NFtevviv->Fill((*vivfittrackz0).size());
      NFtdif->Fill(fabs((*fittrackz0).size() - (*vivfittrackz0).size()));

      if((*vivfittrackz0).size() != 0 && (*fittrackz0).size() != 0 ){
	      
	Dphi->Fill((*fittrackphi0)[0] - (*vivfittrackphi0)[0]);
	Drinv->Fill((*fittrackrinv)[0] - (*vivfittrackrinv)[0]);
	Dz->Fill((*fittrackz0)[0] - (*vivfittrackz0)[0]);
	Dt->Fill((*fittrackt)[1] - (*vivfittrackt)[1]);

	DphiDrinv->Fill((*fittrackphi0)[0] - (*vivfittrackphi0)[0],(*fittrackrinv)[0] - (*vivfittrackrinv)[0]);


      }

      if((*vivfittrackz0).size() == 2 && (*fittrackz0).size() == 2 ){
	      
 	Dphi->Fill((*fittrackphi0)[1] - (*vivfittrackphi0)[1]);
	Drinv->Fill((*fittrackrinv)[1] - (*vivfittrackrinv)[1]);
	Dz->Fill((*fittrackz0)[1] - (*vivfittrackz0)[1]);
	Dt->Fill((*fittrackt)[1] - (*vivfittrackt)[1]);
	DphiDrinv->Fill((*fittrackphi0)[0] - (*vivfittrackphi0)[0],(*fittrackrinv)[0] - (*vivfittrackrinv)[0]);

      }
      
   }

   cout<<allfinemu<<endl;
   cout<<allfinemuV<<endl;

   TFile *f1 = new TFile("Plots.root","recreate");
   f1->cd();
   Ntlev->Write();
   Ntlevviv->Write(); 

   NFtdif->Write();
   NFtev->Write();
   NFtevviv->Write();
   
   
   Dphi->Write();
   Drinv->Write();
   Dz->Write();
   Dt->Write();
   DphiDrinv->Write();

}
