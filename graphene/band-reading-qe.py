import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='Read pw.x bands.')
parser.add_argument('prefix', help='the prefix used in the pw.x calculation')
args = parser.parse_args()

# Eigenvalues in QE files are in Ha
HatoeV = 27.2107 

prefix    = args.prefix
folder    = '%s.save' % prefix
eig_xml   = 'eigenval.xml'
datafile  = 'data-file.xml'

# Read the number of KPOINTS
datafile_xml = ET.parse( "%s/%s"%(folder, datafile)).getroot()
nkpoints = int(datafile_xml.find("BAND_STRUCTURE_INFO/NUMBER_OF_K-POINTS").text)
nbands   = int(datafile_xml.find("BAND_STRUCTURE_INFO/NUMBER_OF_BANDS").text)
print "nkpoints:", nkpoints
print "nbands:", nbands

eigen     = []
print 'Reading eigenvalues...',
for ik in xrange(nkpoints):
    for EIGENVALUES in ET.parse( "%s/K%05d/%s" % (folder,(ik + 1),eig_xml) ).getroot().findall("EIGENVALUES"):
        eigen.append(map(float, EIGENVALUES.text.split()))
print 'Done!'

print 'Writing in gnuplot format...',
f = open('%s.dat'%prefix,'w')
for ib in xrange(nbands):
    for ik in xrange(nkpoints):
        f.write("%.1lf %.4lf \n " % (ik,eigen[ik][ib]*HatoeV) )
    f.write("\n")
f.close()
print 'Done!'
