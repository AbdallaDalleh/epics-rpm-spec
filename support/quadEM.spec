# 
# Quad Electrometers EPICS Driver
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/quadEM

Name:			quadEM
Version:		%{_version}
Release:		%{build_number}%{?dist}
Summary:		Quad Electrometers EPICS Driver
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		%{name}-%{_version}.%{build_number}.tar.gz
BuildRequires:	asyn area-detector-core area-detector-support
Requires:   	asyn area-detector-core area-detector-support

%description
Quad Electrometers EPICS Driver

%prep
%setup -q -n %{name}-%{_version}.%{build_number}

%build


%install
shopt -s extglob

export EPICS_HOST_ARCH=linux-x86_64
export LD_LIBRARY_PATH=%{buildroot}%{epics_prefix}/lib/${EPICS_HOST_ARCH}:/opt/epics/support/areaDetector/support/lib/${EPICS_HOST_ARCH}

make -C "%{_builddir}/%{?buildsubdir}" %{?_smp_mflags} \
LINKER_USE_RPATH=NO \
SHRLIB_VERSION=%{version} \
INSTALL_LOCATION="%{buildroot}%{epics_prefix}" \
FINAL_LOCATION=%{epics_prefix} \
BIN_PERMISSIONS=755 \
LIB_PERMISSIONS=644 \
SHRLIB_PERMISSIONS=755 \
TIRPC=YES

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{epics_prefix}/op

mv %{buildroot}%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}
mv %{buildroot}%{epics_prefix}/bin/linux-x86_64/* %{buildroot}%{_bindir}

ln -sr %{buildroot}%{_libdir}/* %{buildroot}%{epics_prefix}/lib/linux-x86_64/
ln -sr %{buildroot}%{_bindir}/* %{buildroot}%{epics_prefix}/bin/linux-x86_64/

cp -a %{_builddir}/%{?buildsubdir}/quadEMApp/op/!(Makefile) %{buildroot}%{epics_prefix}/op
cp -a %{_builddir}/%{?buildsubdir}/quadEMApp/Db/*.req       %{buildroot}%{epics_prefix}/db

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
%dir %{epics_prefix}/db
%dir %{epics_prefix}/dbd
%dir %{epics_prefix}/lib
%dir %{epics_prefix}/lib/linux-x86_64
%dir %{epics_prefix}/op
%dir %{epics_prefix}/op/edl
%dir %{epics_prefix}/op/adl
%dir %{epics_prefix}/op/ui
%dir %{epics_prefix}/op/bob
%dir %{epics_prefix}/op/opi
%dir %{epics_prefix}/include

%{epics_prefix}/bin/linux-x86_64/*
%{epics_prefix}/configure/*
%{epics_prefix}/db/*
%{epics_prefix}/dbd/*
%{epics_prefix}/include/*
%{epics_prefix}/lib/linux-x86_64/*
%{epics_prefix}/op/edl/*
%{epics_prefix}/op/adl/*
%{epics_prefix}/op/opi/*
%{epics_prefix}/op/bob/*
%{epics_prefix}/op/ui/*

%{_libdir}/*
%{_bindir}/*

%changelog
* Wed Dec 31 2025 Abdalla Al-Dalleh 9.6
  - New build sequence.
