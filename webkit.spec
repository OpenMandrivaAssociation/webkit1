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

%define lib3ver  3.0
%define major3   0
%define lib3name	%mklibname webkitgtk %{lib3ver} %{major3}
%define develname3	%mklibname webkitgtk %{lib3ver} -d
%define inspector3name	webkit%{lib3ver}-webinspector

%define pango	0
%if %pango
%define fontreq		pango-devel
%define fontback	pango
%else
%define fontreq		fontconfig-devel >= 1.0.0
%define fontback	freetype
%endif

%define rel 7

Summary:	Web browser engine
Epoch:		1
Name:		webkit
Version:	1.4.1
Release:	%mkrel %rel
License:	BSD and LGPLv2+
Group:		System/Libraries
Source0:	http://www.webkitgtk.org/%{oname}-%{version}.tar.gz
Patch0:		webkit-1.3.13-link.patch
# (blino) needed for first-time wizard (display_help) to be able to close its window with javascript
Patch2: webkit-1.4.1-allowScriptsToCloseWindows.patch
URL:		http://www.webkitgtk.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	curl-devel >= 7.11.0
BuildRequires:	flex
BuildRequires:	%{fontreq}
BuildRequires:	gperf
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libsoup-devel >= 2.29.90
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	libxt-devel
BuildRequires:	pkgconfig
BuildRequires:	gtk+2-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libgail-3.0-devel
BuildRequires:	sqlite3-devel
BuildRequires:	xft2-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	enchant-devel
BuildRequires:	gail-devel
Requires:	%{libname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
WebKit is an open source web browser engine.

%package -n %{name}%{libver}
Summary:        GTK+ port of WebKit web browser engine - shared files
Group:          Development/GNOME and GTK+
Requires:	%{libname}
Conflicts:	%{libname} < 1:1.4.1-5
Conflicts:	%{name} < 1:1.4.1-6
Conflicts:	%{_lib}webkitgtk1.0_2 < 1:1.4.1

%description -n %{name}%{libver}
WebKit is an open source web browser engine.
This package contains the shared files used by %{name}%{libver}

%package -n %{libname}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Requires:	%{name}
Requires:	%{name}%{libver}
Obsoletes:	%{mklibname WebKitGdk 0} <= 0-0.30465
Obsoletes:	%{mklibname WebKitGtk 1} <= 0-0.32877
Obsoletes:	%{mklibname webkitgtk 1} <= 1.1.1-3mdv
Obsoletes:	%{mklibname webkitgtk 2} <= 1.1.1-3mdv
# (fhimpe) This provides should probably be removed when major changes
Provides:	%{mklibname webkitgtk 2} = %{version}-%{release}
Provides:	libwebkitgtk = %{version}-%{release}
# Needed for Web Inspector feature to work
Suggests:	%{inspectorname}
Conflicts:	gir-repository < 0.6.5-7mdv2010.1

%description -n %{libname}
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
Requires:	curl-devel >= 7.11.0
Requires:	fontconfig-devel >= 1.0.0
Requires:	librsvg-devel >= 2.2.0
Requires:	libstdc++-devel
Requires:	xft2-devel >= 2.0.0
Obsoletes:	%{mklibname WebKitGtk -d} <= 0-0.32877
Obsoletes:	%{mklibname webkitgtk -d} < 1.1.1-2mdv
Conflicts:	gir-repository < 0.6.5-7mdv2010.1

%description -n %{develname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package gtklauncher
Summary:	WebKit GTK+ example application
Group:		Development/GNOME and GTK+
Conflicts:	%mklibname WebKitGtk 0 <= 0-0.30465

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
Requires:       %{lib3name}

%description -n %{name}3
WebKit is an open source web browser engine.

%package -n %{name}%{lib3ver}
Summary:        GTK+3 port of WebKit web browser engine - shared files
Group:          Development/GNOME and GTK+
Requires:       %{lib3name}
Conflicts:	%{lib3name} < 1:1.4.1-5
Conflicts:	%{name} < 1:1.4.1-6

%description -n %{name}%{lib3ver}
WebKit is an open source web browser engine.
This package contains the shared files used by %{name}%{lib3ver}

%package -n %{lib3name}
Summary:        GTK+3 port of WebKit web browser engine
Group:          System/Libraries
Requires:       %{name}3
Requires:       %{name}%{lib3ver}
Provides:       libwebkitgtk3 = %{version}-%{release}
# Needed for Web Inspector feature to work
Suggests:       %{inspector3name}

%description -n %{lib3name}
The GTK+3 port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+3 UI toolkit on platforms like
Linux.

%package -n %{develname3}
Summary:        Development files for WebKit GTK+3 port
Group:          Development/GNOME and GTK+
Provides:       webkitgtk3-devel = %{version}-%{release}
Provides:       libwebkitgtk3-devel = %{version}-%{release}
Requires:       %{lib3name} = %{epoch}:%{version}-%{release}

%description -n %{develname3}
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

%prep
%setup -q
%patch0 -p0 -b.link
%patch2 -p1 -b .allowScriptsToCloseWindows

%build
mkdir -p gtk2
pushd gtk2
CONFIGURE_TOP=.. %configure2_5x	--with-gtk=2.0 \
	--with-font-backend=%{fontback} \
	--enable-video --enable-introspection
%make
popd

mkdir -p gtk3
pushd gtk3
CONFIGURE_TOP=.. %configure2_5x  --with-gtk=3.0 \
	--with-font-backend=%{fontback} \
	--enable-video --enable-introspection
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

%clean
rm -rf %{buildroot}

%files -f %{name}-2.0.lang

%files -n %{name}%{libver}
%{_datadir}/glib-2.0/schemas/org.webkitgtk-1.0.gschema.xml
%dir %{_datadir}/webkitgtk-1.0
%{_datadir}/webkitgtk-1.0/images
%{_datadir}/webkit-1.0/resources
%_libdir/girepository-1.0/JSCore-%{libver}.typelib
%_libdir/girepository-1.0/WebKit-%{libver}.typelib

%files -n %{develname}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}gtk-%{libver}.so
%{_libdir}/lib%{name}gtk-%{libver}.la
%{_includedir}/%{name}-%{libver}
%{_libdir}/pkgconfig/%{name}-%{libver}.pc
%_datadir/gir-1.0/JSCore-%{libver}.gir
%_datadir/gir-1.0/WebKit-%{libver}.gir

%files -n %{libname}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}gtk-%{libver}.so.%{major}*

%files gtklauncher
%defattr(0755,root,root)
%{_libdir}/%{name}/GtkLauncher

%files jsc
%defattr(0755,root,root)
%{_bindir}/jsc-1

%files -n %{inspectorname}
%defattr(0755,root,root)
%{_datadir}/%{name}gtk-%{libver}/webinspector

%files -n %{name}3 -f %{name}-3.0.lang

%files -n %{name}%{lib3ver}
%{_datadir}/glib-2.0/schemas/org.webkitgtk-3.0.gschema.xml
%dir %{_datadir}/webkitgtk-3.0
%{_datadir}/webkitgtk-3.0/images
%{_datadir}/webkit-3.0/resources
%_libdir/girepository-1.0/JSCore-%{lib3ver}.typelib
%_libdir/girepository-1.0/WebKit-%{lib3ver}.typelib

%files -n %{develname3}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}gtk-%{lib3ver}.so
%{_libdir}/lib%{name}gtk-%{lib3ver}.la
%{_includedir}/%{name}-%{lib3ver}
%{_libdir}/pkgconfig/%{name}gtk-%{lib3ver}.pc
%_datadir/gir-1.0/JSCore-%{lib3ver}.gir
%_datadir/gir-1.0/WebKit-%{lib3ver}.gir

%files -n %{lib3name}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}gtk-%{lib3ver}.so.%{major3}*

%files -n %{name}3-gtklauncher
%defattr(0755,root,root)
%{_libdir}/%{name}3/GtkLauncher

%files -n %{name}3-jsc
%defattr(0755,root,root)
%{_bindir}/jsc-3

%files -n %{inspector3name}
%defattr(0755,root,root)
%{_datadir}/%{name}gtk-%{lib3ver}/webinspector
