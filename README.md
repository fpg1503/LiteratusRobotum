# LiteratusRobotum
🔓 A simple Python script to extract desired strings from native Android libraries

# Usage

    python3 extract.py <filename.apk> <libname.so> <desired length>
    
or

    python3 extract.py <filename.apk> <libname.so> <minimum length> <maximum length>

For example: to extract all strings of length 20 simply run:

    python3 extract.py myapp.apk mylib.so 20
