# LiteratusRobotum
🔓 A simple Python script to extract desired strings from native Android libraries

# Usage

    python3 extract.py -f <filename.apk> -l <libname.so> -s <desired length>
    
or

    python3 extract.py -f <filename.apk> -l <libname.so> -s <minimum length> <maximum length>

To see all the options use

    python3 extract.py --help

For example: to extract all strings of length 20 simply run:

    python3 extract.py -f myapp.apk -l mylib.so -s 20
