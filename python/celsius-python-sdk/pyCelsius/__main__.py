import sys
from pyCelsius import __version__ as pyCel_ver

def main():
    print('Python ver {}'.format(sys.version.replace('\n', ' ')))
    print('pyCelsius ver {}'.format(pyCel_ver))

if __name__ == '__main__':
    main()