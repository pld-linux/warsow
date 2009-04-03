# TODO:	- use our libs instead of static ones
#	- bconds
#	- BRs
#	- polish description
#
Summary:	A Fast Paced FPS Game
Name:		warsow
Version:	0.42
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://data.rodix.free.fr/warsow/files/%{name}_%{version}_sdk.zip
# Source0-md5:	94c9bb2a48ac6f2687b38809e003f3b9
Source1:	http://data.rodix.free.fr/warsow/files/%{name}_%{version}_unified.zip
# Source1-md5:	cba5fe9b8af01b378e685959098fa84f
Patch0:		%{name}-flags.patch
Patch1:		%{name}-dirs.patch
URL:		http://www.warsow.net/
BuildRequires:	dos2unix
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Warsow is a standalone first person shooter for Windows and Linux. It
is under the GPL and based on the 3D Engine Qfusion (a modification of
Quake 2's engine). It offers eSport oriented FPS, fast-paced gameplay
focused on trix (trick jumps) and the art of move. It offers a
complete Power-up System including Weak and Strong fire mode for each
weapon. The graphics are in a cartoonish style with
celshading-like_but_not_Manga style, mixing dark, flashy and dirty
textures, matching the action full of fun and speed. The game got some
of its inspiration from titles like Quakeworld, Quake3 CPMA, Jet Set
Radio or Speedball.

%prep
%setup -q -c %{name}-%{version} -a 1
%patch0 -p1
%patch1 -p1

%build
%{__make} -C %{name}_%{version}_src/source/ \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cd %{name}_%{version}_src
dos2unix source/release/warsow

install source/release/warsow* $RPM_BUILD_ROOT%{_bindir}
cp -r source/release/libs $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r ../%{name}_%{version}_unified/basewsw $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/warsow*
%{_datadir}/%{name}
