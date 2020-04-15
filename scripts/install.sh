crontab -l > tmp
echo "0 */6 * * * sh /var/www/bots/gorgar-speaks/scripts/run.sh" >> tmp
crontab tmp
