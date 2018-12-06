
source ~/.bash_profile

cd /select_stock/

celery -A celery_pj.celery_start worker -l info



