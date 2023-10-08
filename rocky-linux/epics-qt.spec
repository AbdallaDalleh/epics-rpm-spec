
%define qwt 6.1.3
%define epics_host linux-x86_64
%define epics_prefix /usr/local/epics-qt
%define debug_package %{nil}

Name:		epics-qt
Version:	3.6
Release:	3%{?dist}
Summary:	EPICS-based widgets and client interface for Qt Framework

Group:		Applications/Engineering
License:	GPL+
URL:		https://qtepics.github.io
Source0:	epics-qt-3.6.3.tar.gz

BuildRequires:	qwt qt5-qtbase qt5-qtbase-common qt5-qtbase-devel qt5-qtbase-examples qt5-qtbase-gui qt5-qtbase-private-devel qt5-qttools qt5-qttools-common qt5-qttools-devel qt5-qttools-examples qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qttools-libs-help qt5-qttools-static
Requires:	qwt qt5-qtbase qt5-qtbase-common qt5-qtbase-devel qt5-qtbase-examples qt5-qtbase-gui qt5-qtbase-private-devel qt5-qttools qt5-qttools-common qt5-qttools-devel qt5-qttools-examples qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qttools-libs-help qt5-qttools-static

Epoch:		1

%description
EPICS-based widgets and client interface for Qt Framework.

%prep
%setup -q -n epics-qt-3.6.3


%build

%install
mkdir -p %{buildroot}/usr/local/epics-qt

export EPICS_HOST_ARCH=%{epics_host}
export QWT_ROOT=/usr/local/qwt-%{qwt}
export QWT_INCLUDE_PATH=${QWT_ROOT}/include
export QE_TARGET_DIR=%{buildroot}/usr/local/epics-qt
export LD_LIBRARY_PATH=/opt/epics/base/lib/${EPICS_HOST_ARCH}:${QWT_ROOT}/lib

make -C "%{_builddir}/%{?buildsubdir}" %{?_smp_mflags} \
LINKER_USE_RPATH=NO \
SHRLIB_VERSION=%{version} \
INSTALL_LOCATION="%{buildroot}%{epics_prefix}" \
FINAL_LOCATION=%{epics_prefix} \
BIN_PERMISSIONS=755 \
LIB_PERMISSIONS=644 \
SHRLIB_PERMISSIONS=755

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /usr/local/epics-qt
%dir /usr/local/epics-qt/configure
%dir /usr/local/epics-qt/lib
%dir /usr/local/epics-qt/lib/%{epics_host}
%dir /usr/local/epics-qt/lib/%{epics_host}/designer
%dir /usr/local/epics-qt/include

/usr/local/epics-qt/configure/RELEASE
/usr/local/epics-qt/include/*
/usr/local/epics-qt/lib/%{epics_host}/libQEFramework.so
/usr/local/epics-qt/lib/%{epics_host}/designer/libQEPlugin.so

%changelog

