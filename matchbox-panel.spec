%define	debugcflags %nil
Summary: 	Panel for the Matchbox Desktop
Name: 		matchbox-panel
Version: 	2.0
Release: 	2
Url: 		http://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0:	http://downloads.yoctoproject.org/releases/matchbox/matchbox-panel-2/%{version}/%name-2-%version.tar.bz2
Patch0:		gcc-4.6.0-compile.patch
Patch1:		silence-warnings.patch

BuildRequires:	libiw-devel
BuildRequires:	apmd-devel
BuildRequires:	pkgconfig(libmb)
BuildRequires:	pkgconfig(libstartup-notification-1.0)

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the panel from Matchbox.

%package	devel
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}

%description	devel
This package includes the development files for %{name}.

%prep
%setup -qn %name-2-%version
%apply_patches
sed -i 's|sync |xsync |g' applets/showdesktop/showdesktop.c
find -type f -name 'Makefile*' -exec sed -i 's|-Werror||g' {} \;
glib-gettextize --force --copy
autoreconf -fiv

%build
export LDFLAGS=-lX11
%configure --enable-nls \
	   --with-battery=apm \
	   --enable-startup-notification --enable-dbus
%make

%install
%makeinstall
#% find_lang %name

%files
#-f %name.lang
%doc AUTHORS README ChangeLog
%{_bindir}/*
%{_libdir}/matchbox-panel/*.so
%{_datadir}/matchbox-panel/*

%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc
