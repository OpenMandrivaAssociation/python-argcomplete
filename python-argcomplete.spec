Name:		python-argcomplete
Version:	3.5.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/argcomplete/argcomplete-%{version}.tar.gz
Summary:	Bash tab completion for argparse
URL:		https://pypi.org/project/argcomplete/
License:	Apache Software License
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildSystem:	python
BuildArch:	noarch

%description
Bash tab completion for argparse

%files
%{_bindir}/activate-global-python-argcomplete
%{_bindir}/python-argcomplete-check-easy-install-script
%{_bindir}/register-python-argcomplete
%{py_sitedir}/argcomplete
%{py_sitedir}/argcomplete-*.*-info
