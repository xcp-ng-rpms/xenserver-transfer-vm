Summary: XenServer Transfer VM
Name: xenserver-transfer-vm
Version: 7.1.3
Release: 1
License: GPLv2
Vendor: Citrix Systems, Inc.
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}
BuildArch: noarch
Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/transfer-vm/archive?at=%{version}&prefix=%{name}-%{version}&format=tar.gz#/%{name}-%{version}.tar.gz 
Source1: https://repo.citrite.net/xs-local-contrib/citrix/transfer-vm/1.0.1/transfer-vm.tar
Source2: https://repo.citrite.net/xs-local-contrib/citrix/transfer-vm/1.0.1/transfer-vm-sources.tar.gz

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
* Wed Oct 19 2016 Rob Dobson <rob.dobson@citrix.com> - 7.1.0-1 
- Initial repack of the Transfer VM
