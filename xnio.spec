Name:          xnio
Version:       3.4.0
Release:       10
Summary:       A simplified low-level I/O layer
License:       ASL 2.0 and LGPLv2+
URL:           http://www.jboss.org/xnio
Source0:       https://github.com/xnio/xnio/archive/%{version}.Final/xnio-%{version}.Final.tar.gz
BuildArch:     noarch
BuildRequires: maven-local mvn(java_cup:java_cup) mvn(jdepend:jdepend) mvn(junit:junit)
BuildRequires: mvn(org.jboss:jboss-parent:pom:) mvn(org.jboss.apiviz:apiviz)
BuildRequires: mvn(org.jboss.byteman:byteman) mvn(org.jboss.byteman:byteman-bmunit)
BuildRequires: mvn(org.jboss.byteman:byteman-install) mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-annotations) mvn(org.jmock:jmock)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.logmanager:jboss-logmanager) mvn(org.jmock:jmock-junit4)
BuildRequires: mvn(org.wildfly.common:wildfly-common)

Patch0001:     0001-Disable-tests-use-TLSv1-protocol.patch
Patch0002:     0002-skip-connect-timeout.patch
%if "%{_arch}" == "riscv64"
Patch0003:     0003-skip-test-for-riscv.patch
%endif

%description
XNIO is a simplified low-level I/O layer which can be used anywhere you are using NIO today.
It frees you from the hassle of dealing with Selectors and the lack of NIO support for
multicast sockets and non-socket I/O, while still maintaining all the capabilities present in NIO,
and it opens the door to non-obvious optimizations.

%package       help
Summary:       Javadoc for xnio

Provides:      xnio-javadoc = %{version}-%{release}
Obsoletes:     xnio-javadoc < %{version}-%{release}

%description   help
This package provides the API documentation for xnio.

%prep
%autosetup -n xnio-%{version}.Final -p1

%pom_remove_plugin "org.jboss.bridger:bridger" api
%pom_remove_plugin -r :maven-source-plugin
rm nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioSslTcpConnectionTestCase.java \
   nio-impl/src/test/java/org/xnio/nio/test/NioSslTcpChannelTestCase.java \
   nio-impl/src/test/java/org/xnio/nio/test/NioSslTcpConnectionTestCase.java \
   nio-impl/src/test/java/org/xnio/nio/test/NioStartTLSTcpChannelTestCase.java \
   nio-impl/src/test/java/org/xnio/nio/test/NioStartTLSTcpConnectionTestCase.java \
   nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioSslTcpChannelTestCase.java \
   nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioStartTLSTcpConnectionTestCase.java \
   nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioStartTLSTcpChannelTestCase.java \
   nio-impl/src/test/java/org/xnio/nio/test/NioTcpConnectionTestCase.java \
   nio-impl/src/test/java/org/xnio/nio/test/MultiThreadedNioTcpConnectionTestCase.java
rm api/src/test/java/org/xnio/racecondition/ResumeReadsOnHandlingReadableChannelTestCase.java \
   api/src/test/java/org/xnio/racecondition/ResumeWritesOnHandlingWritableChannelTestCase.java \
   api/src/test/java/org/xnio/racecondition/SetReadListenerOnHandlingReadableChannelTestCase.java \
   api/src/test/java/org/xnio/racecondition/SetReadReadyOnHandlingReadableChannelTestCase.java \
   api/src/test/java/org/xnio/racecondition/SetWriteListenerOnHandlingWritableChannelTestCase.java \
   api/src/test/java/org/xnio/racecondition/SetWriteReadyOnHandlingWritableChannelTestCase.java \

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files help -f .mfiles-javadoc

%changelog
* Wed Mar 30 2022 YukariChiba <i@0x7f.cc> - 3.4.0-10
- Fix a previous mistake introduced in 3.4.0-9

* Tue Mar 22 2022 YukariChiba <i@0x7f.cc> - 3.4.0-9
- Fix test case by disable concurrent server thread test in RISCV64

* Sat Aug 6 2021 Lu Weitao <luweitaobe@163.com> - 3.4.0-8
- skip tests when connect timeout

* Tue Feb 23 2021 lingsheng <lingsheng@huawei.com> - 3.4.0-7
- Disable tests use TLSv1 protocol

* Mon Dec 23 2019 Tianfei <tianfei16@huawei.com> - 3.4.0-6
- Package init
