%global tl_name toolbox
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.1
Release:	%{tl_revision}.1
Summary:	Tool macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/toolbox
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/toolbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/toolbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/toolbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for (La)TeX which provides some macros which are convenient
for writing indexes, glossaries, or other macros. It contains macros
which support: implicit macros; fancy optional arguments; loops over
tokenlists and itemlists; searching and splitting; controlled expansion;
redefinition of macros; and concatenated macro names; macros for text
replacement.

