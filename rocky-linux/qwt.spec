
%define qwt_prefix /usr/local/qwt-%{_version}.%{build_number}
%define debug_package %{nil}

Name:		qwt
Version:	%{_version}
Release:	%{build_number}%{?dist}
Summary:	Qt Widgets for Technical Applications

Group:		Applications/Engineering
License:	GPL+
URL:		https://nav.dl.sourceforge.net/project/qwt/qwt/6.1.3/qwt-6.1.3.zip
Source0:	qwt-%{_version}.%{build_number}.zip
BuildRequires:	qt5-qtbase qt5-qtbase-devel qt5-qtbase-gui qt5-qttools qt5-qttools-devel qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qtsvg qt5-qtsvg-devel
Requires:	    qt5-qtbase qt5-qtbase-devel qt5-qtbase-gui qt5-qttools qt5-qttools-devel qt5-qttools-libs-designer qt5-qttools-libs-designercomponents qt5-qtsvg qt5-qtsvg-devel

%description
Qt Widgets for Technical Applications

%prep
%setup -q -n qwt-%{_version}.%{build_number}

%build
export QWT_ROOT=%{buildroot}%{qwt_prefix}
sed -i 's/-dev//g' qwtconfig.pri
qmake qwt.pro
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{qwt_prefix}
make install INSTALL_ROOT=%{buildroot}

%files
%defattr(-,root,root)
%dir %{qwt_prefix}/
%dir %{qwt_prefix}/features
%dir %{qwt_prefix}/include
%dir %{qwt_prefix}/lib
%dir %{qwt_prefix}/plugins
%dir %{qwt_prefix}/plugins/designer
# %dir %{qwt_prefix}/doc/
# %{qwt_prefix}/doc/*
%{qwt_prefix}/features/*
%{qwt_prefix}/include/*
%{qwt_prefix}/lib/*
%{qwt_prefix}/plugins/designer/*

%changelog
* Mon Sep 8 2025 Abdalla Al-Dalleh 1:6.1.3
  - Fixed deprecated QString::null in src/qwt_text.h
