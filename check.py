import pandas as pd
import sys
# fn = sys.argv[1] # "test-sheet.tsv"
fn = "test-sheet-1.tsv"
regfile = "/Users/frank/model-209-election/RegisteredList.csv"
regfile =  "only.tsv"

regdata = pd.read_csv(regfile, delimiter="\t", dtype={'ADDR_NUM': object,
                                                      'ADDR_DIR': object,})
testdata = pd.read_csv(fn, delimiter="\t", dtype={'ADD': object,
                                                  'DIR': object})

for index, rec in testdata.iterrows():
    if pd.isnull(rec.DIR):
        recs = regdata[ (regdata['ADDR_NUM'] == rec['ADD']) & \
                        (regdata.ADDR_STR == rec.STR) & \
                        (regdata['ADDR_CITY'] == rec['CITY'])]
        rec.DIR=""
    else:
        recs = regdata[ (regdata['ADDR_NUM'] == rec['ADD']) & \
                        (regdata.ADDR_DIR == rec.DIR) & \
                        (regdata.ADDR_STR == rec.STR) & \
                        (regdata['ADDR_CITY'] == rec['CITY'])]

    print " ".join(rec)
    print "\n".join(recs.NAME)
    print "************\n"
                    

    



