Name:		librdkafka
Version:	1.1.0
Release:	1%{?dist}
Summary:	The Apache Kafka C library
 
License:	BSD
URL:		https://github.com/edenhill/librdkafka
Source0:	https://github.com/edenhill/librdkafka/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
 
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	python2
BuildRequires:  openssl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  lz4-devel
 
%description
Librdkafka is a C/C++ library implementation of the Apache Kafka protocol,
containing both Producer and Consumer support.
It was designed with message delivery reliability and high performance in mind,
current figures exceed 800000 messages/second for the producer and 3 million
messages/second for the consumer.
 
%package	devel
Summary:	The Apache Kafka C library (Development Environment)
Requires:	%{name}%{?_isa} = %{version}-%{release}
 
%description	devel
librdkafka is a C/C++ library implementation of the Apache Kafka protocol,
containing both Producer and Consumer support.
This package contains headers and libraries required to build applications
using librdkafka.
 
%prep
%setup -q
 
%build
%configure --enable-lz4 \
           --enable-ssl \
           --enable-sasl
 
%make_build
%check
make check
 
%install
%make_install
find %{buildroot} -name '*.a' -delete -print
 
%files
%{_libdir}/librdkafka.so.*
%{_libdir}/librdkafka++.so.*
 
%files devel
%dir %{_includedir}/librdkafka
%attr(0644,root,root) %{_includedir}/librdkafka/*
%attr(0755,root,root) %{_libdir}/librdkafka.so
%attr(0755,root,root) %{_libdir}/librdkafka++.so
%{_libdir}/pkgconfig/rdkafka.pc
%{_libdir}/pkgconfig/rdkafka++.pc
%{_libdir}/pkgconfig/rdkafka-static.pc
%{_libdir}/pkgconfig/rdkafka++-static.pc
 
