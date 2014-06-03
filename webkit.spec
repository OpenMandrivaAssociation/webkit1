#
# BEFORE UPDATING THIS PACKAGE, YOU _MUST_ DO THE FOLLOWING:
# - DO A LOCAL BUILD
# - INSTALL IT IN A TEST MACHINE
# - CHECK THAT 'display_help http://google.com' STILL WORK (INCLUDING CLOSING IT)
# - CHECK THAT MCC STILL RUNS
#


# lib is called libwebkitgtk-%{libver}.so.%{major}
%define libver  1.0
%define major   0
%define oname		webkitgtk
%define libname		%mklibname webkitgtk %{libver} %{major}
%define devname		%mklibname webkitgtk %{libver} -d
%define inspectorname	webkit%{libver}-webinspector
%define libgirname      %mklibname %name-gir %{libver}
%define libgitjscore    %mklibname javascriptcore-gir %{libver}
%define libjavascriptcoregtk	%mklibname javascriptcoregtk %{libver} %{major}

%define lib3ver  3.0
%define major3   0
%define	major2	25
%define lib3name	%mklibname webkitgtk %{lib3ver} %{major3}
%define libwebkit2	%mklibname webkit2gtk %{lib3ver} %{major2}
%define devname3	%mklibname webkitgtk %{lib3ver} -d
%define inspector3name	webkit%{lib3ver}-webinspector
%define girname3	%mklibname %{name}-gir %{lib3ver}
%define girjscore3	%mklibname jscore-gir %{lib3ver}
%define libjavascriptcoregtk3	%mklibname javascriptcoregtk %{lib3ver} %{major3}

%define libgirname3	%mklibname %{name}-gir %{lib3ver}
%define libgirname2	%mklibname %{name}2-gir %{lib3ver}
%define libgitjscore3	%mklibname javascriptcore-gir %{lib3ver}
%define libgirname2extension %mklibname %{name}2webextension-gir %{lib3ver}

Summary:	Web browser engine
Name:		webkit
Epoch:		1
Version:	2.4.3
Release:	1
License:	BSD and LGPLv2+
Group:		System/Libraries
Url:		http://www.webkitgtk.org
Source0:	http://www.webkitgtk.org/releases/%{oname}-%{version}.tar.xz
Patch0:		webkit-2.3.90-link.patch
# (blino) needed for first-time wizard (display_help) to be able to close its window with javascript
Patch2:		webkit-2.1.90-allowScriptsToCloseWindows.patch
Patch3:		webkitgtk-2.1.92-gtk-includes.patch
Patch4:         webkit-1.1.14-nspluginwrapper.patch
Patch5:		webkitgtk-aarch64.patch
Patch6:		webkitgtk-2.4.3-fix-JavaScriptCore-sharedlib-name.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	icu-devel >= 49
BuildRequires:	jpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(gail)
BuildRequires:	pkgconfig(gail-3.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(geoclue)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0) >= 1.2.4
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
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libsecret-1)

%description
WebKit is an open source web browser engine.

%package -n %{name}%{libver}
Summary:        GTK+ port of WebKit web browser engine - shared files
Group:          Development/GNOME and GTK+
Requires:	%{libname} = %{epoch}:%{version}

%description -n %{name}%{libver}
WebKit is an open source web browser engine.
This package contains the shared files used by %{name}%{libver}

%package -n %{libname}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	%{name}%{libver} = %{epoch}:%{version}
Obsoletes:	%{mklibname WebKitGdk 0} <= 0-0.30465
Obsoletes:	%{mklibname WebKitGtk 1} <= 0-0.32877
Obsoletes:	%{mklibname webkitgtk 1} <= 1.1.1-3mdv
Obsoletes:	%{mklibname webkitgtk 2} <= 1.1.1-3mdv
Obsoletes:      %{mklibname webkitgtk-1.00} <= 1.3.12-3.mga1
# (fhimpe) This provides should probably be removed when major changes
Provides:	%{mklibname webkitgtk 2} = %{version}-%{release}
Provides:	libwebkitgtk = %{version}-%{release}
# Needed for Web Inspector feature to work
#Suggests:	%{inspectorname} = %{epoch}:%{version}
Conflicts:	gir-repository < 0.6.5-7mdv2010.1

%description -n %{libname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n %{libjavascriptcoregtk}
Summary:        GTK+ port of WebKit web browser engine
Group:          System/Libraries
Requires:       %{libname} = %{epoch}:%{version}
Obsoletes:	%{_lib}javascriptcoregtk1.0 < %{epoch}:%{version}-%{release}

%description -n %{libjavascriptcoregtk}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n %{devname}
Summary:	Development files for WebKit GTK+ port
Group:		Development/GNOME and GTK+
Provides:	webkitgtk-devel = %{version}-%{release}
Provides:	libwebkitgtk-devel = %{version}-%{release}
Provides:	%{mklibname webkitgtk -d} = %{version}-%{release}
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Requires:	%{libjavascriptcoregtk} = %{epoch}:%{version}-%{release}
Requires:	%{libgitjscore} = %epoch:%{version}-%{release}
Requires:	%{libgirname} = %epoch:%{version}-%{release}
Obsoletes:	%{mklibname WebKitGtk -d} <= 0-0.32877
Obsoletes:	%{mklibname webkitgtk -d} < 1.1.1-2mdv
Conflicts:	gir-repository < 0.6.5-7mdv2010.1

%description -n %{devname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package gtklauncher
Summary:	WebKit GTK+ example application
Group:		Development/GNOME and GTK+
Conflicts:	%{mklibname WebKitGtk 0} <= 0-0.30465

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
Provides:	webkit-webinspector = %{version}-%{release}
Obsoletes:	webkit-webinspector < 1.1.1-2mdv

%description -n %{inspectorname}
WebKit GTK+ has a feature called the Web Inspector, which allows
detailed analysis of any given page's page source, live DOM hierarchy
and resources. This package contains the data files necessary for Web
Inspector to work.

%package -n %{name}3
Summary:        Web browser engine
Group:          System/Libraries
Requires:       %{lib3name} = %{epoch}:%{version}

%description -n %{name}3
WebKit is an open source web browser engine.

%package -n %{name}%{lib3ver}
Summary:        GTK+3 port of WebKit web browser engine - shared files
Group:          Development/GNOME and GTK+
Requires:       %{lib3name} = %{epoch}:%{version}

%description -n %{name}%{lib3ver}
WebKit is an open source web browser engine.
This package contains the shared files used by %{name}%{lib3ver}

%package -n %{name}2gtk
Summary:	GTK+3 port of WebKit2 web browser engine - shared files
Group:		Development/GNOME and GTK+

%description -n %{name}2gtk
WebKit is an open source web browser engine.
This package contains the shared files used by %{name}2gtk%{lib3ver}.

%package -n %{lib3name}
Summary:        GTK+3 port of WebKit web browser engine
Group:          System/Libraries
Requires:       %{name}3 = %{epoch}:%{version}
Requires:       %{name}%{lib3ver} = %{epoch}:%{version}
Provides:       libwebkitgtk3 = %{version}-%{release}
# Needed for Web Inspector feature to work
#Suggests:       %{inspector3name} = %{epoch}:%{version}

%description -n %{lib3name}
The GTK+3 port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+3 UI toolkit on platforms like
Linux.

%package -n %{libwebkit2}
Summary:        GTK+3 port of WebKit2 web browser engine
Group:          System/Libraries
Requires:       %{name}3 = %{epoch}:%{version}
Requires:	%{name}2gtk = %{epoch}:%{version}
Provides:       libwebkit2gtk3 = %{version}-%{release}

%description -n %{libwebkit2}
The GTK+3 port of WebKit2 is intended to provide a browser component
primarily for users of the portable GTK+3 UI toolkit on platforms like
Linux.

%package -n %{libjavascriptcoregtk3}
Summary:        GTK+3 port of WebKit web browser engine
Group:          System/Libraries
Requires:       %{lib3name} = %{epoch}:%{version}
Obsoletes:	%{_lib}javascriptcoregtk3.0 < %{epoch}:%{version}-%{release}

%description -n %{libjavascriptcoregtk3}
The GTK+3 port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+3 UI toolkit on platforms like
Linux.

%package -n %{devname3}
Summary:        Development files for WebKit GTK+3 port
Group:          Development/GNOME and GTK+
Provides:       webkitgtk3-devel = %{version}-%{release}
Provides:       libwebkitgtk3-devel = %{version}-%{release}
Requires:       %{lib3name} = %{epoch}:%{version}-%{release}
Requires:	%{libjavascriptcoregtk3} = %{epoch}:%{version}-%{release}
Requires:	%{libgitjscore3} = %{epoch}:%{version}-%{release}
Requires:	%{libgirname3} = %{epoch}:%{version}-%{release}
Requires:	%{libwebkit2} = %{epoch}:%{version}-%{release}
Requires:	%{libgirname2} = %{epoch}:%{version}-%{release}
Requires:	%{libgirname2extension} = %{epoch}:%{version}-%{release}

%description -n %{devname3}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package -n webkit3-gtklauncher
Summary:        WebKit GTK+3 example application
Group:          Development/GNOME and GTK+

%description -n webkit3-gtklauncher
GtkLauncher is an example application for WebKit GTK+3.

%package -n webkit3-jsc
Summary:        JavaScriptCore shell for WebKit GTK+3
Group:          Development/GNOME and GTK+

%description -n webkit3-jsc
jsc is a shell for JavaScriptCore, WebKit's JavaScript engine. It
allows you to interact with the JavaScript engine directly.

%package -n %{inspector3name}
Summary:        Data files for WebKit GTK+'s Web Inspector
Group:          System/Libraries
Provides:       webkit3-webinspector = %{version}-%{release}

%description -n %{inspector3name}
WebKit GTK+3 has a feature called the Web Inspector, which allows
detailed analysis of any given page's page source, live DOM hierarchy
and resources. This package contains the data files necessary for Web
Inspector to work.

%package -n %{libgitjscore}
Summary:        GObject Introspection interface description for JSCore
Group:          System/Libraries
Requires:       %{libjavascriptcoregtk} = %epoch:%{version}-%{release}
Conflicts:	%{_lib}webkitgtk1.0_2 < %epoch:%{version}-%{release}
Obsoletes:	%{_lib}jscore-gir1.0 < 1:2.1.3

%description -n %{libgitjscore}
GObject Introspection interface description for JSCore.

%package -n %{libgirname}
Summary:        GObject Introspection interface description for %name
Group:          System/Libraries
Requires:       %{libname} = %epoch:%{version}-%{release}
Conflicts:	%{_lib}webkitgtk1.0_2 < %epoch:%{version}-%{release}

%description -n %{libgirname}
GObject Introspection interface description for WebKit.

%package -n %{libgitjscore3}
Summary:        GObject Introspection interface description for JSCore
Group:          System/Libraries
Requires:       %{libjavascriptcoregtk3} = %epoch:%{version}-%{release}
Conflicts:	%{libjavascriptcoregtk3} < %epoch:1.5.2-2
Obsoletes:	%{_lib}jscore-gir3.0 < 1:2.1.3

%description -n %{libgitjscore3}
GObject Introspection interface description for JSCore.

%package -n %{libgirname3}
Summary:        GObject Introspection interface description for %name
Group:          System/Libraries
Requires:       %{lib3name} = %epoch:%{version}-%{release}
Conflicts:	%{lib3name} < %epoch:1.5.2-2

%description -n %{libgirname3}
GObject Introspection interface description for WebKit.

%package -n %{libgirname2}
Summary:        GObject Introspection interface description for %name
Group:          System/Libraries
Requires:       %{libwebkit2} = %epoch:%{version}-%{release}

%description -n %{libgirname2}
GObject Introspection interface description for WebKit2.

%package -n %{libgirname2extension}
Summary:	GObject Introspection interface description for %name
Group:		System/Libraries

%description -n %{libgirname2extension}
GObject Introspection interface description for WebKit2.


%prep
%setup -qn %{oname}-%{version}
%apply_patches
autoreconf  -fiv

mkdir -p .gtk{2,3}/DerivedSources/{webkit{,2},WebCore,ANGLE,WebKit2,webkitdom,InjectedBundle,Platform} 
cp -a * .gtk2
cp -a * .gtk3
mv .gtk2 gtk2
mv .gtk3 gtk3

%build
%global optflags %{optflags} -g1 -fno-var-tracking-assignments -fno-record-gcc-switches
# Use linker flags to reduce memory consumption on low-mem architectures
%ifarch %{arm}
%global optflags %{optflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads
mkdir -p bfd
ln -s %{_bindir}/ld.bfd bfd/ld
export PATH=$PWD/bfd:$PATH
export CC="%{__cc} -fuse-ld=bfd"
export CXX="%{__cxx} -fuse-ld=bfd"
%global ldflags %{ldflags} -fuse-ld=bfd
%endif

pushd gtk2
%configure2_5x \
	--with-gtk=2.0 \
	--disable-webkit2 \
	--enable-jit \
	--enable-gamepad \
	--enable-accelerated-compositing \
	--enable-introspection
%make
popd

pushd gtk3
%configure2_5x \
	--with-gtk=3.0 \
	--enable-webkit2 \
	--enable-jit \
	--enable-gamepad \
	--enable-accelerated-compositing \
	--enable-introspection
%make 
popd


%install
%makeinstall_std -C gtk2
%makeinstall_std -C gtk3

install -p -m755 gtk2/Programs/GtkLauncher -D %{buildroot}%{_libexecdir}/%{name}/GtkLauncher

install -p -m755 gtk3/Programs/GtkLauncher -D %{buildroot}%{_libexecdir}/%{name}3/GtkLauncher

# only useful for testing, should not be installed system-wide.
# reported upstream as 22812 - AdamW 2008/12
rm -rf %{buildroot}%{_libdir}/libtestnetscapeplugin.*

%find_lang WebKitGTK-2.0
%find_lang WebKitGTK-3.0

%files -f WebKitGTK-2.0.lang

%files -n %{name}%{libver}
%dir %{_datadir}/webkitgtk-1.0
%{_datadir}/webkitgtk-1.0/images
%{_datadir}/webkitgtk-1.0/resources

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/webkit2gtk
%{_libdir}/lib%{name}gtk-%{libver}.so
%{_libdir}/libjavascriptcoregtk-%{libver}.so
%{_includedir}/%{name}gtk-%{libver}
%{_libdir}/pkgconfig/%{name}-%{libver}.pc
%{_libdir}/pkgconfig/javascriptcoregtk-%{libver}.pc
%{_datadir}/gir-1.0/JavaScriptCore-%{libver}.gir
%{_datadir}/gir-1.0/WebKit-%{libver}.gir

%files -n %{libname}
%{_libdir}/lib%{name}gtk-%{libver}.so.%{major}*

%files -n %{libjavascriptcoregtk}
%{_libdir}/libjavascriptcoregtk-%{libver}.so.%{major}*

%files -n %{libgitjscore}
%_libdir/girepository-1.0/JavaScriptCore-%{libver}.typelib

%files -n %{libgirname}
%_libdir/girepository-1.0/WebKit-%{libver}.typelib

%files gtklauncher
%{_libexecdir}/%{name}/GtkLauncher

%files jsc
%{_bindir}/jsc-1

#files -n %{inspectorname}
#{_datadir}/%{name}gtk-%{libver}/webinspector

%files -n %{name}3 -f WebKitGTK-3.0.lang

%files -n %{name}%{lib3ver}
%dir %{_datadir}/webkitgtk-3.0
%{_datadir}/webkitgtk-3.0/images
%{_datadir}/webkitgtk-3.0/resources

%files -n %{name}2gtk
%dir %{_libdir}/webkit2gtk-%{lib3ver}
%dir %{_libdir}/webkit2gtk-%{lib3ver}/injected-bundle
%{_libdir}/webkit2gtk-%{lib3ver}/injected-bundle/libwebkit2gtkinjectedbundle.so
%{_libexecdir}/WebKitNetworkProcess
%{_libexecdir}/WebKitPluginProcess
%{_libexecdir}/WebKitWebProcess

%files -n %{devname3}
%doc %{_datadir}/gtk-doc/html/webkitgtk
%doc %{_datadir}/gtk-doc/html/webkitdomgtk
%{_libdir}/lib%{name}gtk-%{lib3ver}.so
%{_libdir}/libjavascriptcoregtk-%{lib3ver}.so
%{_libdir}/libwebkit2gtk-%{lib3ver}.so
%{_includedir}/%{name}gtk-%{lib3ver}
%{_libdir}/pkgconfig/%{name}gtk-%{lib3ver}.pc
%{_libdir}/pkgconfig/javascriptcoregtk-%{lib3ver}.pc
%{_libdir}/pkgconfig/%{name}2gtk-%{lib3ver}.pc
%{_libdir}/pkgconfig/%{name}2gtk-web-extension-%{lib3ver}.pc
%{_datadir}/gir-1.0/JavaScriptCore-%{lib3ver}.gir
%{_datadir}/gir-1.0/WebKit-%{lib3ver}.gir
%{_datadir}/gir-1.0/WebKit2-%{lib3ver}.gir
%{_datadir}/gir-1.0/WebKit2WebExtension-%{lib3ver}.gir

%files -n %{lib3name}
%{_libdir}/lib%{name}gtk-%{lib3ver}.so.%{major3}*

%files -n %{libwebkit2}
%{_libdir}/lib%{name}2gtk-%{lib3ver}.so.%{major2}
%{_libdir}/lib%{name}2gtk-%{lib3ver}.so.%{major2}.*

%files -n %{libjavascriptcoregtk3}
%{_libdir}/libjavascriptcoregtk-%{lib3ver}.so.%{major}*

%files -n %{name}3-gtklauncher
%{_libexecdir}/%{name}3/GtkLauncher

%files -n %{name}3-jsc
%{_bindir}/jsc-3

%files -n %{libgitjscore3}
%{_libdir}/girepository-1.0/JavaScriptCore-%{lib3ver}.typelib

%files -n %{libgirname3}
%{_libdir}/girepository-1.0/WebKit-%{lib3ver}.typelib

%files -n %{libgirname2}
%{_libdir}/girepository-1.0/WebKit2-%{lib3ver}.typelib

%files -n %{libgirname2extension}
%{_libdir}/girepository-1.0/WebKit2WebExtension-%{lib3ver}.typelib
