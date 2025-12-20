%global forgeurl https://gitlab.com/hyask/swaysome
%global tag 2.3.2

%define _build_id_links none
%define debug_package %{nil}

Name:           swaysome
Version:        %{tag}
Release:        1%{?dist}
Summary:        AwesomeWM-like workspaces for sway

%forgemeta

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}


BuildRequires: git-core
BuildRequires: rust
BuildRequires: cargo

%description
This binary helps you configure sway to work a bit more like AwesomeWM. This means that workspaces are namespaced in what are called workspace groups, and workspace groups can be moved around the differents outputs easily.

For example, with workspace 11 on the first output, and workspace 21 on the second output, triggering the swaysome focus 1 shortcut to get workspace 1 would lead you to workspace 11 if your focus is on the first output, and workspace 21 is the focus is on the second one.

By default, swaysome init will create a workspace group per active output, but you may create other groups while working, by either triggering swaysome focus-group <new-number> and opening a new window, or sending an existing window to it first with swaysome move-to-group <new-number>.

%prep
%autosetup -n %{name}-%{tag}

%build
cargo build --release --bin %{name}

%install
install -Dpm 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 swaysome.1 %{buildroot}%{_mandir}/man1/swaysome.1

%files
%license LICENSE
%doc README.md
%doc HACKING.md
%{_mandir}/man1/swaysome.1.gz
%{_bindir}/%{name}

%changelog
%autochangelog
