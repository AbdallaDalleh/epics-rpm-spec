# 
# Area detector drivers for pylon Cameras
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global debug_package %{nil}
%global epics_prefix /opt/epics/support/areaDetector/pylon

Name:		area-detector-pylon
Version:	%{_version}
Release:	%{build_number}%{?dist}
Summary:	pylon Cameras drivers for EPICS
Group:		Applications/Engineering
License:	GPL+
URL:		https://epics.anl.gov
Source0:	%{name}-%{_version}.%{build_number}.tar.gz
AutoReq:	0
BuildRequires:	epics-base area-detector-genicam
Requires:		epics-base area-detector-genicam
Epoch: 2

%description
pylon Cameras Drivers for EPICS

%prep
%setup -q -n %{name}-%{_version}.%{build_number}

%build


%install
shopt -s extglob

export EPICS_HOST_ARCH=linux-x86_64
export LD_LIBRARY_PATH=%{buildroot}%{epics_prefix}/lib/${EPICS_HOST_ARCH}

make -C "%{_builddir}/%{?buildsubdir}" %{?_smp_mflags} \
LINKER_USE_RPATH=NO \
INSTALL_LOCATION="%{buildroot}%{epics_prefix}" \
FINAL_LOCATION=%{epics_prefix} \
BIN_PERMISSIONS=755 \
LIB_PERMISSIONS=644 \
SHRLIB_PERMISSIONS=755

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{epics_prefix}/op

mv %{buildroot}%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}
ln -sr %{buildroot}%{_libdir}/* %{buildroot}%{epics_prefix}/lib/linux-x86_64/
cp -a  %{_builddir}/%{?buildsubdir}/pylonApp/op/!(Makefile) %{buildroot}%{epics_prefix}/op
cp -a  %{_builddir}/%{?buildsubdir}/pylonApp/Db/*.req %{buildroot}%{epics_prefix}/db

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /opt/epics/support/
%dir /opt/epics/support/areaDetector
%dir %{epics_prefix}
%dir %{epics_prefix}/configure
%dir %{epics_prefix}/db
%dir %{epics_prefix}/dbd
%dir %{epics_prefix}/lib/
%dir %{epics_prefix}/lib/linux-x86_64/
%dir %{epics_prefix}/op/
%dir %{epics_prefix}/op/adl

%{epics_prefix}/configure/RELEASE
%{epics_prefix}/op/adl/*
%{epics_prefix}/db/*
%{epics_prefix}/dbd/*
%{epics_prefix}/lib/linux-x86_64/*

%{_libdir}/*

%changelog
* Sun Sep 17 2023 Abdalla 0.0-1:1
  - Epoch=2: Added pylon SDK 7.3
* Mon Aug 07 2023 Abdalla Al-Dalleh 0.0-1
  - Initial Release
