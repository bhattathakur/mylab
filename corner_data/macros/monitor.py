#!/usr/bin/python3

from datetime   import datetime
from matplotlib import dates as matdates
from matplotlib import pyplot

dirs = [
    'door'
    ]
sources = [
    'na22',
    'co60',
    'ba133',
    'cs137',
    'eu152',
    'pb210',
    'ra226',
    'am241'
    ]

times       = []
runtm       = []
endtm       = []
ticks       = []
labels      = []
keV_chn     = []
keV_chn_err = []
chn_0       = []
chn_0_err   = []
for dir in dirs:
    for source in sources:
        file = open( dir+'/'+source+'.gdf', 'r' )
        lines = file.readlines()
        keV_chn.append(     float( lines[-8].split()[ 1] ) )
        chn_0.append(       float( lines[-7].split()[ 1] ) )
        keV_chn_err.append( float( lines[-8].split()[ 2] ) )
        chn_0_err.append(   float( lines[-7].split()[ 2] ) )
        labels.append( source[0].upper() + source[1] + '-' + source[2:] )
        if len(ticks) == 0:
            ticks.append(1)
        else:
            ticks.append( ticks[-1]+1 )
        file = open( dir+'/dat/'+source+'.dat', 'r' )
        lines = file.readlines()
        times.append(       int( lines[ 2].split()[-2] ) )
        runtm.append(     float( lines[ 3].split()[-2] ) )
        endtm.append( times[-1]+runtm[-1] )
        # The following Pb-210 calibration start time is exactly the same as
        # the Am-241 calibration. Recalculate the start time from the
        # time stamp on the file (ET) and the run time for this run.
        if source == 'pb210' and dir == 'door':
            times[-1] = datetime(2020, 2,14,12-1,41,57).timestamp() - runtm[-1]

pyplot.errorbar( ticks, keV_chn, yerr=keV_chn_err, fmt='.' )
pyplot.xticks(ticks, labels)
pyplot.ylabel('keV/channel')
pyplot.savefig( 'keV_chn.pdf', bbox_inches='tight')
pyplot.clf()

pyplot.errorbar( ticks, chn_0, yerr=chn_0_err, fmt='.' )
pyplot.xticks(ticks, labels)
pyplot.ylabel('keV')
pyplot.savefig( 'chn_0.pdf', bbox_inches='tight')
pyplot.clf()

dates = []
for t in times:
#for t in endtm:
    dates.append( datetime.fromtimestamp(t) )
    #print(dates[-1])
date_fmt = '%d-%m-%y %H:%M:%S'
date_fmt = '%m-%d %H:%M'
date_formatter = matdates.DateFormatter(date_fmt)

pyplot.errorbar( dates, keV_chn, yerr=keV_chn_err, fmt='.' )
axis   = pyplot.gca()
figure = pyplot.gcf()
axis.get_xaxis().set_major_formatter(date_formatter)
axis.get_xaxis().set_minor_locator( matdates.MinuteLocator(interval=15) )
axis.get_xaxis().set_major_locator( matdates.HourLocator(interval=1) )
figure.autofmt_xdate()
pyplot.ylabel('keV/channel')
pyplot.savefig( 'keV_chn_trend.pdf', bbox_inches='tight')
pyplot.clf()

pyplot.errorbar( dates, chn_0, yerr=chn_0_err, fmt='.' )
axis   = pyplot.gca()
figure = pyplot.gcf()
axis.get_xaxis().set_major_formatter(date_formatter)
#axis.get_xaxis().set_minor_locator( matdates.MinuteLocator(interval=10) )
#axis.get_xaxis().set_major_locator( matdates.HourLocator(interval=1) )
figure.autofmt_xdate()
pyplot.ylabel('keV')
pyplot.savefig( 'chn_0_trend.pdf', bbox_inches='tight')
pyplot.clf()
