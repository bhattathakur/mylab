{

  TString input_file("ba133.root");    //input file
  double BR1=100/100.; //BR for Ba133->Cs133

  TFile * f = new TFile(input_file);
  int total_events=1e8;
  //total events based on the number of beamon evetns .mac or total events 
  cout<<"total_events\t"<<total_events<<endl;
  //f->ls();
  //f->Print();
  //Defining the histogram
TH1F * h1=new TH1F("h1","",401,-0.5,400.5);
tT1->Draw("1000*TrueEnergy>>h1");
//cout<<"Print the histogram info......\n";
//h1->Scale(1000);
//h1->Print();
h1->Draw();
//  tT1->Draw("TrueEnergy");
  gPad->SetLogy();          //logy
//creating the file to write the output
ofstream myfile ("ba133simulation.csv");

//array of interested energy
//double energy [6]={53,80.9979,276.394,302.851,356.013,383.849};
// Energy at 80 keV and 276 keV are ignored as there are other energy close to those peaks
double energy []={53,302.851,356.013,383.849};

cout<<"size of the energy array\t"<<sizeof(energy)/sizeof(energy[0])<<endl;
int array_len=sizeof(energy)/sizeof(energy[0]);

int n=15;
cout<<right;
cout<<setprecision(5);
myfile<<right;
myfile<<setprecision(5);

myfile<<"Energy,n-1,n,n+1,background,signal,efficiency"<<endl;
cout<<"Energy"<<setw(n-4)<<"n-1"<<setw(n)<<"n"<<setw(n)<<"n+1"<<setw(n)<<"background"<<setw(n)<<"signal"<<setw(n)<<"efficiency"<<endl;
for(int i=0;i<array_len;i++){
  //cout<<i<<setw(n)<<energy[i]<<endl;
  //cout<<h1->GetBinContent(energy[i]+1)<<endl;
  //get former and later bin content to for background
  double e=energy[i];
  //int bin0=h1->GetBinContent(energy[i]-1);
  int bin0=h1->GetBinContent(h1->FindBin(e-1));
  //int bin1=h1->GetBinContent(energy[i]);
  int bin1=h1->GetBinContent(h1->FindBin(e));
  int bin2=h1->GetBinContent(h1->FindBin(e+1));
  double bkg=(bin0+bin2)/2.;
  double signal=bin1-bkg;
  double eff=abs(signal)/total_events;
  eff=eff/BR1; 
  //int bin2=h1->GetBinContent(energy[i]+1);
  //int bin3=h1->GetBinContent(energy[i]+2);
  //cout<<"energy:\t"<<e<<"\tbin0:\t"<<bin0<<"\tbin1:\t"<<bin1<<"\tbin2:"<<bin2<<endl;
  //myfile<<"former:\t"<<bin0<<"\tcurrent:\t"<<bin1<<"\tlater:\t"<<bin2<<endl;
cout<<e<<setw(n)<<bin0<<setw(n)<<bin1<<setw(n)<<bin2<<setw(n)<<bkg<<setw(n)<<signal<<setw(n)<<eff<<endl;
  myfile<<e<<","<<bin0<<","<<bin1<<","<<bin2<<","<<bkg<<","<<signal<<","<<eff<<endl;



  //cout<<h1->GetBinContent(energy[i]+1)<<endl;
//cout<<h1->GetBinContent(energy[i]+1)<<endl;
}
myfile.close();
//
//cout<<"test\t"<<h1->GetBinContent(81)<<endl;
//


}
