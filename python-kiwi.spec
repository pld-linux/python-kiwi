%define		module	kiwi
Summary:	Framework for Python GUI applications
Summary(pl.UTF-8):	Szkielet do budowania GUI w Pythonie
Name:		python-%{module}
Version:	1.9.26
Release:	7
License:	LGPL
Group:		Libraries/Python
Source0:	http://download.gnome.org/sources/kiwi/1.9/%{module}-%{version}.tar.bz2
# Source0-md5:	43c2aab9acf8d95321ee1ccec2c5e4e4
Patch0:		%{name}_es_locale_fix.patch
URL:		http://www.async.com.br/projects/kiwi/
BuildRequires:	gettext-tools
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel >= 2:2.8
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
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
Requires:	%{name} = %{version}-%{release}
Requires:	gazpacho >= 0.6.6

%description gazpacho
This package contains additional files necessary for integration with
Gazpacho glade editor.

%description gazpacho -l pl.UTF-8
Ten pakiet zawiera dodatkowe pliki koniecznie dla integracji z
edytorem plików glade Gazpacho.

%package doc
Summary:	Documentation related to python-kiwi
Summary(pl.UTF-8):	Dokumentacja związana z python-kiwi
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
Obsoletes:	python-kiwi-docs

%description doc
This package contains documentation that contains APIs and related
materials, useful for reference when writing software using Kiwi.

%description doc -l pl.UTF-8
Ten pakiet zawiera dokumentację opisującą API i związane z nim
materiały, użyteczne podczas pisania oprogramowania używającego Kiwi.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%{__sed} -i -e 's|share/doc/kiwi|share/doc/%{name}-%{version}|' setup.py
# es locale quick fix
mv -f locale/es_ES locale/es
mv -f po/es_ES.po po/es.po

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

rm -rf $RPM_BUILD_ROOT%{_docdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# move gazpacho stuff to proper place
mv $RPM_BUILD_ROOT%{py_scriptdir}/dist-packages/gazpacho $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_postclean

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/kiwi*
%{_datadir}/kiwi
%dir %{py_sitescriptdir}/kiwi
%{py_sitescriptdir}/kiwi/*.py[co]
%dir %{py_sitescriptdir}/kiwi/db
%{py_sitescriptdir}/kiwi/db/*.py[co]
%dir %{py_sitescriptdir}/kiwi/i18n
%{py_sitescriptdir}/kiwi/i18n/*.py[co]
%dir %{py_sitescriptdir}/kiwi/ui
%{py_sitescriptdir}/kiwi/ui/*.py[co]
%dir %{py_sitescriptdir}/kiwi/ui/test
%{py_sitescriptdir}/kiwi/ui/test/*.py[co]
%dir %{py_sitescriptdir}/kiwi/ui/widgets
%{py_sitescriptdir}/kiwi/ui/widgets/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/kiwi-*.egg-info
%endif

%files gazpacho
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/gazpacho
%{py_sitescriptdir}/gazpacho/widgets
%{_datadir}/gazpacho/catalogs
%{_datadir}/gazpacho/resources

%files doc
%defattr(644,root,root,755)
%doc doc/*
%{_examplesdir}/%{name}-%{version}
