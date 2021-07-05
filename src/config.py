import os

HOST = '0.0.0.0'

PORT = int(os.getenv('PORT'))

RELOAD = os.getenv('RELOAD') == 'true'
