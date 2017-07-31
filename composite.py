import os, subprocess, re, time
from stat import *
from ast import literal_eval as make_tuple
composite_command = ' -blend 75 '
CONVERT = True
IN2_DIR = '/home/mkim/Downloads/ECEI.009141/cropped_resized/'
IN_DIR = './'

OUT_DIR = './composite/'
TEST_CONVERT = False
TEST_DATETIME = False

PT = re.compile("-([^.]+)")

def convert(filename):
    
    num = PT.search(re.escape(filename)).group()
    print(num)
    outfile = OUT_DIR + "composite" + num + ".png"
    if (not os.path.isfile(outfile)):
        #clean_outfile = OUT_DIR + re.escape(outfile)
        info_command = 'composite '
        #print info_command
        output_command = info_command + composite_command
        output_command = output_command + ' ' + filename
        output_command = output_command + ' ' + IN2_DIR + 'ECEI.009141_' + num[1:] 
        output_command = output_command + '.png '
        output_command = output_command + outfile 

        
        p = subprocess.Popen(output_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        s, err = p.communicate()
        if len(err) > 0:
            print("Error:", err)
        #print(output_command)
    else:
        print ('ALREADY EXISTS: ' + outfile)

cnt = 1
for filename in os.listdir(IN_DIR):
    if filename.endswith(".pnm"):
        cnt += 1
        convert(filename)    

print( "Finished # " + str(cnt) )