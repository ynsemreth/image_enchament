# şehirlere ayrılmış dosyalardaki fotoğrafları aşağıdaki dizinde yer alan kelimeleri çıkartarak sadece kişi ismiyle bulunduğu şehrin klasörü içerisine dosyalar 23-567  547  558-550
# not 28. dönemden önceki refah partisi yedinden refah değil replace kısmında "yrp" yerine "rp" yazılmalı
import os
import re

folder_path = r"C:\Users\cypoi\Masaüstü\23.DÖNEM MİLLETVEKİLLERİ VESİKALIK"



party_names = ["  ",
               "A"," A","  A","   A","    A","     A","      A","       A","        A","         A","          A",
               "AA"," AA","  AA","   AA","    AA","     AA","      AA","       AA","        AA","         AA","          AA",
               "AAA"," AAA","  AAA","   AAA","    AAA","     AAA","      AAA","       AAA","        AAA","         AAA","          AAA",
               "AAAA"," AAAA","  AAAA","   AAAA","    AAAA","     AAAA","      AAAA","       AAAA","        AAAA","         AAAA","          AAAA",
               "AAAAA"," AAAAA","  AAAAA","   AAAAA","    AAAAA","     AAAAA","      AAAAA","       AAAAA","        AAAAA","         AAAAA","          AAAAA",
               "AAAAAA"," AAAAAA","  AAAAAA","   AAAAAA","    AAAAAA","     AAAAAA","      AAAAAA","       AAAAAA","        AAAAAA","         AAAAAA","          AAAAAA",
               "AAAAAAA"," AAAAAAA","  AAAAAAA","   AAAAAAA","    AAAAAAA","     AAAAAAA","      AAAAAAA","       AAAAAAA","        AAAAAAA","         AAAAAAA","          AAAAAAA",
               "AAAAAAAA"," AAAAAAAA","  AAAAAAAA","   AAAAAAAA","    AAAAAAAA","     AAAAAAAA","      AAAAAAAA","       AAAAAAAA","        AAAAAAAA","         AAAAAAAA","          AAAAAAAA",
               "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "14","15","16","17","18","19","20","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","40","41","42","43","44","45","46","47","48","49","50","51",
               " 0"," 1"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9"," 10"," 11"," 12"," 13"," 14"," 15"," 16"," 17",
               "  0","  1","  2","  3","  4","  5","  6","  7","  8","  9","  10","  11","  12","  13","  14","  15","  16","  17",
               "   0","   1","   2","   3","   4","   5","   6","   7","   8","   9","   10","   11","   12","   13","   14","   15","   16","   17",
               "    0","    1","    2","    3","    4","    5","    6","    7","    8","    9","    10","    11","    12","    13","    14","    15","    16","    17",
               "     0","     1","     2","     3","     4","     5","     6","     7","     8","     9","     10","     11","     12","     13","     14","     15","     16","     17",
               "1a","2a","3a","4a","5a","6a","7a","8a","9a","10a","11a","12a","13a","14a",
               "1aa","2aa","3aa","4aa","5aa","6aa","7aa","8aa","9aa","10aa","11aa","12aa","13aa","14aa",
               "1b","2b","3b","4b","5b","6b","7b","8b","9b","10b","11b","12b","13b","14b",
               "1bb","2bb","3bb","4bb","5bb","6bb","7bb","8bb","9bb","10bb","11bb","12bb","13bb","14bb",
               "1c","2c","3c","4c","5c","6c","7c","8c","9c","10c","11c","12c","13c","14c",
               "1cc","2cc","3cc","4cc","5cc","6cc","7cc","8cc","9cc","10cc","11cc","12cc","13cc","14cc",
               "17.DÖNEM","18.DÖNEM","19.DÖNEM","20.DÖNEM","21.DÖNEM","22.DÖNEM","23.DÖNEM","24.DÖNEM","25.DÖNEM","26.DÖNEM","27.DÖNEM","28.DÖNEM",
               "17.","18.","19.","20.","21.","22.","23.","24.","25.","26.","27.","28.",
               "DÖNEM","DÖNEM1","DÖNEM2","DÖNEM3","DÖNEM4","DÖNEM5","DÖNEM6","DÖNEM7","DÖNEM8","DÖNEM9","DÖNEM10",
               "p","p1","p2","p3","p4","p5","p6","p7","p8","p9","p10",
               
            "ALBUM","ALBÜM","5x6","5x5","5x4","5X","vs",'ves','ve','copy','2aaa','bıometrık','bometrık','BIOMET','biometrik','VSS','bıom','BIO','bio','8bio','12bio','24BİOMETRİK','24VESİKALIK',
            'kopyala','- Kopya','SSSSSSSSSSSSSS',' ,,','-',' -','- ','i1','i2','i3','i4','i5','-1','-2','-3','-4','-5','-6','-7','-8','-9','-10',
            'VESİKALIK','8ADET','adet','12adet','ESKİ','MİLLETVEKİLİ','BAĞIMSIZ','BAGIMSIZ','MV']




# Dosya isimlerini düzenleme ve klasörlere taşıma  
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".jpg") or filename.endswith(".JPG"):
            new_filename = (filename.replace(" jpg", ".jpg")
                            
                            .replace("AK PARTİ1","AKP 1").replace("AK PARTİ2","AKP 2").replace("AK PARTİ3","AKP 3").replace("AK PARTİ4","AKP 4")
                            .replace("AK PARTİ5","AKP 5").replace("AK PARTİ6","AKP 6").replace("AK PARTİ7","AKP 7").replace("AK PARTİ8","AKP 8").replace("AK PARTİ9","AKP 9")
                            .replace("AKPA","AKP").replace("AKPAA","AKP").replace("AKPAAA","AKP").replace("AKPAAAA","AKP").replace("AKPAAAAA","AKP").replace("AKPAAAAAA","AKP").replace("AKPAAAAAAA","AKP")
                            .replace("CHP1","CHP").replace("CHPAA","CHP").replace("CHPAAA","CHP").replace("CHPAAAA","CHP").replace("CHPAAAAA","CHP").replace("CHPAAAAA","CHP").replace("CHPAAAAAAA","CHP")
                            .replace("MHP1","MHP").replace("MHPAA","MHP").replace("MHPAAA","MHP").replace("MHPAAAA","MHP").replace("MHPAAAAA","MHP").replace("MHPAAAAA","MHP").replace("MHPAAAAAAA","MHP")
                            .replace("HDP1","HDP").replace("HDPAA","HDP").replace("HDPAAA","HDP").replace("HDPAAAA","HDP").replace("HDPAAAAA","HDP").replace("HDPAAAAA","HDP").replace("HDPAAAAAAA","HDP")
                            .replace("AKPALBÜM","AKP").replace("CHPALBÜM","CHP").replace("MHPALBÜM","MHP").replace("MHPALBÜM","MHP")
                            .replace("- 1","1").replace("- 2","2").replace("- 3","3").replace("- 4","4").replace("- 5","5").replace("- 6","6").replace("- 7","7").replace("- 8","8").replace("- 9","9").replace("- 10","10").replace("- 11","11").replace("- 12","12").replace("- 13","13").replace("- 14","14").replace("- 15","15").replace("- 16","16")
                            .replace("FAZILET PARTISI","FP").replace("FAZILET","FP").replace("REFAH","YRP").replace("MÇP","MCP").replace("BAGIMSIZ","BAĞIMSIZ").replace("AKPBAŞBAKAN","AKP").replace("AKP4.dönem","AKP").replace("YEŞİL SOL PARTİ","YSP")
                            )
            




            os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
            

            
            name, ext = os.path.splitext(new_filename)
            new_name = re.sub(r'\(\d+\)', ' ', name)
            for party_name in party_names:
                new_name = re.sub(fr'\b{party_name}\b', ' ', new_name, flags=re.IGNORECASE)
            new_name = new_name.strip()
            if new_name:
                new_path = os.path.join(root, new_name)
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                new_file_path = os.path.join(new_path, new_filename)
                try:
                    os.rename(os.path.join(root, new_filename), new_file_path)
                except:
                    print(" ")
