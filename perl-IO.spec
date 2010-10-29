#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	IO
%define		pdir	IO
# NOTE: keep this ver macro and use 1.23_01 not 1.2301 as rpm version to avoid epoch bumps
%define		ver	%(echo %{version} | tr -d _)
Summary:	IO - Perl core IO modules
Summary(pl.UTF-8):	IO - moduły dystrybucyjne IO perla 5
Name:		perl-IO
Version:	1.25
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pnam}-%{ver}.tar.gz
# Source0-md5:	b88aaf2bb7437725b11e9eb48dfb6c93
URL:		http://search.cpan.org/dist/IO/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-dirs >= 1.0-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl core IO modules.

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

rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/IO/.packlist

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
