# JAVA

## Setup
### OpenJDK

 1. [Get the complete source code](#getting-the-source-code): \
    `git clone https://git.openjdk.org/jdk/`

 2. [Run configure](#running-configure): \
    `bash configure`

    If `configure` fails due to missing dependencies (to either the
    [toolchain](#native-compiler-toolchain-requirements), [build tools](
    #build-tools-requirements), [external libraries](
    #external-library-requirements) or the [boot JDK](#boot-jdk-requirements)),
    most of the time it prints a suggestion on how to resolve the situation on
    your platform. Follow the instructions, and try running `bash configure`
    again.

 3. [Run make](#running-make): \
    `make images`

 4. Verify your newly built JDK: \
    `./build/*/images/jdk/bin/java -version`

 5. [Run basic tests](##running-tests): \
    `make run-test-tier1`

### Additional Info on Building OpenJDK

- There are a list of pre-requisites that need to be
installed to build OpenJDK from source: https://github.com/openjdk/jdk/blob/master/doc/building.md#external-library-requirements

- The script `install_openjdk.sh` can be used to automatically install `openjdk` on your machine after installing all pre-reqs. Note that some variables need to be changed to install on your specific machine. Use `./install_openjdk.sh <install_dir>` to install to desired directory.
