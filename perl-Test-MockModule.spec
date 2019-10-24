#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-MockModule
Version  : 0.171.0
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/G/GF/GFRANKS/Test-MockModule-v0.171.0.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GF/GFRANKS/Test-MockModule-v0.171.0.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-mockmodule-perl/libtest-mockmodule-perl_0.170.0-1.debian.tar.xz
Summary  : 'Override subroutines in a module for unit testing'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-MockModule-license = %{version}-%{release}
Requires: perl-Test-MockModule-perl = %{version}-%{release}
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
Requires: perl-Test-MockModule = %{version}-%{release}

%description dev
dev components for the perl-Test-MockModule package.


%package license
Summary: license components for the perl-Test-MockModule package.
Group: Default

%description license
license components for the perl-Test-MockModule package.


%package perl
Summary: perl components for the perl-Test-MockModule package.
Group: Default
Requires: perl-Test-MockModule = %{version}-%{release}

%description perl
perl components for the perl-Test-MockModule package.


%prep
%setup -q -n Test-MockModule-v0.171.0
cd ..
%setup -q -T -D -n Test-MockModule-v0.171.0 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Test-MockModule-v0.171.0/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
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
cp %{_builddir}/Test-MockModule-v0.171.0/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-MockModule/35c343d76fd64f49397bd23062dcd3f7d3c0a6f4
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::MockModule.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-MockModule/35c343d76fd64f49397bd23062dcd3f7d3c0a6f4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Test/MockModule.pm
