#! python3
# Compress the input folder and create a zip file in output path.
# Useful in automating backups and also in copying large files over slow network.
__author__ = "Technokan"
__credits__ = ["Technokan"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Technokan"
__email__ = "kanayak123@yahoo.co.in"
__status__ = "Production"
import os, argparse, zipfile, stat
def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        fullPath = os.path.join(args.output, zipFilename)
        if not os.path.exists(fullPath):
            break
        number = number + 1
    print('Creating %s...' % (fullPath))
    backupZip = zipfile.ZipFile(fullPath, 'w')
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
    compressed_size = os.stat(fullPath).st_size
    print('Compressed File Size on output path: %s' % compressed_size)

parser = argparse.ArgumentParser(conflict_handler='resolve', formatter_class=argparse.RawDescriptionHelpFormatter, description='Example command for unix: python pyCompry.py -i /user/somepath -o /home/somebackuppath OR for Windows: python pyCompry.py -i d:\somepath -o e:\somebackuppath. Please refer to the documentation for more details')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-o','--output',help='Output file name', required=True)
args = parser.parse_args()
print ("Input folder: %s" % args.input )
print ("Output folder: %s" % args.output )
backupToZip(args.input)
