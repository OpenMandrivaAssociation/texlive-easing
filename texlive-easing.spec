%global tl_name easing
%global tl_revision 75712

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Easing functions for pgfmath
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/easing
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easing.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easing.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/easing.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This library implements a collection of easing functions and adds them
to the PGF mathematical engine.

