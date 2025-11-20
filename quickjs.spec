%define ver     2025-
%define commit  9688007ccbba2024b339ddcd52044b23e2a4d982
%define gitdate 20251105

%define rel	2

%define devname %mklibname -d %{name}

Name:           quickjs
Version:        2025.
Release:        %mkrel %{?gitdate:-c 0git%{gitdate}} %{rel}
Summary:        Small and embeddable Javascript engine
Group:          Networking/WWW
License:        MIT
URL:            https://bellard.org/quickjs/
Source0:        https://github.com/bellard/quickjs/archive/%{commit}.tar.gz
Patch:          0001-Set-build-flags.patch
Patch:          0002-Fix-linking.patch
Patch:          0003-Install-static-lib-to-usr-lib64-on-64-bit-arches.patch
BuildRequires:  gcc
BuildRequires:  make
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description
QuickJS is a small and embeddable JavaScript engine and compiler that supports reference ES2020.

%package -n %{devname}
Summary:        Development headers for quickjs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-devel < 2025.09.13-0.0git20251105.2
Conflicts:      %{name} < 2025.09.13-0.0git20251105.2

%description -n %{devname}
Development headers for quickjs

%prep
%autosetup -n %{name}-%{?gitdate:%commit}%{!?gitdate:%ver} -p1

%build
%make_build PREFIX=%{_prefix} LIBDIR=%{_lib} CONFIG_LTO=y

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib} CONFIG_LTO=y STRIP=%{_bindir}/true

%files
%{_bindir}/qjs
%{_bindir}/qjsc

%files -n %{devname}
%{_includedir}/%{name}/
%dir %{_libdir}/%{name}/
%{_libdir}/quickjs/libquickjs{,.lto}.a
