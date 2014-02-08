%define upstream_name    String-ShellQuote
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    9

Summary:	Quote strings for passing through the shell
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.perl.com/CPAN-local/authors/id/R/RO/ROSCH/String-ShellQuote-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  perl-devel

%description
This perl module contains some functions which are useful for quoting strings
which are going to pass through the shell or a shell-like object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/String/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-6mdv2012.0
+ Revision: 765660
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-5
+ Revision: 764171
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-4
+ Revision: 763099
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-3
+ Revision: 667313
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.40.0-2mdv2011.0
+ Revision: 564754
- rebuild for perl 5.12.1

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 552636
- update to 1.04

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.1
+ Revision: 408047
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.03-6mdv2009.1
+ Revision: 351723
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.03-5mdv2009.0
+ Revision: 224058
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.03-4mdv2008.1
+ Revision: 180570
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.03-3mdv2008.0
+ Revision: 64806
- rebuild


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.03-2mdv2007.0
+ Revision: 108450
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-String-ShellQuote

* Fri May 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.03-1mdk
- 1.03

* Wed Feb 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.02-1mdk
- 1.02

