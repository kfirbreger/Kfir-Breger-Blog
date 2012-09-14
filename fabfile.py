from fabric.api import *
import os
#import fabric.contrib.project as project

PROD = 'spilotro.dreamhost.com'
DEST_PATH = '/home/kbreger/www/blog.kfirbreger.com'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
DEPLOY_PATH = os.path.join(ROOT_PATH, 'output')


def clean():
    local('rm -rf ./output/*')


def regen():
    clean()
    local('pelican . -s pelican.conf.py')
    # Cleaning the less files from the output
    local('rm -rf ./output/theme/sass')


# This is for now, until I have a chance to study the fabric docs for rsync
def publish():
    local("rsync -haz --size-only --exclude '*/.DS_Store' output/ spilotro.dreamhost.com:/home/kbreger/www/blog.kfirbreger.com")

def republish():
    regen()
    publish()

# @hosts(PROD)
# def publish():
#     regen()
#     project.rsync_project(
#         remote_dir=DEST_PATH,
#         local_dir=DEPLOY_PATH.rstrip('/') + '/',
#         delete=True
#     )
