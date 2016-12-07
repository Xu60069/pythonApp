"""
Scan file folder for duplicate files. You may have downloaded file over time from phone, social network, etc.
And it becomes very difficult to know if some photos already exist when there are thousands of them.
This python program would scan through all files under a folder and compute SHA-512 hash value and store hash value in dictionary.
A file a considered duplicate if its hash is found in the dictionary.
This program will produce a log to report duplicate files.
Run this program as
Hashfilescan.py folder
"""
import hashlib
import os
import sys
import time

starttime=time.time()
statusReportTime=starttime
walk_dir = "."  #default to scan current working directory
deletedup=False
if (len(sys.argv)>1): #2 arguments, example: hashfilescan.py scandir
    walk_dir = sys.argv[1]
if (len(sys.argv)>2): #3 arguments, example: hashfilescan.py scandir del
    if sys.argv[2]=="del":
        deletedup=True
print("Command: hashfilescan.py [scandir] [del]");
filedict = {}
totalNew=0
totalDup=0
# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
with open(".\my-filescan.txt", 'wb') as list_file: #file will be closed at end of block
    list_file.write(('walk_dir %s absolute path %s\r\n' % (walk_dir, os.path.abspath(walk_dir))).encode('utf-8'))

    #walk recursively into all subfolders, depth first (keep going into subfolder until no more, then go back up)
    for root, subdirs, files in os.walk(walk_dir):
        list_file.write(('--\nroot = ' + root+'\r\n').encode('utf-8'))
        #list all subfolders under this root. subfolder will be the new root at end of the for loop
        for subdir in subdirs:
            list_file.write(('\t- subdirectory ' + subdir+'\r\n').encode('utf-8'))

        #loop through all files under the root folder
        for filename in files:
            if filename[0]=='.':  #skip system file
                continue
            if time.time()-statusReportTime > 10:  #report scan status every 10 sec
                print("New files %d Duplicate %d after %d sec" % (totalNew, totalDup, time.time()-starttime))
                statusReportTime = time.time()
            file_path = os.path.join(root, filename)   #full path file name

            sha = hashlib.sha512()
            filelen =0
            with open(file_path, 'rb') as f:
                f_content = f.read()
                sha.update(f_content);  # SHA-512 hashing of a file should be unique
                filelen = len(f_content)
            if sha.hexdigest() in filedict.keys():  # find hash in dictionary, meaning find existing file
                fileName, length=filedict[sha.hexdigest()] #use tuple to retrieve both filename and length from dictionary
                if length != filelen:  #should neve happen but check just in case two different share same hash
                    list_file.write('Hash collision warning\r\n'.encode('utf-8'))
                elif length != 0:
                    if deletedup:
                        os.remove(file_path)
                        list_file.write(('delete File %s len: %d\r\n' % (file_path,filelen)).encode('utf-8'))   
                    totalDup += 1  #increment duplicate file count
                list_file.write(('File %s len: %d exists as %s, hash %s.\r\n' % (file_path,filelen,fileName,sha.hexdigest())).encode('utf-8'))
            else:  #new file, hash is not in current dictionary
                filedict[sha.hexdigest()]=(file_path,filelen)  # insert the hash string to dictionary, with tuple value of filename and length
                #list_file.write(('New File %s len: %d hash %s\r\n' % (file_path,filelen,sha.hexdigest())).encode('utf-8'))
                totalNew += 1  #increment unique file count
    endtime = time.time()
    list_file.write(('New files %d Duplicate %d. Took %d sec\r\n' % (totalNew, totalDup, endtime-starttime)).encode('utf-8'))
    
print("New files %d Duplicate %d took %d sec" % (totalNew, totalDup, endtime-starttime))
