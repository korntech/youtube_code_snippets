# -*- coding: utf-8 -*-

import argparse
import os
import pandas as pd
import scapy.all as scapy


def get_args():
    
    parser = argparse.ArgumentParser(prog='Network Scanner',
                                     description='Network scanner based on ARP protocol',
                                     epilog='Super adming is watching!')
    parser.add_argument('-t', '--target',required='True', help='Provide IPv4 network range')
    parser.add_argument('-v', '--verbose', help='Turn on verbose mode', 
                        action='store_true')
    parser.add_argument('-o', dest='fout', help='Save program output to a file')
    
    # parse args passed on the cli
    args = parser.parse_args()
    
    return args


def net_scan(net):
    
    arp_req = scapy.ARP(pdst=net)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_broad_req = broadcast/arp_req
    ans, unans = scapy.srp(arp_broad_req, timeout=2, verbose=False)

    res_dict = {}
    ips =  []
    macs = []
    
    for elem in ans:
        ips.append(elem[1].psrc)
        macs.append(elem[1].hwsrc)
        
    res_dict['IPAddress'] = ips
    res_dict['MAC Address'] = macs
        
    return ans, unans, res_dict
     
  
def print_results(results, verbose=False):
    
    ans = results[0]
    unans = results[1]
    
    print("MAC Address\t\tIPAddress")
    print(35 * '-')
    for elem in ans:
        print(elem[1].hwsrc + '\t' +  elem[1].psrc)
        
    if verbose:
        print("\nPrinting unanswered summary")
        print(35 * '-') 
        for elem in unans:
            print(elem.summary())
      

def main():
    
    args = get_args()
    results = net_scan(args.target)
    res_dict = results[2]
    
    if args.verbose:
        print_results(results, verbose=True)
    else:
        print_results(results)
    
    if args.fout:
        cwd = os.getcwd()
        df = pd.DataFrame(res_dict)
        df.to_csv('test.csv', index=False)
        print(f'Results saved under the following directory {cwd}.')
        
        
if __name__ == "__main__":
    main()
