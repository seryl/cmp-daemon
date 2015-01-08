Summary:       Fan Control Daemon for Mac Mini's.
Name:          cmp-daemon
Version:       0.0.1
Release:       1%{?dist}
License:       MIT

URL:           https://github.com/seryl/cmp-daemon
Source0:       https://github.com/seryl/%{name}/archive/v%{version}.tar.gz
BuildRequires: gcc


%description
Mac Mini Fan Controller for centos6/7


%prep
%setup -c -n cmp-daemon

%build
gcc -Wall cmp-daemon.c -o cmp-daemon

%install
install -p -m 755 %{buildroot}%{_bindir}/cmp-daemon

# Install cmp-daemon service
install -d %{buildroot}%{_unitdir}
install -p -m 644 cmp-daemon.service %{buildroot}%{_unitdir}

%files
%defattr(-,root,root,-)
%{_bindir}/cmp-daemon
%{_unitdir}/cmp-daemon.service

%pre
/usr/sbin/modprobe applesmc -v

%post
/bin/systemctl daemon-reload
/bin/systemctl enable cmp-daemon
/bin/systemctl start cmp-daemon

%preun
if [ $1 = 0 ] ; then
  /bin/systemctl stop cmp-daemon >/dev/null 2>&1
  /bin/systemctl daemon-reload
fi

%changelog
* Wed Jan 7 2015 Josh Toft <joshtoft@gmail.com> - 0.0.1
- Initial rpm spec
