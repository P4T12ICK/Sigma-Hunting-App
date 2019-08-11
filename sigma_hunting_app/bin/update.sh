#!/bin/sh
unset PYTHONPATH
unset LD_LIBRARY_PATH

if [ -z $SPLUNK_HOME ]; then
    splunk_path='/opt/splunk'
else
    splunk_path=$SPLUNK_HOME
fi


# look for config /local/settings.conf otherwise /default/settings.conf
repository=''
folder=''
FILE=$splunk_path/etc/apps/sigma_hunting_app/local/settings.conf

repository=$(cat $splunk_path/etc/apps/sigma_hunting_app/default/settings.conf | grep repository | cut -d ' ' -f3)
folder=$(cat $splunk_path/etc/apps/sigma_hunting_app/default/settings.conf | grep folder | cut -d ' ' -f3)

if [ -f $FILE ]; then
    check_repository=$(cat $splunk_path/etc/apps/sigma_hunting_app/local/settings.conf | grep repository | cut -d ' ' -f3)
    if ! [ -z $check_repository ]; then
        repository=$check_repository
    fi 

    check_folder=$(cat $splunk_path/etc/apps/sigma_hunting_app/local/settings.conf | grep folder | cut -d ' ' -f3)
    if ! [ -z $check_folder ]; then
        folder=$check_folder
    fi
fi

cd $splunk_path/etc/apps/sigma_hunting_app/Sigma2SplunkAlert 
rm -rf rules/*
cd rules 
git clone $repository > /dev/null 2>&1
cd ..



if ! [ "${folder:-1}" == "/" ]; then
  folder=$folder/
fi

./sigma2splunkalert --config config/config.yml --sigma-config sigma_config/splunk-all.yml rules/$folder > savedsearches.conf
cp savedsearches.conf ../default/savedsearches.conf  


