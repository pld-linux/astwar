Summary: 	AstWar is a terminal based 2D space shooter
Summary(pl):	AstWar to terminalowa strzelanina kosmiczna 2D
Name:		astwar
Version:	0.4.5
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://freesoftware.fsf.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	09f9cccaea530e78eeb0bcfef796142e
URL:		http://www.freesoftware.fsf.org/%{name}/index.html
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
 
%description
Astwar is a ncurses based simple space shooter; two little ships
(asterisks), each on one side of the screen, try to shoot each other.
There is network support with several multiplayer options and user
extension with Scheme (via Guile) to program the little ship to do
some things automatically are in the works.

%description -l pl
Astwar to oparta na ncurses prosta strzelanina kosmiczna. Dwa ma³e
statki (gwiazdki), ka¿dy z innej strony ekranu, próbuj± siê
zastrzeliæ. Gra ma obs³ugê sieci z kilkoma opcjami gry dla wielu
graczy i pozwala na rozszerzenia w Scheme (poprzez Guile), aby
zaprogramowaæ statek, by robi³ niektóre rzeczy automatycznie.

%prep
%setup -q

%build
%configure2_13 
%{__make} INCLUDES=-I/usr/include/ncurses

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/astwar
%doc AUTHORS COPYING ChangeLog README
%{_infodir}/*
%{_mandir}/man1/*
