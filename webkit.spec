%define major	0
%define rev	30005

%define name	webkit
%define qtn	%mklibname QtWebKit %major
%define qtdev	%mklibname QtWebKit -d
%define gtk	%mklibname WebKitGtk %major
%define gtkdev	%mklibname WebKitGtk -d

Summary:	Embeddable web component 
Name:		%{name}
Version:	0
Release:	%mkrel 0.%{rev}.1
License:	BSD-like
Group:		System/Libraries
Source0:	webkit-svn%{rev}.tar.lzma
URL:		http://www.webkit.org/
# (tpg) http://bugs.webkit.org/show_bug.cgi?id=14750
# this patch enables plugins support, hopefully it will be merged upstream quite soon
# please check if there is a newer version aof this gainst latest upstream svn revision
# if yes, update it then ;)
Patch0:		webkit-Implement-plugin-support-in-GTK-backend.patch
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
WebKit is an open source web browser engine.

%package -n %qtn
Summary:	Web browser engine
Group:		System/Libraries

%description -n %qtn
WebKit is an open source web browser engine.

%package -n %qtdev
Summary:	Development files for QtWebKit
Group:		Development/KDE and Qt
Provides:	QtWebKit-devel = %{version}-%{release}
Provides:	libQtWebKit-devel = %{version}-%{release}
Requires:	%{qtn} = %{version}-%{release}

%description -n %qtdev
Development files for QtWebKit

%package -n %gtk
Summary:	Gtk port of WebKit
Group:		System/Libraries
Obsoletes:	%mklibname WebKitGdk 0

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

%description -n %gtkdev
Development files for GtkWebKit

%prep
%setup -q -n %name
%patch0 -p0

%build

mkdir -p build-gtk
cd build-gtk

%{qt4bin}/qmake -r \
	OUTPUT_DIR="$PWD" \
	QMAKE_STRIP=/bin/true \
	QMAKE_RPATH= \
	QMAKE_CFLAGS="%optflags" \
	QMAKE_CXXFLAGS="%optflags" \
	VERSION=%major \
	CONFIG-=qt CONFIG+=gtk-port CONFIG+=plugins \
	WEBKIT_INC_DIR=%{_includedir}/WebKit \
	WEBKIT_LIB_DIR=%{_libdir} \
	../WebKit.pro

%make 

cd ..
 
mkdir -p build-qt
cd build-qt

%{qt4bin}/qmake -r \
	OUTPUT_DIR="$PWD" \
	QMAKE_STRIP=/bin/true \
	QMAKE_RPATH= \
	QMAKE_CFLAGS="%optflags" \
	QMAKE_CXXFLAGS="%optflags" \
	VERSION=%major \
	CONFIG+=qt-port CONFIG-=plugins \
	WEBKIT_INC_DIR=%{_includedir}/WebKit \
	WEBKIT_LIB_DIR=%{_libdir} \
	../WebKit.pro

%make
 
%install
rm -rf %{buildroot}

make -C build-gtk install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_libdir}/WebKit
install -m 755 build-gtk/WebKitTools/GtkLauncher/GtkLauncher %{buildroot}%{_libdir}/WebKit

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

%files -n %qtn
%defattr(644,root,root,755)
%{qt4lib}/libQtWebKit.so.*
%{qt4lib}/WebKit/QtLauncher
%{qt4lib}/WebKit/DumpRenderTree

%files -n %gtkdev
%defattr(644,root,root,755)
%{_libdir}/libWebKitGtk.so
%{_libdir}/libWebKitGtk.prl
%{_includedir}/WebKit
%{_libdir}/pkgconfig/WebKitGtk.pc

%files -n %gtk
%defattr(644,root,root,755)
%{_libdir}/libWebKitGtk.so.*
%{_libdir}/WebKit/GtkLauncher
