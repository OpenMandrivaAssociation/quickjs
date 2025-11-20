%define ver     2025-11-15
%define commit  fcbf5ea2a63510f35f9ab2baadd59781be16a167
%define gitdate 20251115

%define devname %mklibname -d %{name}

Name:           quickjs
Version:        2025.11.15
Release:        1
Summary:        Small and embeddable Javascript engine
Group:          Networking/WWW
License:        MIT
URL:            https://bellard.org/quickjs/
Source0:        https://github.com/bellard/quickjs/archive/%{name}-%{commit}.tar.gz
#Patch0:          0001-Set-build-flags.patch
#Patch1:          0002-Fix-linking.patch
#Patch2:          0003-Install-static-lib-to-usr-lib64-on-64-bit-arches.patch
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
%autosetup -n quickjs-%{commit} -p1

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
