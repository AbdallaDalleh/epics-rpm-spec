# 
# Siemens S7 PLCs libnodave-based driver for EPICS
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/s7nodave
%global _version 3.0.2

Name:			s7nodave
Version:		3.0
Release:		2%{?dist}
Summary:		Siemens S7 PLCs libnodave-based driver for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://oss.aquenos.com/epics/s7nodave/download/s7nodave-3.0.2.tar.gz
Source0:		%{name}-%{_version}.tar.gz
BuildRequires:	epics-base asyn
Requires:		epics-base asyn

%description
Siemens S7 PLCs libnodave-based driver for EPICS

%prep
%setup -q -n %{name}-%{_version}

%build


%install
shopt -s extglob

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
%dir %{epics_prefix}/configure
%dir %{epics_prefix}/include
%dir %{epics_prefix}/dbd
%dir %{epics_prefix}/lib
%dir %{epics_prefix}/lib/linux-x86_64

%{epics_prefix}/configure/*
%{epics_prefix}/include/*
%{epics_prefix}/dbd/*
%{epics_prefix}/lib/linux-x86_64/*

%{_libdir}/*

%changelog
* Sun Dec 26 2021 Abdalla Al-Dalleh 3.0.2
  - Initial RPM spec.
