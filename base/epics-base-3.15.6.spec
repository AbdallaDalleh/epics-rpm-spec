# 
# EPICS Base 3.15.6 RPM SPEC file
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/base

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
%autosetup

%build
# There is no build section, EPICS build system is not a standard autoconf build.

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
install -d %{buildroot}%{_sysconfdir}/systemd/system
install -d %{buildroot}%{_bindir}
mv %{buildroot}/opt/epics/base/lib/linux-x86_64/* %{buildroot}%{_libdir}/
# mv %{buildroot}/opt/epics/base/bin/linux-x86_64/* %{buildroot}%{_bindir}/

ln -sr %{buildroot}%{_libdir}/* %{buildroot}/opt/epics/base/lib/linux-x86_64/
# ln -sr %{buildroot}%{_bindir}/* %{buildroot}/opt/epics/base/bin/linux-x86_64/
ln -sr %{buildroot}/opt/epics/base/bin/linux-x86_64/ca!(*.pl) %{buildroot}%{_bindir}

sed -i 's|%{buildroot}||g' %{buildroot}%{_bindir}/caRepeater.service
cp %{buildroot}%{_bindir}/caRepeater.service %{buildroot}%{_sysconfdir}/systemd/system
chmod 664 %{buildroot}%{_sysconfdir}/systemd/system/caRepeater.service

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%post
systemctl daemon-reload
systemctl enable caRepeater.service
/sbin/ldconfig

%preun
systemctl disable caRepeater.service
systemctl daemon-reload
/sbin/ldconfig

%files
%defattr(-,root,root)
%dir /opt/epics
%dir /opt/epics/base
%dir /opt/epics/base/bin
%dir /opt/epics/base/bin/linux-x86_64
%dir /opt/epics/base/configure
%dir /opt/epics/base/db
%dir /opt/epics/base/dbd
%dir /opt/epics/base/html
%dir /opt/epics/base/include
%dir /opt/epics/base/lib
%dir /opt/epics/base/lib/linux-x86_64
%dir /opt/epics/base/lib/perl
%dir /opt/epics/base/lib/pkgconfig
%dir /opt/epics/base/templates
%dir /opt/epics/base/startup

/opt/epics/base/bin/linux-x86_64/*
/opt/epics/base/configure/*
/opt/epics/base/db/*
/opt/epics/base/dbd/*
/opt/epics/base/html/*
/opt/epics/base/include/*
/opt/epics/base/lib/linux-x86_64/*
/opt/epics/base/lib/perl/*
/opt/epics/base/lib/pkgconfig/*
/opt/epics/base/templates/*
/opt/epics/base/startup/*

%{_libdir}/*
%{_bindir}/*
%{_sysconfdir}/systemd/system/caRepeater.service

%changelog
* Sun May 09 2021 Abdalla Al-Dalleh 3.15.5-0
  - Simplified files listings, fixed caRepeater.service location
