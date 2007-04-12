%define module String-ShellQuote
%define name perl-%{module}
%define version 1.03
%define release %mkrel 2

Summary:	Quote strings for passing through the shell
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.perl.com/CPAN-local/authors/id/R/RO/ROSCH/String-ShellQuote-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This perl module contains some functions which are useful for quoting strings
which are going to pass through the shell or a shell-like object.

%prep
%setup -q -n %module-%version

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/String/*

%clean
rm -rf $RPM_BUILD_ROOT


