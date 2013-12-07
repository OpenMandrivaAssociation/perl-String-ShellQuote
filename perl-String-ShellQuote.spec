%define modname	String-ShellQuote
%define modver	1.04

Summary:	Quote strings for passing through the shell
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.perl.com/CPAN-local/authors/id/R/RO/ROSCH/String-ShellQuote-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This perl module contains some functions which are useful for quoting strings
which are going to pass through the shell or a shell-like object.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_bindir}/*
%{perl_vendorlib}/String/*
%{_mandir}/man1/*
%{_mandir}/man3/*

