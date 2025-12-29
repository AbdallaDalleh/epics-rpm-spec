# 
# caQtDM: an MEDM replacement based on Qt framework.
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/extensions/caqtdm

Name:			caqtdm
Version:		%{_version}
Release:		%{build_number}%{?dist}
Summary:		Qt-Based Replacement for MEDM.
Group:			Applications/Engineering
License:		GPL+
URL:			https://github.com/caqtdm/caqtdm/archive/V4.2.4.tar.gz
Source0:		%{name}-%{_version}.%{build_number}.tar.gz
BuildRequires:	epics-base, qwt, qt5-qtbase, qt5-qtbase-gui, qt5-qtsvg
Requires:		epics-base, qwt, qt5-qtbase, qt5-qtbase-gui, qt5-qtsvg
Provides:       libadlParser.so()(64bit) libedlParser.so()(64bit)

%description
caQtDM is an MEDM replacement based on Qt

%prep
%setup -q -n %{name}-%{_version}.%{build_number}

%build
export QWTVERSION=6.3.0
export QWTHOME=/usr/local/qwt-${QWTVERSION}
export QWTINCLUDE=${QWTHOME}/include
export QWTLIB=${QWTHOME}/lib
export QWTLIBNAME=qwt
export EPCIS_BASE=/opt/epics/base
export EPICSEXTENSIONS=%{buildroot}%{epics_prefix}
export QTDM_LIBINSTALL=%{buildroot}%{epics_prefix}/lib
export QTDM_BININSTALL=%{buildroot}%{epics_prefix}/bin
export PYTHONVERSION=3.9
QTDM_PATH=%{buildroot} yes | ./caQtDM_BuildAll

%install
install -d %{buildroot}%{epics_prefix}/controlsystems
install -d %{buildroot}%{epics_prefix}/designer
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}

export QWTHOME=/usr/local/qwt-6.3.0
export QWTINCLUDE=${QWTHOME}/include
export QWTLIB=${QWTHOME}/lib
export QWTLIBNAME=qwt
export QWTVERSION=6.3.0
export EPCIS_BASE=/opt/epics/base
export EPICSEXTENSIONS=%{buildroot}%{epics_prefix}
export QTDM_LIBINSTALL=%{buildroot}%{epics_prefix}
export QTDM_BININSTALL=%{buildroot}%{epics_prefix}
export PYTHONVERSION=3.9
QTDM_PATH=%{buildroot} yes | ./caQtDM_Install

for bin in caQtDM adl2ui edl2ui; do
	mv     %{buildroot}%{epics_prefix}/$bin %{buildroot}%{_bindir}
	ln -sr %{buildroot}%{_bindir}/$bin %{buildroot}%{epics_prefix}
done

for lib in libarchiveSF_plugin.so libdemo_plugin.so libepics3_plugin.so; do
	mv     %{buildroot}%{epics_prefix}/controlsystems/$lib %{buildroot}%{_libdir}
	ln -sr %{buildroot}%{_libdir}/$lib %{buildroot}%{epics_prefix}/controlsystems
done

for lib in libqtcontrols_controllers_plugin.so libqtcontrols_graphics_plugin.so libqtcontrols_monitors_plugin.so libqtcontrols_utilities_plugin.so; do
	mv     %{buildroot}%{epics_prefix}/designer/$lib %{buildroot}%{_libdir}
	ln -sr %{buildroot}%{_libdir}/$lib %{buildroot}%{epics_prefix}/designer
done

for lib in libcaQtDM_Lib.so libqtcontrols.so; do
	mv     %{buildroot}%{epics_prefix}/$lib %{buildroot}%{_libdir}
	ln -sr %{buildroot}%{_libdir}/$lib %{buildroot}%{epics_prefix}
done

pwd
find . -type f -name libadlParser.so

cp ./caQtDM_Binaries/libadlParser.so %{buildroot}%{epics_prefix}
cp ./caQtDM_Binaries/libedlParser.so %{buildroot}%{epics_prefix}
cp ./caQtDM_Binaries/libadlParser.a  %{buildroot}%{epics_prefix}
cp ./caQtDM_Binaries/libedlParser.a  %{buildroot}%{epics_prefix}

export QA_SKIP_BUILD_ROOT=1

%files
%defattr(-,root,root)
%dir /opt/epics/extensions
%dir %{epics_prefix}
%dir %{epics_prefix}/designer
%dir %{epics_prefix}/controlsystems

%{epics_prefix}/adl2ui
%{epics_prefix}/edl2ui
%{epics_prefix}/caQtDM
%{epics_prefix}/startDM
%{epics_prefix}/controlsystems/*
%{epics_prefix}/designer/*
%{epics_prefix}/*.so
%{epics_prefix}/*.a

%{_bindir}/*
%{_libdir}/*

%changelog
* Mon Sep 12 2022 Abdalla Al-Dalleh 4.2-4
	- Added v4.2.4.
* Thu May 20 2021 Abdalla Al-Dalleh 4.2-4
	- Initial RPM release.

