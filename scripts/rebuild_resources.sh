#!/bin/bash
#
# Run supporting pyrcc files to generate resource files and future
# designer conversions into python code. Run this from the home project
# directory like:
# <project root> $ ./scripts/rebuild_resources.sh

CMD_NAME="pyside-rcc"
UIC_NAME="pyside-uic"


if [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    echo "Windows detected"
    CMD_NAME="C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe"
    UIC_NAME="C:\Python27\Lib\site-packages\PySide\pyside-uic.exe"
    if [ ! -e $UIC_NAME ]
    then
        echo "git-bash pyside-uic.exe with no prefix instead"
        UIC_NAME="pyside-uic.exe"
    fi
fi

echo "Rebuilding resources file"

# Use the relative package name glob so the build is portable across
# other projects
#$CMD_NAME \
#    */assets/resources.qrc \
#    -o */assets/resources_rc.py

# Process all of the QRC Files
for QRC_FILE in */assets/*.qrc;
    do echo "QRC Processing $QRC_FILE";

    PREFIX=$(echo $QRC_FILE | cut -d '.' -f 1)
    DEST_RC=${PREFIX}_rc.py
    $CMD_NAME $QRC_FILE -o $DEST_RC

done

for UIC_FILE in */assets/*.ui;
    do echo "UIC Processing $UIC_FILE";

    PREFIX=$(echo $UIC_FILE | cut -d '.' -f 1)
    DEST_PY=${PREFIX}.py
    $UIC_NAME  $UIC_FILE  -o $DEST_PY

done

