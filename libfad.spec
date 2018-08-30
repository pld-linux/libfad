Summary:	Flash Animation Decode library
Summary(pl.UTF-8):	Biblioteka Flash Animation Decode - dekodowanie animacji Flash
Name:		libfad
Version:	0.9.6
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/fad/%{name}-%{version}.tar.bz2
# Source0-md5:	13e2b5df91f1627a8c5cdab573784aab
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-dirs.patch
URL:		http://fad.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.8
BuildRequires:	cairo-devel >= 0.9.2
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libmad-devel >= 0.15.1b
BuildRequires:	zlib-devel >= 1.2.3
Requires:	cairo >= 0.9.2
Requires:	libjpeg >= 6b
Requires:	libmad >= 0.15.1b
Requires:	zlib >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libFAD is a Flash Animation Decode library.

%description -l pl.UTF-8
libFAD (Flash Animation Decode) to biblioteka do dekodowania animacji
Flash.

%package devel
Summary:	Header files for libFAD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libFAD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 0.9.2

%description devel
Header files for libFAD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libFAD.

%package static
Summary:	Static libFAD library
Summary(pl.UTF-8):	Statyczna biblioteka libFAD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libFAD library.

%description static -l pl.UTF-8
Statyczna biblioteka libFAD.

%package player
Summary:	SDL based Flash Animation Player
Summary(pl.UTF-8):	Odtwarzacz animacji Flash oparty na SDL
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	SDL >= 1.2.8

%description player
SDL based Flash Animation Player.

%description player -l pl.UTF-8
Odtwarzacz animacji Flash oparty na SDL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG="%{rpmcflags} %{rpmcppflags} -DLIBFAD_DO_RENDER"
	DEBUG_CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README
%attr(755,root,root) %{_libdir}/libfad.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfad.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfad.so
%{_includedir}/fad.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libfad.a

%files player
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fap
