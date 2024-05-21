#!/bin/bash

##########################################################################################################
##                                                                                                      ##
## Description: This script will find all files with extension "log" and compress it                    ##
##              and move the compressed file to "backup" directory                                      ##
## Author:      Nitish Kothekar                                                                         ##
##                                                                                                      ##
##########################################################################################################


#env variables
log_file_name="find_logs.log"
{
current_date=$(date +"%Y%m%d")
backup_dir=backup
archive_file="logs-${current_date}.tar.gz"


echo -e "\n******************** Starting Logs Backup Script ******************** \n"
error_function()
{
        echo "The script $0 has failed at \"$BASH_COMMAND\"\n"
        echo "\n******************** An error has been encountered ******************** \n"
        exit
}
trap error_function ERR

# Create backup directory 
echo "Creating ${backup_dir} directory"
mkdir -p ${backup_dir}

# Find log files
echo "Searching files with .log extension"
log_files=$(find . -type f -name *.log)
#echo $log_files

# Create tar file
echo "Compressing log files"
tar -cvzf ${backup_dir}/${archive_file} ${log_files}

echo -e "\n******************** Script executed successfully ******************** \n"
} 2>&1 | sed "s|^|$(date +%Y\ %b\ %d\ \ %H:%M:%S)  |" | tee -a ${log_file_name}
