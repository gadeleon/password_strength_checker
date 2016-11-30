'''
Quick n' dirty script/regex to check if password complexity requirements are
met in a file.
'''

import re
import argparse

def rate_password(password):
    '''rate_password - checks password complexity'''
    password_scores = {0:'Horrible', 1:'Weak', 2:'Medium', 3:'Strong', 4:'Best'}
    password_strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num', 'has_symbol'], False)
    password_strength['has_upper'] = bool(re.search(r'[A-Z]', password))
    password_strength['has_lower'] = bool(re.search(r'[a-z]', password))
    password_strength['has_num'] = bool(re.search(r'[0-9]', password))
    password_strength['has_symbol'] = bool(re.search(r'[\W]', password))
    score = len([b for b in password_strength.values() if b])
    #print '{}:{}'.format(password, password_scores[score])
    return password_scores[score]

def main():
    '''main - reads in file and returns results'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 0.1.0')
    parser.add_argument('file', type=str, nargs='+',
                        help='RIHF file(s) with passwords')
    parser.add_argument('--dl', '--delimiter', nargs=1, default=':')
    args = parser.parse_args()
    for data in args.file:
        with open(data, 'r') as infile:
            for line in infile:
                # Parsing happens here, adjust for your needs!
                if ".edu" in line.lower() or '.edu.' in line.lower(): #or '.edu:' in line.lower():
                    try:
                        password = line.split(args.dl[0])[1].split('\r')[0]
                        password = password.strip('\n')
                        #print password
                        if rate_password(password) == 'Strong' or rate_password(password) == 'Best':
                            print line.strip('\n')
                    except IndexError:
                        pass#print 'failed!'

if __name__ == '__main__':
    main()
