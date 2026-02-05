%define module argcomplete

Name:		python-argcomplete
Version:	3.6.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Bash tab completion for argparse
URL:		https://pypi.org/project/argcomplete/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
Bash tab completion for argparse

%files
%{_bindir}/activate-global-python-argcomplete
%{_bindir}/python-argcomplete-check-easy-install-script
%{_bindir}/register-python-argcomplete
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
