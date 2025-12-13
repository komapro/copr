%global package_version 0.3.0
%global goipath github.com/Adembc/lazyssh

%define _build_id_links none
%define debug_package %{nil}

Name:           lazyssh
Version:        %{package_version}
Release:        1%{?dist}
Summary:        A terminal-based SSH manager

License:        Apache-2.0
URL:            https://github.com/Adembc/lazyssh
Source0:        %{URL}/archive/refs/tags/v%{package_version}.tar.gz#/%{name}-%{package_version}.tar.gz


BuildRequires: golang >= 1.19
BuildRequires: make
BuildRequires: git-core
BuildRequires: go-rpm-macros

%description
A terminal-based SSH manager inspired by lazydocker and k9s.
Provides an intuitive TUI for managing SSH connections.

%prep
%autosetup -n %{name}-%{package_version}

%build
export VERSION=%{package_version}
%make_build build

%install
install -Dpm 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
