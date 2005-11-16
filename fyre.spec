Summary:	GTK+2-based explorer for iterated chaotic functions
Summary(pl):	Oparta na GTK+ przegl±darka iterowanych funkcji chaotycznych
Name:		fyre
Version:	1.0.0
Release:	0.1
License:	GPL
Vendor:		David Trowbridge <trowbrds@cs.colorado.edu> Micah Dowty <micah@navi.cx>
Group:		Applications/Graphics
Source0:	http://flapjack.navi.cx/releases/fyre/%{name}-%{version}.tar.gz
# Source0-md5:	2ea0cbef438c5f63f7e6e5c4a62995e0
URL:		http://fyre.navi.cx/
BuildRequires:	OpenEXR-devel
BuildRequires:	gnet-devel >= 2.0
BuildRequires:	gtk+2-devel
Requires:	gnet >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fyre is a tool for producing computational artwork based on histograms
of iterated chaotic functions. At the moment, it implements the Peter
de Jong map in a fixed-function pipeline with an interactive GTK+
frontend and a command line interface for easy and efficient rendering
of high-resolution, high quality images.

%description -l pl
Fyre to narzêdzie do tworzenia sztuki obliczeniowej w oparciu o
histogramy iterowanych funkcji chaotycznych. Aktualnie implementuje
odwzorowanie Petera de Jonga w potoku funkcji sta³ych z interaktywnym
frontendem GTK+ oraz interfejsem linii poleceñ do ³atwego i wydajnego
renderowania obrazów wysokiej rozdzielczo¶ci z wysok± jako¶ci±.

%prep
%setup -q

%build
%configure \
	--enable-gnet \
	--enable-openexr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fyre
%{_desktopdir}/*.desktop
%{_datadir}/fyre
%{_iconsdir}/hicolor/48x48/mimetypes/application-x-fyre-animation.png
%{_pixmapsdir}/*.png
%{_datadir}/mime/packages/fyre.xml
