#!/bin/sh

COMMIT=$(git rev-parse HEAD)

if [ -z "${COMMIT}" ]; then
    echo "Error: Unable to determine the current commit hash."
    exit 1
fi

VERSION=$(cat CMakeLists.txt | grep -m 1 "^\s*project.*VERSION" | grep -P "\d+\.\d+\.\d+" -o)

if [ -z "${VERSION}" ]; then
    echo "Error: Unable to determine the version from CMakeLists.txt."
    exit 1
fi

echo "Commit: ${COMMIT}"
echo "Version: ${VERSION}"

RPMBUILD=$(pwd)/build/rpmbuild
mkdir -p ${RPMBUILD}/{SOURCES,SPECS,SRPMS}

SPEC_OUT="${RPMBUILD}/SPECS/kandle.spec"

sed \
	-e "s/@COMMITHASH0@/${COMMIT}/" \
	-e "s/@VERSION@/${VERSION}/" \
	kandle.tmpl.spec > ${SPEC_OUT}

rm -f ${RPMBUILD}/SRPMS/*

rpmbuild --define="_topdir ${RPMBUILD}" --undefine=_disable_source_fetch -ba "${SPEC_OUT}"
SRPM_KICAD=$(find ${RPMBUILD}/SRPMS/ -name "kicad-${VERSION}*.src.rpm")

set +x
echo "Prepared ${SRPM_KICAD}."
set -x

