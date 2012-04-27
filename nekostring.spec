%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define git_snapshot gitc677b77
%endif


Name:       nekostring
Summary:    70's String Ensemble DSSI plugin
Version:    0.1.1

%if %branch
Release:        0.%git_snapshot.1
%else
Release:        1
%endif

Source:     https://github.com/gordonjcp/nekostring/gordonjcp-nekostring-c677b77.tar.gz
URL:        https://github.com/gordonjcp/nekostring
License:    GPLv2
Group:      Sound

BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-2.0)

%description
70's String Ensemble DSSI plugin

%prep
%setup -q -n gordonjcp-nekostring-c677b77

%build

%if %branch
autoreconf -i
%endif

%configure --with-dssi-dir=%{buildroot}%{_libdir}/dssi --disable-static

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%defattr(-,root,root)
%doc COPYING README
%_bindir/*
%_libdir/dssi/*
