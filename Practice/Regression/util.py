"""

    util.py
    download data files and pre-processing
    made by Wonbin Kim

"""

import numpy as np
import math
import timeit
from six.moves import urllib
import sys, tarfile, glob
import shutil

def printProgress(current, total, prefix='Progress', suffix='Complete', barLength=100):
    percent = (current)*100 / float(total)
    assert current <= total  and percent >= 0, "Invaild total and current %d %d %d" %(current, total, percent)
    progressed = int(percent * barLength / 100)
    bar = '#' * progressed + '-' * (barLength-progressed)
    sys.stdout.write('\r%s |%s| %3.2f %s %s'%(prefix, bar, percent, '%', suffix))
    if current == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

    
def file_download(url, path_):
    file_name = url.split('/')[-1]
    u = urllib.request.urlopen(url)
    file_meta = u.info()
    file_size = int(file_meta['Content-Length'])
    file_path = path.join(path_,file_name)
    if not path.exists(file_path) or stat(file_path).st_size != file_size:
        with open(file_path, 'wb') as f:
            print ("Downloading: %s Bytes: %s" % (file_path, file_size))
            file_size_dl = 0
            file_block_sz = 1024 * 64
            while True:
                buffer = u.read(file_block_sz)
                if not buffer:
                       break
                file_size_dl += len(buffer)
                f.write(buffer)
                printProgress(file_size_dl, file_size)
    return file_path


def handling_xlsx(fname, attr_exist=False):
    """
        Arg
        - fname : file_name (with path to file)
        - attr_exist : (if attribute name is in first row)
        
        The first low entities in xlsx file must not have any meaningless entities.
        And also other low entites at least should have some value in given attribute.
    """
    import zipfile
    from xml.etree.ElementTree import iterparse
    z = zipfile.ZipFile(fname)
    strings = [el.text for e, el in iterparse(z.open('xl/sharedStrings.xml'))
                if el.tag.endswith('}t')]
    no_attr = len(strings)
    rows = []
    row = {}
    data, label = [], None
    tag, counter = True, 0
    value = ''
    for e, el in iterparse(z.open('xl/worksheets/sheet1.xml')):
        if el.tag.endswith('}v'):
            value = el.text
        if el.tag.endswith('}c'):
            if el.attrib.get('t') == 's':
                value = strings[int(value)]
            letter = el.attrib['r']
            while letter[-1].isdigit():
                letter = letter[:-1]
            if counter >= no_attr : continue
            if not value : break
            if label:
                row[label[letter]] = value
            else:
                row[letter] = value
            counter += 1
            value = ''
        if el.tag.endswith('}row'):
            
            if attr_exist and tag:
                label = row
                tag = False
            else:
                rows.append(row)
            row, counter = {}, 0
    return rows    

def _shuffle(covariate, response):
    d = list(zip(covariate, response))
    from random import shuffle, seed
    seed('2018')
    shuffle(d)
    new_covariate, new_response = zip(*d)
    return np.array(new_covariate), np.array(new_response)