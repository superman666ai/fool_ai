
source ~/.bash_profile

# cd /home/xiets/work/python/debug_python/select_cta/src
cd /opt/pytrade/select_cta/src

export C_FORCE_ROOT="true"

/opt/anaconda2/envs/envtrade/bin/celery -A execute_script worker -l debug > ../logs/celery.log 2>&1 &

