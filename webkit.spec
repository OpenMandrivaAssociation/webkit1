%define major	0
%define rev	25144

%define name	webkit
%define qtn	%mklibname QtWebKit %major
%define qtdev	%mklibname QtWebKit -d
%define gdk	%mklibname WebKitGdk %major
%define gdkdev	%mklibname WebKitGdk -d

Summary:	WebKit embeddable web component 
Name:		%name
Version:	0
Release:	%mkrel 0.%{rev}.1
License:	BSD-like
Group:		X11/Libraries
Source0:	webkit-svn%{rev}.tar.gz
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
# For qmake
BuildRequires:	qt4-devel
BuildRequires:	sqlite3-devel
BuildRequires:	xft2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root

%description
WebKit is an open source web browser engine.

%package -n %qtn
Summary:	Open source web browser engine
Group:		System/Libraries

%description -n %qtn
WebKit is an open source web browser engine.

%package -n %qtdev
Summary:	Development files for QtWebKit
Group:		Development/KDE and Qt
Requires:	%{qtn} = %{version}-%{release}

%description -n %qtdev
Development files for QtWebKit

%package -n %gdk
Summary:	Gdk port of WebKit
Group:		System/Libraries

%description -n %gdk
The Gdk port of WebKit is intended to provide a browser component primarily for
users of the portable Gtk+ UI toolkit on platforms like Linux.

%package -n %gdkdev
Summary:	Development files for GdkWebKit
Group:		Development/GNOME and GTK+
Requires:	%{gdk} = %{version}-%{release}
Requires:	curl-devel >= 7.11.0
Requires:	fontconfig-devel >= 1.0.0
Requires:	librsvg-devel >= 2.2.0
Requires:	libstdc++-devel
Requires:	xft2-devel >= 2.0.0

%description -n %gdkdev
Development files for GdkWebKit

%prep
%setup -q -n %name

%build

mkdir -p build-gdk
cd build-gdk

%{qt4bin}/qmake -r \
	OUTPUT_DIR="$PWD" \
	QMAKE_STRIP=/bin/true \
	QMAKE_RPATH= \
	QMAKE_CFLAGS="%optflags" \
	QMAKE_CXXFLAGS="%optflags" \
	VERSION=%major \
	CONFIG-=qt CONFIG+=gdk-port \
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
	CONFIG+=qt-port \
	WEBKIT_INC_DIR=%{_includedir}/WebKit \
	WEBKIT_LIB_DIR=%{_libdir} \
	../WebKit.pro

%make
 
%install
rm -rf $RPM_BUILD_ROOT

make -C build-gdk install INSTALL_ROOT=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/WebKit
install -m 755 build-gdk/WebKitTools/GdkLauncher/GdkLauncher $RPM_BUILD_ROOT%{_libdir}/WebKit

make -C build-qt install INSTALL_ROOT=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{qt4lib}/WebKit
install -m 755 build-qt/bin/QtLauncher $RPM_BUILD_ROOT%{qt4lib}/WebKit
install -m 755 build-qt/WebKitTools/DumpRenderTree/DumpRenderTree.qtproj/DumpRenderTree $RPM_BUILD_ROOT%{qt4lib}/WebKit
#FIXME find how to tell qmake to put it there
mv $RPM_BUILD_ROOT%{qt4lib}/pkgconfig/QtWebKit.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/QtWebKit.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %qtn -p /sbin/ldconfig
%postun	-n %qtn -p /sbin/ldconfig

%post -n %gdk -p /sbin/ldconfig
%postun	-n %gdk -p /sbin/ldconfig

%files -n %qtdev
%defattr(644,root,root,755)
%{qt4lib}/libQtWebKit.so
%{qt4lib}/libQtWebKit.prl
%{qt4include}/*
%{qt4dir}/mkspecs/features
%{_libdir}/pkgconfig/QtWebKit.pc

%files -n %qtn
%defattr(644,root,root,755)
%{qt4lib}/libQtWebKit.so.*
%{qt4lib}/WebKit/QtLauncher
%{qt4lib}/WebKit/DumpRenderTree

%files -n %gdkdev
%defattr(644,root,root,755)
%{_libdir}/libWebKitGdk.so
%{_libdir}/libWebKitGdk.prl
%{_includedir}/WebKit
%{_libdir}/pkgconfig/WebKitGdk.pc

%files -n %gdk
%defattr(644,root,root,755)
%{_libdir}/libWebKitGdk.so.*
%{_libdir}/WebKit/GdkLauncher
