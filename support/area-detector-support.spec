# 
# Area detector support libraries for EPICS
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/areaDetector/support

Name:			area-detector-support
Version:		%{_version}
Release:		%{build_number}%{?dist}
Summary:		Area detector support libraries for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		%{name}-%{_version}.%{build_number}.tar.gz
BuildRequires:	epics-base
Requires:		epics-base

%description
Area detector support libraries for EPICS

%prep
%setup -q -n %{name}-%{_version}.%{build_number}

%build


%install
export EPICS_HOST_ARCH=linux-x86_64
export LD_LIBRARY_PATH=%{buildroot}%{epics_prefix}/lib/${EPICS_HOST_ARCH}

make -C "%{_builddir}/%{?buildsubdir}" %{?_smp_mflags} \
LINKER_USE_RPATH=NO \
INSTALL_LOCATION="%{buildroot}%{epics_prefix}" \
FINAL_LOCATION=%{epics_prefix} \
BIN_PERMISSIONS=755 \
LIB_PERMISSIONS=644 \
SHRLIB_PERMISSIONS=755

# install -d %{buildroot}%{_libdir}
# install -d %{buildroot}%{_bindir}
# 
# mv %{buildroot}%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}
# mv %{buildroot}%{epics_prefix}/bin/linux-x86_64/* %{buildroot}%{_bindir}
# ln -sr %{buildroot}%{_libdir}/* %{buildroot}%{epics_prefix}/lib/linux-x86_64/
# ln -sr %{buildroot}%{_bindir}/* %{buildroot}%{epics_prefix}/bin/linux-x86_64/

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
%dir %{epics_prefix}/include
%dir %{epics_prefix}/lib
%dir %{epics_prefix}/lib/linux-x86_64

%{epics_prefix}/bin/linux-x86_64/*
%{epics_prefix}/configure/*
%{epics_prefix}/include/*
%{epics_prefix}/lib/linux-x86_64/*

# %{_libdir}/*
# %{_bindir}/*

%changelog
* Tue May 18 2021 Abdalla Al-Dalleh 1.9.1
  - New build sequence.
