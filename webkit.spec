%define major	1
%define rev	32877

%define oname		WebKit
%define libname		%mklibname webkitgtk %major
%define develname	%mklibname webkitgtk -d

Summary:	Web browser engine
Name:		webkit
Version:	0
Release:	%mkrel 0.%{rev}.1
License:	BSD-like
Group:		System/Libraries
# Use the nightlies, don't grab SVN directly: the nightlies are
# MASSIVELY smaller and easier to manage - AdamW 2008/04
Source0:	http://nightly.webkit.org/files/trunk/src/%{oname}-r%{rev}.tar.bz2
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
BuildRequires:	sqlite3-devel
BuildRequires:	xft2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
WebKit is an open source web browser engine.

%package -n %{libname}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Obsoletes:	%{mklibname WebKitGdk 0} <= 0-0.30465
Obsoletes:	%{mklibname WebKitGtk 0} <= 0-0.32877

%description -n %{libname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n %{develname}
Summary:	Development files for WebKit GTK+ port
Group:		Development/GNOME and GTK+
Provides:	webkitgtk-devel = %{version}-%{release}
Provides:	libwebkitgtk-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	curl-devel >= 7.11.0
Requires:	fontconfig-devel >= 1.0.0
Requires:	librsvg-devel >= 2.2.0
Requires:	libstdc++-devel
Requires:	xft2-devel >= 2.0.0
Requires:	libnspr-devel
Obsoletes:	%{mklibname WebKitGtk -d} <= 0-0.32877

%description -n %{develname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux. This package contains development headers.

%package gtklauncher
Summary:	GtkWebKit example application
Group:		Development/GNOME and GTK+
Conflicts:	%mklibname WebKitGtk 0 <= 0-0.30465

%description gtklauncher
GtkLauncher is an example application for WebKit GTK+.

%prep
%setup -q -n %{oname}-r%{rev}

%build
./autogen.sh
%configure2_5x --enable-svg-experimental
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 755 Programs/GtkLauncher %{buildroot}%{_libdir}/%{name}

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun	-n %{libname} -p /sbin/ldconfig

%files -n %{develname}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}-1.0.so
%{_libdir}/lib%{name}-1.0.la
%{_includedir}/%{name}-1.0
%{_libdir}/pkgconfig/%{name}-1.0.pc

%files -n %{libname}
%defattr(644,root,root,755)
%{_libdir}/lib%{name}-1.0.so.%{major}*

%files gtklauncher
%defattr(0755,root,root)
%{_libdir}/%{name}/GtkLauncher

