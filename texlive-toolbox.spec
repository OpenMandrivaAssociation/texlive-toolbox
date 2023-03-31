Name:		texlive-toolbox
Version:	32260
Release:	2
Summary:	Tool macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/toolbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/toolbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/toolbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/toolbox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for (La)TeX which provides some macros which are
convenient for writing indexes, glossaries, or other macros. It
contains macros which support: implicit macros; fancy optional
arguments; loops over tokenlists and itemlists; searching and
splitting; controlled expansion; redefinition of macros; and
concatenated macro names; macros for text replacement.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/toolbox/toolbox.sty
%doc %{_texmfdistdir}/doc/latex/toolbox/README
%doc %{_texmfdistdir}/doc/latex/toolbox/toolbox.pdf
%doc %{_texmfdistdir}/doc/latex/toolbox/toolbox.tex
%doc %{_texmfdistdir}/doc/latex/toolbox/toolbox.txt
#- source
%doc %{_texmfdistdir}/source/latex/toolbox/toolbox.dtx
%doc %{_texmfdistdir}/source/latex/toolbox/toolbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
