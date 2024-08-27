# TODO: init script, user/group
Summary:	GEAM Encrypts Automagically Mail
Summary(pl.UTF-8):	GEAM - automagiczne szyfrowanie poczty
Name:		geam
Version:	0.8.4
Release:	0.1
License:	GPL v2+
Group:		Networking/Daemons
Source0:	https://www.gnupg.org/ftp/gcrypt/geam/%{name}-%{version}.tar.gz
# Source0-md5:	cc35eec9b3f7d9f2e427bd1de4a59b8d
URL:		https://www.gnupg.org/
BuildRequires:	pth-devel >= 1.2.1
Requires:	gnupg >= 1.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GEAM (GEAM Encrypts Automagically Mail) is a SMTP proxy which is able
to encrypt or decrypt mail on the fly. It is not a full MTA as it
depends on smarthosts for routing.

%description -l pl.UTF-8
GEAM (GEAM Encrypts Automagically Mail, czyli GEAM automagicznie
szyfruje pocztę) to proxy SMTP potrafiące szyfrować i odszyfrowywać
pocztę w locie. Nie jest to pełny MTA jako że do routingu poczty
polega na zewnętrznych smarthostach.

%prep
%setup -q

%build
%configure
%{__make} \
	simple_mta_LDADD='$(LDADD)'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%lang(de) %doc doc/manual.de.html
%attr(755,root,root) %{_sbindir}/geamd
%{_mandir}/man8/geamd.8*
