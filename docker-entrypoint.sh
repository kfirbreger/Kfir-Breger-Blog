set -e
set -x

cd /app
pelican src
nginx -g 'daemon off;'
