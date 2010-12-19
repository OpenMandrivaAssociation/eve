Summary: A web browser based on the EFL and EWebKit
Name: eve
Version: 0.3.0
Release: %mkrel 1
License: LGPLv3+
Group: Graphical desktop/Enlightenment
URL: http://trac.enlightenment.org/e/wiki/Eve
Source: http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: webkit-efl-devel
BuildRequires: libx11-devel
BuildRequires: ecore-devel
BuildRequires: evas-devel
BuildRequires: eet-devel
BuildRequires: eina-devel
BuildRequires: edje
BuildRequires: edje-devel
BuildRequires: embryo
BuildRequires: e_dbus-devel
BuildRequires: elementary-devel
BuildRequires: cairo-devel
Provides: webclient

%description
Eve is a web browser based on the EFL and EWebKit, aimed primarily to be
used on mobile devices with touch screens -- but it works like a charm
on the desktop, too.

Although still in its infancy, the browser is quite featureful to the
point of being actually usable. Some highlights:
  * Multiple pages can be opened simultaneously
  * Bookmarks
  * History (no search yet -- but it possible to filter it)
  * Privacy mode
  * Comprehensive settings dialog

There are, of course, more things hidden behind the curtains.

%prep
%setup -q -n %name-%version

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
