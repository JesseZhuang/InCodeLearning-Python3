#!/bin/sh

pushd test-runtime # python runtime library path
TEST_ARGS=("$*")
# add test-runtime dirs to be the beginning of the paths
# this way openssl & c_rehash resolve properly in our integ tests
PATH=`pwd`/bin:$PATH
LD_LIBRARYl_PATH=`pwd`/lib:$LD_LIBRARY_PATH
# -s supresses capturing output to stdout.  we want the full output so it's
# easier to debug. If you only want the pytest output remove -s
LD_LIBRARY_PATH=$LD_LIBRARY_PATH PATH=$PATH TEST_ARGS=$TEST_ARGS bin/python3 -m pytest -v test-integ -s
# note that the print script in test-integ may not flush
# https://stackoverflow.com/questions/107705/disable-output-buffering
# https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
retval=$?

popd
exit $retval
