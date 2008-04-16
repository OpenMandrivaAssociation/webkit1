%define gtkmajor	1
%define qtmajor		4

%define rev	31893

%define name	webkit
%define oname	WebKit
%define qtn	%mklibname QtWebKit %qtmajor
%define qtdev	%mklibname QtWebKit -d
%define gtk	%mklibname WebKitGtk %gtkmajor
%define gtkdev	%mklibname WebKitGtk -d

# libnspr-devel doesn't provide this, so except it and do it manually
# lower down - AdamW 2008/04
%define _requires_exceptions devel(libnspr4)

Summary:	Embeddable web component 
Name:		%{name}
Version:	0
Release:	%mkrel 0.%{rev}.2
License:	BSD-like
Group:		System/Libraries
Source0:	http://nightly.webkit.org/files/trunk/src/%{oname}-r%{rev}.tar.bz2
# From https://bugs.webkit.org/show_bug.cgi?id=14750 , rediffed:
# enables plugin support for webkitgtk - AdamW 2008/04
Patch0:		webkit-31326-plugin.patch
URL:		http://www.webkit.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	curl-devel >= 7.11.0
BuildRequires:	flex
BuildRequires:	fontconfig-devel >= 1.0.0
BuildRequires:	gperf
BuildRequires:	libicu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool 
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	gtk2-devel
BuildRequires:	qt4-devel
BuildRequires:	qtxmllib
BuildRequires:	qtnetworklib
BuildRequires:	sqlite3-devel
BuildRequires:	xft2-devel
BuildRequires:	libnspr-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
WebKit is an open source web browser engine.

%package -n %qtn
Summary:	Web browser engine
Group:		System/Libraries
Obsoletes:	%{mklibname QtWebKit 0} <= 0-0.30465
Conflicts:	%{qtdev} <= 0-0.30465

%description -n %qtn
WebKit is an open source web browser engine.

%package -n %qtdev
Summary:	Development files for QtWebKit
Group:		Development/KDE and Qt
Provides:	QtWebKit-devel = %{version}-%{release}
Provides:	libQtWebKit-devel = %{version}-%{release}
Requires:	%{qtn} = %{version}-%{release}
Conflicts:	%{qtn} <= 0-0.30465

%description -n %qtdev
Development files for QtWebKit

%package -n %gtk
Summary:	Gtk port of WebKit
Group:		System/Libraries
Obsoletes:	%{mklibname WebKitGdk 0} <= 0-0.30465
Obsoletes:	%{mklibname WebKitGtk 0} <= 0-0.30465

%description -n %gtk
The Gtk port of WebKit is intended to provide a browser component primarily for
users of the portable Gtk+ UI toolkit on platforms like Linux.

%package -n %gtkdev
Summary:	Development files for WebKitGtk
Group:		Development/GNOME and GTK+
Provides:	WebKitGtk-devel = %{version}-%{release}
Provides:	libWebKitGtk-devel = %{version}-%{release}
Requires:	%{gtk} = %{version}-%{release}
Requires:	curl-devel >= 7.11.0
Requires:	fontconfig-devel >= 1.0.0
Requires:	librsvg-devel >= 2.2.0
Requires:	libstdc++-devel
Requires:	xft2-devel >= 2.0.0
Requires:	libnspr-devel

%description -n %gtkdev
Development files for GtkWebKit

%package gtklauncher
Summary:	GtkWebKit example application
Group:		Development/GNOME and GTK+
Conflicts:	%mklibname WebKitGtk 0 <= 0-0.30465

%description gtklauncher
GtkLauncher is an example application for WebKitGtk.

%package qtlauncher
Summary:	GtkWebKit example application
Group:		Development/KDE and Qt
Conflicts:	%mklibname QtWebKit 0 <= 0-0.30465

%description qtlauncher
QtLauncher is an example application for QtWebKit.

%prep
%setup -q -n %{oname}-r%{rev}
%patch0 -p0 -b .plugin

%build
mkdir -p build-gtk
pushd build-gtk
../autogen.sh
CONFIGURE_TOP=../ %configure2_5x --enable-svg --enable-svg-foreign-object --enable-svg-use-element --enable-svg-fonts --enable-svg-as-image --enable-icon-database
%make
popd

mkdir -p build-qt
cd build-qt

%{qt4bin}/qmake -r \
	OUTPUT_DIR="$PWD" \
	QMAKE_STRIP=/bin/true \
	QMAKE_RPATH= \
	QMAKE_CFLAGS="%{optflags}" \
	QMAKE_CXXFLAGS="%{optflags}" \
	VERSION=%qtmajor \
	CONFIG+=qt-port CONFIG-=plugins \
	WEBKIT_INC_DIR=%{_includedir}/WebKit \
	WEBKIT_LIB_DIR=%{_libdir} \
	../WebKit.pro

%make
 
%install
rm -rf %{buildroot}
pushd build-gtk
%makeinstall_std
popd
mkdir -p %{buildroot}%{_libdir}/WebKit
install -m 755 build-gtk/Programs/GtkLauncher %{buildroot}%{_libdir}/WebKit

make -C build-qt install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{qt4lib}/WebKit
install -m 755 build-qt/bin/QtLauncher %{buildroot}%{qt4lib}/WebKit
install -m 755 build-qt/bin/DumpRenderTree %{buildroot}%{qt4lib}/WebKit
#FIXME find how to tell qmake to put it there
mv %{buildroot}%{qt4lib}/pkgconfig/QtWebKit.pc %{buildroot}%{_libdir}/pkgconfig/QtWebKit.pc

%clean
rm -rf %{buildroot}

%post -n %qtn -p /sbin/ldconfig
%postun	-n %qtn -p /sbin/ldconfig

%post -n %gtk -p /sbin/ldconfig
%postun	-n %gtk -p /sbin/ldconfig

%files -n %qtdev
%defattr(644,root,root,755)
%{qt4lib}/libQtWebKit.so
%{qt4lib}/libQtWebKit.prl
%{qt4include}/*
%{qt4dir}/mkspecs/features
%{qt4plugins}/imageformats/libqtwebico.so
%{_libdir}/pkgconfig/QtWebKit.pc
%{qt4lib}/WebKit/DumpRenderTree

%files -n %qtn
%defattr(644,root,root,755)
%{qt4lib}/libQtWebKit.so.%{qtmajor}*

%files qtlauncher
%defattr(0755,root,root)
%{qt4lib}/WebKit/QtLauncher

%files -n %gtkdev
%defattr(644,root,root,755)
%{_libdir}/lib%{name}-1.0.so
%{_libdir}/lib%{name}-1.0.la
%{_includedir}/%{name}-1.0
%{_libdir}/pkgconfig/%{name}-1.0.pc

%files -n %gtk
%defattr(644,root,root,755)
%{_libdir}/lib%{name}-1.0.so.%{gtkmajor}*

%files gtklauncher
%defattr(0755,root,root)
%{_libdir}/WebKit/GtkLauncher

