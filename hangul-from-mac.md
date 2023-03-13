### 한글 자모 분리되는 현상 해결

python 로직으로 문제의 파일을 찾아 자모결합되는 문자열로 변경

```python
import sys
from unicodedata import normalize
import os

def change_nfc_all_dir(dirname):
    print("checking dir : "+dirname)
    if os.path.exists(dirname) == False:
        print("Not exists")
        return

    if os.path.isdir(dirname) == False:
        print("Not directory")
        return

    filenames = os.listdir(dirname)
    for filename in filenames:
        before_filename = os.path.join(dirname, filename)
        after_filename = normalize('NFC', before_filename)
        next_dir = before_filename
        if(before_filename != after_filename):
            print("changing : "+before_filename +" --> " + after_filename)
            next_dir = after_filename
            os.rename(before_filename, after_filename)

        if os.path.isdir(next_dir):
            change_nfc_all_dir(next_dir)

change_nfc_all_dir("C:/Users/user1/PoC-proposal/02. 제안서작성")
```
