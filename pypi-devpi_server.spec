#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-devpi_server
Version  : 6.8.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/41/fa/aa3e4d4d3725baf9d83d7d8cb1f34db68584867eee8f7e40115bb3c85e85/devpi-server-6.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/41/fa/aa3e4d4d3725baf9d83d7d8cb1f34db68584867eee8f7e40115bb3c85e85/devpi-server-6.8.0.tar.gz
Summary  : devpi-server: reliable private and pypi.org caching server
Group    : Development/Tools
License  : MIT
Requires: pypi-devpi_server-bin = %{version}-%{release}
Requires: pypi-devpi_server-license = %{version}-%{release}
Requires: pypi-devpi_server-python = %{version}-%{release}
Requires: pypi-devpi_server-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=============================================================================
devpi-server: server for private package indexes and PyPI caching
=============================================================================

%package bin
Summary: bin components for the pypi-devpi_server package.
Group: Binaries
Requires: pypi-devpi_server-license = %{version}-%{release}

%description bin
bin components for the pypi-devpi_server package.


%package license
Summary: license components for the pypi-devpi_server package.
Group: Default

%description license
license components for the pypi-devpi_server package.


%package python
Summary: python components for the pypi-devpi_server package.
Group: Default
Requires: pypi-devpi_server-python3 = %{version}-%{release}

%description python
python components for the pypi-devpi_server package.


%package python3
Summary: python3 components for the pypi-devpi_server package.
Group: Default
Requires: python3-core
Provides: pypi(devpi_server)
Requires: pypi(aiohttp)
Requires: pypi(argon2_cffi)
Requires: pypi(attrs)
Requires: pypi(defusedxml)
Requires: pypi(devpi_common)
Requires: pypi(itsdangerous)
Requires: pypi(lazy)
Requires: pypi(passlib)
Requires: pypi(platformdirs)
Requires: pypi(pluggy)
Requires: pypi(py)
Requires: pypi(pyramid)
Requires: pypi(repoze.lru)
Requires: pypi(ruamel.yaml)
Requires: pypi(strictyaml)
Requires: pypi(waitress)

%description python3
python3 components for the pypi-devpi_server package.


%prep
%setup -q -n devpi-server-6.8.0
cd %{_builddir}/devpi-server-6.8.0
pushd ..
cp -a devpi-server-6.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680184484
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-devpi_server
cp %{_builddir}/devpi-server-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-devpi_server/cf3eaf29116a37a7d9ba773e776104c067c8e5fc || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/devpi-export
/usr/bin/devpi-fsck
/usr/bin/devpi-gen-config
/usr/bin/devpi-gen-secret
/usr/bin/devpi-import
/usr/bin/devpi-init
/usr/bin/devpi-passwd
/usr/bin/devpi-server

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-devpi_server/cf3eaf29116a37a7d9ba773e776104c067c8e5fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
