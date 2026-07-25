%define modname	String-ShellQuote
%define modver	1.04

Summary:	Quote strings for passing through the shell
Name:		perl-%{modname}
Version:	%{modver}
Release:	23
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/String-ShellQuote
Source0:	https://cpan.metacpan.org/authors/id/R/RO/ROSCH/String-ShellQuote-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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

