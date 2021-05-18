# 
# Stream device driver support for EPICS
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/stream
%global _version 2.8.19

Name:			stream-device
Version:		2.8
Release:		19%{?dist}
Summary:		Stream device driver support for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		%{name}-%{_version}.tar.gz
BuildRequires:	epics-base seq sscan calc asyn
Requires:		epics-base seq sscan calc asyn

%description
Stream device driver support for EPICS

%prep
%setup -q -n %{name}-%{_version}

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

mv %{buildroot}%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}
ln -sr %{buildroot}%{_libdir}/* %{buildroot}%{epics_prefix}/lib/linux-x86_64/

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /opt/epics/support/
%dir %{epics_prefix}
%dir %{epics_prefix}/bin
%dir %{epics_prefix}/bin/linux-x86_64
%dir %{epics_prefix}/configure
%dir %{epics_prefix}/dbd
%dir %{epics_prefix}/lib
%dir %{epics_prefix}/lib/linux-x86_64
%dir %{epics_prefix}/include

%{epics_prefix}/bin/linux-x86_64/*
%{epics_prefix}/configure/*
%{epics_prefix}/dbd/*
%{epics_prefix}/include/*
%{epics_prefix}/lib/linux-x86_64/*

%{_libdir}/*

%changelog
* Sun May 16 2021 Abdalla Al-Dalleh 2.8.19
  - New build sequence.
