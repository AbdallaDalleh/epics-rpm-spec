# 
# Sequencers EPICS support
#
# Author: Abdalla Al-Dalleh <abdalla.ahmad@sesame.org.jo>
#

%global epics_prefix /opt/epics/support/seq
%global _version 2.2.8

Name:			synapps-seq
Version:		2.2
Release:		8%{?dist}
Summary:		SNL Sequencers support for EPICS
Group:			Applications/Engineering
License:		GPL+
URL:			https://epics.anl.gov
Source0:		synapps-seq-%{_version}.tar.gz
BuildRequires:	epics-base
Requires:		epics-base

%description
State notation language sequencers support for EPICS

%prep
%setup -q -n synapps-seq-%{_version}

%build

%install

export EPICS_HOST_ARCH=linux-x86_64
export LD_LIBRARY_PATH=%{buildroot}%{epics_prefix}/lib/${EPICS_HOST_ARCH}

make -C "%{_builddir}/%{?buildsubdir}" %{?_smp_mflags} \
LINKER_USE_RPATH=NO \
SHRLIB_VERSION=%{version} \
INSTALL_LOCATION="%{buildroot}%{epics_prefix}" \
FINAL_LOCATION=%{epics_prefix} \
BIN_PERMISSIONS=755 \
LIB_PERMISSIONS=644 \
SHRLIB_PERMISSIONS=755

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_bindir}
cp -a $RPM_BUILD_ROOT/%{epics_prefix}/lib/linux-x86_64/* %{buildroot}%{_libdir}/
cp -a $RPM_BUILD_ROOT/%{epics_prefix}/bin/linux-x86_64/* $RPM_BUILD_ROOT/usr/bin

export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

# mkdir -p $RPM_BUILD_ROOT/opt/epics/support/seq 
# mkdir -p $RPM_BUILD_ROOT/usr/local/lib64
# mkdir -p $RPM_BUILD_ROOT/usr/local/bin
# cp -a bin/ configure/ db/ dbd/ lib/ html/ include/ $RPM_BUILD_ROOT/opt/epics/support/seq
# cp -a lib/linux-x86_64/* $RPM_BUILD_ROOT/usr/local/lib64
# cp -a bin/linux-x86_64/* $RPM_BUILD_ROOT/usr/local/bin
# rm -rf /opt/epics/support/seq

%files
%dir %attr(-,root,root) /opt/epics/support/
%dir %attr(-,root,root) /opt/epics/support/seq
%dir %attr(-,root,root) /opt/epics/support/seq/bin
%dir %attr(-,root,root) /opt/epics/support/seq/bin/linux-x86_64
%dir %attr(-,root,root) /opt/epics/support/seq/configure
%dir %attr(-,root,root) /opt/epics/support/seq/db
%dir %attr(-,root,root) /opt/epics/support/seq/dbd
%dir %attr(-,root,root) /opt/epics/support/seq/lib
%dir %attr(-,root,root) /opt/epics/support/seq/lib/linux-x86_64
%dir %attr(-,root,root) /opt/epics/support/seq/html
%dir %attr(-,root,root) /opt/epics/support/seq/include

%attr(0755,root,root) /opt/epics/support/seq/bin/linux-x86_64/*
%attr(-,root,root)    /opt/epics/support/seq/configure/*
%attr(-,root,root)    /opt/epics/support/seq/db/*
%attr(-,root,root)    /opt/epics/support/seq/dbd/*
%attr(-,root,root)    /opt/epics/support/seq/html/*
%attr(-,root,root)    /opt/epics/support/seq/include/*
%attr(-,root,root)    /opt/epics/support/seq/lib/linux-x86_64/*.so*
%attr(-,root,root)    /opt/epics/support/seq/lib/linux-x86_64/*.a

%attr(-,root,root)    /usr/lib64/libcmdButtonsSupport.a
%attr(-,root,root)    /usr/lib64/libpv.a
%attr(-,root,root)    /usr/lib64/libseq.a
%attr(-,root,root)    /usr/lib64/libseqSoftIocSupport.a
%attr(-,root,root)    /usr/lib64/libcmdButtonsSupport.so
%attr(-,root,root)    /usr/lib64/libpv.so
%attr(-,root,root)    /usr/lib64/libseq.so
%attr(-,root,root)    /usr/lib64/libseqSoftIocSupport.so
%attr(-,root,root)    /usr/lib64/libcmdButtonsSupport.so.%{version}
%attr(-,root,root)    /usr/lib64/libpv.so.%{version}
%attr(-,root,root)    /usr/lib64/libseq.so.%{version}
%attr(-,root,root)    /usr/lib64/libseqSoftIocSupport.so.%{version}

%attr(0755,root,root) /usr/bin/cmdButtons
%attr(0755,root,root) /usr/bin/johng
%attr(0755,root,root) /usr/bin/lemon
%attr(0755,root,root) /usr/bin/pvGetAsync
%attr(0755,root,root) /usr/bin/snc
%attr(0755,root,root) /usr/bin/sncExample
%attr(0755,root,root) /usr/bin/sncExEntry
%attr(0755,root,root) /usr/bin/sncExOpt

%changelog
* Tue May 04 2021 Abdalla Al-Dalleh 2.2.8
  - New build sequence.
