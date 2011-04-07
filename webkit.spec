#
# BEFORE UPDATING THIS PACKAGE, YOU _MUST_ DO THE FOLLOWING:
# - DO A LOCAL BUILD
# - INSTALL IT IN A TEST MACHINE
# - CHECK THAT 'display_help http://google.com' STILL WORK (INCLUDING CLOSING IT)
# - CHECK THAT MCC STILL RUNS
#

# lib is called libwebkitgtk-%{libver}.so.%{major}
%define libver  1.0 
%define major	2
%define rev	0

%if %rev
%define oname		WebKit
%else
%define oname		webkit
%endif
%define libname		%mklibname webkitgtk %{libver} %{major}
%define develname	%mklibname webkitgtk %{libver} -d
%define inspectorname	webkit%{libver}-webinspector

%define pango	0
%if %pango
%define fontreq		pango-devel
%define fontback	pango
%else
%define fontreq		fontconfig-devel >= 1.0.0
%define fontback	freetype
%endif

%if %mandriva_branch == Cooker
# Cooker
%define rel 3
%else
# Old distros
%define subrel 1
%define rel 0
%endif

Summary:	Web browser engine
Epoch:		1
Name:		webkit
Version:	1.2.7
%if %rev
Release:	%mkrel -c %rev %rel
%else
Release:	%mkrel %rel
%endif
License:	BSD and LGPLv2+
Group:		System/Libraries
# Use the nightlies, don't grab SVN directly: the nightlies are
# MASSIVELY smaller and easier to manage - AdamW 2008/04
%if %rev
Source0:	http://nightly.webkit.org/files/trunk/src/%{oname}-r%{rev}.tar.bz2
%else
Source0:	http://www.webkitgtk.org/%{oname}-%{version}.tar.gz
%endif
Patch0: webkit-1.1.21-fix-linking.patch
Patch1: webkit-gtk-1.2.5-tests-build.patch
# (blino) needed for first-time wizard (display_help) to be able to close its window with javascript
Patch2: webkit-1.2.3-allowScriptsToCloseWindows.patch
Patch3: webkit-1.2.3-gir-1.2.patch
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
BuildRequires:	gtk2-devel
BuildRequires:	sqlite3-devel
BuildRequires:	xft2-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	gobject-introspection-devel
%if %mdvver <= 201020
#gw for Soup-2.4.gir
BuildRequires:	gir-repository
%endif
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

%prep
%if %rev
%setup -q -n %{oname}-r%{rev}
%else
%setup -q 
%endif
%patch0 -p1 -b .link
%patch1 -p1 -b .check
%patch2 -p1 -b .allowScriptsToCloseWindows
%if %mdvver >= 201100
%patch3 -p0 -b .gir
%endif
%if %rev
./autogen.sh
%endif
automake

%build
%configure2_5x	\
	--with-font-backend=%{fontback} \
	--enable-video --enable-introspection

%make

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 755 Programs/GtkLauncher %{buildroot}%{_libdir}/%{name}

# only useful for testing, should not be installed system-wide.
# reported upstream as 22812 - AdamW 2008/12
rm -rf %{buildroot}%{_libdir}/libtestnetscapeplugin.*

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun	-n %{libname} -p /sbin/ldconfig
%endif

%files -f %{name}.lang

%files -n %{name}%{libver}
%{_datadir}/webkit-1.0/resources
%{_datadir}/webkit-1.0/images

%files -n %{develname}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}-%{libver}.so
%{_libdir}/lib%{name}-%{libver}.la
%{_includedir}/%{name}-%{libver}
%{_libdir}/pkgconfig/%{name}-%{libver}.pc
%_datadir/gir-1.0/JSCore-%{libver}.gir
%_datadir/gir-1.0/WebKit-%{libver}.gir

%files -n %{libname}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}-%{libver}.so.%{major}*
%_libdir/girepository-1.0/JSCore-%{libver}.typelib
%_libdir/girepository-1.0/WebKit-%{libver}.typelib

%files gtklauncher
%defattr(0755,root,root)
%{_libdir}/%{name}/GtkLauncher

%files jsc
%defattr(0755,root,root)
%{_bindir}/jsc

%files -n %{inspectorname}
%defattr(0755,root,root)
%{_datadir}/%{name}-%{libver}/webinspector

