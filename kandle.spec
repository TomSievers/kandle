Name:           kandle
Version:        0.1
Release:        1%{?dist}
Summary:        KiCAD Component Handler CLI

License:        MIT
URL:            https://github.com/TomSievers/kandle
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  clang-devel

%description

A CLI that handles external components in a KiCad project by automatically importing them into your project symbol, footprint and 3d-model libraries.

It supports files downloaded from several vendors such as: SnapEDA, Ultra Librarian and Component Search Engine

%prep
%autosetup

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install


%files
%attr(0755, root, root) %{_bindir}/*
%license LICENCE

%changelog

