Summary:	UCL Network Text Editor
Summary(pl.UTF-8):   Sieciowy edytor tekstu
Name:		nte
Version:	1.7.0
Release:	1
License:	custom
Group:		X11/Applications/Multimedia
#Source0Download: http://www-mice.cs.ucl.ac.uk/multimedia/software/nte/download.html
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/nte/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cd94f5c588ab31c630a1ef98f5007e28
Source1:	%{name}-COPYRIGHT
Patch0:		%{name}-paths.patch
Patch1:		%{name}-optflags.patch
Patch2:		%{name}-no_tk_ext.patch
Patch3:		%{name}-stdio.patch
URL:		http://www-mice.cs.ucl.ac.uk/multimedia/software/nte/
BuildRequires:	tcl-devel >= 8.3
BuildRequires:	tk-devel >= 8.3
BuildRequires:	ucl-common-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debugcflags	-O1 -g

%description
NTE is a shared text editor designed for use on the Mbone.

%description -l pl.UTF-8
NTE to sieciowy edytor tekstu, stworzony do użytku w Mbone.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -r src/text2html
rm -r src/tcl2c
cd linux
sh ./configure
%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install linux/nte $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/{CHANGES,KNOWN_BUGS} COPYRIGHT
%attr(755,root,root) %{_bindir}/*
