import zipfile

zf=zipfile.ZipFile('demo.zip',mode='w')
zf.write('datatext.txt')
zf.write('demofile2.txt')
zf.close
