Name: hunspell-th
Summary: Thai hunspell dictionaries
%define upstreamid 20061212
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/th_TH.zip
Group: Applications/Text
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Thai hunspell dictionaries.

%prep
%setup -q -c -n hunspell-th

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_TH.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20061212-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20061212-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20061212-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.20061212-2
- clarify license version

* Wed Feb 14 2007 Caolan McNamara <caolanm@redhat.com> - 0.20061212-1
- update to latest

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20050530-1
- initial version
