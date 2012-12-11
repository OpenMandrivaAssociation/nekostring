%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define git_snapshot gitc677b77
%endif


Name:       nekostring
Summary:    70's String Ensemble DSSI plugin
Version:    0.1.1

%if %branch
Release:        0.%git_snapshot.2
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

%make bindir=%{_libdir}/dssi/%name

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall bindir=%{buildroot}%{_libdir}/dssi/%name

%files
%defattr(-,root,root)
%doc COPYING README
%_libdir/dssi/*



%changelog
* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 0.1.1-0.gitc677b77.2
+ Revision: 794050
- fixed GUI binary installation path

* Fri Apr 27 2012 Frank Kober <emuse@mandriva.org> 0.1.1-0.gitc677b77.1
+ Revision: 793852
- imported package nekostring

