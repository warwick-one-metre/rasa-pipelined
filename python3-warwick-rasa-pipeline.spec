Name:           python3-warwick-rasa-pipeline
Version:        1.1.1
Release:        0
License:        GPL3
Summary:        Common backend code for the RASA prototype telescope pipeline daemon
Url:            https://github.com/warwick-one-metre/rasa-pipelined
BuildArch:      noarch

%description
Part of the observatory software for the RASA prototype telescope.

python36-warwick-rasa-pipeline holds the common pipeline code.

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
