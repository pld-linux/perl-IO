%include	/usr/lib/rpm/macros.perl
Summary:	IO - load various IO perl modules
Summary(pl):	Modu³ perla IO
Name:		perl-IO
Version:	1.20
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/IO/IO-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO - load various IO perl modules

%description -l pl
Modu³y perla IO

%prep
%setup -q -n IO-%{version}

%build
perl Makefile.PL POLLUTE=1
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_archlib}/IO/*
