Name:      rasa-pipeline-server
Version:   2.2.8
Release:   0
Url:       https://github.com/warwick-one-metre/rasa-pipelined
Summary:   Data pipeline server for the RASA prototype telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires: nfs-utils
Requires: python34, python34-Pyro4, python34-pyds9, python34-sep, python34-Pillow
Requires: python34-warwick-rasa-pipeline, python34-warwick-observatory-common, observatory-log-client

%description
Part of the observatory software for the RASA prototype telescope.

pipelined manages the data pipeline for frames after they have been acquired.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/pipelined %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/pipelined.service %{buildroot}%{_unitdir}

%pre
%if 0%{?suse_version}
%service_add_pre pipelined.service
%endif

%post
%if 0%{?suse_version}
%service_add_post pipelined.service
%endif
%if 0%{?centos_ver}
%systemd_post pipelined.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal pipelined.service
%service_del_preun pipelined.service
%endif
%if 0%{?centos_ver}
%systemd_preun pipelined.service
%endif

%postun
%if 0%{?suse_version}
%restart_on_update pipelined.service
%service_del_postun pipelined.service
%endif
%if 0%{?centos_ver}
%systemd_postun_with_restart pipelined.service
%endif

%files
%defattr(0755,root,root,-)
%{_bindir}/pipelined
%defattr(0644,root,root,-)
%{_unitdir}/pipelined.service

%changelog
