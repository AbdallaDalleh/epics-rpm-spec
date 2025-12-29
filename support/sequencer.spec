# 
# Sequencers EPICS support
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%define debug_package %{nil}
%global epics_prefix /opt/epics/support/seq

Name:			sequencer
Version:		%{_version}
Release:		%{build_number}%{?dist}
Summary:		SNL Sequencers support for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		%{name}-%{_version}.%{build_number}.tar.gz
BuildRequires:	epics-base
Requires:		epics-base

%description
State notation language sequencers support for EPICS

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
install -d %{buildroot}%{_bindir}
mv %{buildroot}/%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}/
mv %{buildroot}/%{epics_prefix}/bin/linux-x86_64/* %{buildroot}%{_bindir}/
ln -sr %{buildroot}%{_libdir}/* %{buildroot}%{epics_prefix}/lib/linux-x86_64/
ln -sr %{buildroot}%{_bindir}/* %{buildroot}%{epics_prefix}/bin/linux-x86_64/
ln -sr %{buildroot}%{epics_prefix}/cfg/* %{buildroot}%{epics_prefix}/configure

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /opt/epics/support/
%dir /opt/epics/support/seq
%dir /opt/epics/support/seq/cfg
%dir /opt/epics/support/seq/bin
%dir /opt/epics/support/seq/bin/linux-x86_64
%dir /opt/epics/support/seq/configure
%dir /opt/epics/support/seq/db
%dir /opt/epics/support/seq/dbd
%dir /opt/epics/support/seq/lib
%dir /opt/epics/support/seq/lib/linux-x86_64
%dir /opt/epics/support/seq/html
%dir /opt/epics/support/seq/include

/opt/epics/support/seq/cfg/*
/opt/epics/support/seq/bin/*
/opt/epics/support/seq/configure/*
/opt/epics/support/seq/db/*
/opt/epics/support/seq/dbd/*
/opt/epics/support/seq/html/*
/opt/epics/support/seq/include/*
/opt/epics/support/seq/lib/linux-x86_64/*

%{_libdir}/*
%{_bindir}/*

%changelog
* Wed May 05 2021 Abdalla Al-Dalleh 2.2.8
  - Used relative symbolic links to all binaries.
* Tue May 04 2021 Abdalla Al-Dalleh 2.2.8
  - New build sequence.

