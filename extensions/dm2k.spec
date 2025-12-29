%global final_loc /opt/epics/extensions/dm2k

Name:           dm2k
Version:        %{_version}
Release:        %{build_number}%{?dist}
Summary:        A new version of MEDM
License:        GPL+
URL:            https://github.com/epicsdeb/dm2k
Source0:        dm2k-2.6.2.tar.gz

BuildRequires:  libXt-devel openmotif-devel libXpm-devel epics-base expat fontconfig freetype glibc libgcc libICE libjpeg-turbo libpng libSM libstdc++ libuuid libX11 libXau libxcb libXext libXft libXmu libXp libXrender motif ncurses-libs readline zlib
Requires:       libXt-devel openmotif-devel libXpm-devel epics-base expat fontconfig freetype glibc libgcc libICE libjpeg-turbo libpng libSM libstdc++ libuuid libX11 libXau libxcb libXext libXft libXmu libXp libXrender motif ncurses-libs readline zlib

%description
A new version of MEDM

%prep
%setup -q -n %{name}-%{_version}.%{build_number}

%build

%install

export EPICS_HOST_ARCH=linux-x86_64
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{final_loc}/lib/linux-x86_64

make -C "%{_builddir}/%{?buildsubdir}" \
LINKER_USE_RPATH=NO \
INSTALL_LOCATION="%{buildroot}%{final_loc}" \
BIN_PERMISSIONS=755 \
LIB_PERMISSIONS=777 \
SHRLIB_PERMISSIONS=755

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}
mv %{buildroot}%{final_loc}/lib/linux-x86_64/*    %{buildroot}%{_libdir}
mv %{buildroot}%{final_loc}/bin/linux-x86_64/dm2k %{buildroot}%{_bindir}
ln -sr %{buildroot}%{_libdir}/*    %{buildroot}%{final_loc}/lib/linux-x86_64
ln -sr %{buildroot}%{_bindir}/dm2k %{buildroot}%{final_loc}/bin/linux-x86_64
export QA_SKIP_BUILD_ROOT=1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir /opt/epics/extensions
%dir /opt/epics/extensions/dm2k
%dir /opt/epics/extensions/dm2k/bin
%dir /opt/epics/extensions/dm2k/bin/linux-x86_64
%dir /opt/epics/extensions/dm2k/lib
%dir /opt/epics/extensions/dm2k/lib/linux-x86_64
%dir /opt/epics/extensions/dm2k/configure
%dir /opt/epics/extensions/dm2k/etc
%dir /opt/epics/extensions/dm2k/include

/opt/epics/extensions/dm2k/configure/*
/opt/epics/extensions/dm2k/etc/*
/opt/epics/extensions/dm2k/include/*
/opt/epics/extensions/dm2k/bin/linux-x86_64/dm2k
/opt/epics/extensions/dm2k/lib/linux-x86_64/*
%{_bindir}/dm2k
%{_libdir}/*

%changelog
* Thu Aug 24 2023 rami.khrais <rami.khrais@sesame.org.jo>
- Initial Release.
