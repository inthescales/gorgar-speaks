python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
crontab -l > tmp
echo "0 */6 * * * bash /var/www/bots/gorgar-speaks/scripts/run.sh" >> tmp
crontab tmp
