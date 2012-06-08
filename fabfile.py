from fabric.api import *
import os
#import fabric.contrib.project as project

PROD = 'blog.kfirbreger.com'
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

# @hosts(PROD)
# def publish():
#     regen()
#     project.rsync_project(
#         remote_dir=DEST_PATH,
#         local_dir=DEPLOY_PATH.rstrip('/') + '/',
#         delete=True
#     )