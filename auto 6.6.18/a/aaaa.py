import codecs
with codecs.open('log.txt','a') as f:  
    s = str("hiii babuy")
    f.write(s)
    f.write('\n')
    f.close()
