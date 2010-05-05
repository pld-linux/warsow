#
Summary:	Warsow - data files for game
Summary(pl.UTF-8):	Warsow - pliki danych dla gry
Name:		warsow-data
Version:	0.5
Release:	0.2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://data.rodix.free.fr/warsow/files/warsow_%{version}_unified.zip
# Source0-md5:	d0cb961256bbc1b93bf240b8bcf8eff5
URL:		http://www.warsow.net/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Warsow data files.

%description -l pl.UTF-8
Pliki danych dla gry Warsow.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/warsow}

install warsow wsw_server wswtv_server $RPM_BUILD_ROOT%{_bindir}
cp -r basewsw $RPM_BUILD_ROOT%{_datadir}/warsow

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/warsow
%{_datadir}/warsow/basewsw
