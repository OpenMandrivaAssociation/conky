Summary:	A lightweight system monitor
Name:		conky
Version:	1.7.2
Release:	%mkrel 2
License:	GPLv3+
Group:		Monitoring
Url:		http://conky.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	curl-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	X11-devel
BuildRequires:	libxslt-proc
BuildRequires:	libiw-devel
BuildRequires:	lua-devel
BuildRequires:	libalsa-devel
BuildRequires:	imlib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Conky is a free, light-weight system monitor for X, 
that displays any information on your desktop.

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath \
	--enable-ibm \
	--enable-rss \
	--enable-wlan \
	--enable-imlib2 \
	--enable-openmp

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
%doc
%config(noreplace) %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/*
