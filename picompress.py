import zlib,sys,time,base64,os

file = raw_input('enter file name')
data = open(file,'rb').read()
compressed = zlib.compress(data,9)
decompress = zlib.decompress(compressed)
print 'original' + data
print 'zipped: \n ' + compressed
print 'unzipped' + decompress