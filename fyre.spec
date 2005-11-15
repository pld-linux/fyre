%define _sharedir %{_prefix}/share

Summary:	gtk2-based explorer for iterated chaotic functions
#Summary(pl):	-
Name:		fyre
Version:	1.0.0
Release:	0.1
License:	GPL
Vendor:		David Trowbridge <trowbrds@cs.colorado.edu> Micah Dowty <micah@navi.cx>
Group:		Applications/Graphics
Source0:	http://flapjack.navi.cx/releases/fyre/%{name}-%{version}.tar.gz
# Source0-md5:	2ea0cbef438c5f63f7e6e5c4a62995e0
URL:		http://fyre.navi.cx
BuildRequires:	gnet-devel >= 2.0
BuildRequires:	gtk+2-devel
BuildRequires:	OpenEXR-devel
Requires:	gnet >= 2.0
Requires:	gtk+2
Requires:	OpenEXR
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fyre is a tool for producing computational artwork based on histograms
of iterated chaotic functions. At the moment, it implements the Peter
de Jong map in a fixed-function pipeline with an interactive GTK+
frontend and a command line interface for easy and efficient rendering
of high-resolution, high quality images.

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

%post

%postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fyre
%{_desktopdir}/*.desktop
%{_datadir}/fyre
%{_datadir}/icons/hicolor/48x48/mimetypes/application-x-fyre-animation.png
%{_pixmapsdir}/*.png
%{_datadir}/mime/packages/fyre.xml
