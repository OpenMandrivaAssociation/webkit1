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

Summary:	Web browser engine
Name:		webkit
Version:	1.1.1
%if %rev
Release:	%mkrel 0.%{rev}.1
%else
Release:	%mkrel 3
%endif
License:	BSD and LGPLv2+
Group:		System/Libraries
# Use the nightlies, don't grab SVN directly: the nightlies are
# MASSIVELY smaller and easier to manage - AdamW 2008/04
%if %rev
Source0:	http://nightly.webkit.org/files/trunk/src/%{oname}-r%{rev}.tar.bz2
%else
Source0:	http://cafe.minaslivre.org/webkit/%{oname}-%{version}.tar.gz
%endif
URL:		http://www.webkit.org/
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
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	gtk2-devel
BuildRequires:	sqlite3-devel
BuildRequires:	xft2-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	gnome-keyring-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
WebKit is an open source web browser engine.

%package -n %{libname}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Obsoletes:	%{mklibname WebKitGdk 0} <= 0-0.30465
Obsoletes:	%{mklibname WebKitGtk 1} <= 0-0.32877
Obsoletes:	%{mklibname webkitgtk 1} <= 1.1.1-3mdv
Obsoletes:	%{mklibname webkitgtk 2} <= 1.1.1-3mdv
# (fhimpe) This provides should probably be removed when major changes
Provides:	%{mklibname webkitgtk 2} = %{version}-%{release}
Provides:	libwebkitgtk = %{version}-%{release}
# Needed for Web Inspector feature to work
Suggests:	%{inspectorname}

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
Requires:	%{libname} = %{version}-%{release}
Requires:	curl-devel >= 7.11.0
Requires:	fontconfig-devel >= 1.0.0
Requires:	librsvg-devel >= 2.2.0
Requires:	libstdc++-devel
Requires:	xft2-devel >= 2.0.0
Obsoletes:	%{mklibname WebKitGtk -d} <= 0-0.32877
Obsoletes:	%{mklibname webkitgtk -d} < 1.1.1-2mdv

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

%build
%if %rev
./autogen.sh
%endif
%configure2_5x	--enable-svg-experimental \
              	--with-font-backend=%{fontback} \
		--enable-video \
%ifarch %ix86
		--enable-jit \
%endif
		--enable-gnomekeyring \

%make

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 755 Programs/GtkLauncher %{buildroot}%{_libdir}/%{name}

# only useful for testing, should not be installed system-wide.
# reported upstream as 22812 - AdamW 2008/12
rm -rf %{buildroot}%{_libdir}/libtestnetscapeplugin.*

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun	-n %{libname} -p /sbin/ldconfig
%endif

%files -n %{develname}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}-%{libver}.so
%{_libdir}/lib%{name}-%{libver}.la
%{_includedir}/%{name}-%{libver}
%{_libdir}/pkgconfig/%{name}-%{libver}.pc

%files -n %{libname}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}-%{libver}.so.%{major}*

%files gtklauncher
%defattr(0755,root,root)
%{_libdir}/%{name}/GtkLauncher

%files jsc
%defattr(0755,root,root)
%{_bindir}/jsc

%files -n %{inspectorname}
%defattr(0644,root,root)
%{_datadir}/%{name}-%{libver}/webinspector

