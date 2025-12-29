# 
# Extensible Display Manager
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/extensions/edm
%global _version 1.12.105
%define debug_package %{nil}

Name:			edm
Version:		1.12
Release:		105%{?dist}
Summary:		Extensible Display Manager for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		%{name}-%{_version}.tar.gz
BuildRequires:	expat fontconfig freetype glibc libgcc libICE libjpeg libSM libstdc++ libuuid libX11 libXau libxcb libXext libXft libXi libXmu libXp libXrender libXt libXtst motif ncurses readline zlib fontconfig-devel freetype-devel glibc-devel libICE-devel libjpeg-devel libSM-devel libstdc++-devel libuuid-devel libXau-devel libxcb-devel libXext-devel libXft-devel libXi-devel libXmu-devel libXp-devel libXrender-devel libXt-devel libXtst-devel motif-devel ncurses-devel readline-devel expat-devel epics-base
Requires:		expat fontconfig freetype glibc libgcc libICE libjpeg libSM libstdc++ libuuid libX11 libXau libxcb libXext libXft libXi libXmu libXp libXrender libXt libXtst motif ncurses readline zlib fontconfig-devel freetype-devel glibc-devel libICE-devel libjpeg-devel libSM-devel libstdc++-devel libuuid-devel libXau-devel libxcb-devel libXext-devel libXft-devel libXi-devel libXmu-devel libXp-devel libXrender-devel libXt-devel libXtst-devel motif-devel ncurses-devel readline-devel expat-devel epics-base

%description
Extensible Display Manager for EPICS

%prep
%setup -q -n %{name}-%{_version}

%build


%install
export EPICS_HOST_ARCH=linux-x86_64

make -C "%{_builddir}/%{?buildsubdir}" \
LINKER_USE_RPATH=NO \
INSTALL_LOCATION="%{buildroot}%{epics_prefix}" \
BIN_PERMISSIONS=755 \
LIB_PERMISSIONS=644 \
SHRLIB_PERMISSIONS=755

install -d %{buildroot}%{_bindir}
mv %{buildroot}%{epics_prefix}/include/edm/* %{buildroot}%{epics_prefix}/include
mv %{buildroot}%{epics_prefix}/bin/linux-x86_64/edm %{buildroot}%{_bindir}
ln -sr %{buildroot}%{_bindir}/edm %{buildroot}%{epics_prefix}/bin/linux-x86_64

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /opt/epics/extensions
%dir %{epics_prefix}
%dir %{epics_prefix}/bin
%dir %{epics_prefix}/bin/linux-x86_64
%dir %{epics_prefix}/lib
%dir %{epics_prefix}/lib/linux-x86_64
%dir %{epics_prefix}/include/
%dir %{epics_prefix}/include/os
%dir %{epics_prefix}/include/os/Linux

%{epics_prefix}/bin/linux-x86_64/edm
%{epics_prefix}/lib/linux-x86_64/*
%{epics_prefix}/include/*.h
%{epics_prefix}/include/os/Linux/*.h

%{_bindir}/edm

%changelog
* Thu Jun 20 2019 Abdalla Al-Dalleh 1.12-103
  - Added missing folder.
* Tue May 14 2019 Abdalla Al-Dalleh 1.12-103
  - Initial Release.

