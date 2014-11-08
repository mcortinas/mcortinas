#!/usr/bin/python
'''
Created on 13/08/2014
@author: mcortinas
This python script parse CSV obtained from phantomas and send all files to graphite 
EXAMPLE:
phantomas http://foo.com --no-externals -R csv:timestamp > foo.com
python phan2graph.py -H localhost -f foo.com
 
Basic Steps 
 1. Check params
 2. Check file
 3. Read CVSfile
 4. Set the matrics value name from he basename from csv file
 5. Convert timestamp from ISO8601 to Unix time
 6. Load headers metrics names
 7. Load values array
 8. Import data to graphite
 
'''
import os.path
import socket
import logging
import optparse
import csv
import datetime
import calendar

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')

def sendtographite(message,server,port):
    CARBON_SERVER = server
    CARBON_PORT = int(port) 
    logging.debug('sending message:'+message+' to '+CARBON_SERVER)
    sock = socket.socket()
    sock.connect((CARBON_SERVER, CARBON_PORT))
    sock.sendall(message)
    sock.close()


def main():
    logging.info('Start PhantomasCSV to Graphite Script')
    parser = optparse.OptionParser("%prog -H <Host> -f <csv filepath> [options]")
    parser.add_option('-H','--host', help='mandatory: host or ip of graphite server',dest='host')
    parser.add_option('-f','--file',help='mandatory: file path of csv source',dest='file')
    parser.add_option('-p','--port',help='port of graphite server, default 2003',dest='port',default='2003')
    #parser.add_option('--dry-run',help='no actions taken, only read and emulate',dest='dryrun',default=False,action='store_true')
    #parser.add_option('-v','--verbose',help='verbose mode, all actions will be logged',dest='verbose',default=False,action='store_true')
    (opts,args)=parser.parse_args()
    mandatories=['host','file']
    
    for m in mandatories:
        if not opts.__dict__[m]:
            logging.error('mandatory options is missing')
            parser.print_help()
            logging.info('End PhantomasCSV to Graphite Script')
            exit(-1)
    
    logging.debug('Host: '+opts.__dict__['host']+' File:'+opts.__dict__['file']+' Port:'+opts.__dict__['port'])             
    
    #verify CSV file exist
    if not os.path.exists(opts.__dict__['file']):
        logging.error('File '+opts.__dict__['file']+'not found')
        exit(-1)
    
    #Parse CSV file, obtain timestamp from first field and send to graphite
    head, urltest = os.path.split(opts.__dict__['file'])    
    infile = open(opts.__dict__['file'], 'r')
    reader = csv.reader(infile, delimiter=',')
    rownum = 0
    for row in reader:
        if rownum == 0 :
            #create header list with metric titles from first field
            header = row
            logging.debug(rownum)
            logging.debug(header)    
        else:
            colnum = 0
            for col in row :
                if colnum == 0 :
                    timestamp=calendar.timegm(datetime.datetime.strptime(col, "%Y-%m-%dT%H:%M:%S").timetuple()) 
                    logging.debug(timestamp)
                else:
                    message='metric.'+urltest+'.'+header[int(colnum)]+' '+col+' '+str(timestamp)+'\n'
                    logging.debug(message)
                    sendtographite(message,socket.gethostbyname(opts.__dict__['host']),opts.__dict__['port']) 
                colnum += 1
        rownum += 1        

    logging.info('End PhantomasCSV to Graphite Script')
    
if __name__ == "__main__":
    main()
 