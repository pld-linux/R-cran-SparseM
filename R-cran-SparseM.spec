%define		fversion	%(echo %{version} |tr r -)
%define		modulename	SparseM
Summary:	Sparse Linear Algebra
Name:		R-cran-%{modulename}
Version:	1.03
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	b887496ec57bb0dc8c14ad4938560066
URL:		http://www.econ.uiuc.edu/~roger/research/sparse/sparse.html
BuildRequires:	R >= 2.8.1
BuildRequires:	texlive-fonts-cmsuper
BuildRequires:	texlive-latex-ae
BuildRequires:	texlive-latex-bibtex
BuildRequires:	texlive-xetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Basic linear algebra for sparse matrices.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
