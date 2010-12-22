#!/usr/bin/env sh

PYXB_ROOT=${PYXB_ROOT:-`pwd`/../pyxb}
export PYTHONPATH=${PYXB_ROOT}
export PATH=${PYXB_ROOT}/scripts:${PATH}


# Extract the parameters
URI=$1
shift

MAIN_PREFIX=$1

PREFIXES=""
until [ -z "$1" ]
do
    PREFIXES=$PREFIXES" -m $1"
    shift
done

rm -rf $MAIN_PREFIX
mkdir $MAIN_PREFIX ; cd $MAIN_PREFIX
pyxbgen \
   --schema-root=.. \
   $PREFIXES \
   -u "${URI}" \
   -r 
if [ ! -f ${MAIN_PREFIX}.py ] ; then
  echo "from raw.${MAIN_PREFIX} import *" > ${MAIN_PREFIX}.py
fi
touch __init__.py

cd ..
