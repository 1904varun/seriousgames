import os, sys
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run_flow
from oauth2client.file import Storage

def return_token(): 
  return get_oauth2_token();


def disable_stout():
  o_stdout = sys.stdout 
  o_file = open(os.devnull, 'w')
  sys.stdout = o_file
  return (o_stdout, o_file)


def enable_stout(o_stdout, o_file):
  o_file.close()
  sys.stdout = o_stdout


def get_oauth2_token():
    CLIENT_ID = '1093977386222-t301lrl380vkc218fdamkgrhfhb1noq9.apps.googleusercontent.com'
    CLIENT_SECRET = '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'
    SCOPE = 'https://accounts.google.com/o/oauth2/auth/fitness.activity.read	'
    REDIRECT_URI = 'http://127.0.0.1:8000/oauth2/callback/google'

    o_stdout, o_file = disable_stout()

    flow = OAuth2WebServerFlow(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope=SCOPE,
        redirect_uri=REDIRECT_URI)

    storage = Storage('creds.data')
    credentials = run_flow(flow, storage)
    enable_stout(o_stdout, o_file)

    print ("access_token: %s" % credentials.access_token)

if __name__ == '__main__':
  return_token()