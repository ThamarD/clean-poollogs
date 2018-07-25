import requests
import json
import sys
import time
import argparse

if sys.version_info[0] < 3:
        print ('python2 not supported, please use python3')
        sys.exit (0)


# Parse command line args
parser = argparse.ArgumentParser(description='DPoS delegate - Poollogs.json Clean-up script')
parser.add_argument('-c', metavar='config.json', dest='cfile', action='store',
                   default='config.json',
                   help='set a config file (default: config.json)')

args = parser.parse_args ()


# Load the config file
try:
        conf = json.load (open (args.cfile, 'r'))
except:
        print ('Unable to load config file.')
        sys.exit ()


if 'logfile' in conf:
        LOGFILE = conf['logfile']
else:
        LOGFILE = 'poollogs.json'


# load the logfile: poollogs.json
def loadLog (logfilename):
        try:
                data = json.load (open (logfilename, 'r'))
        except:
                data = {
                        "lastpayout": 0,
                        "accounts": {},
                        "skip": []
                }
        return data


def saveLog (log, logfilename):
        json.dump (log, open (logfilename, 'w'), indent=4, separators=(',', ': '))



def cleanup_poollogs ():
        poollogsfilename = LOGFILE
        cleanuppoollogsfilename = 'removedvotes' + LOGFILE

        log = loadLog(poollogsfilename)
        logcleanup = loadLog(cleanuppoollogsfilename)

        # Hisotry crunching starts after 48 hour
        daytime = 24 * 60 * 60
        currenttime = int(time.time())

        today_timestamp_readable = time.strftime("%Y-%m-%d %H:%M", time.localtime(int(currenttime)))

        # step 1 get all people who currently voted for me as a delegate - get their address
        d = requests.get(conf['node'] + '/api/delegates/voters?publicKey=' + conf['pubkey']).json()


        # Update last time the cleanup script has run
        logcleanup['lastpayout'] = int(time.time())

        currentvotingaddresses = []
        newcleanupaddresses = []

        # put all current votingadresses in een array
        for r in d['accounts']:
                currentvotingaddresses.append(r['address'])

        # detect if an address in the poollogs.json is not anymore in the currentlist of votingadresses and put this addres in another array
        # we cannot delete x in log when we are using the for loop
        # if a voter has returned and left again. The total amount of  pending and received are totalized
        for x in log['accounts']:
                if not x in currentvotingaddresses:
                        newcleanupaddresses.append(x)
                        if not x in logcleanup['accounts']:
                                logcleanup['accounts'][x] = {
                                        'pending': log['accounts'][x]['pending'],
                                        'received': log['accounts'][x]['received'],
                                        'unvotedate': []
                                }
                        else:
                            try:
                                logcleanup['accounts'][x] = {
                                        'pending': logcleanup['accounts'][x]['pending'] + log['accounts'][x]['pending'],
                                        'received': logcleanup['accounts'][x]['received'] + log['accounts'][x]['received'],
                                         'unvotedate': logcleanup['accounts'][x]['unvotedate']
                                }
                            except KeyError:
                                logcleanup['accounts'][x] = {
                                        'pending': logcleanup['accounts'][x]['pending'] + log['accounts'][x]['pending'],
                                        'received': logcleanup['accounts'][x]['received'] + log['accounts'][x]['received'],
                                        'unvotedate': []
                                }

                        logcleanup['accounts'][x]["unvotedate"].append(str(today_timestamp_readable))
#                        print('\tcleanup in poollogs.json:', x)

        # remove  the cleanup voters from the log (where all the poollogs.json adresses are in)
        for x in newcleanupaddresses:
                if x in log['accounts']:
                        del log['accounts'][x]
#                       print ('\tRemoved cleanup: ', x)

        #save 2 files, first the 'clean' poollogs.json; second the cleanup in same format as poollogs.json so we can display them in the same way
        saveLog (log, poollogsfilename)
        saveLog (logcleanup, cleanuppoollogsfilename)


if __name__ == "__main__":
    cleanup_poollogs()

