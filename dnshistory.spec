Summary:	Processes various log file formats doing dns IP Address lookups
Name:		dnshistory
Version:	1.3
Release:	%mkrel 1
License:	GPL
Group:		File tools
URL:		http://www.stedee.id.au/dnshistory
Source:		http://www.stedee.id.au/files/%{name}-%{version}.tar.bz2
BuildRequires:	db4-devel
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
    --enable-database-dir=%{_localstatedir}/%{name}

%make

%install
rm -rf %{buildroot}

%makeinstall

install -d %{buildroot}%{_localstatedir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc ChangeLog COPYING INSTALL README
%{_bindir}/%{name}
%dir %{_localstatedir}/%{name}
%{_mandir}/man1/%{name}.1*

