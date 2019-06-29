%bcond_with audacious
%bcond_with nvidia
%bcond_without wlan

Name:           conky
Version:        1.11.4
Release:        1
Summary:        A lightweight system monitor
License:        GPLv3+
Group:          Monitoring
Url:            https://github.com/brndnmtthws/conky
Source0:        https://github.com/brndnmtthws/conky/archive/v%{version}/%{name}-%{version}.tar.gz
#Patch1:         conky-1.10.1-fix-cmake-build.patch
#Patch2:		lua53.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook2x
BuildRequires:  git
BuildRequires:  man
BuildRequires:  pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:  xsltproc
BuildRequires:  libiw-devel
BuildRequires:  pkgconfig(lua)
BuildRequires:  tolua++-devel
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(alsa)

%{?with_nvidia:BuildRequires: libXNVCtrl-devel}
%{?with_wlan:BuildRequires: wireless-tools}
# There is no audclient beginning with audacious 3.5
# which is our current cauldron one and compilation
# fails. Disable audacious support until it is fixed by upstream.
%{?with_audacious:BuildRequires:        pkgconfig(dbus-glib-1) pkgconfig(audacious)}


%description
Conky is a free, light-weight system monitor for X,
that displays any information on your desktop.

%prep
%setup -q
%apply_patches

# remove -Werror from CFLAGS
sed -i 's|-Werror||' cmake/ConkyBuildOptions.cmake

# our tolua++ is linked with lua 5.3
sed -i \
       -e 's|\(LUA REQUIRED\) lua5.1 lua-5.1 lua51 lua|\1 lua>=5.3|' \
       -e 's|\(NOT LUA_VERSION VERSION_LESS\) 5.2.0|\1 5.4.0|' \
    cmake/ConkyPlatformChecks.cmake


# remove executable bits from files included in %{_docdir}
chmod a-x extras/convert.lua

for i in AUTHORS; do
    iconv -f iso8859-1 -t utf8 -o ${i}{_,} && touch -r ${i}{,_} && mv -f ${i}{_,}
done

%build
%cmake \
        -DMAINTAINER_MODE=ON \
        -DBUILD_BUILTIN_CONFIG=OFF \
        -DBUILD_PORT_MONITORS=OFF \
        -DBUILD_CURL=ON \
        -DBUILD_IBM=OFF \
        -DBUILD_IMLIB2=ON \
	-DBUILD_JOURNAL=ON \
	-DBUILD_HDDTEMP=ON \
	-DBUILD_WLAN=ON \
	-DBUILD_I18N=ON \
        -DBUILD_LUA_CAIRO=ON \
        -DBUILD_LUA_IMLIB2=ON \
	-DBUILD_PULSEAUDIO=ON \
        -DBUILD_MOC=OFF \
        -DBUILD_MPD=OFF \
        -DBUILD_NCURSES=OFF \
        -DBUILD_RSS=ON \
        -DBUILD_WEATHER_METAR=ON \
        -DBUILD_WEATHER_XOAP=ON \
        -DBUILD_XDBE=ON \
    %{?with_audacious:      -DBUILD_AUDACIOUS=ON} \
    %{?with_nvidia:         -DBUILD_NVIDIA=ON} \
    %{?with_wlan:           -DBUILD_WLAN=ON} \

%make_build

%install
pushd build
%make_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/conky
popd
install -m644 -p data/conky.conf $RPM_BUILD_ROOT%{_sysconfdir}/conky
rm -rf $RPM_BUILD_ROOT%{_docdir}/conky-*

%files
%doc AUTHORS COPYING README.md extras/*
%dir %{_sysconfdir}/conky
%config(noreplace) %{_sysconfdir}/conky/conky.conf
%{_bindir}/conky
%{_libdir}/conky
%{_libdir}/libconky_core.so
%{_datadir}/applications/conky.desktop
%{_iconsdir}/hicolor/scalable/apps/conky-logomark-violet.svg
#{_mandir}/man1/conky.1*
