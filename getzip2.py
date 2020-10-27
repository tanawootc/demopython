import zipfile

zf=zipfile.ZipFile('demo.zip',mode='r')

zf.namelist()
zf.extractall('data2')
zf.close
