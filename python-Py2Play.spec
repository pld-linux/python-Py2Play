%include	/usr/lib/rpm/macros.python
%define pname	Py2Play
Summary:	Network game engine
Summary(pl):	Sieciowy silnik gier
Name:		python-Py2Play
Version:	0.1.6
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://oomadness.tuxfamily.org/downloads/%{pname}-%{version}.tar.gz
# Source0-md5:	15f6bc003fa2da379fc93b32abe075b2
URL:		http://oomadness.tuxfamily.org/en/py2play/
Requires:	python-tkinter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Py2Play is a network game engine written in Python, and it rests on a
Peer To Peer model (ala Napster) and not a client-server one, as it is
usually done.

%description -l pl
Py2Play jest sieciowym silnikiem gier napisanym w Pythonie. Jest on
zbudowany w oparciu o model Peer To Peer (tak jak Napster), a nie
klient-serwer, tak jak jest to zazwyczaj.

%prep
%setup -q -n %{pname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-purelib=%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/py2play
%{py_sitedir}/py2play/*.py[co]
