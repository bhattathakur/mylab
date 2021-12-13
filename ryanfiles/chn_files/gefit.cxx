#include <iostream>
#include "TApplication.h"
#include "GeDataSet.h"
#include "GeFit.h"

using namespace std;

int main(int argc,char **argv){
  TApplication theApp("tapp", &argc, argv);
  cout <<"Running gefit..." << endl;
  GeFit gefit;
  GeDataSet *ds = new GeDataSet();
  ds->ReadDat("combined.dat");
  cout<<"dsnc"<<ds->GetNumberOfChannels()<<endl;
  gefit.LoadDataSet(ds);
  gefit.Minimize();
  gefit.ShowRawSpectrum();
  cout<<"This far"<<endl;
  theApp.Run();
  return 0;
}
