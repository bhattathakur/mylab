//Add this to GeDataSet as a member function that combines two runs...then combine as many runs as required as the previous pair plus another one.

#include "GeDataSet.h"
#include <iomanip>
#include <sstream>

struct runHeader
{
  std::string fileName;
  time_t startTime;
  double runTime;
  double liveTime;
  double stopTime;
};
bool sortByStartTime(runHeader &lhs, runHeader &rhs)
{
  return lhs.startTime < rhs.startTime;
}


int main(int argc, char *argv[])
{
  std::ifstream fin(argv[1]);
  std::string str;
  std::vector<runHeader> runHeaders;
  while ( getline(fin,str) ){
    std::istringstream sstr(str);
    runHeaders.push_back( runHeader() );
    sstr >> runHeaders[runHeaders.size()-1].fileName;
  }
  if ( runHeaders.size() == 0 ) {
    std::cerr << "No files found in runlist provided?" << std::endl;
  }
  std::vector<runHeader>::iterator it = runHeaders.begin();
  GeDataSet ds;// will become combined dataset
  std::vector<int32_t> data;
  while ( it != runHeaders.end() ) {
    ds.ReadDat( it->fileName, false );
    it->startTime = ds.GetStartTime();
    it->runTime   = ds.GetRunTime();
    it->liveTime  = ds.GetLiveTime();
    it->stopTime  = ds.GetStartTime() + ds.GetRunTime();
    if ( data.size() == 0 ) data.resize( ds.GetNumberOfChannels() );
    for (uint16_t i=0; i<ds.GetNumberOfChannels(); i++) {
      data[i] += ds.GetData()[i];
    }
    it++;
  }
  std::sort ( runHeaders.begin(), runHeaders.end(), sortByStartTime);
  ds.ReadDat( runHeaders.begin()->fileName, false );// set combined dataset to first

  time_t startTime = runHeaders.begin()->startTime;
  double stopTime  = (runHeaders.end()-1)->stopTime;
  double runTime   = stopTime - startTime;

  double liveTime = 0;
  double deadTime = 0;
  double mean     = 0;
  double weight   = 0;
  it = runHeaders.begin();
  while ( it != runHeaders.end() ) {
    double t = ( it->startTime + it->stopTime ) / 2;
    double w =   it->liveTime  * it->liveTime;
    mean    += t * w * w;
    weight  +=     w * w;
    liveTime+= it->liveTime;
    deadTime+= it->runTime - it->liveTime;
    it++;
  }

  ds.ReadDat( runHeaders.begin()->fileName, false );
  ds.SetRunTime ( runTime  );
  ds.SetLiveTime( liveTime );
  ds.SetData    ( data );
  ds.WriteDat("combined.dat");

  std::cout << std::endl;
  std::cout << "Mean of run times...: " << std::fixed << std::setprecision(3) << mean/weight << std::endl;
  std::cout << "Total dead time.....: " << std::fixed << std::setprecision(2) << deadTime << std::endl;
  std::cout << std::endl;

  return 0;
}
