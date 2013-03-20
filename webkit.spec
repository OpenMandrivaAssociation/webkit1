#
# BEFORE UPDATING THIS PACKAGE, YOU _MUST_ DO THE FOLLOWING:
# - DO A LOCAL BUILD
# - INSTALL IT IN A TEST MACHINE
# - CHECK THAT 'display_help http://google.com' STILL WORK (INCLUDING CLOSING IT)
# - CHECK THAT MCC STILL RUNS
#
%define debug_package %{nil}
# *** ERROR: same build ID in nonidentical files!
#        /usr/bin/jsc-3
#   and  /usr/bin/jsc-1


# lib is called libwebkitgtk-%{libver}.so.%{major}
%define libver  1.0
%define major   0
%define oname		webkitgtk
%define libname		%mklibname webkitgtk %{libver} %{major}
%define devname	%mklibname webkitgtk %{libver} -d
%define inspectorname	webkit%{libver}-webinspector
%define girname		%mklibname %{name}-gir %{libver}
%define girjscore	%mklibname jscore-gir %{libver}
%define libjavascriptcoregtk	%mklibname javascriptcoregtk %{libver} %{major}

%define lib3ver  3.0
%define major3   0
%define lib3name	%mklibname webkitgtk %{lib3ver} %{major3}
%define devname3	%mklibname webkitgtk %{lib3ver} -d
%define inspector3name	webkit%{lib3ver}-webinspector
%define girname3	%mklibname %{name}-gir %{lib3ver}
%define girjscore3	%mklibname jscore-gir %{lib3ver}
%define libjavascriptcoregtk3	%mklibname javascriptcoregtk %{lib3ver} %{major3}

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
Version:	1.10.2
Release:	1
License:	BSD and LGPLv2+
Group:		System/Libraries
Url:		http://www.webkitgtk.org
Source0:	http://www.webkitgtk.org/releases/%{oname}-%{version}.tar.xz
# (blino) needed for first-time wizard (display_help) to be able to close its window with javascript
Patch0:		webkit-1.10.2-link.patch
Patch1:		webkit-1.6.1-allowScriptsToCloseWindows.patch
Patch2:		webkit-1.7.90-fix-documentation-build.patch
# suse patches
Patch3:		webkit-gir-fixup.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gperf
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	%{fontreq}
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
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
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
Requires:	%{libname} = %{EVRD}
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
# Needed for Web Inspector feature to work
Requires:	%{inspectorname}

%description -n %{libname}
The GTK+ port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+ UI toolkit on platforms like
Linux.

%package -n %{libjavascriptcoregtk}
Summary:	GTK+ port of WebKit web browser engine
Group:		System/Libraries
Obsoletes:	%{_lib}javascriptcoregtk1.0 < %{EVRD}

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
Requires:	%{libname} = %{EVRD}
Requires:	%{libjavascriptcoregtk} = %{EVRD}
Requires:	%{girjscore} = %{EVRD}
Requires:	%{girname} = %{EVRD}

%description -n %{devname}
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
Requires:	%{lib3name} = %{EVRD}
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
Obsoletes:	%{_lib}javascriptcoregtk3.0 < %{EVRD}

%description -n %{libjavascriptcoregtk3}
The GTK+3 port of WebKit is intended to provide a browser component
primarily for users of the portable GTK+3 UI toolkit on platforms like
Linux.

%package -n %{devname3}
Summary:	Development files for WebKit GTK+3 port
Group:		Development/GNOME and GTK+
Provides:	webkitgtk3-devel = %{version}-%{release}
Provides:	libwebkitgtk3-devel = %{version}-%{release}
Requires:	%{lib3name} = %{EVRD}
Requires:	%{libjavascriptcoregtk3} = %{EVRD}
Requires:	%{girjscore3} = %{EVRD}
Requires:	%{girname3} = %{EVRD}

%description -n %{devname3}
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
Conflicts:	%{_lib}webkitgtk1.0_2 < %{EVRD}

%description -n %{girjscore}
GObject Introspection interface description for JSCore.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}webkitgtk1.0_2 < %{EVRD}

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
%setup -qn %{oname}-%{version}
%apply_patches
# Don't force -O2
sed -i 's/-O2//g' configure.ac

%build
# Use linker flags to reduce memory consumption on low-mem architectures
%ifarch %{arm}
%define lowmemflags -Wl,--no-keep-memory -Wl,--reduce-memory-overheads
export CFLAGS="`echo %{optflags} %lowmemflags | sed -e 's/-gdwarf-4//' -e 's/-fvar-tracking-assignments//' -e 's/-frecord-gcc-switches//'`"
mkdir -p bfd
ln -s %{_bindir}/ld.bfd bfd/ld
export PATH=$PWD/bfd:$PATH
%global ldflags %{ldflags} -fuse-ld=bfd
%else
export CFLAGS="`echo %{optflags} | sed -e 's/-gdwarf-4//' -e 's/-fvar-tracking-assignments//' -e 's/-frecord-gcc-switches//'`"
%endif
export CXXFLAGS="$CFLAGS"

mkdir -p ../gtk2 ../gtk3
cp -a ./* ../gtk2/
mv ../gtk2 ../gtk3 .
cp -a gtk2/* gtk3/
pushd gtk2
%configure2_5x \
	--enable-dependency-tracking \
	--with-gtk=2.0 \
	--with-gstreamer=0.10 \
	--disable-webkit2 \
	--with-font-backend=%{fontback} \
	--enable-jit \
	--enable-video \
	--enable-introspection

make V=1 -j4
popd

pushd gtk3
%configure2_5x \
	--enable-dependency-tracking \
	--with-gtk=3.0 \
	--with-gstreamer=1.0 \
	--disable-webkit2 \
	--with-font-backend=%{fontback} \
	--enable-jit \
	--enable-video \
	--enable-introspection

make V=1 -j4
popd

%install
%makeinstall_std -C gtk2
%makeinstall_std -C gtk3
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 755 gtk2/Programs/GtkLauncher %{buildroot}%{_libdir}/%{name}

mkdir -p %{buildroot}%{_libdir}/%{name}3
install -m 755 gtk3/Programs/GtkLauncher %{buildroot}%{_libdir}/%{name}3

# only useful for testing, should not be installed system-wide.
# reported upstream as 22812 - AdamW 2008/12
rm -rf %{buildroot}%{_libdir}/libtestnetscapeplugin.*

%find_lang %{oname}-2.0
%find_lang %{oname}-3.0

%files -n %{name}%{libver} -f %{oname}-2.0.lang
%dir %{_datadir}/webkitgtk-1.0
%{_datadir}/webkitgtk-1.0/images
%{_datadir}/webkitgtk-1.0/resources

%files -n %{devname}
%{_libdir}/lib%{name}gtk-%{libver}.so
%{_libdir}/libjavascriptcoregtk-%{libver}.so
%{_includedir}/%{name}gtk-%{libver}
%{_libdir}/pkgconfig/%{name}-%{libver}.pc
%{_libdir}/pkgconfig/javascriptcoregtk-%{libver}.pc
%{_datadir}/gir-1.0/JSCore-%{libver}.gir
%{_datadir}/gir-1.0/WebKit-%{libver}.gir
%{_datadir}/gtk-doc/html/webkitgtk/*

%files -n %{libname}
%{_libdir}/lib%{name}gtk-%{libver}.so.%{major}*

%files -n %{libjavascriptcoregtk}
%{_libdir}/libjavascriptcoregtk-%{libver}.so.%{major}*

%files -n %{girjscore}
%{_libdir}/girepository-1.0/JSCore-%{libver}.typelib

%files -n %{girname}
%{_libdir}/girepository-1.0/WebKit-%{libver}.typelib

%files gtklauncher
%{_libdir}/%{name}/GtkLauncher

%files jsc
%{_bindir}/jsc-1

%files -n %{inspectorname}
%{_datadir}/%{name}gtk-%{libver}/webinspector

%files -n %{name}%{lib3ver} -f %{oname}-3.0.lang
%dir %{_datadir}/webkitgtk-3.0
%{_datadir}/webkitgtk-3.0/images
%{_datadir}/webkitgtk-3.0/resources

%files -n %{devname3}
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
%{_libdir}/girepository-1.0/JSCore-%{lib3ver}.typelib

%files -n %{girname3}
%{_libdir}/girepository-1.0/WebKit-%{lib3ver}.typelib

%changelog
* Fri Apr 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 1:1.8.1-1
+ Revision: 794110
- new version 1.8.1
- cleaned up spec

  + Bernhard Rosenkraenzer <bero@bero.eu>
    - Rebuild for icu 49.1

  + Lev Givon <lev@mandriva.org>
    - Update to 1.6.3.

* Mon Nov 21 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:1.6.1-1
+ Revision: 732103
-fixed devel & devel3 file lists
- fixed resources dirs
- added missing packages and descriptions
- added p2 to fix build error with glib2.0 gt 2.31.0
- split out gir pkgs
- merged lang pkgs into name-libver pkgs
- more clean ups
- new version 1.6.1
- rediff p0 & p1
- switched to apply_patches
- converted BRs to pkgconfig provides
- rebuild without .la files
- removed defattr
- removed clean section
- removed reqs for devel pkgs in devel pkg
- cleaned up spec
- removed mkrel & BuildRoot
- removed subrel
- removed old obsoletes & conflicts

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.4.2-1.1
+ Revision: 702857
- attempt to relink against libpng15.so.15

* Thu Sep 29 2011 Alexander Barakin <abarakin@mandriva.org> 1:1.4.2-0.1
+ Revision: 701912
- imported package webkit

* Sun Jun 26 2011 Funda Wang <fwang@mandriva.org> 1:1.4.1-7
+ Revision: 687220
- rebuild
- add more conflicts to ease upgrade
- bump rel
- correct move typelib files

* Mon Jun 20 2011 Eugeni Dodonov <eugeni@mandriva.com> 1:1.4.1-5
+ Revision: 686294
- Move typelib files into common packages to prevent conflicts on upgrade.

* Sun Jun 19 2011 Funda Wang <fwang@mandriva.org> 1:1.4.1-4
+ Revision: 686026
- br gail3
- New version 1.4.1 (merged with webkit3)

* Sun Jun 05 2011 Funda Wang <fwang@mandriva.org> 1:1.2.7-4
+ Revision: 682819
- rebuild for new icu

* Fri Apr 08 2011 Funda Wang <fwang@mandriva.org> 1:1.2.7-3
+ Revision: 651869
- disable parallel build
- add gentoo patch to not build test programs
- rebuild for update libtool archive

* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 1:1.2.7-2
+ Revision: 644528
- rebuild for new icu

* Wed Mar 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.2.7-1
+ Revision: 641251
- 1.2.7

* Thu Jan 27 2011 Götz Waschk <waschk@mandriva.org> 1:1.2.6-1
+ Revision: 633189
- update to new version 1.2.6

* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 1:1.2.5-2mdv2011.0
+ Revision: 625009
- BR xt
- new version 1.2.5

* Sat Sep 18 2010 Funda Wang <fwang@mandriva.org> 1:1.2.4-1mdv2011.0
+ Revision: 579501
- new version 1.2.4
- more gir 1.2 fixes
- hardcode as gir 1.2
- rebuild for new gir

  + Götz Waschk <waschk@mandriva.org>
    - only apply gir patch on cooker

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 1:1.2.3-2mdv2011.0
+ Revision: 563973
- hardcode 1.1 as repo version :(

* Tue Jul 20 2010 Funda Wang <fwang@mandriva.org> 1:1.2.3-1mdv2011.0
+ Revision: 555149
- new version 1.2.3

* Tue May 18 2010 Olivier Blin <blino@mandriva.org> 1:1.2.0-3mdv2010.1
+ Revision: 545287
- expose allow-scripts-to-close-windows property in
  WebKitWebSettings for gtk ports, needed for first-time wizard
  (display_help) to be able to close its window with javascript

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 1:1.2.0-2mdv2010.1
+ Revision: 540058
- rebuild so that shared libraries are properly stripped again
- rebuild so that shared libraries are properly stripped again

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 1:1.2.0-1mdv2010.1
+ Revision: 535681
- update to new version 1.2.0

* Mon Mar 22 2010 Götz Waschk <waschk@mandriva.org> 1:1.1.90-1mdv2010.1
+ Revision: 526388
- new version

* Sun Mar 21 2010 Funda Wang <fwang@mandriva.org> 1:1.1.23-2mdv2010.1
+ Revision: 526110
- fix build with icu 4.4
- rebuild for new icu

* Tue Mar 16 2010 Götz Waschk <waschk@mandriva.org> 1:1.1.23-1mdv2010.1
+ Revision: 520720
- new version

* Tue Feb 23 2010 Götz Waschk <waschk@mandriva.org> 1:1.1.22-3mdv2010.1
+ Revision: 509951
- new version

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 1:1.1.21-3mdv2010.1
+ Revision: 503052
- add conflicts for upgrades

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 1:1.1.21-2mdv2010.1
+ Revision: 502909
- enable introspection support
- new version
- fix linking
- bump libsoup dep

* Thu Jan 21 2010 Frederik Himpe <fhimpe@mandriva.org> 1:1.1.19-1mdv2010.1
+ Revision: 494680
- update to new version 1.1.19

* Tue Jan 12 2010 Götz Waschk <waschk@mandriva.org> 1:1.1.18-1mdv2010.1
+ Revision: 490461
- new version
- bump libsoup dep

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.17-5mdv2010.1
+ Revision: 488809
- rebuilt against libjpeg v8

* Wed Dec 30 2009 Pascal Terjan <pterjan@mandriva.org> 1:1.1.17-4mdv2010.1
+ Revision: 483998
- Update BuildRequires

  + Thierry Vignaud <tv@mandriva.org>
    - add a test warning

* Wed Dec 16 2009 Funda Wang <fwang@mandriva.org> 1:1.1.17-3mdv2010.1
+ Revision: 479179
- drop unsupport switches
- fix requires

* Tue Dec 15 2009 Bogdano Arendartchuk <bogdano@mandriva.com> 1:1.1.17-2mdv2010.1
+ Revision: 479044
- bumped epoch as webkit from 2010.0 needs to be downgraded (#56451)

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 1.1.17-1mdv2010.1
+ Revision: 475431
- update to new version 1.1.17

* Mon Nov 09 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.16-1mdv2010.1
+ Revision: 463813
- update to new version 1.1.16

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.15.3-1mdv2010.1
+ Revision: 462265
- update to new version 1.1.15.3

* Wed Sep 23 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.15.1-1mdv2010.0
+ Revision: 447908
- update to new version 1.1.15.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 1.1.15-1mdv2010.0
+ Revision: 446928
- update to new version 1.1.15

* Thu Sep 10 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.14-1mdv2010.0
+ Revision: 437320
- update to new version 1.1.14

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 1.1.13-1mdv2010.0
+ Revision: 420777
- new version
- bump libsoup dep

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.12-4mdv2010.0
+ Revision: 416631
- rebuilt against libjpeg v7

  + Frederik Himpe <fhimpe@mandriva.org>
    - Rebuild for missing webkit-debug package
    - Rebuild for missing debug package

* Tue Jul 28 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.12-2mdv2010.0
+ Revision: 402759
- update to new version 1.1.12

* Mon Jul 13 2009 Götz Waschk <waschk@mandriva.org> 1.1.11-2mdv2010.0
+ Revision: 395646
- new version
- bump libsoup dep

* Mon Jun 22 2009 Götz Waschk <waschk@mandriva.org> 1.1.10-2mdv2010.0
+ Revision: 388022
- bump release
- fix webinspector permissions

* Mon Jun 15 2009 Götz Waschk <waschk@mandriva.org> 1.1.10-1mdv2010.0
+ Revision: 386146
- update to new version 1.1.10

* Sun Jun 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.9-1mdv2010.0
+ Revision: 385845
- Update to new version 1.1.9
- BuildRequires: gail-devel

* Sun May 31 2009 Funda Wang <fwang@mandriva.org> 1.1.8-1mdv2010.0
+ Revision: 381641
- update file list
- New version 1.1.8
- rebuild for new icu libmajor

  + Frederik Himpe <fhimpe@mandriva.org>
    - Remove explicit --enable-jit configure optiont: configure enabled it
      by default if the arch is supported (currently x86 and x86_64)

* Sat May 16 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.7-1mdv2010.0
+ Revision: 376383
- update to new version 1.1.7

* Fri May 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.6-1mdv2010.0
+ Revision: 369986
- Update to new version 1.1.6
- Introduce webkit and webkit1.0 RPMs to package translations
  and shared files for webkit1.0
- BuildRequires enchant-devel
- Fix URL and Source0 URL

* Mon Mar 16 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.3-1mdv2009.1
+ Revision: 355568
- Update to new version 1.1.3

* Sun Mar 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.1-3mdv2009.1
+ Revision: 355169
- Add some obsoletes so that urpmi handles the update from the wrongly
  named library packages a bit more nicely (bug #47803)

* Sat Mar 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.1-2mdv2009.1
+ Revision: 355044
-Build with gnome-keyring support
-Build with jit (a.k.a. Squirrelfish Extreme) on 32 bit x86
-Fix names of library, devel and webinspector packages so that they
 comply with library policy and can be parallel installable with an
 incompatible new future version
- Don't require exact version of webkit-inspector in library package,
  it breaks update when soname changes. Instead use a suggests (libwebkit
  works without the inspector), and don't use strict version requirement

* Thu Mar 12 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.1-1mdv2009.1
+ Revision: 354351
- Update to new stable version 1.1.1 (new major)
- Remove underlinking patch: not needed anymore

* Sun Feb 15 2009 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.40957.1mdv2009.1
+ Revision: 340397
- buildrequires libsoup-devel
- new release 40957

* Wed Jan 14 2009 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.39872.1mdv2009.1
+ Revision: 329267
- test enabling HTML5 video support (introduces dep on gstreamer)
- drop bison_24.patch (merged upstream)
- new snapshot 39872

* Tue Dec 30 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.39474.1mdv2009.1
+ Revision: 321296
- new snapshot 39474

* Fri Dec 19 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.39370.1mdv2009.1
+ Revision: 316374
- drop include.patch (merged upstream)
- update to rev 39370 (seems much less crash-y...)

* Fri Dec 12 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.39090.1mdv2009.1
+ Revision: 313504
- add include.patch, fixes a build-breaking missing include
- remove an incorrectly installed library
- comment the underlink patch
- add underlink.patch: try and fix underlinking in the unit tests
- add bison_24.patch from upstream #22205 (Bernhard Rosenkraenzer) - fix
  build with bison 2.4
- new snapshot 39090

* Tue Nov 25 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.38707.1mdv2009.1
+ Revision: 306697
- new snapshot 38707

* Fri Nov 07 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.38209.1mdv2009.1
+ Revision: 300836
- package the webinspector stuff into a new subpackage
- new snapshot 38209

* Thu Sep 11 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.36309.1mdv2009.0
+ Revision: 283896
- add some conditionals so i can easily test pango build
- new snapshot 36309

* Sat Sep 06 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.36120.1mdv2009.0
+ Revision: 281774
- new nightly 36120

* Tue Aug 26 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.35933.1mdv2009.0
+ Revision: 276371
- new snapshot 35933

* Wed Aug 13 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.35718.1mdv2009.0
+ Revision: 271515
- new nightly 35718

* Sun Aug 03 2008 Pascal Terjan <pterjan@mandriva.org> 1.0.2-0.35417.1mdv2009.0
+ Revision: 261540
- Update to r35417

* Thu Jul 17 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.2-0.35203.1mdv2009.0
+ Revision: 237829
- disable the underlinking workarounds, they weren't actually helping, let's
  see if it works yet...
- drop icuconfig.patch (fixed in our icu package)
- new snapshot 35203
- seems like we have to disable as-needed as well?
- disable --no-undefined: build breaks due to some internal problem with
  it enabled, looks hard to solve
- add icuconfig.patch to fix call to icu-config in configure
- set version to 1.0.2 (there was a somewhat obscure 1.0.1 'release')
- new snapshot 35177

* Fri Jun 27 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.34824.1mdv2009.0
+ Revision: 229572
- add a subpackage for the newly added javascript shell
- new snapshot 34824

* Fri Jun 20 2008 Götz Waschk <waschk@mandriva.org> 0-0.34503.2mdv2009.0
+ Revision: 227438
- add libwebkitgtk to allow noarch webkit-sharp bindings

* Thu Jun 12 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.34503.1mdv2009.0
+ Revision: 218575
- new snapshot 34503

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 21 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.33943.1mdv2009.0
+ Revision: 209799
- correct license (it's dual BSD and LGPL)
- new snapshot

* Mon May 12 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.33029.3mdv2009.0
+ Revision: 206271
- devel package doesn't require libnspr-devel (this was an error in some versions of the plugin patch)

* Mon May 12 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.33029.2mdv2009.0
+ Revision: 206248
- fix the obsoletes
- new snapshot 33029

* Mon May 05 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.32877.1mdv2009.0
+ Revision: 201569
- whoops, missed a stray reference to the old (more complex) way of building
- drop the uppercase naming
- improve summaries and descriptions
- clean spec
- drop the qt build (now in upstream qt4)
- new snapshot

* Fri May 02 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.32778.1mdv2009.0
+ Revision: 199975
- drop plugin.patch and brace.patch (both merged upstream)
- update snapshot

* Thu May 01 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.32698.1mdv2009.0
+ Revision: 199841
- add brace.patch (from upstream SVN, fixes an error that breaks Qt 4.3 build)
- updated plugin patch
- new snapshot

* Fri Apr 25 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.32531.2mdv2009.0
+ Revision: 197473
- tweak configure params to try and get 100/100 acid3
- drop all nspr stuff, it was a bogus addition to the plugin patch anyway

* Fri Apr 25 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.32531.1mdv2009.0
+ Revision: 197442
- update plugin patch (improved version from upstream)
- update nightly

* Wed Apr 23 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.32416.4mdv2009.0
+ Revision: 196963
- add qt43.patch to fix a bug which caused build with Qt < 4.4 to fail
- updated version of plugin patch
- new snapshot

* Fri Apr 18 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.31893.4mdv2009.0
+ Revision: 195485
- try and fix up the requires_exceptions again...

* Thu Apr 17 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.31893.3mdv2009.0
+ Revision: 195320
- same fix for this patch was needed as for the other one...
- updated version of upstream patch (earlier was incomplete)
- fix a stray reference to a non-existent file in upstream patch
- new version of the plugin patch from upstream bug, hopefully this one will work!

* Thu Apr 17 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.31893.2mdv2009.0
+ Revision: 195033
- drop the patch until i know why it's not working. anyway, it makes acid3 test crash the browser, for some reason
- fix nspr devel requires (autorequires has problems here)
- final plugin patch fixup (but it still doesn't seem to work...will consult with upstream)
- more patch fixing..
- buildrequires libnspr-devel
- ...and one more fix
- more hacking on the patch
- fix changed function name in patch
- oops, bump release
- readd GTK+ plugin patch (31326-plugin.patch), from upstream bug report slightly rediffed

* Tue Apr 15 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.31893.1mdv2009.0
+ Revision: 194083
- new snapshot 31893

* Thu Mar 20 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.31157.1mdv2008.1
+ Revision: 189105
- protect majors in file lists
- move DumpRenderTree to the qt -devel package (aka obey libification policy)
- adjust to new upstream build method for GTK build (using autotools not qmake)
- split GtkLauncher and QtLauncher into separate packages (they're mostly useless demo code and were breaking libification policy)
- correct majors
- use upstream nightly tarball instead of creating one ourselves (apart from anything else it's, like, ten times smaller)
- new snapshot

* Fri Feb 22 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.30465.1mdv2008.1
+ Revision: 173823
- drop Implement-plugin-support-in-GTK-backend.patch (merged upstream)
- new snapshot 30465

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Feb 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0-0.30005.1mdv2008.1
+ Revision: 163896
- Patch0: add support for external plugins (flashplayer and so forth). At the current stage this supports only GTK version of WebKit. Patch should be merged into upstream svn quite soon. For more info please see http://bugs.webkit.org/show_bug.cgi?id=14750
- fix buildroot

* Wed Jan 30 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.29866.1mdv2008.1
+ Revision: 160152
- new snapshot 29866

* Sat Jan 05 2008 Adam Williamson <awilliamson@mandriva.org> 0-0.29184.1mdv2008.1
+ Revision: 145662
- 29013 doesn't build, go to current (29184)
- new snapshot 29013 (required by latest midori)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Adam Williamson <awilliamson@mandriva.org> 0-0.28663.1mdv2008.1
+ Revision: 119551
- package a newly-introduced file
- new SVN snapshot 28663

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary

* Wed Nov 21 2007 Thierry Vignaud <tv@mandriva.org> 0-0.26100.2mdv2008.1
+ Revision: 111025
- rebuild for new libicu

* Mon Oct 08 2007 Pascal Terjan <pterjan@mandriva.org> 0-0.26100.1mdv2008.0
+ Revision: 95684
- Obsoletes libWebKitGdk0
- Update to revision 26100
- s/Gdk/Gtk/g; s/gdk/gtk/
- DumpRenderTree changed location

* Sun Sep 02 2007 Pascal Terjan <pterjan@mandriva.org> 0-0.25144.3mdv2008.0
+ Revision: 78087
- Add some BuildRequires for the Qt version
- Oops fix the Provides

* Sat Sep 01 2007 Pascal Terjan <pterjan@mandriva.org> 0-0.25144.2mdv2008.0
+ Revision: 77413
- Add some provides on -devel packages

* Sat Sep 01 2007 Pascal Terjan <pterjan@mandriva.org> 0-0.25144.1mdv2008.0
+ Revision: 77392
- Fix group
- Put QtWebKit.pc in a place where pkgconfig will find it
- Import webkit



* Fri Aug 31 2007 Pascal Terajn <pterjan@mandriva.org> 0-0.25144.1mdv2008.0
- Initial Mandriva package (some inspiration from Debian)
