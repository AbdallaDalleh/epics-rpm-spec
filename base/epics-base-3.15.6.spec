# 
# EPICS Base 3.15.6 RPM SPEC file
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/base
# %define debug_package %{nil}
# %define __os_install_post %{nil}

Name:			epics-base
Version:		3.15.6
Release:		0%{?dist}
Summary:		Experimental Physics and Industrial Control System (EPICS base 3.15.6)
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov/download/base/base-3.15.6.tar.gz
Source0:		epics-base-3.15.6.tar.gz
BuildRequires:	readline-devel
Autoreq:		0
Conflicts:		epics-base-3.14 epics-base-7
Epoch:			0

%description
EPICS is a software toolkit for building control system for physics facilities 
such as synchrotron light sources.

%prep
# %setup -q -n epics-base-3.15.6
%autosetup

%build


%install
export EPICS_HOST_ARCH=linux-x86_64
export LD_LIBRARY_PATH=%{buildroot}%{epics_prefix}/lib/${EPICS_HOST_ARCH}

make -C "%{_builddir}/%{?buildsubdir}" %{?_smp_mflags} \
LINKER_USE_RPATH=NO \
SHRLIB_VERSION=%{version} \
INSTALL_LOCATION="%{buildroot}%{epics_prefix}" \
FINAL_LOCATION=%{epics_prefix} \
BIN_PERMISSIONS=755 \
LIB_PERMISSIONS=644 \
SHRLIB_PERMISSIONS=755

cp -a %{_builddir}/%{?buildsubdir}/startup %{buildroot}%{epics_prefix}/

install -d %{buildroot}%{_libdir}
install -d %{buildroot}/usr/lib/systemd/system
install -d %{buildroot}%{_bindir}
cp -a $RPM_BUILD_ROOT/opt/epics/base/lib/linux-x86_64/* %{buildroot}%{_libdir}/
cp -a $RPM_BUILD_ROOT/opt/epics/base/bin/linux-x86_64/* $RPM_BUILD_ROOT/usr/bin
cp -a $RPM_BUILD_ROOT/opt/epics/base/bin/linux-x86_64/caRepeater.service $RPM_BUILD_ROOT/usr/lib/systemd/system

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%post
# cp /usr/bin/caRepeater.service /usr/lib/systemd/system
systemctl enable caRepeater
/sbin/ldconfig

%files
%dir %attr(-,root,root) /opt/epics
%dir %attr(-,root,root) /opt/epics/base
%dir %attr(-,root,root) /opt/epics/base/bin
%dir %attr(-,root,root) /opt/epics/base/bin/linux-x86_64
%dir %attr(-,root,root) /opt/epics/base/configure
%dir %attr(-,root,root) /opt/epics/base/configure/os
%dir %attr(-,root,root) /opt/epics/base/db
%dir %attr(-,root,root) /opt/epics/base/dbd
%dir %attr(-,root,root) /opt/epics/base/html
%dir %attr(-,root,root) /opt/epics/base/include
%dir %attr(-,root,root) /opt/epics/base/lib
%dir %attr(-,root,root) /opt/epics/base/lib/linux-x86_64
%dir %attr(-,root,root) /opt/epics/base/lib/perl
%dir %attr(-,root,root) /opt/epics/base/lib/pkgconfig
%dir %attr(-,root,root) /opt/epics/base/templates
%dir %attr(-,root,root) /opt/epics/base/startup

%attr(755,root,root)    /opt/epics/base/bin/linux-x86_64/*
%attr(-,root,root)      /opt/epics/base/configure/RELEASE
%attr(-,root,root)      /opt/epics/base/configure/CONFIG*
%attr(-,root,root)      /opt/epics/base/configure/RULES*
%attr(-,root,root)      /opt/epics/base/configure/os/*
%attr(-,root,root)      /opt/epics/base/db/*
%attr(-,root,root)      /opt/epics/base/dbd/*
%attr(-,root,root)      /opt/epics/base/html/*
%attr(-,root,root)      /opt/epics/base/include/*
%attr(-,root,root)      /opt/epics/base/lib/linux-x86_64/*.so.*
%attr(-,root,root)      /opt/epics/base/lib/linux-x86_64/libCap5.so
%attr(-,root,root)      /opt/epics/base/lib/linux-x86_64/*.a
%attr(-,root,root)      /opt/epics/base/lib/linux-x86_64/libca.so
%attr(-,root,root)      /opt/epics/base/lib/linux-x86_64/libcas.so
%attr(-,root,root)      /opt/epics/base/lib/linux-x86_64/libCom.so
%attr(-,root,root)      /opt/epics/base/lib/linux-x86_64/libdbCore.so
%attr(-,root,root)      /opt/epics/base/lib/linux-x86_64/libdbRecStd.so
%attr(-,root,root)      /opt/epics/base/lib/linux-x86_64/libgdd.so
%attr(-,root,root)      /opt/epics/base/lib/perl/*
%attr(-,root,root)      /opt/epics/base/lib/pkgconfig/*
%attr(-,root,root)      /opt/epics/base/templates/*
%attr(755,root,root)    /opt/epics/base/startup/*

/usr/lib64/libca.so.3.15.6
/usr/lib64/libcas.so.3.15.6
/usr/lib64/libCom.so.3.15.6
/usr/lib64/libdbCore.so.3.15.6
/usr/lib64/libdbRecStd.so.3.15.6
/usr/lib64/libgdd.so.3.15.6
/usr/lib64/libca.a
/usr/lib64/libcas.a
/usr/lib64/libCom.a
/usr/lib64/libdbCore.a
/usr/lib64/libdbRecStd.a
/usr/lib64/libgdd.a
/usr/lib64/libCap5.so
/usr/lib64/libca.so
/usr/lib64/libcas.so
/usr/lib64/libCom.so
/usr/lib64/libdbCore.so
/usr/lib64/libdbRecStd.so
/usr/lib64/libgdd.so

/usr/bin/acctst
/usr/bin/aitGen
/usr/bin/antelope
/usr/bin/ascheck
/usr/bin/caConnTest
/usr/bin/caDirServ
/usr/bin/caEventRate
/usr/bin/caget
/usr/bin/cainfo
/usr/bin/camonitor
/usr/bin/caput
/usr/bin/caRepeater
/usr/bin/casw
/usr/bin/ca_test
/usr/bin/catime
/usr/bin/e_flex
/usr/bin/excas
/usr/bin/genApps
/usr/bin/iocLogServer
/usr/bin/makeBpt
/usr/bin/msi
/usr/bin/S99caRepeater
/usr/bin/S99logServer
/usr/bin/softIoc
/usr/bin/caRepeater.service
/usr/bin/*.pl
/usr/lib/systemd/system/caRepeater.service

%changelog
* Thu May 09 2019 Abdalla Al-Dalleh 3.15.5-1
  - Removed perl scripts from /usr/local/bin
