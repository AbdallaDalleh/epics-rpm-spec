# 
# Autosave EPICS support
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/ipac

Name:			ipac
Version:		%{_version}
Release:		%{build_number}%{?dist}
Summary:		IPAC support for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		%{name}-%{_version}.%{build_number}.tar.gz
BuildRequires:	epics-base
Requires:		epics-base

%description
IPAC support for EPICS

%prep
%setup -q -n %{name}-%{_version}.%{build_number}

%build


%install
export EPICS_HOST_ARCH=linux-x86_64
export EPICS_BASE=/opt/epics/base
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
mv $RPM_BUILD_ROOT/%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}/
ln -sr %{buildroot}%{_libdir}/* $RPM_BUILD_ROOT/%{epics_prefix}/lib/linux-x86_64/

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /opt/epics/support
%dir /opt/epics/support/ipac
%dir /opt/epics/support/ipac/configure
%dir /opt/epics/support/ipac/dbd
%dir /opt/epics/support/ipac/lib/
%dir /opt/epics/support/ipac/lib/linux-x86_64/
%dir /opt/epics/support/ipac/include/
%dir /opt/epics/support/ipac/html

/opt/epics/support/ipac/configure/*
/opt/epics/support/ipac/dbd/*
/opt/epics/support/ipac/html/*
/opt/epics/support/ipac/include/*
/opt/epics/support/ipac/lib/linux-x86_64/*

%{_libdir}/*

%changelog
* Sun May 09 2021 Abdalla Al-Dalleh 2.16
  - Simplified files listing.
* Wed May 05 2021 Abdalla Al-Dalleh 2.16
  - New build sequence
