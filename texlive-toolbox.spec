# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/toolbox
# catalog-date 2008-02-29 19:54:55 +0100
# catalog-license lppl
# catalog-version 5.1
Name:		texlive-toolbox
Version:	5.1
Release:	1
Summary:	Macros for writing indices, glossaries
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/toolbox
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/toolbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/toolbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/toolbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package for (La)TeX which provides some macros which are
convenient for writing indices, glossaries, or other macros. It
contains macros which support: implicit macros; fancy optional
arguments; loops over tokenlists and itemlists; searching and
splitting; controlled expansion; redefinition of macros; and
concatenated macro names; macros for text replacement.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/toolbox/toolbox.sty
%doc %{_texmfdistdir}/doc/latex/toolbox/README
%doc %{_texmfdistdir}/doc/latex/toolbox/toolbox.tex
%doc %{_texmfdistdir}/doc/latex/toolbox/toolbox.txt
#- source
%doc %{_texmfdistdir}/source/latex/toolbox/toolbox.dtx
%doc %{_texmfdistdir}/source/latex/toolbox/toolbox.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
