#!/bin/bash

set -e

function build_rpm() {
	name="$1"
	_version="$2"
	major=$(echo $_version | cut -d. -f1)
	minor=$(echo $_version | cut -d. -f2)
	build=$(echo $_version | cut -d. -f3)

	version=${major}.${minor}
	[[ -z "$build" ]] && build=0

	rpmbuild -ba --define "_version ${version}" --define "build_number ${build}" SPECS/${name}.spec # 2&>1 /dev/null
 	sudo yum -y install $(ls -tr RPMS/x86_64/"$name"-"$version"* | grep -v debug | tail -n-1)
}

[[ "$#" -ne 1 && "$#" -ne 2 ]] && {
	echo "Usage:"
	echo "		$0 name version"
	echo "		$0 all"
	exit
}

if [[ "$1" == "all" ]]; then
    build_rpm sequencer 2.2.9
    build_rpm autosave 6.0.0
    build_rpm iocStats 3.2.0
    build_rpm ether-ip 3.3.0
    build_rpm sscan 2.11.6
    build_rpm calc 3.7.5
    build_rpm asyn 4.45.0
    build_rpm scaler 4.1.0
    build_rpm stream-device 2.8.26
    build_rpm modbus 3.4.0
    build_rpm busy 1.7.4
    build_rpm std 3.6.4
    build_rpm motor 7.3.1
    build_rpm mca 7.10.0
    build_rpm area-detector-support 1.10.0
    build_rpm area-detector-core 3.14.0
    build_rpm dxp 6.1.0
    build_rpm area-detector-simulation 2.11.0
    build_rpm area-detector-genicam 1.10.0
    build_rpm area-detector-aravis 2.3.0
    build_rpm area-detector-pylon 0.0.1
    build_rpm area-detector-pilatus 2.9.0
    build_rpm area-detector-spinnaker 3.3.0
else
    build_rpm "$1" "$2"
fi

