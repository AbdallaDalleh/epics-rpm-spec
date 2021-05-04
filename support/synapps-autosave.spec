# 
# Autosave 5.10.2 EPICS support
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/autosave

# %define debug_package %{nil}
# %define __os_install_post %{nil}

Name:			synapps-autosave
Version:		5.10
Release:		2%{?dist}
Summary:		Autosave support for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		synapps-autosave-%{version}.2.tar.gz
BuildRequires:	epics-base
Requires:		epics-base

%description
Autosave support for EPICS

%prep
%setup -q -n synapps-autosave-%{version}.2

%build
# mkdir -p /opt/epics/support/autosave
# make INSTALL_LOCATION=/opt/epics/support/autosave %{_smp_mflags}

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
cp -a $RPM_BUILD_ROOT/%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}/
cp -a $RPM_BUILD_ROOT/%{epics_prefix}/bin/linux-x86_64/* $RPM_BUILD_ROOT/usr/bin

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

# mkdir -p $RPM_BUILD_ROOT/opt/epics/support/autosave
# mkdir -p $RPM_BUILD_ROOT/usr/local/lib64/
# mkdir -p $RPM_BUILD_ROOT/usr/local/bin/
# cp -a /opt/epics/support/autosave/* $RPM_BUILD_ROOT/opt/epics/support/autosave
# cp -a /opt/epics/support/autosave/lib/linux-x86_64/* $RPM_BUILD_ROOT/usr/local/lib64/
# cp -a /opt/epics/support/autosave/bin/linux-x86_64/* $RPM_BUILD_ROOT/usr/local/bin
# rm -rf /opt/epics/support/autosave

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

%attr(-,root,root) /opt/epics/support/autosave/bin/linux-x86_64/asApp
%attr(-,root,root) /opt/epics/support/autosave/bin/linux-x86_64/asVerify
%attr(-,root,root) /opt/epics/support/autosave/configure/RELEASE
%attr(-,root,root) /opt/epics/support/autosave/db/*
%attr(-,root,root) /opt/epics/support/autosave/dbd/*
# %attr(-,root,root) /opt/epics/support/autosave/iocsh/*
%attr(-,root,root) /opt/epics/support/autosave/include/os/Linux/osdNfs.h
%attr(-,root,root) /opt/epics/support/autosave/lib/linux-x86_64/libautosave.so*
%attr(-,root,root) /opt/epics/support/autosave/lib/linux-x86_64/libautosave.a

/usr/lib64/libautosave.so
/usr/lib64/libautosave.so.%{version}
/usr/lib64/libautosave.a
/usr/bin/asApp
/usr/bin/asVerify

%changelog
* Thu Nov 08 2018 Abdalla Al-Dalleh 5.9
  - Initial Release
