[settings]

SECRET_KEY=django-insecure-riz$zzqgl^*fgts2p9i1491k_s9ne1!eo#u)%%vhg#wakfc59eq

DEBUG=True

NAME_DB=drinkbuddydb
USER_DB=postgres
PASSWORD_DB=raman123
HOST=127.0.0.1  
PORT=5432



WEATHER_API_KEY=8184c753e9c94575a9a164118232906