#export ENERGY_MATEO_USER=
#export ENERGY_MATEO_PWD=
export SOURCE_FILE="/Users/pfriedland/Documents/projects/enel/na-markets/aeso"
export OPENSSL_CONF=$SOURCE_FILE/openssl.cnf
export NA_MARKETS_AESO_CONFIG_FILE=$SOURCE_FILE/config.json
#export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
bash -c "source $SOURCE_FILE/.pyenv/bin/activate; python3 $SOURCE_FILE/main.py" 
