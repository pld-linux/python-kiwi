# TODO:
# - doublecheck this, as almost raw stolen from FC
# - py_postclean?
#
%define		module	kiwi
Summary:	Framework for Python GUI applications
Summary(pl.UTF-8):	Szkielet do budowania GUI w Pythonie
Name:		python-%{module}
Version:	1.9.19
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://download.gnome.org/sources/kiwi/1.9/%{module}-%{version}.tar.bz2
# Source0-md5:	6c721d501ca3da121fb6c74c98231ef5
URL:		http://www.async.com.br/projects/kiwi/
BuildRequires:	gettext-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygtk-devel >= 2:2.8
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig
%pyrequires_eq	python-libs
Requires:	python-pygtk-gtk >= 2:2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kiwi consists of a set of classes and wrappers for PyGTK that were
developed to provide a sort of framework for applications. Fully
object-oriented, and roughly Smalltalk's MVC, Kiwi provides a simple,
practical way to build forms, windows and widgets that transparently
access and display your object data.

%description -l pl.UTF-8
Kiwi składa się ze zbioru klas i wrapperów dla PyGTK które zostały
napisane by dostarczać pewnego rodzaju szkielet dla aplikacji. Kiwi,
będąc w pełni zorientowanym obiektowo i z grubsza zainspirowanym MVC w
Smalltalku, dostarcza prosty i praktyczny sposób do budowania
formatek, okienek i kontrolek które w przezroczysty sposób pobierają i
wyświetlają dane.

%package gazpacho
Summary:	Gazpacho integration for kiwi
Summary(pl.UTF-8):	Integracja Gazpacho dla kiwi
Group:		Development/Libraries
Requires:	gazpacho >= 0.6.6
Requires:	%{name} = %{version}-%{release}

%description gazpacho
This package contains additional files necessary for integration with
Gazpacho glade editor.

%description gazpacho -l pl.UTF-8
Ten pakiet zawiera dodatkowe pliki koniecznie dla integracji z
edytorem plików glade Gazpacho.

%package docs
Summary:	Documentation related to python-kiwi
Summary(pl.UTF-8):	Dokumentacja związana z python-kiwi
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description docs
This package contains documentation that contains APIs and related
materials, useful for reference when writing software using Kiwi.

%description docs -l pl.UTF-8
Ten pakiet zawiera dokumentację opisującą API i związane z nim
materiały, użyteczne podczas pisania oprogramowania używającego Kiwi.

%prep
%setup -q -n %{module}-%{version}
sed -i -e 's|share/doc/kiwi|share/doc/%{name}-%{version}|' setup.py

%build
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	-O1 \
	--skip-build \
	--root $RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}

# The install script mis-guesses where gazpacho is installed on
# non-x86 platforms
if [ "%{python_sitearch}" != "%{py_sitedir}" ]; then
	mv $RPM_BUILD_ROOT%{python_sitearch}/gazpacho \
		$RPM_BUILD_ROOT%{py_sitedir}
fi

%find_lang kiwi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kiwi.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/kiwi
%{py_sitedir}/kiwi

%files gazpacho
%defattr(644,root,root,755)
%{py_sitescriptdir}/gazpacho/widgets/*
%{_datadir}/gazpacho/catalogs/*
%{_datadir}/gazpacho/resources/*

%files docs
%defattr(644,root,root,755)
%doc doc/* examples
