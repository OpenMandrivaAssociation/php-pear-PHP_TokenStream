%define  upstream_name PHP_TokenStream

Summary:	Wrapper around PHP's tokenizer extension
Name:		php-pear-%{upstream_name}
Version:	1.1.1
Release:	3
License:	BSD
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/PHP_TokenStream-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-pear-PHPUnit >= 3.6.3
Suggests:	php-tokenizer

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

This package provides a Wrapper around PHP's tokenizer extension for PHPUnit.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/ChangeLog.markdown
%doc %{upstream_name}-%{version}/LICENSE
%doc %{upstream_name}-%{version}/README.markdown
%{_datadir}/pear/PHP/Token
%{_datadir}/pear/PHP/*.php
%{_datadir}/pear/packages/PHP_TokenStream.xml



%changelog
* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdv2012.0
+ Revision: 730885
- import php-pear-PHP_TokenStream


* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdv2010.2
- initial Mandriva package
