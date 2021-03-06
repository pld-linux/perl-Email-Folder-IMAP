#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Email
%define		pnam	Folder-IMAP
Summary:	Email::Folder::IMAP - Email::Folder Access to IMAP Folders
Summary(pl.UTF-8):	Email::Folder::IMAP - dostęp do folderów IMAP dla klasy Email::Folder
Name:		perl-%{pdir}-%{pnam}
Version:	1.102
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4e85d317dced5ff659661d86e0743b39
URL:		http://search.cpan.org/dist/Email-Folder-Type/
%if %{with tests}
BuildRequires:	perl-Email-Folder
BuildRequires:	perl-Email-FolderType-Net
BuildRequires:	perl-Net-IMAP-Simple
BuildRequires:	perl-URI-imap
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This software adds IMAP functionality to Email::Folder. Its interface
is identical to the other Email::Folder::Reader subclasses.

%description -l pl.UTF-8
Ta klasa dodaje funkcjonalność IMAP do Email::Folder. Jej interfejs
jest taki sam, jak innych podklas Email::Folder::Reader.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Email/Folder/IMAP.pm
%{_mandir}/man3/*
