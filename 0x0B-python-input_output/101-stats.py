#!/usr/bin/python3
"""
101-stats.py
"""
import sys


def printer(fsize):
    print(f'File size: {fsize:d}')
    for st, v in sorted(status.items()):
        if v != 0:
            print(f'{st}: {v:d}')


def main(fsize, status):
    rcount = 0
    for request in sys.stdin:
        request = request.split()
        if len(request) != 9 or type(request[-1]) != int \
                or type(request[-2]) != int:
            continue
        fsize += int(request[-1])
        status[request[-2]] += 1
        rcount += 1
        if (rcount == 10):
            printer(fsize)
            rcount = 0
    printer(fsize)


if __name__ == '__main__':
    fsize = 0
    status = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
    try:
        main(fsize, status)
    except KeyboardInterrupt:
        printer(fsize)
        sys.exit(0)
