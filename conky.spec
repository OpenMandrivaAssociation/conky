Summary:	A lightweight system monitor
Name:		conky
Version:	1.7.2
Release:	%mkrel 3
License:	GPLv3+
Group:		Monitoring
Url:		http://conky.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		conky-1.7.2-fix-module.patch
BuildRequires:	curl-devel
BuildRequires:	X11-devel
BuildRequires:	libxslt-proc
BuildRequires:	libiw-devel
BuildRequires:	lua-devel
BuildRequires:	tolua++-devel
BuildRequires:	libalsa-devel
BuildRequires:	imlib2-devel
BuildRequires:	gettext-devel
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Conky is a free, light-weight system monitor for X, 
that displays any information on your desktop.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/*
