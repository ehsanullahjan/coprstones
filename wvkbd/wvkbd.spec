Name:           wvkbd
Version:        0.20
Release:        1%{?dist}
Summary:        On-screen keyboard for wlroots compositors

License:        GPL-3.0-only
URL:            https://github.com/jjsullivan5196/wvkbd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  scdoc

%description
wvkbd is a Wayland virtual keyboard tailored for wlroots compositors.

%prep
%autosetup
sed -i 's/^CFLAGS = /CFLAGS += /' config.mk

%build
export CFLAGS="${CFLAGS} -fPIE"
export LDFLAGS="${LDFLAGS} -pie"
%make_build PREFIX=%{_prefix} LAYOUT=mobintl
%make_build PREFIX=%{_prefix} LAYOUT=deskintl

%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir} LAYOUT=mobintl
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir} LAYOUT=deskintl
ln -s wvkbd-mobintl %{buildroot}%{_bindir}/wvkbd
ln -s wvkbd.1 %{buildroot}%{_mandir}/man1/wvkbd-mobintl.1
ln -s wvkbd.1 %{buildroot}%{_mandir}/man1/wvkbd-deskintl.1

%files
%{_bindir}/wvkbd
%{_bindir}/wvkbd-mobintl
%{_bindir}/wvkbd-deskintl
%{_mandir}/man1/wvkbd.1*
%{_mandir}/man1/wvkbd-mobintl.1*
%{_mandir}/man1/wvkbd-deskintl.1*
%license LICENSE

%changelog
* Fri Oct 23 2026 ehsanj <ehsanullahjan@gmail.com> - 0.20-1
- Initial packaging for Graystone: https://github.com/ehsanullahjan/graystone
