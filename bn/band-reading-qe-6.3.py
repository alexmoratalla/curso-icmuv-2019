import xml.etree.ElementTree as ET
import argparse

parser = argparse.ArgumentParser(description='Read pw.x bands.')
parser.add_argument('prefix', help='the prefix used in the pw.x calculation')
args = parser.parse_args()

# Eigenvalues in QE files are in Ha
HatoeV = 27.2107 

prefix    = args.prefix

# Read the number of KPOINTS
datafile_xml = ET.parse( "%s.xml"%(prefix)).getroot()
print datafile_xml
nkpoints = int(datafile_xml.find("input/k_points_IBZ/nk").text)
nbands   = int(datafile_xml.find("input/bands/nbnd").text)
print "nkpoints:", nkpoints
print "nbands:", nbands

eigen     = []
print 'Reading eigenvalues...',
#print datafile_xml.find("output/band_structure/ks_energies/eigenvalues").text

for ik in xrange(nkpoints):
    for EIGENVALUES in ET.parse("%s.xml"%(prefix)).getroot().findall("output/band_structure/ks_energies/eigenvalues"):
        eigen.append(map(float, EIGENVALUES.text.split() ) )

print 'Writing in gnuplot format...',
f = open('%s.dat'%prefix,'w')
for ib in xrange(nbands):
    for ik in xrange(nkpoints):
        f.write("%.1lf %.4lf \n " % (ik,eigen[ik][ib]*HatoeV) )
    f.write("\n")
f.close()
print 'Done!'
