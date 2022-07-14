# 
# caput Recorder for EPICS
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/caputRecorder

Name:			caputRecorder
Version:		%{_version}
Release:		%{build_number}%{?dist}
Summary:		caput Recorder support for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		%{name}-%{_version}.%{build_number}.tar.gz
BuildRequires:	epics-base
Requires:		epics-base

%description
CAput Recorder Support for EPICS

%prep
%setup -q -n %{name}-%{_version}.%{build_number}


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

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{epics_prefix}/op

mv %{buildroot}%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}
ln -sr %{buildroot}%{_libdir}/* %{buildroot}%{epics_prefix}/lib/linux-x86_64/
cp -a  %{_builddir}/%{?buildsubdir}/caputRecorderApp/op/* %{buildroot}%{epics_prefix}/op
rm -f  %{buildroot}%{epics_prefix}/op/Makefile

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /opt/epics/support/
%dir %{epics_prefix}
%dir %{epics_prefix}/configure
%dir %{epics_prefix}/db
%dir %{epics_prefix}/dbd
%dir %{epics_prefix}/op
%dir %{epics_prefix}/op/adl
%dir %{epics_prefix}/op/edl
%dir %{epics_prefix}/op/opi
%dir %{epics_prefix}/op/ui
%dir %{epics_prefix}/op/bob
%dir %{epics_prefix}/op/python
%dir %{epics_prefix}/lib
%dir %{epics_prefix}/lib/linux-x86_64

%{epics_prefix}/configure/RELEASE
%{epics_prefix}/db/*
%{epics_prefix}/dbd/caputRecorder.dbd
%{epics_prefix}/lib/linux-x86_64/*
%{epics_prefix}/op/adl/*
%{epics_prefix}/op/edl/*
%{epics_prefix}/op/opi/*
%{epics_prefix}/op/ui/*
%{epics_prefix}/op/bob/*
%{epics_prefix}/op/python/*

%{_libdir}/*

%changelog
* Sun May 05 2021 Abdalla Al-Dalleh 1.7-3
  - New build structure.
