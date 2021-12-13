#include "TCanvas.h"
#include "TH1I.h"
#include "TROOT.h"
#include <fstream>
#include <iostream>
#include <sstream>
using namespace std;

int main(int argc, char *argv[]) {
  ifstream fin(argv[1], ios::in);
  string str;
  getline(fin, str);
  getline(fin, str);

  size_t dots = 25;

  time_t startSeconds;
  getline(fin, str);
  istringstream iss(str);
  iss.ignore(dots);
  iss >> startSeconds;

  getline(fin, str);

  double livetime;
  getline(fin, str);
  iss.clear();
  iss.str(str);
  iss.ignore(dots);
  iss >> livetime;

  ushort nChannels;
  getline(fin, str);
  iss.clear();
  iss.str(str);
  iss.ignore(dots);
  iss >> nChannels;

  int *counts = new int[nChannels](); 
  TH1I *h1 = new TH1I("h1","",nChannels, 0.5, nChannels+0.5);
  for (size_t i=0; i<nChannels; i++) {
    getline(fin, str);
    iss.clear();
    iss.str(str);
    size_t chn;
    iss >> chn >> counts[i];
    h1->SetBinContent( chn+1, counts[i] );
  }

  h1->Draw();  
  TCanvas *c1 = new TCanvas("c1");
  c1->Print("h1.C");

  double b;
  getline(fin, str);
  iss.clear();
  iss.str(str);
  iss.ignore(31);
  iss >> b;

  char sgn;
  iss.ignore(5);
  iss >> sgn;

  double m;
  iss >> m;
  if (sgn == '-') m *= -1;

  TH1I *he = new TH1I("he", "", nChannels, b, b+m*nChannels);
  for (size_t i=0; i<nChannels; i++)
    he->SetBinContent(i+1, counts[i]);
  he->Draw();
  c1->Print("he.C");

  return 0;

}
