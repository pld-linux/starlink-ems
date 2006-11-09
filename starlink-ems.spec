Summary:	EMS - Error Message Service
Summary(pl):	EMS - us³uga obs³ugi b³êdów
Name:		starlink-ems
Version:	2.0_7.218
Release:	1
License:	non-commercial use and distribution (see EMS_CONDITIONS)
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/ems/ems.tar.Z
# Source0-md5:	cd30d7ab01dc89c5e05fb7f2f67e5a95
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_EMS.html
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-cnf-devel
BuildRequires:	starlink-sae-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
EMS is the Error Message Service. The purpose of EMS is to provide
facilities for constructing and storing error messages for future
delivery to the user - usually via the Starlink Error Reporting
System, ERR. EMS can be regarded as a simplified version of ERR
without the binding to any software environment (e.g. for message
output or access to the parameter and data systems).

%description -l pl
EMS (Error Message Service) to us³uga obs³ugi b³êdów. Celem EMS jest
dostarczenie mo¿liwo¶ci konstruowania i przechowywania komunikatów
b³êdów do pó¼niejszego dostarczenia do u¿ytkownika - zwykle poprzez
ERR - Starlink Error Reporting System (system raportowania b³êdów).
EMS mo¿na uwa¿aæ za uproszczon± wersjê ERR, nie powi±zan± z ¿adnym
¶rodowiskiem programowym (np. do wypisywania komunikatów lub dostêpu
do systemów parametrów i danych).

%package devel
Summary:	Header files for EMS libraries
Summary(pl):	Pliki nag³ówkowe bibliotek EMS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	starlink-cnf-devel

%description devel
Header files for EMS libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek EMS.

%package static
Summary:	Static Starlink EMS libraries
Summary(pl):	Statyczne biblioteki Starlink EMS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink EMS libraries.

%description static -l pl
Statyczne biblioteki Starlink EMS.

%prep
%setup -q -c

sed -i -e "s/ -O'/ %{rpmcflags} -fPIC'/;s/ ld -shared -soname / %{__cc} -shared \\\$\\\$3 -Wl,-soname=/" mk
sed -i -e "s/\\('\\\$(OBJECT_FILES_CF)' '-L\\\$(STAR_\\)LIB)'/\\1SHARE) -lcnf -L. -lems'/" makefile

%build
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc EMS_CONDITIONS ems.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/ssn*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/ems_dev
%attr(755,root,root) %{stardir}/bin/ems_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
