# Just a test script
# Demonstrates unzipping, editing and zipping of ODT documents in python
# Source ODT file "in.odt" shall exist in "/tmp"
# If ODT file contains string token, it will be replaced with string replacement
#

import os
import zipfile
import fileinput
import subprocess
import shutil

rootDirURL="ApplicationBot/src/files/"

tmpDir="~odt_contents"
tmpDirURL=rootDirURL+"/"+tmpDir

zipSourceFile="input_cover_letter.odt"
zipSourceFileURL=rootDirURL+"/"+zipSourceFile

zipOutFile="output_cover_letter.odt"
zipOutFileURL=rootDirURL+"/"+zipOutFile

xmlFile="content.xml"
xmlFileURL=tmpDirURL+"/"+xmlFile

token1="[job title]"
replacement1="Automation Engineer"

token2="[company name]"
replacement2="SpaceX"

#
# Unzip ODT
#
print (" -- Extracting ---------------------")
print ("%s -> %s" % (zipSourceFileURL, tmpDirURL))

zipdata = zipfile.ZipFile(zipSourceFileURL)
zipdata.extractall(tmpDirURL)

#
# Find and replace tokens
#
print (" -- Replacing -------------")
print (xmlFileURL)

for line in fileinput.input(xmlFileURL, inplace=1):
    print (line.replace(token1,replacement1))

for line in fileinput.input(xmlFileURL, inplace=1):
    print (line.replace(token2,replacement2))

# Zip contents of the temporary directory to ODT
# Use file list from the original archive
# This preserves the file structure in the new Zip file
# The most important is that the "mimetype" is the first file in archive

print (" -- Compressing --------------------")
print ("%s -> %s" % (tmpDirURL , zipOutFileURL))

with zipfile.ZipFile(zipOutFileURL, 'w') as outzip:
    zipinfos = zipdata.infolist()
    for zipinfo in zipinfos:
        fileName=zipinfo.filename # The name and path as stored in the archive
        fileURL=tmpDirURL+"/"+fileName # The actual name and path
        outzip.write(fileURL,fileName)

### covert odt document to pdf
input_filename = 'output_cover_letter.odt'
subprocess.call(f'cd files;libreoffice --headless --convert-to pdf {input_filename}', shell=True)