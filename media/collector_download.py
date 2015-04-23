import sys
import os
import re

urlpat = r'((http[s]?):\/\/)?(\w+\.)*(?P<domain>\w+)\.(\w+)(\/.*)?'

links = sys.argv[1]
links = open( links , 'r')

outf = sys.argv[2]

log = open('log.txt', 'w')

for link in links:

    link = link.strip()

    try:

        ## link format: id, url
        _link = link.split(',')
        out = open( outf + '/' + _link[0] + '.txt', 'w' )

        _link = _link[1]
        ## try to dynamically load the correct script using the domain name
        loader = re.match( urlpat , _link ).group('domain')
        loader = structures = __import__( 'sites.' + loader, fromlist = [ loader ] )

        ## load the current story
        loader.nouda( _link, out )
        out.close()

    except:

        log.write( link + '\n')