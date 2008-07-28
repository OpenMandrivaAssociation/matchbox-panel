%define name 	matchbox-panel
%define version 0.9.3
%define release %mkrel 3

Summary: 	Panel for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://matchbox-project.org/sources/%name/0.9/%name-%version.tar.bz2

BuildRequires:	pkgconfig libmatchbox-devel libapm-devel startup-notification-devel libiw-devel

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

