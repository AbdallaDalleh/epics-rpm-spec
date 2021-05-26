# 
# Area detector simulation drivers for EPICS
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/areaDetector/simulation
%global _version 2.10

Name:			area-detector-simulation
Version:		2.10
Release:		0%{?dist}
Summary:		Area Detector Simulation drivers for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		%{name}-%{_version}.tar.gz
BuildRequires:	epics-base area-detector-core
Requires:		epics-base area-detector-core

%description
Area Detector Simulation drivers for EPICS

%prep
%setup -q -n %{name}-%{_version}

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
cp -a  %{_builddir}/%{?buildsubdir}/simDetectorApp/op/!(Makefile) %{buildroot}%{epics_prefix}/op

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
%dir %{epics_prefix}/include
%dir %{epics_prefix}/lib/
%dir %{epics_prefix}/lib/linux-x86_64/
%dir %{epics_prefix}/op/
%dir %{epics_prefix}/op/adl
%dir %{epics_prefix}/op/edl
%dir %{epics_prefix}/op/opi
%dir %{epics_prefix}/op/ui

%{epics_prefix}/configure/RELEASE
%{epics_prefix}/op/adl/*
%{epics_prefix}/op/edl/*
%{epics_prefix}/op/opi/*
%{epics_prefix}/op/ui/*
%{epics_prefix}/db/*
%{epics_prefix}/dbd/*
%{epics_prefix}/include/*
%{epics_prefix}/lib/linux-x86_64/*

%{_libdir}/*

%changelog
* Thu May 20 2021 Abdalla Al-Dalleh 2.10-0
  - Initial Release
