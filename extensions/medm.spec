# 
# Motif Extensible Display Manager
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/extensions/medm
%global _version 3.1.20

Name:			medm
Version:		3.1
Release:		20%{?dist}
Summary:		Motif Extensible Display Manager for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		%{name}-%{_version}.tar.gz
BuildRequires:	epics-base expat fontconfig freetype glibc libgcc libICE libjpeg-turbo libpng libSM libstdc++ libuuid libX11 libXau libxcb libXext libXft libXmu libXp libXrender libXt motif ncurses-libs readline zlib
Requires:		epics-base expat fontconfig freetype glibc libgcc libICE libjpeg-turbo libpng libSM libstdc++ libuuid libX11 libXau libxcb libXext libXft libXmu libXp libXrender libXt motif ncurses-libs readline zlib

%description
Motif Extensible Display Manager for EPICS

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
mv %{buildroot}%{epics_prefix}/bin/linux-x86_64/medm %{buildroot}%{_bindir}
ln -sr %{buildroot}%{_bindir}/medm %{buildroot}%{epics_prefix}/bin/linux-x86_64

%files
%dir /opt/epics/extensions
%dir /opt/epics/extensions/medm
%dir /opt/epics/extensions/medm/bin
%dir /opt/epics/extensions/medm/bin/linux-x86_64
%dir /opt/epics/extensions/medm/lib
%dir /opt/epics/extensions/medm/lib/linux-x86_64

/opt/epics/extensions/medm/bin/linux-x86_64/medm
/opt/epics/extensions/medm/lib/linux-x86_64/*

%{_bindir}/medm

%changelog
* Thu May 20 2021 Abdalla Al-Dalleh 3.1-9
  - Initial Release.

