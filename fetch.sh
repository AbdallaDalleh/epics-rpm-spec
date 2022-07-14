#!/bin/bash

set -e

sources="/home/control/work/epics-modules"
rpmbuild="/home/control/rpmbuild"
modules_repos="asyn autosave busy calc caputRecorder dxp iocStats ipac mca modbus motor sscan std stream-device ether-ip"
ad_repos="ADCore|core ADSupport|support ADSimDetector|simulation ADGenICam|genicam ADAravis|aravis"
repos="${modules_repos} ${ad_repos}"
seq_version="2.2.9"

for module in $repos; do
	if [[ "$module" == "stream-device" ]]; then
		url="https://github.com/paulscherrerinstitute/StreamDevice"
	elif [[ "$module" == "ether-ip" ]]; then
		url="https://github.com/EPICSTools/ether_ip"
	elif [[ "$module" == AD* ]]; then
		repo_name=$(echo $module | cut -d'|' -f1)
		module=area-detector-$(echo $module | cut -d'|' -f2)
		url="https://github.com/areaDetector/${repo_name}"
	else
		url="https://github.com/epics-modules/$module"
	fi

	if [[ ! -d $module/.git ]]; then
		rm -rf $module
		git clone --quiet "$url" $module
	fi

	cd $module
	git checkout --quiet -- .
	git checkout --quiet master
	git pull --quiet origin master
	git fetch --quiet --all --tags
	[[ "$module" == "motor" ]] && git submodule update --init --recursive
	version="$(git describe --tags "$(git rev-list --tags --max-count=1)")"
	git checkout --quiet "${version}"

	cd ../
	version=$(echo $version | sed -e "s/ether_ip-//g" -e "s/R//g" -e "s/-/./g")
	[[ -z "$(echo $version | cut -d. -f3)" ]] && version=${version}.0
	echo ${module} - ${version}
	rm -rf $rpmbuild/SOURCES/$module-$version
	cp -a $module $rpmbuild/SOURCES/$module-$version
	cd $rpmbuild/SOURCES/$module-$version
	find . -name ".git*" | xargs rm -rf
	[[ -f ${sources}/release-files/${module}.RELEASE ]]     && cp ${sources}/release-files/${module}.RELEASE     configure/RELEASE
	[[ -f ${sources}/release-files/${module}.CONFIG_SITE ]] && cp ${sources}/release-files/${module}.CONFIG_SITE configure/CONFIG_SITE
	[[ "$module" == area-detector-!(core) || "$module" == "dxp" ]] && find . -name Makefile -exec sed -i "s/ADApp/cfg/g" {} \;
	[[ "$module" == "motor" ]] && grep -rHE "^SUPPORT\s?=" | cut -d: -f1 | xargs sed -i -e "s/SUPPORT=.*/SUPPORT=\/opt\/epics\/support/g" -e "s/SUPPORT =.*/SUPPORT=\/opt\/epics\/support/g"

	cd $rpmbuild/SOURCES
	tar czvf ${module}-${version}.tar.gz ${module}-${version}/ > /dev/null 2>&1
	cd ${sources}
done

# Sequencer
[[ ! -f seq-${seq_version}.tar.gz ]] && wget https://www-csr.bessy.de/control/SoftDist/sequencer/releases/seq-${seq_version}.tar.gz > /dev/null 2>&1
if [[ -f seq-${seq_version}.tar.gz ]]; then
	tar xvf seq-${seq_version}.tar.gz > /dev/null 2>&1
	sed -i "s/^EPICS_BASE.*/EPICS_BASE=\/opt\/epics\/base/g" seq-${seq_version}/configure/RELEASE
	cp -a seq-${seq_version} $rpmbuild/SOURCES/
	cd $rpmbuild/SOURCES
	tar czvf seq-${seq_version}.tar.gz seq-${seq_version}/ > /dev/null 2>&1
	cd ~-
fi

exit

# Area Detector
# for item in $ad_repos; do
# 	module=$(echo $item | cut -d'|' -f1)
# 	name=area-detector-$(echo $item | cut -d'|' -f2)
# 	if [[ ! -d $name/.git ]]; then
# 		git clone --quiet https://github.com/areaDetector/$module $name
# 	fi
# 
# 	cd $name
# 	git checkout --quiet master
# 	git pull --quiet origin master
# 	git fetch --quiet --all --tags
# 	version="$(git describe --tags "$(git rev-list --tags --max-count=1)")"
# 	git checkout --quiet "${version}"
# 	cd ../
# 	
# 	version=$(echo $version | sed -e "s/R//g" -e "s/-/./g")
# 	[[ -z "$(echo $version | cut -d. -f3)" ]] && version=${version}.0
# 	echo ${module} - ${version}
# 	rm -rf $rpmbuild/SOURCES/$name-$version
# 	cp -a $name $rpmbuild/SOURCES/$name-$version
# 	[[ -f release-files/${name}.RELEASE ]]     && cp release-files/${name}.RELEASE $rpmbuild/SOURCES/$name-$version/configure/RELEASE
# 	[[ -f release-files/${name}.CONFIG_SITE ]] && cp release-files/${name}.CONFIG_SITE $rpmbuild/SOURCES/$name-$version/configure/CONFIG_SITE
# 	cd $rpmbuild/SOURCES/${name}-${version}
# 	find . -name ".git*" | xargs rm -rf
# 	[[ "$name" == "area-detector-simulation" ]] && sed -i "s/ADApp/cfg/g" simDetectorApp/src/Makefile 
# 	cd $rpmbuild/SOURCES
# 	tar czvf ${name}-${version}.tar.gz ${name}-${version}/ > /dev/null 2>&1
# 	cd /home/control/work/epics-modules
# done
 
