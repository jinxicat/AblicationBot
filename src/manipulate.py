# Just a test script
# Demonstrates unzipping, editing and zipping of ODT documents in python
# Source ODT file "in.odt" shall exist in "/tmp"
# If ODT file contains string token, it will be replaced with string replacement
#

import os
import zipfile
import fileinput

rootDirURL="/home/chyper/application_bot/src/files/"

tmpDir="~odt_contents"
tmpDirURL=rootDirURL+"/"+tmpDir

zipSourceFile="input.odt"
zipSourceFileURL=rootDirURL+"/"+zipSourceFile

zipOutFile="BrennanCoverLetter.odt"
zipOutFileURL=rootDirURL+"/"+zipOutFile

xmlFile="content.xml"
xmlFileURL=tmpDirURL+"/"+xmlFile

token="Cloud and DevOps Infrastructure Analyst"
replacement="TEST SUCCESSFUL"

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
    print (line.replace(token,replacement))

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