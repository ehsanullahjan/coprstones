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
wvkbd is a Wayland virtual keyboard tailored for wlroots compositors, featuring text-input-v3 support.

%prep
%autosetup

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir}
ln -s wvkbd-mobintl %{buildroot}%{_bindir}/wvkbd

%files
%{_bindir}/wvkbd-mobintl
%{_bindir}/wvkbd
%{_mandir}/man1/wvkbd.1*
%license LICENSE

%changelog
* Fri Oct 23 2026 ehsanj <ehsanullahjan@gmail.com> - 0.20-1
- Initial packaging for Graystone: https://github.com/ehsanullahjan/graystone
