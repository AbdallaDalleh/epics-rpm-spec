# 
# Autosave EPICS support
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/autosave
%global _version 5.10.2

Name:			autosave
Version:		5.10
Release:		2%{?dist}
Summary:		Autosave support for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		autosave-%{_version}.tar.gz
BuildRequires:	epics-base
Requires:		epics-base

%description
Autosave support for EPICS

%prep
%setup -q -n autosave-%{_version}

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
install -d %{buildroot}%{_bindir}
mv %{buildroot}%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}
mv %{buildroot}%{epics_prefix}/bin/linux-x86_64/* %{buildroot}%{_bindir}

ln -sr %{buildroot}%{_libdir}/* %{buildroot}%{epics_prefix}/lib/linux-x86_64
ln -sr %{buildroot}%{_bindir}/* %{buildroot}%{epics_prefix}/bin/linux-x86_64

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%dir %attr(-,root,root) /opt/epics/support/
%dir %attr(-,root,root) /opt/epics/support/autosave
%dir %attr(-,root,root) /opt/epics/support/autosave/bin
%dir %attr(-,root,root) /opt/epics/support/autosave/bin/linux-x86_64
%dir %attr(-,root,root) /opt/epics/support/autosave/configure
%dir %attr(-,root,root) /opt/epics/support/autosave/db
%dir %attr(-,root,root) /opt/epics/support/autosave/dbd
%dir %attr(-,root,root) /opt/epics/support/autosave/lib
%dir %attr(-,root,root) /opt/epics/support/autosave/lib/linux-x86_64
%dir %attr(-,root,root) /opt/epics/support/autosave/include
%dir %attr(-,root,root) /opt/epics/support/autosave/include/os
%dir %attr(-,root,root) /opt/epics/support/autosave/include/os/Linux

%attr(-,root,root) /opt/epics/support/autosave/bin/linux-x86_64/*
%attr(-,root,root) /opt/epics/support/autosave/configure/*
%attr(-,root,root) /opt/epics/support/autosave/db/*
%attr(-,root,root) /opt/epics/support/autosave/dbd/*
%attr(-,root,root) /opt/epics/support/autosave/include/*
%attr(-,root,root) /opt/epics/support/autosave/lib/linux-x86_64/*

%{_libdir}/*
%{_bindir}/*

%changelog
* Sun May 09 2021 Abdalla Al-Dalleh 5.10.2
  - New build sequence.
