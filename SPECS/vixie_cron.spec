Name:          vixie-cron
Version:       3.0pl1
Release:       1
Summary:       First take at creating a RPM package :)
Group:         System/Tools
Vendor:        Paul Vixie / zeamoceq
Distribution:  SailfisfOS
Packager:      juiceme <juice@swagman.org>
URL:           www.dhrider.co.cc

License:       BSD

Source:        vixie-cron-3.0pl1.tar

Buildroot:    /home/nemo/rpmbuild/BUILDROOT/

%description
vixie-crond adaptation to SailfishOS platform

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,sbin}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,5,8}
mkdir -p $RPM_BUILD_ROOT/lib/systemd/system
mkdir -p $RPM_BUILD_ROOT/var/cron
chmod 700 $RPM_BUILD_ROOT/var/cron
install -c -D -m  755 -s $RPM_BUILD_DIR/%{name}-%{version}/cron         $RPM_BUILD_ROOT/usr/sbin/vixie_crond
install -c -D -m 4755 -s $RPM_BUILD_DIR/%{name}-%{version}/crontab      $RPM_BUILD_ROOT/usr/bin/crontab
install -c -D -m  644    $RPM_BUILD_DIR/%{name}-%{version}/cron.service $RPM_BUILD_ROOT/lib/systemd/system/cron.service
install -c -D -m  755    $RPM_BUILD_DIR/%{name}-%{version}/crontab.1    $RPM_BUILD_ROOT/usr/share/man/man1/crontab.1
install -c -D -m  755    $RPM_BUILD_DIR/%{name}-%{version}/cron.8       $RPM_BUILD_ROOT/usr/share/man/man8/cron.8
install -c -D -m  755    $RPM_BUILD_DIR/%{name}-%{version}/crontab.5    $RPM_BUILD_ROOT/usr/share/man/man5/crontab.5

%clean
rm -rf $RPM_BUILD_ROOT

%files

%defattr(111,root,root)
/usr/sbin/vixie_crond
%defattr(4111,root,root)
/usr/bin/crontab
%defattr(644,root,root)
/lib/systemd/system/cron.service
%defattr(755,root,root)
/usr/share/man/man1/crontab.1.gz
/usr/share/man/man8/cron.8.gz
/usr/share/man/man5/crontab.5.gz
%defattr(700,root,root)
/var/cron
 
%post
systemctl enable cron.service
systemctl start cron.service

%preun
systemctl stop cron.service
systemctl disable cron.service
systemctl daemon-reload

