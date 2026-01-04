%global debug_package %{nil}

Name:		pylon
Version:	7.4
Release:	0%{?dist}
Summary:	Pylon SDK for Basler cameras
License:    GPL+
Source0:	pylon-7.4.0.tar.gz

BuildRequires:  qt5-qtbase qt5-qtbase-common qt5-qtbase-devel qt5-qtbase-doc qt5-qtbase-examples qt5-qtbase-gui qt5-qtbase-mysql qt5-qtbase-odbc qt5-qtbase-postgresql qt5-qtbase-private-devel qt5-qtbase-static qt5-qttools qt5-qttools-common qt5-qttools-devel qt5-qttools-doc qt5-qttools-examples qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qttools-libs-help qt5-qttools-static
Requires:       qt5-qtbase qt5-qtbase-common qt5-qtbase-devel qt5-qtbase-doc qt5-qtbase-examples qt5-qtbase-gui qt5-qtbase-mysql qt5-qtbase-odbc qt5-qtbase-postgresql qt5-qtbase-private-devel qt5-qtbase-static qt5-qttools qt5-qttools-common qt5-qttools-devel qt5-qttools-doc qt5-qttools-examples qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qttools-libs-help qt5-qttools-static
Provides:       libAppCoreComponents.so.2()(64bit) libFirmwareUpdate_gcc_v3_1_Basler_pylon.so()(64bit) libGCBase_gcc_v3_1_Basler_pylon.so()(64bit) libLoggingCore.so.2()(64bit) libPluginCore.so.2()(64bit) libPylonViewerComponents.so.7()(64bit) libPylonViewerHelper.so.7()(64bit) libUtils.so.2()(64bit) libgxapi.so.7.4()(64bit) liblog4cpp_gcc_v3_1_Basler_pylon.so()(64bit) libpylonbase.so.7.4()(64bit)


%description
Pylon SDK for Basler Cameras

%prep
%setup -q -n pylon-7.4.0

%build
# Nothing to build, it is a pre-built SDK.

%install
mkdir -p %{buildroot}%{_prefix}/pylon
cp -a *  %{buildroot}%{_prefix}/pylon

%files
%defattr(-,root,root)
%dir %{_prefix}/pylon/
%dir %{_prefix}/pylon/share
%dir %{_prefix}/pylon/include
%dir %{_prefix}/pylon/lib
%dir %{_prefix}/pylon/bin

%{_prefix}/pylon/share/*
%{_prefix}/pylon/include/*
%{_prefix}/pylon/lib/*
%{_prefix}/pylon/bin/*
%{_prefix}/pylon/INSTALL

%changelog

