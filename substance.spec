#TODO provide javadoc 

Name:           substance
Version:        4.3.11
Release:        %mkrel 0.0.2
Summary:        Substance Look and Feel
License:        BSD
Group:          Development/Java
Url:            https://substance.dev.java.net/
Source0:        https://substance.dev.java.net/files/documents/3294/85735/substance-all.zip
Source1:        build.properties
BuildRequires:  jpackage-utils
BuildRequires:  java-rpmbuild 
BuildRequires:  ant
BuildRequires:  laf-widget
BuildRequires:  laf-plugin
BuildRequires:  jgoodies-forms
BuildRequires:  asm2
BuildRequires:  swingx
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A configurable and customizable production-quality Java look and feel library
for Swing applications. 
This Java look and feel is available for JDK 5.0+ only.

#%package        javadoc
#Summary:        Javadoc for %{name}
#Group:          Development/Java
#
#%description javadoc
#Javadoc for %{name}.

%prep
%setup -q -c %{name}-%{version}
cp %{SOURCE1} build.properties
%remove_java_binaries

%build
export CLASSPATH=$(build-classpath asm2 laf-widget laf-plugin jgoodies-forms swingx)
ln -s $(build-classpath laf-plugin) lib/laf-plugin-50.jar
ln -s $(build-classpath laf-widget) lib/laf-widget.jar
%{ant} -Dbuild.sysclasspath=first all

%install
rm -rf %{buildroot}
install -m644 drop/%{name}.jar -D %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -m644 drop/%{name}-lite.jar -D %{buildroot}%{_javadir}/%{name}-lite-%{version}.jar
install -m644 drop/%{name}-lite-feel.jar -D %{buildroot}%{_javadir}/%{name}-lite-feel-%{version}.jar

#install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
#cp -r docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
#ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%create_jar_links

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_javadir}/*

#%files javadoc
#%defattr(644,root,root,755)
#%{_javadocdir}/%{name}
#%{_javadocdir}/%{name}-%{version}
 