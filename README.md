#pyCompry
###A Python Script to Compress and Copy a Folder = pyCompry

####This is the README file for pyCompry, a script to automate compression and transfer of any folder.

#### Installation & Usage
#####On UNIX
1. Install python and execute the script
This script is devopped using Python 3. Therefore, you will need to install python 3 package.

Run this command to install python on Unix

    apt-get install python3

After installing python3, verify if the python3 is installed correctly. Just run the below command and it should return the python version number.

    python3 --version

2. Clone this repository onto the server or device you are planning to run this script. Once dowloaded, your may run the script by running the below command. Please correct the paths as per your actual paths.

    python pyCompry.py -i /user/somesourcefolder -o /mnt/remotemount/somebackupfolder

####On Windows
Download and install the Python 3. You may download from https://www.python.org/downloads/

Open CMD and run this command

    python pyCompry.py -i d:\somesourcefolder -o x:\SomeMappedRemoteFolder

You can use this script to automate backup of any folder. This script, once executed with input and output arguments, will check the output folder for any previously created zip file and then create a new zip file containing the contents of the input folder. This is useful in automating backup of any folder as well as useful in transferring large files over a slow network since it compresses the source. Example:- You have scheduled a daily backup of your Database and destination to store backup files is a local folder within the same server. Now you want to automate the transfer of these backup files to a DR server. In such cases, you can use this script to automate the backup of these files to a DR server/site.

You will need to schedule this script in the task scheduler if you want completely automate this script. Use crontab in Unix or Task Scheduler on Windows to schedule the script.
