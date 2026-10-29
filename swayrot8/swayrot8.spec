Name:           swayrot8
Version:        1.0.0
Release:        1%{?dist}
Summary:        Tablet auto-rotation daemon for SwayWM

License:        MIT
URL:            https://github.com/ehsanullahjan/swayrot8
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       sway
Requires:       iio-sensor-proxy

%description
swayrot8 is a simple auto-rotation daemon for tablets and 2-in-1 laptops
running SwayWM. It integrates with monitor-sensor (iio-sensor-proxy) to
rotate the screen based on accelerometer data.

%prep
%autosetup

%install
install -Dm755 swayrot8 %{buildroot}%{_libexecdir}/swayrot8
install -Dm644 sway-rot8.service %{buildroot}%{_usr}/lib/systemd/user/sway-rot8.service
install -Dm644 config.example %{buildroot}%{_sysconfdir}/swayrot8/config

%files
%{_libexecdir}/swayrot8
%{_usr}/lib/systemd/user/sway-rot8.service
%dir %{_sysconfdir}/swayrot8
%config(noreplace) %{_sysconfdir}/swayrot8/config
%license LICENSE
%doc README.md

%changelog
* Thu Oct 29 2026 ehsanj <ehsanullahjan@gmail.com> - 1.0.0-1
- Initial packaging for Graystone: https://github.com/ehsanullahjan/graystone
