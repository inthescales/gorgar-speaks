crontab -l > tmp
echo "0 */4 * * * sh /var/www/bots/gorgar-speaks/scripts/run" >> tmp
crontab tmp