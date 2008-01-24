Summary:	AstWar is a terminal based 2D space shooter
Summary(pl.UTF-8):	AstWar to terminalowa strzelanina kosmiczna 2D
Name:		astwar
Version:	0.4.5
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://freesoftware.fsf.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	09f9cccaea530e78eeb0bcfef796142e
URL:		http://www.freesoftware.fsf.org/astwar/index.html
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Astwar is a ncurses based simple space shooter; two little ships
(asterisks), each on one side of the screen, try to shoot each other.
There is network support with several multiplayer options and user
extension with Scheme (via Guile) to program the little ship to do
some things automatically are in the works.

%description -l pl.UTF-8
Astwar to oparta na ncurses prosta strzelanina kosmiczna. Dwa małe
statki (gwiazdki), każdy z innej strony ekranu, próbują się
zastrzelić. Gra ma obsługę sieci z kilkoma opcjami gry dla wielu
graczy i pozwala na rozszerzenia w Scheme (poprzez Guile), aby
zaprogramować statek, by robił niektóre rzeczy automatycznie.

%prep
%setup -q

%build
%configure2_13

%{__make} INCLUDES=-I/usr/include/ncurses

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/astwar
%{_infodir}/*.info*
%{_mandir}/man1/*
