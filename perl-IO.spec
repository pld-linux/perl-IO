#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	IO
%define		pdir	IO
Summary:	IO - the perl5 IO distribution
Summary(pl.UTF-8):	IO - moduły dystrybucyjne IO perla 5
Name:		perl-IO
Version:	1.23_01
%define		ver	%(echo %{version} | tr -d _)
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pnam}-%{ver}.tar.gz
# Source0-md5:	4f209b75851b27f39a4d221d01a19b92
URL:		http://search.cpan.org/dist/IO/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 1.0-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the perl5 IO distribution.

%description -l pl.UTF-8
Są to moduły dystrybucyjne IO perla 5.

%prep
%setup -q -n %{pnam}-%{ver}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorarch}/IO.pm
%{perl_vendorarch}/IO/*
%{perl_vendorarch}/auto/IO/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/IO/*.so
%{_mandir}/man3/*
