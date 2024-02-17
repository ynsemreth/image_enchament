import os
import re

folder_path = r"C:\Users\cypoi\Masaüstü\23.DÖNEM MİLLETVEKİLLERİ VESİKALIK"


for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".jpg") or filename.endswith(".JPG"):
            new_filename = (filename.replace("AK PARTİ", "AKP")
                            .replace("AKP1","AKP 1").replace("AKP2","AKP 2").replace("AKP3","AKP 3").replace("AKP4","AKP 4").replace("AKP5","AKP 5").replace("AKP6","AKP 6").replace("AKP7","AKP 7").replace("AKP8","AKP 8").replace("AKP9","AKP 9").replace("AKP10","AKP 10").replace("AKP11","AKP 11")
                            .replace("CHP1","CHP 1").replace("CHP2","CHP 2").replace("CHP3","CHP 3").replace("CHP4","CHP 4").replace("CHP5","CHP 5").replace("CHP6","CHP 6").replace("CHP7","CHP 7").replace("CHP8","CHP 8").replace("CHP9","CHP 9").replace("CHP10","CHP 10").replace("CHP11","CHP 11")
                            .replace("MHP1","MHP 1").replace("MHP2","MHP 2").replace("MHP3","MHP 3").replace("MHP4","MHP 4").replace("MHP5","MHP 5").replace("MHP6","MHP 6").replace("MHP7","MHP 7").replace("MHP8","MHP 8").replace("MHP9","MHP 9").replace("MHP10","MHP 10").replace("MHP11","MHP 11")
                            .replace("HDP1","HDP 1").replace("HDP2","HDP 2").replace("HDP3","HDP 3").replace("HDP4","HDP 4").replace("HDP5","HDP 5").replace("HDP6","HDP 6").replace("HDP7","HDP 7").replace("HDP8","HDP 8").replace("HDP9","HDP 9").replace("HDP10","HDP 10").replace("HDP11","HDP 11")
                            .replace("YSP1","YSP 1").replace("YSP2","YSP 2").replace("YSP3","YSP 3").replace("YSP4","YSP 4").replace("YSP5","YSP 5").replace("YSP6","YSP 6").replace("YSP7","YSP 7").replace("YSP8","YSP 8").replace("YSP9","YSP 9").replace("YSP10","YSP 10").replace("YSP11","YSP 11")
                            .replace("HÜDAPAR1","HÜDAPAR 1").replace("HÜDAPAR2","HÜDAPAR 2").replace("HÜDAPAR3","HÜDAPAR 3").replace("HÜDAPAR4","HÜDAPAR 4").replace("HÜDAPAR5","HÜDAPAR 5")
                            .replace("GELECEK1","GELECEK 1").replace("GELECEK2","GELECEK 2").replace("GELECEK3","GELECEK 3").replace("GELECEK4","GELECEK 4").replace("GELECEK5","GELECEK 5")
                            .replace("SAADET1","SAADET 1").replace("SAADET2","SAADET 2").replace("SAADET3","SAADET 3").replace("SAADET4","SAADET 4").replace("SAADET5","SAADET 5").replace("SAADET6","SAADET 6").replace("SAADET7","SAADET 7")
                            .replace("REFAH1","REFAH 1").replace("REFAH2","REFAH 2").replace("REFAH3","REFAH 3").replace("REFAH4","REFAH 4").replace("REFAH5","REFAH 5")
                            .replace("HEDEP1","HEDEP 1").replace("HEDEP2","HEDEP 2").replace("HEDEP3","HEDEP 3").replace("HEDEP4","HEDEP 4").replace("HEDEP5","HEDEP 5")
                            .replace("DEVA1","DEVA 1").replace("DEVA2","DEVA 2").replace("DEVA3","DEVA 3").replace("DEVA4","DEVA 4").replace("DEVA5","DEVA 5")
                            .replace("TİP1","TİP 1")
                            .replace("DP1","DP 1").replace("DP2","DP 2").replace("DP3","DP 3")
                            .replace("SAADET PARTİSİ","SAADET").replace("REFAH PARTİSİ","REFAH").replace("DEMOKRAT","DP").replace("YEŞİL SOL PARTİ","YSP").replace("AKPARTİ","AKP")
                            .replace("AKPARTİ1","AKP 1").replace("AKPARTİ2","AKP 2").replace("AKPARTİ3","AKP 3").replace("AKPARTİ4","AKP 4")
                            .replace("AKPARTİ5","AKP 5").replace("AKPARTİ6","AKP 6").replace("AKPARTİ7","AKP 7").replace("AKPARTİ8","AKP 8").replace("AKPARTİ9","AKP 9")
                            .replace("PARTİ1","PARTİ 1").replace("PARTİ2","PARTİ 2").replace("PARTİ3","PARTİ 3").replace("PARTİ4","PARTİ 4").replace("PARTİ5","PARTİ 5").replace("PARTİ6","PARTİ 6").replace("PARTİ7","PARTİ 7").replace("PARTİ8","PARTİ 8").replace("PARTİ9","PARTİ 9").replace("PARTİ10","PARTİ 10").replace("PARTİ11","PARTİ 11")
                            .replace("- 1","1").replace("- 2","2").replace("- 3","3").replace("- 4","4").replace("- 5","5").replace("- 6","6").replace("- 7","7").replace("- 8","8").replace("- 9","9").replace("- 10","10")
                            
                            )
            try:
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
            except:
                print(" ")
