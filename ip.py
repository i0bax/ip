#!/usr/bin/python

from netaddr import *
from sys import argv
import pprint

cos = raw_input("podaj adres i maske ")
ip = IPAddress('{0}'.format(cos[:-3]))
ipn = IPNetwork('{0}'.format(cos))


print ('\x1b[6;32;42m' + '\t\t\t\t\t\t\t\t' + '\x1b[0m')
print ('\x1b[1;31;40m' + 'Adres hosta : ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t{0}"+ '\x1b[0m').format(ip)
print ('\x1b[6;32;42m' + '\t\t\t\t\t\t\t\t' + '\x1b[0m')

print ('\x1b[1;31;40m' + 'Adres Sieci: ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t{0}"+ '\x1b[0m').format(ipn.network)
print ('\x1b[1;31;40m' + 'maska: ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t\t{0}"+ '\x1b[0m').format(ipn.netmask)
print ('\x1b[1;31;40m' + 'broadcast: ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t{0}"+ '\x1b[0m').format(ipn.broadcast)
print ('\x1b[6;32;42m' + '\t\t\t\t\t\t\t\t' + '\x1b[0m')

print ('\x1b[1;31;40m' + 'Adres hosta bitowo: ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t{0}"+ '\x1b[0m').format(ip.bits())
print ('\x1b[1;31;40m' + 'Adres Sieci bitowo: ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t{0}"+ '\x1b[0m').format(ipn.network.bits())
print ('\x1b[1;31;40m' + 'maska bitowo: ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t\t{0}"+ '\x1b[0m').format(ipn.netmask.bits())
print ('\x1b[6;32;42m' + '\t\t\t\t\t\t\t\t' + '\x1b[0m')

print ('\x1b[1;31;40m' + 'adres pierwszego hosta: ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t{0}"+ '\x1b[0m').format((ipn.network+1))
print ('\x1b[1;31;40m' + 'adres ostatniego hosta: ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t{0}"+ '\x1b[0m').format((ipn.broadcast-1))
print ('\x1b[1;31;40m' + 'Ilosc adresow na hosty: ' + '\x1b[0m'+'\x1b[1;37;40m' + "\t{0}"+ '\x1b[0m').format((ipn.size-2))
print ('\x1b[6;32;42m' + '\t\t\t\t\t\t\t\t' + '\x1b[0m')
