%global tl_name visualtikz
%global tl_revision 54080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.65
Release:	%{tl_revision}.1
Summary:	Visual help for TikZ based on images with minimum text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/visualtikz
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/visualtikz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/visualtikz.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Visual help for TikZ based on images with minimum text: an image per
command or parameter. The document is in French, but will be translated
into English later.

