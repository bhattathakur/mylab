#include <iostream>
#include <string>
#include "TFile.h"
#include "TTree.h"
#include "TH1D.h"
#include "TMath.h"

using namespace std;
int main( int argc, char *argv[] )
{
  // Extract the sumulated efficiency at energy argv[2] from ROOT file argv[1].
  string file=argv[1];
  auto f = new TFile( file.c_str() );
  if ( !f || f->IsZombie() || f->TestBit(TFile::kRecovered) ) {
    cerr << "File " << file << " did not finish processing." << endl;
    exit(0);
  }
  auto t = dynamic_cast<TTree*>( f->Get("tT1") );
  unsigned long long int ngen = t->GetEntries();

  Float_t e;
  t->SetBranchAddress("TrueEnergy",&e);

  auto nchn = 16384;
  auto keV_chn = 0.199101455238E+00;
  auto chn_0   = 0.243953011160E-01;
  TH1D *h1 = new TH1D("h1","",20000,chn_0, chn_0 + 20000*keV_chn);
  for (auto entry=0; entry<ngen; entry++) {
    t->GetEntry( entry );
    h1->Fill( e*1000 );
  }
  if ( argc > 8 ) {
    ngen = atoll( argv[8] );
  }
  auto bin = h1->FindBin( stof(argv[2]) );
  auto blo = bin - atoi( argv[4] );
  auto bhi = bin + atoi( argv[5] );
  if ( h1->Integral(blo,bhi) < 21 ) {
    cerr << "Not enough statistis in file " << file << " to estimate the efficiency at " << argv[2] << endl;
    exit(0);
  }
  auto bkl = blo - atoi( argv[6] );
  auto bkh = bhi + atoi( argv[7] );
  auto norm = 1/stof(argv[3])/ngen;
  cout << argv[2] << " ";
  auto bkg = (bhi - blo)+1.;
  bkg     *= h1->Integral(bkl, bkh) - h1->Integral(blo,bhi);
  bkg     /= (bkh - bkl)+1 - ( (bhi - blo)+1 );
  auto cnt = h1->Integral(blo,bhi) - bkg;
  auto err = h1->Integral(blo,bhi) + bkg;
  err      = TMath::Sqrt(err);
  cout << cnt * norm;
  cout << " +/- " << err * norm;
  cout << " " << file;
  cout << " " << ngen;
  cout << " " << t->GetEntries() << endl;

  return 0;
}
