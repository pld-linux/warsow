# TODO:	- doesn't build without server and without client
#	- polish description
#	- install binaries depending on architecture to better place (now they are stored in /usr/bin)
#
# Conditional build:
%bcond_without	client		# build without client
%bcond_without	openal		# build without openal support
%bcond_without	qf		# build without qf support
%bcond_without	server		# build without server
#
Summary:	A Fast Paced FPS Game
Name:		warsow
Version:	0.5
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://data.rodix.free.fr/warsow/files/%{name}_%{version}_sdk.zip
# Source0-md5:	acd0244435cc63967b0eb3468c21c454
Source1:	http://data.rodix.free.fr/warsow/files/%{name}_%{version}_unified.zip
# Source1-md5:	d0cb961256bbc1b93bf240b8bcf8eff5
Patch0:		%{name}-flags.patch
Patch1:		%{name}-dirs.patch
URL:		http://www.warsow.net/
%{?with_openal:BuildRequires:	OpenAL-devel}
%{?with_qf:BuildRequires:	SDL-devel}
BuildRequires:	curl-devel
BuildRequires:	libjpeg-devel
%{?with_qf:BuildRequires:	libvorbis-devel}
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
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
%{__make} -C source/ \
	CC="%{__cc}" \
	CXX="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}" \
	%{!?with_client:BUILD_CLIENT=NO} \
	%{!?with_openal:BUILD_SND_OPENAL=NO} \
	%{!?with_qf:BUILD_SND_QF=NO} \
	%{!?with_server:BUILD_SERVER=NO}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install source/release/warsow* $RPM_BUILD_ROOT%{_bindir}
cp -r source/release/libs $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r basewsw $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/warsow*
%{_datadir}/%{name}
