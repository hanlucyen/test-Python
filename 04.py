Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
pd.__
>>> pd.__version__
'1.2.4'
>>> import numpy as np
>>> import pandas
>>> df=pandas.read_excel('C:\\monhoc.xlsx')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    df=pandas.read_excel('C:\\monhoc.xlsx')
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\util\_decorators.py", line 299, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\io\excel\_base.py", line 336, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\io\excel\_base.py", line 1071, in __init__
    ext = inspect_excel_format(
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\io\excel\_base.py", line 949, in inspect_excel_format
    with get_handle(
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\io\common.py", line 651, in get_handle
    handle = open(handle, ioargs.mode)
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\monhoc.xlsx'
>>> df=pandas.read_excel('Desktop:\\monhoc.xlsx')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    df=pandas.read_excel('Desktop:\\monhoc.xlsx')
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\util\_decorators.py", line 299, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\io\excel\_base.py", line 336, in read_excel
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\io\excel\_base.py", line 1071, in __init__
    ext = inspect_excel_format(
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\io\excel\_base.py", line 949, in inspect_excel_format
    with get_handle(
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\io\common.py", line 651, in get_handle
    handle = open(handle, ioargs.mode)
OSError: [Errno 22] Invalid argument: 'Desktop:\\monhoc.xlsx'
>>> df=open("Desktop:\\monhoc.xlsx")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    df=open("Desktop:\\monhoc.xlsx")
OSError: [Errno 22] Invalid argument: 'Desktop:\\monhoc.xlsx'
>>> df=open("C:\Users\ASUS\Documents\ctrr\monhoc.xlsx")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> df=open('C:\Users\ASUS\Documents\ctrr\monhoc.xlsx')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> df=open(C:\Users\ASUS\Documents\ctrr\monhoc.xlsx)
SyntaxError: invalid syntax
>>> df=open("C:/Users/ASUS/Documents/ctrr/monhoc.xlsx")
>>> df=pandas.read_excel("C:/Users/ASUS/Documents/ctrr/monhoc.xlsx")
>>> print(df.columns)
Index(['Môn học(A1)', 'Lập trình căn bản', 'Đại số', 'Toán rời rạc', 'Vật lý',
       'Hóa học', 'Thể dục'],
      dtype='object')
>>> giatri=df['<tên cột>'].values
Traceback (most recent call last):
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 3080, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 70, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 101, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 4554, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 4562, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: '<tên cột>'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    giatri=df['<tên cột>'].values
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\core\frame.py", line 3024, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\ASUS\anaconda3\lib\site-packages\pandas\core\indexes\base.py", line 3082, in get_loc
    raise KeyError(key) from err
KeyError: '<tên cột>'
>>> giatri=df['Thể dục'].values
>>> print(giatri)
[nan  0.  0.  1.  0.  0.  0.]
>>> giatri=df['Lập trình căn bản'].values
>>> print(giatri)
['(Lưu ý :giá trị 1:là môn ở dòng cần được học trước môn ở cột)' 0 0 0 0 0
 1]
>>> giatri=df['Đại số'].values
>>> print(giatri)
[nan  1.  0.  0.  0.  0.  1.]
>>> giatri=df['Toán rời rạc'].values
>>> print(giatri)
[nan  1.  0.  0.  0.  0.  1.]
>>> 