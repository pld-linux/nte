Summary:	UCL Network Text Editor
Name:		nte
Version:	1.7.0
Release:	1
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www-mice.cs.ucl.ac.uk/multimedia/software/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-COPYRIGHT
Patch0:		%{name}-paths.patch
Patch1:		%{name}-optflags.patch
Patch2:		%{name}-no_tk_ext.patch
Patch3:		%{name}-stdio.patch
URL:		http://www-mice.cs.ucl.ac.uk/multimedia/software/
License:	Custom
BuildRequires:	ucl-common-devel
BuildRequires:	tcl-devel >= 8.3
BuildRequires:	tk-devel >= 8.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NTE is a shared text editor designed for use on the Mbone.

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
%{__make} OPTFLAGS="%{!?debug:%{rpmcflags}} %{?debug:-O1 -g}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install linux/nte $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} COPYRIGHT

gzip -9nf src/{CHANGES,KNOWN_BUGS} COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/CHANGES* src/KNOWN_BUGS* src/CHANGES*
%attr(755,root,root) %{_bindir}/*