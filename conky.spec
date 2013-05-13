Summary:	A lightweight system monitor
Name:		conky
Version:	1.9.0
Release:	2
License:	GPLv3+
Group:		Monitoring
Url:		http://conky.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/conky/conky/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	curl-devel
BuildRequires:	libxslt-proc
BuildRequires:	libiw-devel
BuildRequires:	lua-devel
BuildRequires:	tolua++-devel
BuildRequires:	imlib2-devel
BuildRequires:	gettext-devel
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xft)
BuildRequires:	ncurses-devel

%description
Conky is a free, light-weight system monitor for X, 
that displays any information on your desktop.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--disable-rpath \
	--enable-ibm \
	--enable-rss \
	--enable-wlan \
	--enable-imlib2 \
	--enable-lua-cairo --enable-lua-imlib2

%make

%install
%makeinstall_std

#% find_lang %{name}

%files 
#-f %{name}.lang
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/*


%changelog
* Sat May 05 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.9.0-1
+ Revision: 796888
- version update 1.9.0

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 1.8.1-2
+ Revision: 635134
- simplify BR

* Sun Oct 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.1-1mdv2011.0
+ Revision: 586301
- update to new version 1.8.1

* Sat Aug 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.0-1mdv2011.0
+ Revision: 567392
- update to new version 1.8.0
- fix url for source0
- drop patch 0

* Sat Nov 21 2009 Funda Wang <fwang@mandriva.org> 1.7.2-3mdv2010.1
+ Revision: 468536
- build lua modules

* Wed Oct 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.2-2mdv2010.0
+ Revision: 455795
- rebuild for new curl SSL backend

* Sun Aug 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.2-1mdv2010.0
+ Revision: 422660
- update to new version 1.7.2

* Sat Jul 18 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1.1-2mdv2010.0
+ Revision: 397059
- add Florian Hubold's suggests to enable more features

* Sun Jun 28 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1.1-1mdv2010.0
+ Revision: 390367
- disable lua support
- update to new version 1.7.1.1

* Sat May 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.0-1mdv2010.0
+ Revision: 373897
- update to new version 1.7.0

* Fri Aug 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.1-1mdv2009.0
+ Revision: 275144
- update to new version 1.6.1

* Sun Jul 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.0-1mdv2009.0
+ Revision: 250440
- update to new version 1.6.0

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed May 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.1-1mdv2009.0
+ Revision: 203290
- add sources and spec file
- Created package structure for conky.

