import glob
glob.iglob('dir/*')
for filename in glob.iglob('dir/*'):
    print(filename)
