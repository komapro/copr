%global package_version 1.4.0
%global goipath https://github.com/yorukot/superfile

%define _build_id_links none
%define debug_package %{nil}

%global bin_name spf

Name:           superfile
Version:        %{package_version}
Release:        1%{?dist}
Summary:        Pretty fancy and modern terminal file manager

License:        MIT
URL:            %{goipath}
Source0:        %{URL}/archive/refs/tags/v%{package_version}.tar.gz#/%{name}-%{package_version}.tar.gz

BuildRequires: golang
BuildRequires: git-core
BuildRequires: go-rpm-macros

%description
Pretty fancy and modern terminal file manager.

%prep
%autosetup -n %{name}-%{package_version}

%build
./build.sh

%install
install -Dpm 0755 bin/%{bin_name} %{buildroot}%{_bindir}/%{bin_name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{bin_name}

%changelog
%autochangelog
