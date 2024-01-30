#!/usr/bin/env bash
echoerr() { echo "ERROR: $@" 1>&2; }

set -o errexit
set -o pipefail
set -o nounset

if [[ "$#" != "1" ]] ; then
  echo "$0 <install dir>"
  exit 1
fi

# user-defined: where to build, and where to install
readonly BUILDROOT="$(mktemp --directory --suffix "-openjdk-builder")"
echo ${BUILDROOT}
#function cleanup() {
#  rm -rf "${BUILDROOT}" &> /dev/null || true
#}
#trap cleanup EXIT


# Some Variables to run build, update depending on system
# This is for x64 linux
readonly SRC_FOLDER_NAME="jdk"
readonly JVM_20_FOLDER="jdk-20.0.1"
readonly JVM_20_LINK="https://download.java.net/java/GA/jdk20.0.1/b4887098932d415489976708ad6d1a4b/9/GPL/openjdk-20.0.1_linux-x64_bin.tar.gz"
readonly HOME_USR_BIN="${HOME}/usr/bin"
readonly INSTALLROOT="$(readlink -f $1)"
readonly JDK_20_TAR_NAME="openjdk-20.0.1_linux-x64_bin.tar.gz"

mkdir -p "${BUILDROOT}"
cd "${BUILDROOT}"

#echo "$PWD"

rm -rf * || true

#git clone git@github.com:openjdk/jdk.git

##################################################
# Get temporary copy of jdk-18
##################################################

#wget ${JVM_20_LINK}

#tar -xvf ${JDK_20_TAR_NAME}

##################################################
# BUILD OpenJDK
##################################################

#cd ${BUILDROOT}/${SRC_FOLDER_NAME}

# Configure build to use OpenJDK 18
#mkdir -p ${INSTALLROOT}

echo "bash configure --with-boot-jdk=${BUILDROOT}/${JVM_20_FOLDER} --exec-prefix=${INSTALLROOT} --prefix=${INSTALLROOT} --with-cups=/usr/ --with-fontconfig-include=/usr/include/ --with-fontconfig=/usr/ --with-jvm-variants=zero"

exit

bash configure --with-boot-jdk=${BUILDROOT}/${JVM_20_FOLDER} --exec-prefix=${INSTALLROOT} --prefix=${INSTALLROOT} --with-cups=/usr/ --with-fontconfig-include=/usr/include/ --with-fontconfig=/usr/ --with-jvm-variants=zero

# Make image and copy to destination folder
make install

echo "Newest OpenJDK version installed in ${INSTALLEDROOT}"

cleanup
