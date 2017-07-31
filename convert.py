import os, subprocess, re, time
from stat import *
from ast import literal_eval as make_tuple
crop_command = ' -crop 55x170+211+32 '
resize_command = ' -resize 96x256! '
CONVERT = True
IN_DIR = './cropped/'
OUT_DIR = './cropped_resized/'
TEST_CONVERT = False
TEST_DATETIME = False



def convert(filename, outfile):
    if (not os.path.isfile(outfile)):
        clean_outfile = OUT_DIR + re.escape(filename)
        info_command = 'convert ' + IN_DIR + re.escape(filename)
        #print info_command
        output_command = info_command + resize_command
        output_command = output_command + ' ' + clean_outfile
        p = subprocess.Popen(output_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        s, err = p.communicate()
        if len(err) > 0:
            print("Error:", err)
        #print(output_command)
    else:
        print ('ALREADY EXISTS: ' + outfile)

cnt = 0
for filename in os.listdir(IN_DIR):
    if filename.endswith(".png"):
        cnt += 1
        outfile = OUT_DIR + filename
        convert(filename, outfile)    

print( "Finished # " + str(cnt) )