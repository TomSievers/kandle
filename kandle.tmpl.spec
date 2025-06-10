%global commit0 @COMMITHASH0@

Name:           kandle
Version:        @VERSION@
Release:        1.git%{commit0}%{?dist}
Summary:        KiCAD Component Handler CLI

License:        MIT
URL:            https://github.com/TomSievers/kandle
Source0:        https://github.com/TomSievers/kandle/archive/%{commit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  clang-devel

%description

A CLI that handles external components in a KiCad project by automatically importing them into your project symbol, footprint and 3d-model libraries.

It supports files downloaded from several vendors such as: SnapEDA, Ultra Librarian and Component Search Engine

%prep
%setup -q -n kandle-%{commit0}

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install


%files
%attr(0755, root, root) %{_bindir}/*
%license LICENSE

%changelog
* Tue Jun 10 2025 tom
- 
