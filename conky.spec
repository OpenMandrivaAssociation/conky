%bcond_with	audacious
%bcond_without	curl
%bcond_with	docs	# pandoc is not packaged yet
%bcond_without	extras
%bcond_without	hddtemp
%bcond_without	i11n
%bcond_without	ibm
%bcond_without	imlib
%bcond_without	lua_cairo
%bcond_without	lua_imlib
%bcond_without	lua_rsvg
%bcond_with	moc
%bcond_without	mpd
%bcond_without	ncurses
%bcond_with	nvidia
%bcond_without	portmon
%bcond_without	pulseaudio
%bcond_without	rss
%bcond_without	tests
%bcond_without	wayland
%bcond_with	wlan
%bcond_without	x11
%bcond_without	xdbe
%bcond_without	xinerama

Name:		conky
Version:	1.22.0
Release:	1
Summary:	A lightweight system monitor
License:	GPLv3+
Url:		https://github.com/brndnmtthws/conky
Source0:	https://github.com/brndnmtthws/conky/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		conky-1.13.1-dont_require_git.patch
BuildRequires:	c++-devel
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook2x
BuildRequires:	git
BuildRequires:	man
BuildRequires:	lcov
BuildRequires:	gettext-devel
BuildRequires:	kernel-headers
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libunwind)
BuildRequires:	pkgconfig(libunwind-llvm)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	python3dist(pyyaml)
BuildRequires:	python3dist(jinja2)
BuildRequires:	xsltproc

# There is no audclient beginning with audacious 3.5.
# Disable audacious support until it is fixed by upstream.
%{?with_audacious:BuildRequires:	pkgconfig(dbus-glib-1) pkgconfig(audacious)}
%{?with_docs:BuildRequires:		pypandoc}
%{?with_curl:BuildRequires:		pkgconfig(libcurl)}
%{?with_rss:BuildRequires:		pkgconfig(libcurl) pkgconfig(libxml-2.0)}
%{?with_imlib:BuildRequires:		pkgconfig(imlib2)}
%{?with_lua_cairo:BuildRequires:	pkgconfig(cairo) tolua++-devel}
%{?with_lua_imlib:BuildRequires:	pkgconfig(imlib2) tolua++-devel}
%{?with_lua_rsvg:BuildRequires:		pkgconfig(librsvg-2.0)}
%{?with_pulseaudio:BuildRequires:	pkgconfig(libpulse)}
%{?with_ncurses:BuildRequires:		pkgconfig(ncurses)}
%{?with_nvidia:BuildRequires: 		%{_lib}XNVCtrl-devel}
%{?with_xinerama:BuildRequires:		pkgconfig(xinerama)}
%if %{with wayland}
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(pangofc)
BuildRequires:	pkgconfig(pangoft2)
%endif
%{?with_wlan:BuildRequires:		wireless-tools}

%description
Conky is a free, light-weight system monitor for X,
that displays any information on your desktop.

%files
%doc AUTHORS COPYING README.md extras/*
%dir %{_sysconfdir}/conky
%config(noreplace) %{_sysconfdir}/conky/conky.conf
%{_bindir}/conky
%{_libdir}/conky
%{_libdir}/libconky_core.so
%{_datadir}/applications/conky.desktop
%{_iconsdir}/hicolor/scalable/apps/conky-logomark-violet.svg
%{?with_docs:
%{_mandir}/man1/conky.1*
}

#---------------------------------------------------------------------------

%prep
%autosetup -p1

# our tolua++ is linked with lua 5.3
#sed -i \
#	-e 's|\(LUA REQUIRED\) lua5.1 lua-5.1 lua51 lua|\1 lua>=5.3|' \
#	-e 's|\(NOT LUA_VERSION VERSION_LESS\) 5.2.0|\1 5.4.0|' \
#	cmake/ConkyPlatformChecks.cmake

%build
%cmake \
	-DMAINTAINER_MODE:BOOL=OFF \
	-DBUILD_BUILTIN_CONFIG:BOOL=OFF \
	-DBUILD_PORT_MONITORS:BOOL=OFF \
	-DBUILD_AUDACIOUS:BOOL=%{?with_audacious:ON}%{!?with_audacious:OFF} \
	-DBUILD_CURL:BOOL=%{?with_curl:ON}%{!?with_curl:OFF} \
	-DBUILD_DOCS:BOOL=%{?with_docs:ON}%{!?with_docs:OFF} \
	-DBUILD_EXTRAS:BOOL=%{?with_extras:ON}%{!?with_extras:OFF} \
	-DBUILD_I18N:BOOL=%{?with_x11n:ON}%{!?with_x11n:OFF} \
	-DBUILD_IBM:BOOL=%{?with_ibm:ON}%{!?with_ibm:OFF} \
	-DBUILD_IMLIB2:BOOL=%{?with_imlib2:ON}%{!?with_imlib2:OFF} \
	-DBUILD_JOURNAL:BOOL=ON \
	-DBUILD_HDDTEMP:BOOL=%{?with_hddtemp:ON}%{!?with_hddtemp:OFF} \
	-DBUILD_I18N:BOOL=%{?with_i11n:ON}%{!?with_i11n:OFF} \
	-DBUILD_LUA_CAIRO:BOOL=%{?with_lua_cairo:ON}%{!?with_lua_cairo:OFF} \
	-DBUILD_LUA_IMLIB2:BOOL=%{?with_lua_imlib:ON}%{!?with_lua_imlib:OFF} \
	-DBUILD_LUA_RSVG:BOOL=%{?with_lua_rsvg:ON}%{!?with_lua_rsvg:OFF} \
	-DBUILD_PULSEAUDIO:BOOL=%{?with_pulseaudio:ON}%{!?with_pulseaudio:OFF} \
	-DBUILD_MOC:BOOL=%{?with_moc:ON}%{!?with_moc:OFF} \
	-DBUILD_MYSQL:BOOL=%{?with_mysql:ON}%{!?with_mysql:OFF} \
	-DBUILD_MPD:BOOL=%{?with_mpd:ON}%{!?with_mpd:OFF} \
	-DBUILD_NCURSES:BOOL=%{?with_ncurses:ON}%{!?with_ncurses:OFF} \
	-DBUILD_NVIDIA:BOOL=%{?with_nvidia:ON}%{!?with_nvidia:OFF} \
	-DBUILD_RSS:BOOL=%{?with_rss:ON}%{!?with_rss:OFF} \
	-DBUILD_WAYLAND:BOOL=%{?with_wayland:ON}%{!?with_wayland:OFF} \
	-DBUILD_WLAN:BOOL=%{?with_wlan:ON}%{!?with_wlan:OFF} \
	-DBUILD_X11:BOOL=%{?with_x11:ON}%{!?with_x11:OFF} \
	-DBUILD_XDBE:BOOL=%{?with_xdbe:ON}%{!?with_xdbe:OFF} \
	-DBUILD_XINERAMA:BOOL=%{?with_xinerama:ON}%{!?with_xinerama:OFF} \
	-DBUILD_TESTS:BOOL=%{?with_tests:ON}%{!?with_tests:OFF} \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

# install default configs
install -dm 0755 %{buildroot}%{_sysconfdir}/%{name}
install -pm 0644 data/conky.conf %{buildroot}%{_sysconfdir}/%{name}

# remove docs
rm -rf %{buildroot}%{_docdir}/conky-*

