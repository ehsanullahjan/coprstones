Name:           lisgd
Version:        0.4.0
Release:        1%{?dist}
Summary:        Libinput synthetic gesture daemon for Wayland

License:        MIT
URL:            https://git.sr.ht/~mil/lisgd
Source0:        %{url}/archive/%{version}.tar.gz
Source1:        70-touchscreen.rules

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(wayland-client)

%description
lisgd provides gesture support for touchscreens on Wayland compositors.

This package is built explicitly for Wayland (no X11 support), and bundles
hardware-agnostic udev rules to automatically map I2C and SPI touchscreens.

%prep
%autosetup

%build
export CFLAGS="${CFLAGS} -fPIE"
export LDFLAGS="${LDFLAGS} -pie"

%make_build CPPFLAGS="-DWITH_WAYLAND" LIBS="-linput -lm -lwayland-client" CC="gcc"

%install
%make_install PREFIX=%{_prefix}

install -Dm 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/70-touchscreen.rules

%files
%license LICENSE
%doc README.md
%{_bindir}/lisgd
%{_udevrulesdir}/70-touchscreen.rules
%{_mandir}/man1/lisgd.1*

%changelog
* Fri Nov 06 2026 ehsanj <ehsanullahjan@gmail.com> - 0.4.0-1
- Initial packaging for Graystone: https://github.com/ehsanullahjan/graystone
- Compile Wayland-only backend, drop X11 dependencies
- Bundle hardware-agnostic udev rules for I2C and SPI digitizers
