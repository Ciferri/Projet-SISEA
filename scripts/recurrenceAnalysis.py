#!/usr/bin/python

import os
import sys
import shutil
import argparse
import textwrap
import subprocess

if sys.version_info[0] > 2 :
    import configparser as ConfParser
else :
    import ConfigParser as ConfParser

configFilePath = os.path.expanduser("~") + "/.recurrenceAnalysis/config.txt"
if not os.path.exists(configFilePath) :
    print('Please create a configuration file for our python scripts. Refer to the README')
    quit()

configParser = ConfParser.RawConfigParser()
configParser.read(configFilePath)

animaDir = configParser.get("anima-scripts",'anima')
animaExtraDataDir = configParser.get("anima-scripts",'extra-data-root')
atlasDir=os.path.join(animaExtraDataDir,"olivier-atlas") # Path to the Atlas used to estimate the TLL

parser = argparse.ArgumentParser(
    prog='recurrenceAnalysis',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''TODO'''))

parser.add_argument('','--CT1',required=True,help='path to the CT image before radiotherapy')
parser.add_argument('','--CT2',required=True,help='path to the CT image after radiotherapy')
parser.add_argument('','--PET1',required=True,help='path to the PET image before radiotherapy')
parser.add_argument('','--PET2',required=True,help='path to the PET image after radiotherapy')
parser.add_argument('','--output',required=True,help='path to output folder')
parser.add_argument('-T','--nbThreads',required=False,type=int,help='Number of execution threads (default: 0 = all cores)',default=0)

args=parser.parse_args()

CT1Image=args.CT1
CT2Image=args.CT2
PET1Image=args.PET1
PET2Image=args.PET2
outputFolder=args.output
nbThreads=str(args.nbThreads)

if(not(os.path.isfile(CT1Image))):
    print("IO Error: the file "+t1Image+" doesn't exists.")
    quit()

if(not(os.path.isfile(CT2Image))):
    print("IO Error: the file "+t2Image+" doesn't exists.")
    quit()

if(not(os.path.isfile(PET1Image))):
    print("IO Error: the file "+PET1Image+" doesn't exists.")
    quit()

if(not(os.path.isfile(PET2Image))):
    print("IO Error: the file "+PET2Image+" doesn't exists.")
    quit()

if(not(os.path.isdir(outputFolder))):
    os.makedirs(outputFolder)


#Anima commands
animaTotalLesionLoad=os.path.join(animaDir,"animaTotalLesionLoad")

command=[animaGcStremMsLesionsSegmentation, "-m", maskImage, "-a", "1", "--rej", h, "--min-fuzzy", fmin, "--max-fuzzy", fmax, "-i", t1Image, "-j", t2Image, "-l", flairImage, "--ini", "2", "-o", os.path.join(tmpFolder,"outputImage.nrrd"), "--WMratio","0.4","-T",nbThreads]
subprocess.call(command)
