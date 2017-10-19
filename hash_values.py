#!/usr/bin/env python3
import sys
import hashlib
import os
from collections import OrderedDict as od

def get_hashsums(file_path):
    hash_values = od()
    hash_values['md5sum'] = hashlib.md5()
    hash_values['sha1sum'] = hashlib.sha1()
    hash_values['sha224sum'] = hashlib.sha224()
    hash_values['sha256sum'] = hashlib.sha256()
    hash_values['sha384sum'] = hashlib.sha384()
    hash_values['sha512sum'] = hashlib.sha512()

    with open(file_path, 'rb') as fd:
        io_read = fd.read(1024)
        while io_read:
              for hashsum in hash_values.keys():
                  hash_values[hashsum].update(io_read)
              io_read = fd.read(1024)

    results = od()
    for key,value in hash_values.items():
         results[key] = value.hexdigest()         
    return results



def main():
    for path in sys.argv[1:]:
        print(">>> ",path)
        for key,value in get_hashsums(path).items():
            print(key,value)

if __name__ == '__main__': main()
