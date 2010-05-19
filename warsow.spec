# TODO:	- doesn't build without server and without client
#	- install binaries depending on architecture to better place (now they are stored in /usr/bin)
#
# Conditional build:
%bcond_without	client		# build without client
%bcond_without	openal		# build without openal support
%bcond_without	qf		# build without qf support
%bcond_without	server		# build without server
#
Summary:	A Fast Paced FPS Game
Summary(pl.UTF-8):	Szybko tocząca się gra FPS
Name:		warsow
Version:	0.5
Release:	0.2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://data.rodix.free.fr/warsow/files/%{name}_%{version}_sdk.zip
# Source0-md5:	acd0244435cc63967b0eb3468c21c454
Patch0:		%{name}-flags.patch
Patch1:		%{name}-dirs.patch
Patch2:		%{name}-gentoo_fixes.patch
Patch3:		%{name}-libjpeg.patch
Patch4:		%{name}-xincludes.patch
Patch5:		%{name}-pic.patch
URL:		http://www.warsow.net/
%{?with_openal:BuildRequires:	OpenAL-devel}
BuildRequires:	OpenGL-devel
%{?with_qf:BuildRequires:	SDL-devel}
BuildRequires:	curl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
%{?with_qf:BuildRequires:	libvorbis-devel}
BuildRequires:	pkgconfig
BuildRequires:	unzip
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}
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

%description -l pl.UTF-8
Warsow to samodzielna strzelanina FPS dla Windows i Linuksa. Została
wydana na licencji GPL i jest oparta na silniku 3D Qfusion
(modyfikacji silnika z Quake 2). Oferuje sportowo zorientowany FPS,
szybko toczącą się grę skupioną na triksach (trick jumps) oraz sztukę
poruszania. Zawiera kompletny system broni z trybem słabego i silnego
ognia. Grafika jest utrzymana w stylu rysunkowym, ale nie Mangi,
łączącym ciemne, błyskające i brudne tekstury, pasujące do akcji
pełnej zabawy i szybkości. Gra została częściowo zainspirowana
tytułami takimi jak Quakeworld, Quake3 CPMA, Jet Set Radio czy
Speedball.

%prep
%setup -q -c
#%%patch0 -p1
#%%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p0

%build
%{__make} -C source/ -j1 \
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_bindir}/warsow*
%attr(755,root,root) %{_datadir}/%{name}/libs
