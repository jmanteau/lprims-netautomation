# Intro to Network Automation with Ansible Exercices

## Instructions

![Instructions](https://github.com/jmanteau/lprims-netautomation/raw/master/TP%20IUT%20Network%20Automation.png)

#### Goals:

- TP 1: Manage Cisco IOS configuration with Ansible
- TP 2: Manage Vyos configuration with Ansible
- TP 3: Manage Cisco / Vyos configuration in more complex data model with Ansible

To gain full understanding of Ansible, I recommend doing [Training Course for Ansible Network Automation](https://github.com/network-automation/linklight) (git clone and open the html in deck folder).

To have a quick overview read [this article](https://leucos.github.io/ansible-files-layout).

For these exercises, the simple structure already given along with the documentations linked below is enough to start.

**Go to the Setup section first to prepare the tooling before starting the exercices**


#### TP1

- Open the gns3project located in the ansible-tp1 folder.

- Obtain the adminstration IP for the two routers

- Complete the file inventory.txt with the extracted values

- Launch the ansible-monitor.sh file. What is happening ? What is the goal of this execution (read the file roles/ping/tasks/main.yml) ?

- Use the ansible.sh script or read its content to have the command to launch Ansible. What is happening ? Read the playbook-apply.yml and explain the sequence of actions occuring (explain the differents roles action)

PS: Inside the roles interfaces is an example with basic from 1 to 5 to show how can we have one task do the same but with different level of modularity and reuse (main.yml is the good one and used by the role)

#### TP2

- Open the gns3project located in the ansible-tp2 folder

- Bootstrap the devices with the configuration below. Modify the inventory.txt with the IPs shown at the end.


The exercise is the same as exercise but with the topology 2. The goal is to modify the playbook to configure the VYOS routers.

Read the roles to see how they have been modified for Vyos. See how the data model is structured compared to TP1.

#### TP3

Open the gns3project located in the ansible-tp3 folder

The goal of this part is to fulfill the roles and data model to configure the topology shown on the diagram.

**The objective is to give the proctor the zip containing the ansible-tp3 working as asked. This course scoring will be based on the successful run of this playbook and on the comments done inline the code to explain the roles / playbook / vars put in place**

## Setup

### GNS3

Direct Download for VM/Client: [Github Release page](https://github.com/GNS3/gns3-gui/releases) Download a client version >= 2.2 corresponding to your OS and the recommended VM (VMWare). Use VirtualBox if you must.

**[Link for 2019 class](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.0a5)**

Follow up the installation documentation for VM/Client installation [GNS3 VM](https://docs.gns3.com/1wdfvS-OlFfOf7HWZoSXMbG58C4pMSy7vKJFiKKVResc/index.html) until the "New Appliance Template" step. Skip this one.

Import this portable [Images Project](https://s3-eu-west-1.amazonaws.com/jmanteau/lprims-netautomation-images.gns3project) from the main menu to have the images ready to use for the labs.

Try to launch both routers (right click on them-> Start). You connect on the console (right click -> Console) to connect to them.

- If you have an error regarding "IOU is not executable" please log on the GNS3 VM Shell (option 3) and type
  ```
  sudo su
  loadkey fr
  chmod +x /opt/gns3/images/IOU/*.bin
  ```
- If you have an error regarding KVM, please ensure that hypervisor capabilites are actived on your VMWare sofware in your VM options (VT-x)
- If you have an error regarding License error for IOU. Connect by SSH to the VM (with the information shown) and select Shell (option 3)
  ```
  wget https://s3.eu-west-3.amazonaws.com/lprims-netautomation/py3-cisco-iou.py
  python3 py3-cisco-iou.py
  ```

General documentation: [GNS3 Client](https://docs.gns3.com/)

@TODO Document VMware import and bridge client (screenshots)

### Ansible

#### Docker Desktop

Install Docker Desktop. You will need to run Ansible without having to install it locally.

[Windows](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe)
[Mac](https://download.docker.com/mac/stable/Docker.dmg)

#### Ansible TP files

Either clone the repo (`git clone https://github.com/jmanteau/lprims-netautomation.git`) or [download an zip of it](https://github.com/jmanteau/lprims-netautomation/archive/master.zip)

Then go to ansible-tpX folder corresponding to the current TP you are doing.

#### Build Ansible Docker image for the TP

Go to ansible-docker folder. Execute the build.sh to build the docker image that will be used to execute Ansible.

#### Usage of Docker with Ansible

The ansible.sh inside each TP folder will pack the launching of Ansible with Docker in an easy way.

**The setup is now finished, you can now start the TP**

## TP Technical Information

|                            | Cisco IOS        | Vyos                            |
| -------------------------- | ---------------- | ------------------------------- |
| Boot Time                  | 20s              | 20s; 2min (without nested virt) |
| User                       | cisco            | vyos                            |
| Password / Enable Password | cisco123 / cisco | vyos                            |

### Boostrap Conf

If needed, use the following commands for each OS in the console to bootstrap them to be reacheable by SSH over the local network from your workstation.

The bootstrap for IOS is normally not needed as the configuration are embedded in the project.

#### Vyos

```
configure
set interfaces ethernet eth0 address dhcp
set service ssh port '22'
commit
save
exit
renew dhcp interface eth0
show interfaces

```

#### IOS

```
conf t
interface Ethernet0/0
ip address dhcp
no shut
username cisco password cisco123
enable password cisco
ip domain-name local
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 4
transport input ssh
login local
exit
exit
show ip int brief
wr

```

## Documentation

### Modules List

[IOS Module listing](http://docs.ansible.com/ansible/latest/modules/list_of_network_modules.html#ios)

[Vyos Module listing](http://docs.ansible.com/ansible/latest/modules/list_of_network_modules.html#vyos)

### Facts

[Vyos Facts](http://docs.ansible.com/ansible/latest/modules/vyos_facts_module.html#vyos-facts-module)

[IOS facts](http://docs.ansible.com/ansible/latest/modules/ios_facts_module.html#ios-facts-module)

### System

[Vyos System](http://docs.ansible.com/ansible/latest/modules/vyos_system_module.html#vyos-system-module)

[IOS System](http://docs.ansible.com/ansible/latest/modules/ios_system_module.html#ios-system-module)

### Interfaces

[Vyos Interface L3](http://docs.ansible.com/ansible/latest/modules/vyos_l3_interface_module.html#vyos-l3-interface-module)

[IOS Interface L3](http://docs.ansible.com/ansible/latest/modules/ios_l3_interface_module.html#ios-l3-interface-module)

### BGP

[IOS Config](http://docs.ansible.com/ansible/latest/modules/ios_config_module.html)

[Vyos Config](http://docs.ansible.com/ansible/latest/modules/vyos_config_module.html#vyos-config-module)

### With_items

[Looping In Ansible](https://codereviewvideos.com/course/ansible-tutorial/video/looping-in-ansible-with-items)

### Global Informations

[Vyos User Guide](https://wiki.vyos.net/wiki/User_Guide)

[some BGP commands on IOS](http://networkqna.com/useful-bgp-commands-on-cisco-routers/)

[Cisco commands 1](https://boubakr92.wordpress.com/2013/09/16/ccna-cheat-sheet-part-1/)
