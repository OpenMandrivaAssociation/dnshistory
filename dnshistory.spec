Summary:	Processes various log file formats doing dns IP Address lookups
Name:		dnshistory
Version:	1.3
Release:	9
License:	GPL
Group:		File tools
URL:		https://www.stedee.id.au/dnshistory
Source:		http://www.stedee.id.au/files/%{name}-%{version}.tar.bz2
BuildRequires:	db-devel
BuildRequires:	pcre-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
dnshistory currently processes Apache CLF and Combined logs, Squid access logs,
FTP xferlog files and iptables based logs. The log format is auto-detected.

%prep

%setup -q -n %{name}-%{version}
 
%build

%configure2_5x \
    --enable-database-name=%{name}.db \
    --enable-database-dir=%{_localstatedir}/lib/%{name}

%make

%install
rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_localstatedir}/lib/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc ChangeLog COPYING INSTALL README
%{_bindir}/%{name}
%dir %{_localstatedir}/lib/%{name}
%{_mandir}/man1/%{name}.1*




%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 1.3-8mdv2012.0
+ Revision: 772948
- relink against libpcre.so.1

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - rebuild with db 5.1 (from fwang | 2011-04-12 10:45:25 +0200)

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-6mdv2011.0
+ Revision: 610256
- rebuild

* Tue Jan 12 2010 Buchan Milne <bgmilne@mandriva.org> 1.3-5mdv2010.1
+ Revision: 490366
- Rebuild for db-4.8

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.3-4mdv2010.0
+ Revision: 428286
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3-3mdv2009.0
+ Revision: 244438
- rebuild

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.3-1mdv2008.1
+ Revision: 136367
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 31 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdv2007.0
+ Revision: 115742
- 1.3

* Sun Jan 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3-0.beta1.1mdv2007.1
+ Revision: 105194
- Import dnshistory

* Sun Jan 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3-0.beta1.1mdv2007.1
- initial Mandriva package

