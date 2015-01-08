Summary:       Fan Control Daemon for Mac Mini's.
Name:          cmp-daemon
Version:       0.0.3
Release:       1%{?dist}
License:       MIT

URL:           https://github.com/seryl/cmp-daemon
Source0:       https://github.com/seryl/%{name}/archive/v%{version}.tar.gz
BuildRequires: gcc


%description
Mac Mini Fan Controller for centos6/7


%prep
%setup -q -n %{name}-%{version}

%build
/bin/gcc -Wall %{name}.c -o %{name}

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}

# Install cmp-daemon service
install -d %{buildroot}%{_unitdir}
install -p -m 644 %{name}.service %{buildroot}%{_unitdir}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%pre
/usr/sbin/modprobe applesmc -v

%post
/bin/systemctl daemon-reload
/bin/systemctl enable %{name}
/bin/systemctl start %{name}

%preun
if [ $1 = 0 ] ; then
  /bin/systemctl stop %{name} >/dev/null 2>&1
  /bin/systemctl daemon-reload
fi

%changelog
* Wed Jan 7 2015 Josh Toft <joshtoft@gmail.com> - 0.0.3
- Rpm build completes

* Wed Jan 7 2015 Josh Toft <joshtoft@gmail.com> - 0.0.1
- Initial rpm spec
