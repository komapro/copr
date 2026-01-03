%global package_version 0.7.2

%define _build_id_links none
%define debug_package %{nil}

Name:           metapac
Version:        %{package_version}
Release:        1%{?dist}
Summary:        Multi-backend declarative package manager

License:        GPL-3.0-or-later
URL:            https://github.com/ripytide/metapac
Source0:        %{URL}/archive/refs/tags/v%{package_version}.tar.gz#/%{name}-%{package_version}.tar.gz


BuildRequires: git-core
BuildRequires: rust
BuildRequires: cargo

%description
metapac allows you to maintain a consistent set of packages across multiple machines. It also makes setting up a new system with your preferred packages from your preferred package managers much easier.

%prep
%autosetup -n %{name}-%{package_version}

%build
cargo build --release --bin %{name}

%install
install -Dpm 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
