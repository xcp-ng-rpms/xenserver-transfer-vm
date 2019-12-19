Summary: XenServer Transfer VM
Name: xenserver-transfer-vm
Version: 7.1.5
Release: 1
License: GPLv2
Vendor: Citrix Systems, Inc.
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}
BuildArch: noarch

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/transfer-vm/archive?at=7.1.5&prefix=xenserver-transfer-vm-7.1.5&format=tar.gz#/xenserver-transfer-vm-7.1.5.tar.gz
Source1: https://repo.citrite.net/xs-local-contrib/citrix/transfer-vm/1.0.1/transfer-vm.tar
Source2: https://repo.citrite.net/xs-local-contrib/citrix/transfer-vm/1.0.1/transfer-vm-sources.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/transfer-vm/archive?at=7.1.5&prefix=xenserver-transfer-vm-7.1.5&format=tar.gz#/xenserver-transfer-vm-7.1.5.tar.gz) = d3d2834be3c705e7712f10ab90fe332c904f5169


%define tvm_dir /opt/xensource/packages/files/transfer-vm
%define xapi_plugins /etc/xapi.d/plugins

%description
The Transfer VM template with control scripts.

%prep
%autosetup -p1 -a 1

%build
exit 0

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}/opt/xensource/packages/files/transfer-vm
%{__install} -m 755 src/install-transfer-vm.sh %{buildroot}/%{tvm_dir}  
%{__install} -m 755 src/uninstall-transfer-vm.sh %{buildroot}/%{tvm_dir}  
%{__install} -m 755 src/do-copy %{buildroot}/%{tvm_dir}  
%{__install} -m 755 src/do-transfer %{buildroot}/%{tvm_dir}  
%{__install}  src/65-install-transfer-vm %{buildroot}/%{tvm_dir}  
%{__install} transfer-vm.xva %{buildroot}/%{tvm_dir} 

# Install XAPI plugins
%{__install} -d %{buildroot}/%{xapi_plugins}
%{__install} src/plugins/copy %{buildroot}/%{xapi_plugins}
%{__install} src/plugins/forest.py %{buildroot}/%{xapi_plugins}
%{__install} src/plugins/pluginlib.py %{buildroot}/%{xapi_plugins}
%{__install} src/plugins/transfer %{buildroot}/%{xapi_plugins}
%{__install} src/plugins/vhd_bitmaps.py %{buildroot}/%{xapi_plugins}
%{__install} src/plugins/vhd.py %{buildroot}/%{xapi_plugins}
%{__install} src/plugins/vm_metadata.py %{buildroot}/%{xapi_plugins}

%clean
exit 0

%files
%defattr(-,root,root,-)
%{tvm_dir}/do-copy
%{tvm_dir}/do-transfer
%{tvm_dir}/install-transfer-vm.sh
%{tvm_dir}/transfer-vm.xva
%{tvm_dir}/uninstall-transfer-vm.sh
%{tvm_dir}/65-install-transfer-vm
/etc/xapi.d/plugins/copy
/etc/xapi.d/plugins/forest.py*
/etc/xapi.d/plugins/pluginlib.py*
/etc/xapi.d/plugins/transfer
/etc/xapi.d/plugins/vhd.py*
/etc/xapi.d/plugins/vhd_bitmaps.py*
/etc/xapi.d/plugins/vm_metadata.py*

%posttrans
touch /opt/xensource/packages/files/transfer-vm/rpm_change

%preun
exit 0

%changelog
* Tue Oct 22 2019 Deli Zhang <deli.zhang@citrix.com> - 7.1.5-1
- CA-329079: Fix ip address validation issue

* Wed Oct 31 2018 Liang Dai <liang.dai1@citrix.com> - 7.1.4-1
- CA-293362: Fail to communicate with the plugin. (CERTIFICATE_VERIFY_FAILED)

* Wed Oct 19 2016 Rob Dobson <rob.dobson@citrix.com> - 7.1.0-1 
- Initial repack of the Transfer VM
