# pyCompry
#A Python Script to Compress and Copy a Folder = pyCompry

This is the README file for pyCompry, a script to automate compression and transfer of any folder.

You can use this script to automate backup of any folder. This script, once executed with input and output arguments, will check the output folder for any previously created zip file and then create a new zip file containing the contents of the input folder. This is useful in automating backup of any folder as well as useful in transferring large files over a slow network since it compresses the source. Example:- You have scheduled a daily backup of your Database and destination to store backup files is a local folder within the same server. Now you want to automate the transfer of these backup files to a DR server. In such cases, you can use this script to automate the backup of these files to a DR server/site.

Usage:

On Unix

Hostname:~# python pyCompry.py -i /user/somesourcefolder -o /mnt/remotemount/somebackupfolder

On Windows

C:\Users\username> python pyCompry.py -i d:\somesourcefolder -o x:\SomeMappedRemoteFolder

You will need to schedule this script in the task scheduler if you want complete automated scheduled run of this script. Use crontab in Unix and Scheduled Task on Windows to schedule the runnning of the script.

Please cerate a 
