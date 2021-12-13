#include "GeDataSet.h"
#include <iostream>
#include <string>

int main(int argc, char *argv[]){
  bool debug = true;

  if (argc < 2) {
    std::cerr << "Input MAESTRO binary file (.chn) filename"  << std::endl;
    std::cerr << " and optionally detector time zone."        << std::endl;
    std::cerr << " and optionally \'q\' for quiet operation." << std::endl;
    return -1;
  }

  std::string timeZone = "CST";
  if (argc < 3)
    std::cout << "Assuming the detector was in central time zone." << std::endl;
  else
    timeZone = argv[2];

  GeDataSet ds;
  ds.ReadCHN(argv[1], timeZone, debug);

  // Strip path from beginning and chn from end of from input file name
  // and replace the latter with dat.
  std::string filename = argv[1];
  size_t pathLength = filename.find_last_of("\\/");
  filename = filename.substr( pathLength + 1, filename.length() - (pathLength+1) - 3 );
  filename += "dat";

  ds.WriteDat(filename);
  ds.ReadDat(filename);

  return 0;
}
