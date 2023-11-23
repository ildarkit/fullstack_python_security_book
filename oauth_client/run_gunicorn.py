#! env python

import sys
import subprocess
import certifi


if __name__ == '__main__':
    args = f'-b localhost:8001 --ca_certs {certifi.where()}'
    print(f'{args=}')
    subprocess.Popen(['gunicorn', sys.argv[1], '-b localhost:8001', f'--ca-certs={certifi.where()}'])
