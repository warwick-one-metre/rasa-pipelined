Name:      rasa-pipeline-client
Version:   2.3.0
Release:   0
Url:       https://github.com/warwick-one-metre/rasa-pipelined
Summary:   Pipeline client for the RASA prototype telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  ds9, xpa, xpa-libs
Requires:  python36, python36-Pyro4, python36-pyds9, python36-warwick-observatory-common, python36-warwick-rasa-pipeline

%description
Part of the observatory software for the RASA prototype telescope.

pipeline is a commandline utility for configuring the pipeline.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/pipeline %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/pipeline %{buildroot}/etc/bash_completion.d/pipeline

%files
%defattr(0755,root,root,-)
%{_bindir}/pipeline
/etc/bash_completion.d/pipeline

%changelog
