#!/bin/bash

set -e

sources="/home/control/work/epics-modules"
rpmbuild="/home/control/rpmbuild"
url_base="${GIT_URL}"

function build() {
	module="$1"
	location="$2"
	tag="$3"

	[[ -z "$2" ]] && location="${1##*/}"
	[[ -d "$location" ]] && rm -rf "$location"


	if [[ ! -z "$tag" ]]; then
		git clone --depth=1 -b "$tag" --quiet "$1" "$location"
        if [[ "$module" == */edm ]]; then
            version=${tag##*-}
        else
		    version="$tag"
        fi
	else
		git clone --quiet "$1" "$location"
		cd "$location"
		git fetch --quiet --all --tags
		latest_tag=$(git rev-list --tags --max-count=1)
		if [[ ! -z "$latest_tag" ]]; then 
			version="$(git describe --tags "$latest_tag")"
			git checkout --quiet "${version}"
		else
			version=0.0.1
			git checkout --quiet master
		fi
		cd ../
	fi

	if [[ "$module" == *motor ]]; then
		cd motor/
		git submodule set-url -- modules/motorMotorSim  "$url_base"/motorMotorSim
		git submodule set-url -- modules/motorMicos     "$url_base"/motorMicos
		git submodule set-url -- modules/motorAcsMotion "$url_base"/motorAcsMotion
		git submodule update --init modules/motorAcsMotion
		git submodule update --init modules/motorMicos
		git submodule update --init modules/motorMotorSim
		cd ../
	fi

	version=$(echo $version | sed -e "s/ether_ip-//g" -e "s/R//g" -e "s/r//g" -e "s/V//g" -e "s/v//g" -e "s/-/./g" -e "s/MEDM//g" -e "s/_/./g")
	[[ -z "$(echo $version | cut -d. -f3)" ]] && version=${version}.0
	module=${location}
    [[ "$module" == "caqtdm" ]] && sed -i "s/contains(QWT_VER_MIN, 2)/contains(QWT_VER_MIN, 2)|contains(QWT_VER_MIN, 3)/g" caqtdm/caQtDM_QtControls/caQtDM_QtControls.pro
    
	rm -rf $rpmbuild/SOURCES/$module-$version
	cp -a $module $rpmbuild/SOURCES/$module-$version
	cd $rpmbuild/SOURCES/$module-$version
	rm -rf .git
	[[ -f ${sources}/release-files/${module}.RELEASE ]]     && cp ${sources}/release-files/${module}.RELEASE     configure/RELEASE
	[[ -f ${sources}/release-files/${module}.CONFIG_SITE ]] && cp ${sources}/release-files/${module}.CONFIG_SITE configure/CONFIG_SITE
	[[ "$module" == *area-detector-!(core) || "$module" == *dxp ]] && find . -name Makefile -exec sed -i "s/ADApp/cfg/g" {} \;
	# [[ "$module" == "motor" ]] && grep -rHE "^SUPPORT\s?=" | cut -d: -f1 | xargs sed -i -e "s/SUPPORT=.*/SUPPORT=\/opt\/epics\/support/g" -e "s/SUPPORT =.*/SUPPORT=\/opt\/epics\/support/g"
	# [[ "$module" == motor* ]] && cp ${sources}/release-files/motor.RELEASE configure/RELEASE 

	cd ${rpmbuild}/SOURCES/
	tar czvf ${module}-${version}.tar.gz ${module}-${version}/ > /dev/null 2>&1

    echo building ${module} v${version} RPM
    
    cd ${rpmbuild}
	_version="$version"
	major=$(echo $_version | cut -d. -f1)
	minor=$(echo $_version | cut -d. -f2)
	build=$(echo $_version | cut -d. -f3)
	[[ -z "$build" ]] && build=0
	version=${major}.${minor}
	
	rpmbuild -ba --define "_version ${version}" --define "build_number ${build}" SPECS/${module}.spec > /dev/null 2>&1

    rpm_file=$(ls -1 RPMS/x86_64/"$module"* | grep -v debug)
    echo installing ${rpm_file##*/}
	sudo dnf -y install $(ls -1 RPMS/x86_64/"$module"* | grep -v debug) > /dev/null 2>&1
}

. $(dirname $(readlink -f $0))/site-config.sh

