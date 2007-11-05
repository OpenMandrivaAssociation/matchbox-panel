%define name 	matchbox-panel
%define version 0.9.2
%define release 3mdk

Summary: 	Panel for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://projects.o-hand.com/matchbox/
License: 	GPL
Group: 		Graphical desktop/Other
Source: 	http://projects.o-hand.com/matchbox/sources/matchbox-panel/%version/%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	pkgconfig libmatchbox-devel libapm-devel

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the panel from Matchbox.

%prep
%setup -q

%build
%configure2_5x --enable-nls --enable-dnotify --enable-startup-notification
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%_bindir/*
%_datadir/pixmaps/*
%_datadir/applications/*

