#!/bin/bash -x

set -e

repos="seq autosave caputRecorder iocStats ether-ip sscan calc ipac asyn scaler stream-device modbus busy std motor mca support area-detector-core dxp area-detector-simulation area-detector-genicam area-detector-aravis area-detector-pylon area-detector-pilatus"

function build_rpm() {
	name="$1"
	_version="$2"
	major=$(echo $_version | cut -d. -f1)
	minor=$(echo $_version | cut -d. -f2)
	build=$(echo $_version | cut -d. -f3)

	version=${major}.${minor}
	[[ -z "$build" ]] && build=0

	rpmbuild -ba --define "_version ${version}" --define "build_number ${build}" SPECS/${name}.spec
}

[[ "$#" -ne 1 && "$#" -ne 2 ]] && {
	echo "Usage:"
	echo "		$0 name version"
	echo "		$0 all"
	exit
}

if [[ "$1" == "all" ]]; then
	# list=$(ls -d -1 SOURCES/*/ | xargs -I% basename %)
	list="$repos";
	for module in $list; do
		module=$(ls -t -1 SOURCES/*$module*.tar.gz | head -n1 | xargs -I% basename %)
		mod_version=${module##*-}
		mod_name=$(echo $module | sed "s/-$mod_version//g")
		echo $mod_name - $mod_version
		build_rpm $mod_name $mod_version
		sudo yum -y install $(ls -1 RPMS/x86_64/"$mod_name"* | grep -v debug)
	done
else
	build_rpm "$1" "$2"
	sudo yum -y install $(ls -1 RPMS/x86_64/"$1"* | grep -v debug)
fi

