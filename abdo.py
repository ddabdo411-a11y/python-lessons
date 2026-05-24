
python Desktop\learn_python.py


"""

import time
import sys
import os

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
if sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

def print_slow(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        else:
            print("\n  >> اختيار غير صحيح، حاول مرة أخرى")

if __name__ == "__main__":
    print_slow("ملاحظة: إذا ظهرت أحرف غير مفهومة، شغّل البرنامج بهذا الأمر:")
    print_slow('  $env:PYTHONIOENCODING="utf-8"; python learn_python.py')
    print()
    main()
 
 