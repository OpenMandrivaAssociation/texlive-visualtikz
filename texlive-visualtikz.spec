Name:		texlive-visualtikz
Version:	54080
Release:	2
Summary:	Visual help for TikZ based on images with minimum text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/visualtikz
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/visualtikz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/visualtikz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Visual help for TikZ based on images with minimum text: an
image per command or parameter. The document is in French, but
will be translated into English later.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/visualtikz

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
