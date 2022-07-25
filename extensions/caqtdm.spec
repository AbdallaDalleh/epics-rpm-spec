# 
# caQtDM: an MEDM replacement based on Qt framework.
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/extensions/caqtdm
%global _version 4.4.0

Name:			caqtdm
Version:		4.4
Release:		0%{?dist}
Summary:		Qt-Based Replacement for MEDM.
Group:			Applications/Engineering
License:		GPL+
URL:			https://github.com/caqtdm/caqtdm/archive/V4.2.4.tar.gz
Source0:		%{name}-%{_version}.tar.gz
BuildRequires:	epics-base, qwt, qt5-qtbase, qt5-qtbase-gui, qt5-qtsvg
Requires:		epics-base, qwt, qt5-qtbase, qt5-qtbase-gui, qt5-qtsvg
Provides:	libadlParser.so()(64bit) libedlParser.so()(64bit)

%description
caQtDM is an MEDM replacement based on Qt

%prep
%setup -q -n %{name}-%{_version}

%build
QTDM_PATH=%{buildroot} ./caQtDM_BuildAll

%install
install -d %{buildroot}%{epics_prefix}/controlsystems
install -d %{buildroot}%{epics_prefix}/designer
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}

export EPICSEXTENSIONS=%{buildroot}%{epics_prefix}
QTDM_PATH=%{buildroot} ./caQtDM_Install

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
%{epics_prefix}/libcaQtDM_Lib.so
%{epics_prefix}/libqtcontrols.so

%{_bindir}/*
%{_libdir}/*

%changelog
* Thu May 20 2021 Abdalla Al-Dalleh 4.2-4
	- Initial RPM release.

