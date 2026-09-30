
%define _prefix /usr
# %define debug_package %{nil}

Name:		pylon-sdk
Version:	26.8
Release:	0.%{?dist}
Summary:	Pylon SDK for Basler cameras
License:	GPL+
Source0:    %{name}-%{version}.%{build_number}.tar.gz

# BuildRequires: qt5-qtbase qt5-qtbase-common qt5-qtbase-devel qt5-qtbase-doc qt5-qtbase-examples qt5-qtbase-gui qt5-qtbase-mysql qt5-qtbase-odbc qt5-qtbase-postgresql qt5-qtbase-private-devel qt5-qtbase-static qt5-qttools qt5-qttools-common qt5-qttools-devel qt5-qttools-doc qt5-qttools-examples qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qttools-libs-help qt5-qttools-static
# Requires: qt5-qtbase qt5-qtbase-common qt5-qtbase-devel qt5-qtbase-doc qt5-qtbase-examples qt5-qtbase-gui qt5-qtbase-mysql qt5-qtbase-odbc qt5-qtbase-postgresql qt5-qtbase-private-devel qt5-qtbase-static qt5-qttools qt5-qttools-common qt5-qttools-devel qt5-qttools-doc qt5-qttools-examples qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qttools-libs-help qt5-qttools-static

Provides:   libAppCoreComponents.so.12()(64bit) libAppCoreInterfaces.so.12()(64bit) libCommonComponents.so.12()(64bit) libFirmwareUpdate_gcc_v3_5_Basler_pylon_v1.so()(64bit) libGCBase_gcc_v3_5_Basler_pylon_v1.so()(64bit) libGenApi_gcc_v3_5_Basler_pylon_v1.so()(64bit) libImageHelper.so.15()(64bit) libLoggingCore.so.12()(64bit) libParameterCollection.so.12()(64bit) libPluginCore.so.12()(64bit) libPylonDataProcessing.so.5()(64bit) libPylonDataProcessingCore.so.7()(64bit) libPylonDataProcessingGui.so.7()(64bit) libPylonViewerComponents.so.15()(64bit) libPylonViewerDataTypes.so.12()(64bit) libPylonViewerHelper.so.15()(64bit) libPylonViewerVToolsHelper.so.12()(64bit) libQt6Concurrent.so.6()(64bit) libQt6Core.so.6()(64bit) libQt6Core.so.6(Qt_6)(64bit) libQt6Core.so.6(Qt_6.5)(64bit) libQt6Core5Compat.so.6()(64bit) libQt6Core5Compat.so.6(Qt_6)(64bit) libQt6Designer.so.6()(64bit) libQt6DesignerComponents.so.6()(64bit) libQt6EglFSDeviceIntegration.so.6()(64bit) libQt6Gui.so.6()(64bit) libQt6Gui.so.6(Qt_6)(64bit) libQt6Help.so.6()(64bit) libQt6JsonRpc.so.6()(64bit) libQt6LabsAnimation.so.6()(64bit) libQt6LabsFolderListModel.so.6()(64bit) libQt6LabsQmlModels.so.6()(64bit) libQt6LabsSettings.so.6()(64bit) libQt6LabsSharedImage.so.6()(64bit) libQt6LabsWavefrontMesh.so.6()(64bit) libQt6LanguageServer.so.6()(64bit) libQt6Multimedia.so.6()(64bit) libQt6MultimediaQuick.so.6()(64bit) libQt6MultimediaWidgets.so.6()(64bit) libQt6Network.so.6()(64bit) libQt6Network.so.6(Qt_6)(64bit) libQt6NetworkAuth.so.6()(64bit) libQt6OpenGL.so.6()(64bit) libQt6OpenGLWidgets.so.6()(64bit) libQt6PrintSupport.so.6()(64bit) libQt6Qml.so.6()(64bit) libQt6Qml.so.6(Qt_6)(64bit) libQt6QmlCompiler.so.6()(64bit) libQt6QmlCore.so.6()(64bit) libQt6QmlLocalStorage.so.6()(64bit) libQt6QmlModels.so.6()(64bit) libQt6QmlWorkerScript.so.6()(64bit) libQt6QmlXmlListModel.so.6()(64bit) libQt6Quick.so.6()(64bit) libQt6Quick.so.6(Qt_6)(64bit) libQt6QuickControls2.so.6()(64bit) libQt6QuickControls2.so.6(Qt_6)(64bit) libQt6QuickControls2Impl.so.6()(64bit) libQt6QuickDialogs2.so.6()(64bit) libQt6QuickDialogs2QuickImpl.so.6()(64bit) libQt6QuickDialogs2Utils.so.6()(64bit) libQt6QuickEffects.so.6()(64bit) libQt6QuickLayouts.so.6()(64bit) libQt6QuickParticles.so.6()(64bit) libQt6QuickShapes.so.6()(64bit) libQt6QuickTemplates2.so.6()(64bit) libQt6QuickTest.so.6()(64bit) libQt6QuickWidgets.so.6()(64bit) libQt6Scxml.so.6()(64bit) libQt6ScxmlQml.so.6()(64bit) libQt6ShaderTools.so.6()(64bit) libQt6SpatialAudio.so.6()(64bit) libQt6Sql.so.6()(64bit) libQt6StateMachine.so.6()(64bit) libQt6StateMachineQml.so.6()(64bit) libQt6Svg.so.6()(64bit) libQt6SvgWidgets.so.6()(64bit) libQt6Test.so.6()(64bit) libQt6UiTools.so.6()(64bit) libQt6WaylandClient.so.6()(64bit) libQt6WaylandCompositor.so.6()(64bit) libQt6WaylandEglClientHwIntegration.so.6()(64bit) libQt6WaylandEglCompositorHwIntegration.so.6()(64bit) libQt6Widgets.so.6()(64bit) libQt6Widgets.so.6(Qt_6)(64bit) libQt6WlShellIntegration.so.6()(64bit) libQt6XcbQpa.so.6()(64bit) libQt6Xml.so.6()(64bit) libRecipeCodeGeneratorHelper.so.15()(64bit) libServiceCore.so.12()(64bit) libStyle.so.15()(64bit) libUtils.so.12()(64bit) libWidgetUtils.so.12()(64bit) libc.so.6(GLIBC_2.32)(64bit) libc.so.6(GLIBC_2.33)(64bit) libc.so.6(GLIBC_2.34)(64bit) libgxapi.so.16()(64bit) libkddockwidgets-qt6.so.2.0()(64bit) liblog4cpp_gcc_v3_5_Basler_pylon_v1.so()(64bit) libm.so.6(GLIBC_2.29)(64bit) libpylonbase.so.12()(64bit) libpylonc.so.10()(64bit) libpylonutility.so.12()(64bit) libstdc++.so.6(CXXABI_1.3.13)(64bit) libstdc++.so.6(GLIBCXX_3.4.26)(64bit) libstdc++.so.6(GLIBCXX_3.4.29)(64bit) libstdc++.so.6(GLIBCXX_3.4.30)(64bit) libuxapi.so.15()(64bit)

%description
Pylon SDK for Basler Cameras

%prep
%setup -q -n %{name}-%{version}.%{build_number}

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

