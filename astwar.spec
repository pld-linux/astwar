Summary: 	AstWar is a terminal based 2D space shooter.
Name:		astwar
Version:	0.4.5
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://freesoftware.fsf.org/download/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.freesoftware.fsf.org/%{name}/index.html
BuildRequires:	ncurses-devel
Requires: 	ncurses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
 
%description
Astwar is a ncurses based simple space shooter; two little 
ships (asterisks), each on one side of the screen, try to 
shoot each other. There is network support with several 
multiplayer options and user extension with Scheme (via Guile)
to program the little ship to do some things automatically are 
in the works.

%prep
%setup -q

%build
%configure2_13 
%{__make} INCLUDES=-I%{_includedir}/ncurses

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/astwar
%doc AUTHORS COPYING ChangeLog README
%{_infodir}/*
%lang(en) %{_mandir}/man1/*
