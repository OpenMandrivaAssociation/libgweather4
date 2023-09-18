%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1
%define oname libgweather

%define api	4
%define major	0
%define gimajor	4.0
%define libname	%mklibname gweather %{api} %{major}
%define girname	%mklibname gweather-gir %{gimajor}
%define devname	%mklibname -d gweather %{api}

Summary:	GNOME Weather applet library
Name:		libgweather4
Version:	4.4.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://www.gnome.org
Source0:	https://ftp.gnome.org/pub/GNOME/sources/libgweather/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires:	libxml2-utils
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:	pkgconfig(gconf-2.0) GConf2
BuildRequires:	pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	timezone
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  python3dist(pygobject)
#BuildRequires:  python3dist(pylint)
BuildRequires:  gtk-doc

%description
This is a library to provide Weather data to the GNOME panel applet.

%package -n %{libname}
Group:		System/Libraries
Summary:	GNOME Weather applet library
Requires:	%{name} >= %{version}-%{release}

%description -n %{libname}
This is a library to provide Weather data to the GNOME panel applet.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	GNOME Weather applet library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson -Denable_vala=true -Dgtk_doc=true

%meson_build

%install
%meson_install
%find_lang %{oname}-%{gimajor} --all-name

%files -f %{oname}-%{gimajor}.lang

%doc NEWS
%{_libdir}/libgweather-%{api}/Locations.bin
%{_datadir}/libgweather-%{api}/Locations.xml
%{_datadir}/libgweather-%{api}/locations.dtd
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather%{api}.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.GWeather%{api}.gschema.xml
#{_datadir}/glade/catalogs/libgweather.xml

%files -n %{libname}
%{_libdir}/libgweather-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GWeather-%{gimajor}.typelib

%files -n %{devname}
%doc %{_datadir}/doc/libgweather-4.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gir-1.0/GWeather-%{gimajor}.gir
%{_datadir}/vala/vapi/gweather%{api}.deps
%{_datadir}/vala/vapi/gweather%{api}.vapi
