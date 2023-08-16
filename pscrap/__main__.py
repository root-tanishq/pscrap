#!/usr/bin/env python3
# [P]scra[P] | Coded with <3 by Tanishq Rathore 
# Version 1.0.0
try:
    from __init__ import printParams
except:
    from pscrap import printParams

import multiprocessing as mp
import sys


def main():
    if not sys.stdin.isatty():
        try:
            urlFile = []
            for line in sys.stdin:
                try:
                    urlFile.append(line.split()[0])
                except:
                    pass
            with mp.Pool(10) as worker:
                worker.map(printParams , urlFile)
        except KeyboardInterrupt:
            exit(0)
        except:
            exit(0)
    else:
        print("[P]scra[P] | Coded with <3 by Tanishq Rathore")
        print("\n[!] provide url list via stdin")

if __name__ == '__main__':
    main()
