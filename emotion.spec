Summary:	Enlightenment Foundation Library
Name:		emotion
Version:	1.7.4
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	ebd59a071b4c5d516747b638411a8a51
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ecore-devel
BuildRequires:	gstreamer010-plugins-base-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A media object library for Evas and Ecore.

%package devel
Summary:	Header files for emotion library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for emotion library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-install-examples	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_libdir} -name *.la -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libemotion.so.1
%attr(755,root,root) %{_libdir}/libemotion.so.*.*.*
%dir %{_libdir}/emotion
%attr(755,root,root) %{_libdir}/emotion/*.so
%{_datadir}/emotion

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libemotion.so
%dir %{_libdir}/edje/modules/emotion
%dir %{_libdir}/edje/modules/emotion/linux-gnu-*
%{_libdir}/edje/modules/emotion/linux-gnu-x86_64-1.0.0/module.so
%{_includedir}/emotion-1
%{_pkgconfigdir}/emotion.pc

