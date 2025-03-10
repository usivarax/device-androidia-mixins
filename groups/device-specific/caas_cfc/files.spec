[mapping]
{{ref_target}}.mk: {{target}}.mk

[devicefiles]
bldr_utils.img: "fastboot image is used when bldr partsize is 0"
compatibility_matrix.xml: "add compatibility for ota verify"
flash_cmd.sh: "ELK mode flash tool"
manifest.xml: "define hidl interface"
framework_manifest.xml: "define hidl framework interface"
overlay: "configurations for SystemUI"
system.prop: "system properties file"
{{ref_target}}.mk: "product definition file"
r2_{{target}}.mk: "Ring 2 target for P.car"
start_flash_usb.sh: "script for flashing qcow2 in Qemu"
start_android_qcow2.sh: "script for starting android in Qemu"
setup_host.sh: "script for setting up virtulization environment on host"
file_share.sh: "script for setting up file sharing environment on host"
sof_audio: "script for sof audio"
auto_switch_pt_usb_vms.sh:"script for switching usb_vms"
guest_pm_control:" Guest PM control"
findall.py: "Find script"
thermald.service: "thermald service"
intel-thermal-conf.xml: "Configuration file"
qmp_events_handler.sh: "Event handler"
setup_audio_host.sh: "scripts for host audio"
wakeup.py: "guest wakeup from vinput-manager"
rpmb_dev: "rpmb simulation application"
cfc_example.sh: "host cfc example"
