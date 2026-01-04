
%define epics_host linux-x86_64
%define epics_prefix /usr/local/epics-qt
%define debug_package %{nil}

Name:	    qegui
Version:	%{_version}
Release:	%{build_number}%{?dist}
Summary:	EPICS Qt Display Manager

Group:		Applications/Engineering
License:	GPL+
URL:		https://qtepics.github.io
Source0:	qegui-%{version}.%{build_number}.tar.gz

BuildRequires:  epics-qt
Requires:       epics-qt

%description
EPICS-based widgets and client interface for Qt Framework.

%prep
%setup -q -n %{name}-%{version}.%{build_number}


%build

%install
mkdir -p %{buildroot}/usr/local/epics-qt

export EPICS_HOST_ARCH=%{epics_host}
export LD_LIBRARY_PATH=/opt/epics/base/lib/${EPICS_HOST_ARCH}:${QWT_ROOT}/lib
unset QE_TARGET_DIR

make -C "%{_builddir}/%{?buildsubdir}" %{?_smp_mflags} \
LINKER_USE_RPATH=NO \
INSTALL_LOCATION="%{buildroot}%{epics_prefix}" \
FINAL_LOCATION=%{epics_prefix} \
BIN_PERMISSIONS=755 \
LIB_PERMISSIONS=644 \
SHRLIB_PERMISSIONS=755

install -d %{buildroot}/%{epics_prefix}/bin/%{epics_host}
install -d %{buildroot}/%{_bindir}

cp %{_builddir}/%{?buildsubdir}/bin/%{epics_host}/qegui %{buildroot}/%{epics_prefix}/bin/%{epics_host}
ln -srf %{buildroot}/%{epics_prefix}/bin/%{epics_host}/qegui %{buildroot}%{_bindir}/qegui
rm -rf  %{buildroot}/%{epics_prefix}/configure/

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /usr/local/epics-qt
%dir /usr/local/epics-qt/bin
%dir /usr/local/epics-qt/bin/%{epics_host}/

/usr/local/epics-qt/bin/%{epics_host}/qegui

/usr/bin/qegui

%changelog

