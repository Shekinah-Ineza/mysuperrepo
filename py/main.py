#!/bin/bash
python3 $PYFILE
print("Best School")
#!/bin/bash
if [ -z "$PYFILE" ]; then
    echo "Error: PYFILE environment variable is not set"
    exit 1
fi

if [ ! -f "$PYFILE" ]; then
    echo "Error: The file '$PYFILE' does not exist"
    exit 1
fi

python3 "$PYFILE"

