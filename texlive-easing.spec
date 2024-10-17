Name:		texlive-easing
Version:	59975
Release:	2
Summary:	easing functions for pgfmath
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/easing
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easing.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easing.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/easing.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This library implements a collection of easing functions and
adds them to the PGF mathematical engine.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/easing
%{_texmfdistdir}/tex/latex/easing
%doc %{_texmfdistdir}/doc/latex/easing

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
