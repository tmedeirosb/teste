# exemplo cap 4
"""
# download de arquivo

# coding: utf-8

import io
import sys
import urllib.request as request

BUFF_SIZE = 1024


def download_length(response, output, length):
    times = length // BUFF_SIZE

    if length % BUFF_SIZE > 0:
        times += 1

    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100))


def download(response, output):
    total_downloaded = 0

    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Download {bytes}'.format(bytes=total_downloaded))


def main():
    # print('Olá')
    # url http://livropython.com.br/dados.zip

    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO('saida.zip', mode='w')

    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)

    response.close()
    out_file.close()

    print('terminou')


if __name__ == '__main__':
    main()
"""

# extrair arquivos
# coding utf-8

import os
import zipfile
import sys

def main(path):
    if not os.path.exists(path):
        print( 'Arquivo {} não existe'.format(path) )
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print('Arquivo extraídos')

if __name__ == "__main__":
    main(sys.argv[1])




