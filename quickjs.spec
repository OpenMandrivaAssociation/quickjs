%define devname %mklibname -d %{name}

Name:           quickjs
Version:        2026.06.04
# Upstream tarball uses hyphens: quickjs-2026-06-04.tar.xz
%define ver %(echo %{version} | sed -e 's,\\.,-,g')
Release:        1
Summary:        Small and embeddable Javascript engine
Group:          Networking/WWW
License:        MIT
URL:            https://bellard.org/quickjs/
Source0:        https://bellard.org/quickjs/quickjs-%{ver}.tar.xz
#Patch0:          0001-Set-build-flags.patch
#Patch1:          0002-Fix-linking.patch
Patch2:          0003-Install-static-lib-to-usr-lib64-on-64-bit-arches.patch
BuildRequires:  make
#Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description
QuickJS is a small and embeddable Javascript engine and compiler that supports reference ES2025.

%package -n %{devname}
Summary:        Development headers for quickjs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}  = %{version}-%{release}

%description -n %{devname}
Development headers for quickjs

%prep
%autosetup -n quickjs-%{ver} -p1

%build
# clang LTO so clang embedders can link; -fPIC for shared objects such as njs
export CFLAGS="%{optflags} -fPIC"
# example .so modules resolve JS_* from the host at load time
export LDFLAGS="${LDFLAGS//-Wl,--no-undefined/}"
%make_build PREFIX=%{_prefix} LIBDIR=%{_lib} CONFIG_CLANG=y CONFIG_LTO=y

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib} CONFIG_CLANG=y CONFIG_LTO=y STRIP=%{_bindir}/true

%files
%{_bindir}/qjs
%{_bindir}/qjsc

%files -n %{devname}
%{_includedir}/%{name}/
%dir %{_libdir}/%{name}/
%{_libdir}/quickjs/libquickjs{,.lto}.a
