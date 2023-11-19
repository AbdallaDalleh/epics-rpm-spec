#!/bin/bash

set -e

function pushd() {
	command pushd "$@" > /dev/null
}

function popd() {
	command popd "$@" > /dev/null
}

sources="${HOME}/work/epics-modules"
rpmbuild="${HOME}/control/rpmbuild"
nfs=/mnt/epics
[[ -z "$base_version" ]] && base_version="3.15.6"
[[ -z "$seq_version"  ]] && seq_version="2.2.9"

if [[ ! -z "$base_version" ]]; then
	rm -rf ${rpmbuild}/SOURCES/epics-base-${base_version}
	cp -a ${nfs}/base-${base_version} ${rpmbuild}/SOURCES/epics-base-${base_version}
	pushd ${rpmbuild}/SOURCES/
	tar czf epics-base-${base_version}.tar.gz epics-base-${base_version}
	popd
fi

# if [[ ! -z "$seq_version" ]]; then
# 	rm -rf ${rpmbuild}/SOURCES/seq-${seq_version}
# 	cp -a ${nfs}/seq ${rpmbuild}/SOURCES/seq-${seq_version}
# 	pushd ${rpmbuild}/SOURCES/
# 	tar czf seq-${seq_version}.tar.gz seq-${seq_version}
# 	popd
# fi

# pushd ${nfs}
for module in $(ls -1 -d ${nfs}/* | grep -v -e "base-"); do
	cp -a -f ${module} .
	module=$(basename ${module})

	if [[ -d ${module}/.git ]]; then
		pushd ${module}
		tags=$(git rev-list --tags --max-count=1)
		if [[ -z "${tags}" ]]; then
			version=0.0.1
			git checkout --quiet master
		else
			version="$(git describe --tags "$(git rev-list --tags --max-count=1)")"
			git checkout --quiet "${version}"
		fi
		popd
	else
		version=$(basename ${module} | awk -F- '{print $NF}')
		mv ${module} $(basename ${module} "-${version}")
		module=$(basename ${module} "-${version}")
	fi

	# cd ../
	version=$(echo $version | sed -e "s/ether_ip-//g" -e "s/R//g" -e "s/-/./g" -e "s/r//g")
	[[ -z "$(echo $version | cut -d. -f3)" ]] && version=${version}.0
	echo ${module} - ${version}
	rm -rf $rpmbuild/SOURCES/$module-$version
	cp -a -f $module $rpmbuild/SOURCES/$module-$version
	rm -rf ${module}
	cd $rpmbuild/SOURCES/$module-$version
	find . -name ".git*" | xargs rm -rf
	[[ -f ${sources}/release-files/${module}.RELEASE ]]     && cp ${sources}/release-files/${module}.RELEASE     configure/RELEASE
	[[ -f ${sources}/release-files/${module}.CONFIG_SITE ]] && cp ${sources}/release-files/${module}.CONFIG_SITE configure/CONFIG_SITE
	[[ "$module" == area-detector-!(core) || "$module" == "dxp" ]] && find . -name Makefile -exec sed -i "s/ADApp/cfg/g" {} \;
	[[ "$module" == "motor" ]] && grep -rHE "^SUPPORT\s?=" | cut -d: -f1 | xargs sed -i -e "s/SUPPORT=.*/SUPPORT=\/opt\/epics\/support/g" -e "s/SUPPORT =.*/SUPPORT=\/opt\/epics\/support/g"
	
	cd ${rpmbuild}/SOURCES/
	tar czvf ${module}-${version}.tar.gz ${module}-${version}/ > /dev/null 2>&1

	# popd
done

# popd

