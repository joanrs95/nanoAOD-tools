#!/usr/bin/env python
import os, sys
import ROOT
import json
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from postprocessing.framework.postprocessor import PostProcessor

isData = sys.argv[-1] == 'data'

### INPUT FILE
#filepath = ['/afs/cern.ch/work/j/jrgonzal/public/pruebaNanoAOD/8EAB6B64-9210-E811-B19D-FA163E759AE3.root']
#filepath = ['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/2CE738F9-C212-E811-BD0E-EC0D9A8222CE.root']
filepath = ['/pool/ciencias/nanoAODv4/5TeV/nanoAODnoSkim/SingleMuon_Run2017G-17Nov2017-v1/191122_134724/0000/myNanoProdMc5TeVMC_NANO_1.root']
#filepath = ['root://cms-xrd-global.cern.ch//store/data/Run2017B/DoubleMuon/NANOAOD/Nano14Dec2018-v1/280000/FB901F01-98AA-214F-A2C2-D67630861952.root']
#filepath = ['/nfs/fanae/user/juanr/nanoAOD/CMSSW_9_4_6/src/PhysicsTools/NanoAODTools/python/postprocessing/skimtree.root']

### OUTPUT
outdir = '/nfs/fanae/user/joanrs/Escritorio/WZ5TeV/'

#OUTPUT NAME
outFileName ='SingleMuon'

### SKIM 
cut = None #'(nElectron + nMuon) >= 0' # nGenDressedLepton >= 2

### SLIM FILE
slimfile = "postprocessing/SlimFile.txt"
#jecfile  = "Spring18_ppRef5TeV_V4_DATA"

### JSON FILE

### MODULES
### Include modules to compute derivate quantities or calculate uncertainties
from postprocessing.modules.jme.jetmetUncertainties import *  # We use this module only to MC sammples because we have gen variables
from postprocessing.modules.common.puWeightProducer import *
from postprocessing.modules.common.muonScaleResProducer import *
from postprocessing.modules.skimNRecoLeps import *
from postprocessing.modules.jme.jetRecalib import * # We use this module only to DATA
#from modules.addSUSYvar import *
#mod = [puAutoWeight(), skimRecoLeps(), addSUSYvarsMC()] # countHistogramsProducer(), jetmetUncertainties2017All()
#mod = [skimRecoLeps(), muonScaleRes2018()] # jetRecalib(jecfile), countHistogramsProducer(), jetmetUncertainties2017All()
#mod=[jetmetUncertainties5TeVDATA()]
mod=[jetmetRecalib5TeVDATA()]
POSTPROCESSOR=PostProcessor(outdir,outFileName,filepath,cut,slimfile,mod,jsonInput="/nfs/fanae/user/joanrs/CMSSW_9_4_6/src/PhysicsTools/NanoAODTools/python/postprocessing/json/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt",provenance=True,outputbranchsel=slimfile)
#p.run()
