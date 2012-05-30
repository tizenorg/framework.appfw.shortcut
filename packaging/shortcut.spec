Name:	    shortcut
Summary:    Shortcut add feature supporting library
Version:    0.0.5
Release:    0
Group:      main/devel
License:    Samsung Proprietary License
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/shortcut.manifest 

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

BuildRequires: cmake, gettext-tools
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(dlog)

%description
[Shortcut] AddToHome feature supporting library for menu/home screen developers.

%package devel
Summary:    AddToHome feature supporting library development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
[Shortcut] AddToHome feature supporting library for menu/home screen developers
(dev).

%prep
%setup -q

%build
cp %{SOURCE1001} .
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post

%postun

%files
%manifest shortcut.manifest
%defattr(-,root,root,-)
%{_libdir}/*.so*

%files devel
%manifest shortcut.manifest
%defattr(-,root,root,-)
%{_includedir}/shortcut/SLP_shortcut_PG.h
%{_includedir}/shortcut/shortcut.h
%{_libdir}/pkgconfig/shortcut.pc
