#!/usr/bin/python2.7

import corr, numpy,sys,os,time,logging


if __name__ == '__main__':
    from optparse import OptionParser 
    import subprocess
    from subprocess import *
    from datetime import datetime

    # class for all same-timestamp data
    from Datum import Datum
    # class for all same-antenna data
    from Antenna_Snapshot import Antenna_Snapshot
    # Python/MongoDB interface that supports python objects as DB records
    from mongoengine import *

    import time
    import redis

    p = OptionParser()
    p.set_usage('%prog [options] ')
    p.set_description(__doc__)
    p.add_option('-v', '--verbose', dest = 'verbose', action = 'store_true',
        help = 'Be verbose about errors.')

    opts, args = p.parse_args(sys.argv[1:])
    verbose=opts.verbose

redisObject=redis.StrictRedis(host='localhost',port=6379, db=0)
# Connect to the MongoDB database (DB)
# It is assumed that mongod is running on 'localhost' at port 27017
# https://docs.mongodb.com/manual/tutorial/manage-mongodb-processes/#start-mongod-processes
connect('ytla')

# intantiate a Datum object to hold all data associated with the same timestamp
# such as antenna data
datum = Datum()

# a collection for Antenna_Snapshot objects
antennas = []
# 7 antennas exist
# an 8th antenna is added for consistency
for antenna in range(0, 8):
    # initialize an Antenna_Snapshot object to contain all data specific to
    # a single antenna at a single moment.
    antennas.append(Antenna_Snapshot())

# Add the antennas to the record
datum.antennas = antennas[]

ant=[0,1,2,3,4,5,6,7]
dictInt = {22070: 0.646, 34164: 1.000, 170898: 5.000}
config_fileX='/home/corr/ytla/ytla7X_280m.conf'
config_fileY='/home/corr/ytla/ytla7Y_280m.conf'
logfileX="/home/corr/ytla/logCorr_X"
logfileY="/home/corr/ytla/logCorr_Y"
logfileSys="/home/corr/ytla/logSys"
logfileLF_Y="/home/corr/ytla/logLF_Y"
logfileLF_X="/home/corr/ytla/logLF_X"
logfileIFLO_Y="/home/corr/ytla/logIFLO_Y"
logfileIFLO_X="/home/corr/ytla/logIFLO_X"

sel1X=[None]*8
sel2X=[None]*8
hybrid_selX=[None]*8
hybrid_selValX=[None]*8
intswX=[None]*8
intswValX=[None]*8
acc_lenX=[None]*8
intLenX=[None]*8

sel1Y=[None]*8
sel2Y=[None]*8
hybrid_selY=[None]*8
hybrid_selValY=[None]*8
intswY=[None]*8
intswValY=[None]*8
acc_lenY=[None]*8
intLenY=[None]*8

lf_Y = [0.0] * 14
lf_X = [0.0] * 14
try:
    print 'Connecting...',
    cX = corr.corr_functions.Correlator(config_file=config_fileX,\
                                   log_level=logging.DEBUG if verbose else logging.INFO,\
                                   connect=False)
    cX.connect()
    print 'done'

except KeyboardInterrupt:
    exit()

try:
    print 'Connecting...',
    cY = corr.corr_functions.Correlator(config_file=config_fileY,\
                                   log_level=logging.DEBUG if verbose else logging.INFO,\
                                   connect=False)
    cY.connect()
    print 'done'

except KeyboardInterrupt:
    exit()

jCorrX=0
jCorrY=0
jSys=0
while (1):
        timenow = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

        # note when the data was collected
        datum.timestamp = timenow

        print timenow
        flogCorrX=open(logfileX,"a")
        i=0
        for f, fpga in enumerate(cX.ffpgas):
           if ant[i] == f:

               #Read back Walsh

               sel1X[i] = fpga.read_int('sel1')
               sel2X[i] = fpga.read_int('sel2')
               print 'Walsh for ADC0 is %i, Walsh for ADC1 is %i, for Ant%i \n' %(sel1X[i], sel2X[i], ant[i])

               #Read back Interrupt value

               intswX[i]=fpga.read_int('intsw')
               if intswX[i] == 1:
                  print 'Internal (CORRECT) interrupt selected for Ant%i \n' %(ant[i])
                  intswValX[i]="CORRECT INTERRUPT"
               elif intswX[i] == 0:
                  print 'External (INCORRECT) interrupt selected for Ant%i \n' %(ant[i])
                  intswValX[i]="INCORRECT INTERRUPT"
               else:
                  print 'There is an error in the setiing of this switch. Needs to be fixed'
                  intswValX[i]="WRONG VALUE"

               #Read back SRR table select value

               hybrid_selX[i]=fpga.read_int('hybrid_sel')
               if hybrid_selX[i] == 1:
                  print 'SRR tables selected for Ant%i \n' %(ant[i])
                  hybrid_selValX[i]="SRR selected"
               elif hybrid_selX[i] == 0:
                  print 'SRR tables NOT selected for Ant%i \n' %(ant[i])
                  hybrid_selValX[i]="SRR NOT selected"
               else:
                  print 'There is an error in the setiing of this switch. Needs to be fixed'
                  hybrid_selValX[i]="WRONG VALUE"
               i +=1

               #Read back Integration time

        i=0
        for x,fpga in enumerate(cX.xfpgas):
               acc_lenX[i] = fpga.read_uint('acc_len')
               intLenX[i]=dictInt.get(acc_lenX[i])
               print 'Reading  acc_len  %i for X engine %i \n'%(acc_lenX[i],i)
               print 'This integration length is %4.3f  for X engine %i\n'%(intLenX[i],i)
               i +=1

        redisObject.lpush('sel1X',str(sel1X))
        redisObject.lpush('sel2X',str(sel2X))
        redisObject.lpush('intswX',str(intswValX))
        redisObject.lpush('hybrid_selX',str(hybrid_selValX))
        redisObject.lpush('intLenX',str(intLenX))

        # Add data for each antenna
        for i in range(0, 7):
            datum.antennas[i].sel1X = sel1X[i]
            datum.antennas[i].sel2X = sel2X[i]
            datum.antennas[i].intswX = intswValX[i]
            datum.antennas[i].hybrid_selX = hybrid_selValX[i]
            datum.antennas[i].intLenX = intLenX[i]

        if (jCorrX == 0):
          flogCorrX.write("%20s %17s %20s %20s %15s \n"%("Timestamp", "Walsh Num", "Interrupt Select", "SRR Selection", "Integration time"))
          flogCorrX.write("%80s\n"%("           "))
          jCorrX=10
        else:
          for antenna in range(0,7):
             flogCorrX.write("Ant%i %22s %4i %4i %20s %20s %6s %5.3f \n"%(antenna,timenow, sel1X[antenna], sel2X[antenna], intswValX[antenna], hybrid_selValX[antenna], " ", intLenX[antenna]))
          flogCorrX.write("%80s\n"%("           "))
        flogCorrX.close()

        i=0
        for f, fpga in enumerate(cY.ffpgas):
           flogCorrY=open(logfileY,"a")
           if ant[i] == f:

               #Read back Walsh

               sel1Y[i] = fpga.read_int('sel1')
               sel2Y[i] = fpga.read_int('sel2')
               print 'Walsh for ADC0 is %i, Walsh for ADC1 is %i, for Ant%i \n' %(sel1Y[i], sel2Y[i], ant[i])

               #Read back Interrupt value

               intswY[i]=fpga.read_int('intsw')
               if intswY[i] == 1:
                  print 'Internal (CORRECT) interrupt selected for Ant%i \n' %(ant[i])
                  intswValY[i]="CORRECT INTERRUPT"
               elif intswY[i] == 0:
                  print 'External (INCORRECT) interrupt selected for Ant%i \n' %(ant[i])
                  intswValY[i]="INCORRECT INTERRUPT"
               else:
                  print 'There is an error in the setiing of this switch. Needs to be fixed'
                  intswValY[i]="WRONG VALUE"

               #Read back SRR table select value

               hybrid_selY[i]=fpga.read_int('hybrid_sel')
               if hybrid_selY[i] == 1:
                  print 'SRR tables selected for Ant%i \n' %(ant[i])
                  hybrid_selValY[i]="SRR selected"
               elif hybrid_selY[i] == 0:
                  print 'SRR tables NOT selected for Ant%i \n' %(ant[i])
                  hybrid_selValY[i]="SRR NOT selected"
               else:
                  print 'There is an error in the setiing of this switch. Needs to be fixed'
                  hybrid_selValY[i]="WRONG VALUE"
               i +=1

               #Read back Integration time

        i=0
        for x,fpga in enumerate(cY.xfpgas):
                      acc_lenY[i] = fpga.read_uint('acc_len')
                      intLenY[i]=dictInt.get(acc_lenY[i])
                      print 'Reading  acc_len  %i for X engine %i \n'%(acc_lenY[i],i)
                      print 'This integration length is %4.3f  for X engine %i\n'%(intLenY[i],i)
                      i +=1


        redisObject.lpush('sel1Y',str(sel1Y))
        redisObject.lpush('sel2Y',str(sel2Y))
        redisObject.lpush('intswY',str(intswValY))
        redisObject.lpush('hybrid_selY',str(hybrid_selValY))
        redisObject.lpush('intLenY',str(intLenY))

        # Add data for each antenna
        for i in range(0, 7):
            datum.antennas[i].sel1Y = sel1Y[i]
            datum.antennas[i].sel2Y = sel2Y[i]
            datum.antennas[i].intswY = intswValY[i]
            datum.antennas[i].hybrid_selY = hybrid_selValY[i]
            datum.antennas[i].intLenY = intLenY[i]

        if (jCorrY == 0):
          flogCorrY.write("%20s %17s %20s %20s %15s \n"%("Timestamp", "Walsh Num", "Interrupt Select", "SRR Selection", "Integration time"))
          flogCorrY.write("%80s\n"%("           "))
          jCorrY=10
        else:
          for antenna in range(0,7):
             flogCorrY.write("Ant%i %22s %4i %4i %20s %20s %6s %5.3f \n"%(antenna,timenow, sel1Y[antenna], sel2Y[antenna], intswValY[antenna], hybrid_selValY[antenna], " ", intLenY[antenna]))
          flogCorrY.write("%80s\n"%("           "))
        flogCorrY.close()


        flogSys=open(logfileSys,"a")
        state = "INIT"

        sout=subprocess.check_output(['/home/corr/modbus/libmodbus-2.0.3/ADAMSOFTWARE/adam-switchNTState',state])
        if (sout[-2] == "0"):
          NTState = "OBSERVING MODE"
          print 'Current State: Main Switch disabled  (CORRECT OBSERVING MODE)'
        elif (sout[-2] == "1"):
          NTState = "MAIN SWITCH ON"
          print 'Current State: Main Switch enabled'

        sout=subprocess.check_output(['/home/corr/modbus/libmodbus-2.0.3/ADAMSOFTWARE/adam-aoNTSelect',state])
        if (int(float(sout[-10:].rstrip('\r\n'))) == 0):
          print 'Current State: Noise enabled '
          NTSelect = "NOISE ENABLED "
        elif (int(float(sout[-10:].rstrip('\r\n'))) == 4):
          NTSelect = "OBSERVING MODE"
          print 'Current State: Tone enabled (CORRECT OBSERVING MODE)'

        sout=subprocess.check_output(['/home/corr/cvr_python_scripts/QuickSynLO.py', str(None), str(None), state])
        print 'Queried LO Frequency',(sout[-26:-14].rstrip('\r\n')),'MHz'
        print 'Queried LO Power', (sout[-12:].rstrip('\r\n')),'dBm'
        LOfreq=float(sout[-26:-14].rstrip('\r\n'))
        LOpower=float(sout[-12:].rstrip('\r\n'))

        redisObject.lpush('Timestamp',timenow)
        redisObject.lpush('NTState',NTState)
        redisObject.lpush('NTSelect',NTSelect)
        redisObject.lpush('LOfreq',LOfreq)
        redisObject.lpush('LOpower',LOpower)

        # Add data associated with all antennas to the record
        datum.timestamp = timenow
        datum.nt_state = NTState
        datum.nt_select = NTSelect
        datum.lo_freq = LOfreq
        datum.lo_power = LOpower

        if (jSys == 0):
            flogSys.write("{:^20}" "{:^30}" "{:25}" "{:^20}" "{:^20}\n".format("Timestamp", "Noise/Tone State", "Noise/Tone Selection", "LO frequency (MHz)", "LO power (dBm)"))
            flogSys.write("{:^80}\n".format("           "))
            jSys=10

        else:
            flogSys.write("%s %22s %22s %24.4f %16.4f\n"%(timenow, NTState, NTSelect, LOfreq, LOpower))
        flogSys.close()

        flogLF_Y=open(logfileLF_Y,"a")
        flogLF_X=open(logfileLF_X,"a")
        flogIFLO_Y=open(logfileIFLO_Y,"a")
        flogIFLO_X=open(logfileIFLO_X,"a")
        try:
          fh_Y=open("/var/www/cgi-bin/lffile","r")
        except:
          lf_Y = [0.0] * 14
        try:
          fh_X=open("/var/www/cgi-bin/lffile_1","r")
        except:
          lf_X = [0.0] * 14
        try:
          Rx0, Rx1, Rx2, Rx3, Rx4, Rx5, Rx6 = numpy.loadtxt('/var/www/cgi-bin/aifileY', usecols=(0, 1 ,2 ,3, 4, 5, 6), unpack=False)
        except IOError:
          Rx0, Rx1, Rx2, Rx3, Rx4, Rx5, Rx6 = [0.0] * 7
        try:
          Rx0_1, Rx1_1, Rx2_1, Rx3_1, Rx4_1, Rx5_1, Rx6_1 = numpy.loadtxt('/var/www/cgi-bin/aifileX', usecols=(0, 1 ,2 ,3, 4, 5, 6), unpack=False)
        except IOError:
          Rx0_1, Rx1_1, Rx2_1, Rx3_1, Rx4_1, Rx5_1, Rx6_1 = [0.0] * 7
        i=0
        for line in fh_Y:
          lf_Y[i]=line.rstrip('\n')
          print lf_Y[i]
          i +=1
        fh_Y.close()
        i=0
        for line in fh_X:
          lf_X[i]=line.rstrip('\n')
          print lf_X[i]
          i +=1

        lf_Xfloat=[float(i) for i in lf_X]
        lf_Yfloat=[float(i) for i in lf_Y]
        redisObject.lpush('lfI_X',str(lf_Xfloat[0::2]))
        redisObject.lpush('lfQ_X',str(lf_Xfloat[1::2]))
        redisObject.lpush('lfI_Y',str(lf_Yfloat[0::2]))
        redisObject.lpush('lfQ_Y',str(lf_Yfloat[1::2]))
        redisObject.lpush('IFLO_X',str([Rx0_1[4], Rx1_1[4], Rx2_1[4], Rx3_1[4], Rx4_1[4], Rx5_1[4], Rx6_1[4]]))
        redisObject.lpush('IFLO_Y',str([Rx0[4], Rx1[4], Rx2[4], Rx3[4], Rx4[4], Rx5[4], Rx6[4]]))

        # Assign values for lfI, X and Y
        for i in range(0, 14, 2):
            datum.lfI_X[i] = lf_Xfloat[i]
            datum.lfI_Y[i] = lf_Yfloat[i]

        # Assign values for lfQ, X and Y
        for i in range(1, 14, 2):
            datum.lfQ_X[i] = lf_Xfloat[i]
            datum.lfQ_Y[i] = lf_Yfloat[i]

        # Create lists for ease of iteration
        iflo_x_s = [Rx0_1, Rx1_1, Rx2_1, Rx3_1, Rx4_1, Rx5_1, Rx6_1]
        iflo_y_s = [Rx0  , Rx1  , Rx2  , Rx3  , Rx4  , Rx5  , Rx6  ]

        # Assign values for iflo, x and y, for every antenna
        for i in range(0, 7):
            datum.antennas[i].iflo_x = iflo_x_s[i]
            datum.antennas[i].iflo_y = iflo_y_s[i]

        # insert the record into the DB
        datum.save()


        flogLF_Y.write("%25s %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f\n"%(timenow, float(lf_Y[0]), float(lf_Y[1]), float(lf_Y[2]), float(lf_Y[3]), float(lf_Y[4]), float(lf_Y[5]), float(lf_Y[6]), float(lf_Y[7]), float(lf_Y[8]), float(lf_Y[9]), float(lf_Y[10]), float(lf_Y[11]), float(lf_Y[12]), float(lf_Y[13])))
        flogLF_Y.write("%80s\n"%("           "))

        flogLF_X.write("%25s %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f\n"%(timenow, float(lf_X[0]), float(lf_X[1]), float(lf_X[2]), float(lf_X[3]), float(lf_X[4]), float(lf_X[5]), float(lf_X[6]), float(lf_X[7]), float(lf_X[8]), float(lf_X[9]), float(lf_X[10]), float(lf_X[11]), float(lf_X[12]), float(lf_X[13])))
        flogLF_X.write("%80s\n"%("           "))

        flogIFLO_Y.write("%25s %10.3f %12.3f %12.3f %12.3f %12.3f %12.3f %12.3f\n"%(timenow, Rx0[4], Rx1[4], Rx2[4], Rx3[4], Rx4[4], Rx5[4], Rx6[4]))
        flogIFLO_Y.write("%80s\n"%("           "))

        flogIFLO_X.write("%25s %10.3f %12.3f %12.3f %12.3f %12.3f %12.3f %12.3f\n"%(timenow, Rx0_1[4], Rx1_1[4], Rx2_1[4], Rx3_1[4], Rx4_1[4], Rx5_1[4], Rx6_1[4]))
        flogIFLO_X.write("%80s\n"%("           "))

        flogLF_X.close()
        flogLF_Y.close()
        flogIFLO_X.close()
        flogIFLO_Y.close()
        time.sleep(2)
