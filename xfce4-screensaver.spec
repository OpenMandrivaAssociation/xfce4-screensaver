%define url_ver	%(echo %{version} | cut -d. -f1,2)

Name:		xfce4-screensaver
Summary:	Screen saver and locker for Xfce4
Version:	0.1.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://git.xfce.org/apps/xfce4-screensaver/about/
Source0:	https://archive.xfce.org/src/apps/xfce4-screensaver/%{url_ver}/xfce4-screensaver-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(garcon-gtk3-1)
BuildRequires:	pam-devel

%description
xfce4-screensaver is a screen saver and locker that aims to have simple, sane,
secure defaults and be well integrated with the desktop.

xfce4-screensaver is a port of MATE Screensaver, itself a port of GNOME
Screensaver. It has been tightly integrated with the Xfce desktop, utilizing
Xfce libraries and the Xfconf configuration backend.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-systemd \
	--enable-locking
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%{_sysconfdir}/pam.d/xfce4-screensaver
%{_sysconfdir}/xdg/autostart/xfce4-screensaver.desktop
%{_sysconfdir}/xdg/menus/xfce4-screensavers.menu
%{_bindir}/xfce4-screensaver
%{_bindir}/xfce4-screensaver-command
%{_bindir}/xfce4-screensaver-preferences
%{_libdir}/pkgconfig/xfce4-screensaver.pc
%{_libexecdir}/xfce4-screensaver-dialog
%{_libexecdir}/xfce4-screensaver-gl-helper
%dir %{_libexecdir}/xfce4-screensaver/
%{_libexecdir}/xfce4-screensaver/floaters
%{_libexecdir}/xfce4-screensaver/popsquares
%{_libexecdir}/xfce4-screensaver/slideshow
%{_datadir}/applications/screensavers/personal-slideshow.desktop
%{_datadir}/applications/screensavers/popsquares.desktop
%{_datadir}/applications/screensavers/xfce-floaters.desktop
%{_datadir}/applications/xfce4-screensaver-preferences.desktop
%{_datadir}/dbus-1/services/org.xfce.ScreenSaver.service
%{_datadir}/desktop-directories/xfce4-screensaver.directory
%{_mandir}/man1/xfce4-screensaver-command.1*
%{_mandir}/man1/xfce4-screensaver-preferences.1*
%{_mandir}/man1/xfce4-screensaver.1*
%{_datadir}/pixmaps/xfce-logo-white.svg
