#!/data/data/com.termux/files/usr/bin/sh

echo "\nPostgresql Install"

echo "\nCreate skeleton database"

mkdir -p PREFIX/var/lib/postgresql

initdb PREFIX/var/lib/postgresql

echo "\nStarting the database"

pg_ctl -D PREFIX/var/lib/postgresql start

echo "\nSimilarly stop the database using"

pg_ctl -D PREFIX/var/lib/postgresql stop

echo "\nCreate User"

createuser --superuser --pwprompt NateWeiler

echo "\nCreate your database:"

createdb mydb

echo "\nOpen your database"

psql mydb

echo "\nYou will now see the promt"

mydb=#
