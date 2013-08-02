time = "2013-07-25 12:54:52,733"
echo | awk '{split("'${time}'",b,":");print array[1]}'

