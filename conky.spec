Summary:	A lightweight system monitor
Name:		conky
Version:	1.9.0
Release:	1
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
BuildRequires:	libx11-devel
BuildRequires:	libxdamage-devel
BuildRequires:	libxext-devel
BuildRequires:	libxfixes-devel
BuildRequires:	libxft-devel
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
