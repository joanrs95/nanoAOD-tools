json_year = {
2017      : '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/5TeV/ReReco/Cert_306546-306826_5TeV_EOY2017ReReco_Collisions17_JSON.txt',
}
paths_year={
    2017: [
        "HLT_HIEle20_WPLoose_Gsf", #306912491.937151670
        "HLT_HIEle20_Ele12_CaloIdL_TrackIdL_IsoVL_DZ", #306912492.407505512
        "HLT_HIEle15_Ele8_CaloIdL_TrackIdL_IsoVL", #306912492.407505512
        "HLT_HIL3Mu20", #306912731.817611098
        "HLT_HIL3DoubleMu0", # 306912731.817611098
        "HLT_HIL3DoubleMu10",  #306912731.817611098
        "HLT_HIEle10_WPLoose_Gsf",  #14931793.119622858
        "HLT_HIEle15_WPLoose_Gsf",  #264409549.181837410
        "HLT_HIL3Mu7", #279681844.128230095
        "HLT_HIL3Mu12",  #306912731.817611098
    ],
    }

for year in [2017]:
    for path in paths_year[year]:
        print "brilcalc lumi -i {json} --hltpath {path}_v* > list_{year}_{path}.txt".format(json=json_year[year], path=path,year=year)
                                                                                                                                                                                                  

