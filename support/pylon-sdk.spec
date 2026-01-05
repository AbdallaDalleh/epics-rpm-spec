
%define debug_package %{nil}

Name:		pylon-sdk
Version:	7.2
Release:	1%{?dist}
Summary:	Pylon SDK for Basler cameras
License:	GPL+
Source0:    pylon-sdk-7.2.1.tar.gz

# BuildRequires: qt5-qtbase qt5-qtbase-common qt5-qtbase-devel qt5-qtbase-doc qt5-qtbase-examples qt5-qtbase-gui qt5-qtbase-mysql qt5-qtbase-odbc qt5-qtbase-postgresql qt5-qtbase-private-devel qt5-qtbase-static qt5-qttools qt5-qttools-common qt5-qttools-devel qt5-qttools-doc qt5-qttools-examples qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qttools-libs-help qt5-qttools-static
# Requires: qt5-qtbase qt5-qtbase-common qt5-qtbase-devel qt5-qtbase-doc qt5-qtbase-examples qt5-qtbase-gui qt5-qtbase-mysql qt5-qtbase-odbc qt5-qtbase-postgresql qt5-qtbase-private-devel qt5-qtbase-static qt5-qttools qt5-qttools-common qt5-qttools-devel qt5-qttools-doc qt5-qttools-examples qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qttools-libs-help qt5-qttools-static

Provides:   libAppCoreComponents.so.1()(64bit) libCameraPoolComponents.so.1()(64bit) libFactoryCore.so.1()(64bit) libhaprt.so()(64bit) libLoggingCore.so.1()(64bit) libParameterCollection.so.1()(64bit) libPluginCore.so.1()(64bit) libPylonDataProcessingCore.so.1()(64bit) libPylonDataProcessingGui.so.1()(64bit) libPylonDataProcessing.so.1()(64bit) libPylonViewerComponents.so.7()(64bit) libPylonViewerHelper.so.7()(64bit) libQtitanDocking.so.1()(64bit) libServiceCore.so.1()(64bit) libsiso_auxport.so()(64bit) libsiso_hw.so()(64bit) libsisoiolibrt.so()(64bit) libUtils.so.1()(64bit)

%description
Pylon SDK for Basler Cameras

%prep
%setup -q -n pylon-sdk-7.2.1

%build
# Nothing to build, it is a pre-built SDK.

%install
mkdir -p %{buildroot}%{_prefix}/pylon
cp -a *  %{buildroot}%{_prefix}/pylon

%files
%defattr(-,root,root)
%dir %{_prefix}/pylon
%{_prefix}/pylon/*

%changelog

