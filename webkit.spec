#
# BEFORE UPDATING THIS PACKAGE, YOU _MUST_ DO THE FOLLOWING:
# - DO A LOCAL BUILD
# - INSTALL IT IN A TEST MACHINE
# - CHECK THAT 'display_help http://google.com' STILL WORK (INCLUDING CLOSING IT)
# - CHECK THAT MCC STILL RUNS
#

# lib is called libwebkitgtk-%{libver}.so.%{major}
%define libver  1.0 
%define major	0
%define oname		webkit
%define libname		%mklibname webkitgtk %{libver} %{major}
%define develname	%mklibname webkitgtk %{libver} -d
%define inspectorname	webkit%{libver}-webinspector
%define girname		%mklibname %{name}-gir %{libver}
%define girjscore	%mklibname jscore-gir %{libver}
%define libjavascriptcoregtk	%mklibname javascriptcoregtk %{libver} %{major}

%define lib3ver  3.0
%define major3   0
%define lib3name	%mklibname webkitgtk %{lib3ver} %{major3}
%define develname3	%mklibname webkitgtk %{lib3ver} -d
%define inspector3name	webkit%{lib3ver}-webinspector
%define libjavascriptcoregtk3	%mklibname javascriptcoregtk %{lib3ver} %{major3}
%define girname3	%mklibname %{name}-gir %{lib3ver}
%define girjscore3	%mklibname jscore-gir %{lib3ver}

%define pango	0
%if %{pango}
%define fontreq		pkgconfig(pango)
%define fontback	pango
%else
%define fontreq		pkgconfig(fontconfig) >= 1.0.0
%define fontback	freetype
%endif

Summary:	Web browser engine
Name:		webkit
Epoch:		1
Version:	1.8.1
Release:	1
License:	BSD and LGPLv2+
Group:		System/Libraries
URL:		http://www.webkitgtk.org
Source0:	http://www.webkitgtk.org/%{oname}-%{version}.tar.xz
# (blino) needed for first-time wizard (display_help) to be able to close its window with javascript
Patch0:		webkit-1.7.90-link.patch
Patch1:		webkit-1.6.1-allowScriptsToCloseWindows.patch
# to fix build errors with glib2.0 > 2.31.0
Patch2:		webkit-1.6.3_typefdef_dups.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	libtool
BuildRequires:	%{fontreq}
BuildRequires:	icu-devel >= 49
BuildRequires:	jpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(gail)
BuildRequires:	pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(geoclue)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcurl) >= 7.11.0
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.2.0
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.29.90
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xt)

%description
WebKit is an open source web browser engine.

%package -n %{name}%{libver}
Summary:	GTK+ port of WebKit web browser engine - shared files
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Conflicts:	%{libname} < 1:1.4.1-5
Conflicts:	%{name} < 1:1.4.1-6
Conflicts:	%{_lib}webkitgtk1.0_2 < 1:1.4.1
%rename %{name}

%description -n %{name}%{libver}
WebKit is an open source web browser engine.
This package contains the shared files used by %{name}%{libver}

%package -n %{libname}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Obsoletes:	%{mklibname webkitgtk 1} <= 1.1.1-3mdv
Obsoletes:	%{mklibname webkitgtk 2} <= 1.1.1-3mdv
# Needed for Web Inspector feature to work
Suggests:	%{inspectorname}
Conflicts:	gir-repository < 0.6.5-7mdv2010.1

%description -n %{libname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n %{libjavascriptcoregtk}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Obsoletes:	%{_lib}javascriptcoregtk1.0 < %{epoch}:%{version}-%{release}

%description -n %{libjavascriptcoregtk}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n %{develname}
Summary:	Development files for WebKit GTK+ port
Group:		Development/GNOME and GTK+
Provides:	webkitgtk-devel = %{version}-%{release}
Provides:	libwebkitgtk-devel = %{version}-%{release}
Provides:	%{mklibname webkitgtk -d} = %{version}-%{release}
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Requires:	%{libjavascriptcoregtk} = %{epoch}:%{version}-%{release}
Requires:	%{girjscore} = %{epoch}:%{version}-%{release}
Requires:	%{girname} = %{epoch}:%{version}-%{release}
Obsoletes:	%{mklibname webkitgtk -d} < 1.1.1-2mdv
Conflicts:	gir-repository < 0.6.5-7mdv2010.1

%description -n %{develname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package gtklauncher
Summary:	WebKit GTK+ example application
Group:		Development/GNOME and GTK+

%description gtklauncher
GtkLauncher is an example application for WebKit GTK+.

%package jsc
Summary:	JavaScriptCore shell for WebKit GTK+
Group:		Development/GNOME and GTK+

%description jsc
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package -n %{inspectorname}
Summary:	Data files for WebKit GTK+'s Web Inspector
Group:		System/Libraries
%rename		webkit-webinspector

%description -n %{inspectorname}
WebKit GTK+ has a feature called the Web Inspector, which allows
detailed analysis of any given page's page source, live DOM hierarchy
and resources. This package contains the data files necessary for Web
Inspector to work.

%package -n %{name}%{lib3ver}
Summary:	GTK+3 port of WebKit web browser engine - shared files
Group:		Development/GNOME and GTK+
Requires:	%{lib3name} =  %{epoch}:%{version}-%{release}
Conflicts:	%{lib3name} < 1:1.4.1-5
Conflicts:	%{name} < 1:1.4.1-6
%rename %{name}3

%description -n %{name}%{lib3ver}
WebKit is an open source web browser engine.
This package contains the shared files used by %{name}%{lib3ver}

%package -n %{lib3name}
Summary:	GTK+3 port of WebKit web browser engine
Group:		System/Libraries
# Needed for Web Inspector feature to work
Suggests:	%{inspector3name}

%description -n %{lib3name}
The GTK+3 port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+3 UI toolkit on platforms like
Linux.

%package -n %{libjavascriptcoregtk3}
Summary:	GTK+3 port of WebKit web browser engine
Group:		System/Libraries
Obsoletes:	%{_lib}javascriptcoregtk3.0 < %{epoch}:%{version}-%{release}

%description -n %{libjavascriptcoregtk3}
The GTK+3 port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+3 UI toolkit on platforms like
Linux.

%package -n %{develname3}
Summary:	Development files for WebKit GTK+3 port
Group:		Development/GNOME and GTK+
Provides:	webkitgtk3-devel = %{version}-%{release}
Provides:	libwebkitgtk3-devel = %{version}-%{release}
Requires:	%{lib3name} = %{epoch}:%{version}-%{release}
Requires:	%{libjavascriptcoregtk3} = %{epoch}:%{version}-%{release}
Requires:	%{girjscore3} = %{epoch}:%{version}-%{release}
Requires:	%{girname3} = %{epoch}:%{version}-%{release}

%description -n %{develname3}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package -n webkit3-gtklauncher
Summary:	WebKit GTK+3 example application
Group:		Development/GNOME and GTK+

%description -n webkit3-gtklauncher
GtkLauncher is an example application for WebKit GTK+3.

%package -n webkit3-jsc
Summary:	JavaScriptCore shell for WebKit GTK+3
Group:		Development/GNOME and GTK+

%description -n webkit3-jsc
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package -n %{inspector3name}
Summary:	Data files for WebKit GTK+'s Web Inspector
Group:		System/Libraries
Provides:	webkit3-webinspector = %{version}-%{release}

%description -n %{inspector3name}
WebKit GTK+3 has a feature called the Web Inspector, which allows
detailed analysis of any given page's page source, live DOM hierarchy
and resources. This package contains the data files necessary for Web
Inspector to work.

%package -n %{girjscore}
Summary:	GObject Introspection interface description for JSCore
Group:		System/Libraries
Conflicts:	%{_lib}webkitgtk1.0_2 < %{epoch}:%{version}-%{release}

%description -n %{girjscore}
GObject Introspection interface description for JSCore.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}webkitgtk1.0_2 < %{epoch}:%{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for WebKit.

%package -n %{girjscore3}
Summary:	GObject Introspection interface description for JSCore
Group:		System/Libraries
Conflicts:	%{libjavascriptcoregtk3} < %{epoch}:1.5.2-2

%description -n %{girjscore3}
GObject Introspection interface description for JSCore.

%package -n %{girname3}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{lib3name} < %{epoch}:1.5.2-2

%description -n %{girname3}
GObject Introspection interface description for WebKit.

%prep
%setup -q
%apply_patches

%build
mkdir -p gtk2
pushd gtk2
CONFIGURE_TOP=.. %configure2_5x	\
	--with-gtk=2.0 \
	--with-font-backend=%{fontback} \
	--with-gnu-ld \
	--enable-video \
	--enable-introspection

%make
popd

mkdir -p gtk3
pushd gtk3
CONFIGURE_TOP=.. %configure2_5x \
	--with-gtk=3.0 \
	--with-font-backend=%{fontback} \
	--with-gnu-ld \
	--enable-video \
	--enable-introspection

%make
popd

%install
rm -rf %{buildroot}
%makeinstall_std -C gtk2
%makeinstall_std -C gtk3
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 755 gtk2/Programs/GtkLauncher %{buildroot}%{_libdir}/%{name}

mkdir -p %{buildroot}%{_libdir}/%{name}3
install -m 755 gtk3/Programs/GtkLauncher %{buildroot}%{_libdir}/%{name}3

# only useful for testing, should not be installed system-wide.
# reported upstream as 22812 - AdamW 2008/12
rm -rf %{buildroot}%{_libdir}/libtestnetscapeplugin.*

%find_lang %{name}-2.0
%find_lang %{name}-3.0
find %{buildroot} -name *.la | xargs rm

%files -n %{name}%{libver} -f %{name}-2.0.lang
%dir %{_datadir}/webkitgtk-1.0
%{_datadir}/webkitgtk-1.0/images
%{_datadir}/webkitgtk-1.0/resources

%files -n %{develname}
%{_libdir}/lib%{name}gtk-%{libver}.so
%{_libdir}/libjavascriptcoregtk-%{libver}.so
%{_includedir}/%{name}gtk-%{libver}
%{_libdir}/pkgconfig/%{name}-%{libver}.pc
%{_libdir}/pkgconfig/javascriptcoregtk-%{libver}.pc
%{_datadir}/gir-1.0/JSCore-%{libver}.gir
%{_datadir}/gir-1.0/WebKit-%{libver}.gir

%files -n %{libname}
%{_libdir}/lib%{name}gtk-%{libver}.so.%{major}*

%files -n %{libjavascriptcoregtk}
%{_libdir}/libjavascriptcoregtk-%{libver}.so.%{major}*

%files -n %{girjscore}
%_libdir/girepository-1.0/JSCore-%{libver}.typelib

%files -n %{girname}
%_libdir/girepository-1.0/WebKit-%{libver}.typelib

%files gtklauncher
%{_libdir}/%{name}/GtkLauncher

%files jsc
%{_bindir}/jsc-1

%files -n %{inspectorname}
%{_datadir}/%{name}gtk-%{libver}/webinspector

%files -n %{name}%{lib3ver} -f %{name}-3.0.lang
%dir %{_datadir}/webkitgtk-3.0
%{_datadir}/webkitgtk-3.0/images
%{_datadir}/webkitgtk-3.0/resources

%files -n %{develname3}
%{_libdir}/lib%{name}gtk-%{lib3ver}.so
%{_libdir}/libjavascriptcoregtk-%{lib3ver}.so
%{_includedir}/%{name}gtk-%{lib3ver}
%{_libdir}/pkgconfig/%{name}gtk-%{lib3ver}.pc
%{_libdir}/pkgconfig/javascriptcoregtk-%{lib3ver}.pc
%{_datadir}/gir-1.0/JSCore-%{lib3ver}.gir
%{_datadir}/gir-1.0/WebKit-%{lib3ver}.gir

%files -n %{lib3name}
%{_libdir}/lib%{name}gtk-%{lib3ver}.so.%{major3}*

%files -n %{libjavascriptcoregtk3}
%{_libdir}/libjavascriptcoregtk-%{lib3ver}.so.%{major}*

%files -n %{name}3-gtklauncher
%{_libdir}/%{name}3/GtkLauncher

%files -n %{name}3-jsc
%{_bindir}/jsc-3

%files -n %{inspector3name}
%{_datadir}/%{name}gtk-%{lib3ver}/webinspector

%files -n %{girjscore3}
%_libdir/girepository-1.0/JSCore-%{lib3ver}.typelib

%files -n %{girname3}
%_libdir/girepository-1.0/WebKit-%{lib3ver}.typelib

