#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-MockModule
Version  : 0.15
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/G/GF/GFRANKS/Test-MockModule-0.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GF/GFRANKS/Test-MockModule-0.15.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-mockmodule-perl/libtest-mockmodule-perl_0.13-1.debian.tar.xz
Summary  : 'Override subroutines in a module for unit testing'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-3.0
Requires: perl-Test-MockModule-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Warnings)

%description
# Test::MockModule - mock subroutines in a module
See the LICENSE section in `lib/Test/MockModule.pm` for usage and
distribution rights.

%package dev
Summary: dev components for the perl-Test-MockModule package.
Group: Development
Provides: perl-Test-MockModule-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-MockModule package.


%package license
Summary: license components for the perl-Test-MockModule package.
Group: Default

%description license
license components for the perl-Test-MockModule package.


%prep
%setup -q -n Test-MockModule-0.15
cd ..
%setup -q -T -D -n Test-MockModule-0.15 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Test-MockModule-0.15/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-MockModule
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-MockModule/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Test-MockModule/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Test/MockModule.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::MockModule.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-MockModule/LICENSE
/usr/share/package-licenses/perl-Test-MockModule/deblicense_copyright
