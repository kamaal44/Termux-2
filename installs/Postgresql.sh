#!/data/data/com.termux/files/usr/bin/sh

echo -e "\nPostgresql Install"

echo -e "\nCreate skeleton database"

mkdir -p PREFIX/var/lib/postgresql

initdb PREFIX/var/lib/postgresql

echo -e "\nStarting the database"

pg_ctl -D PREFIX/var/lib/postgresql start

echo -e "\nSimilarly stop the database using"

pg_ctl -D PREFIX/var/lib/postgresql stop

echo -e "\nCreate User"

createuser --superuser --pwprompt NateWeiler

echo -e "\nCreate your database:"

createdb mydb

echo -e "\nOpen your database"

psql mydb

echo -e "\nYou will now see the promt"

mydb=#
