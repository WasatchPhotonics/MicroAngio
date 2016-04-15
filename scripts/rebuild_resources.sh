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

    echo "rcc $QRC_FILE -o $DEST_RC"
    $CMD_NAME \
        $QRC_FILE \
        -o $DEST_RC
done

for UIC_FILE in */assets/*.ui;
    do echo "UIC Processing $UIC_FILE";

    PREFIX=$(echo $UIC_FILE | cut -d '.' -f 1)
    DEST_PY=${PREFIX}.py

    echo "rcc $UIC_FILE -o $DEST_PY"
    $UIC_NAME \
        $UIC_FILE \
        -o $DEST_PY
done


#echo "Rebuilding uic forms"
#$UIC_NAME \
#    pysideapp/assets/placeholder_layout.ui\
#    -o pysideapp/assets/placeholder_layout.py
