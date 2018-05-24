

# Intro to Network Automation with Ansible Exercices

## Instructions

![Instructions](https://github.com/jmanteau/lprims-netautomation/raw/master/TP%20IUT%20Network%20Automation.png)


#### Goals:

- TP 1: Manage Cisco IOS configuration with Ansible
- TP 2: Manage Vyos configuration with Ansible
- TP 3: Manage Cisco / Vyos configuration in more complex data model with Ansible




To gain full understanding of Ansible, I recommend doing [Training Course for Ansible Network Automation](https://github.com/network-automation/linklight)

(git clone and open the html in deck folder).

To have a quick overview read [this article](https://leucos.github.io/ansible-files-layout).



For these exercises, the simple structure already given along with the documentations linked below is enough to start.



*Go to the Setup section first to prepare the tooling before starting the exercices*



#### TP1

Use the ansible.sh script or read its content to have the command to launch Ansible.

The goal is to modify the playbook to configure the IOS routers.

The data model (host_vars) is setup correctly.

Read the different roles to understand what they do. Read the playbook to understand how the roles are called.

Inside the roles interfaces is an example with basic from 1 to 5 to show how can we have one task do the same but with different level of modularity and reuse (main.yml is the good one)

#### TP2

The exercise is the same as exercise but with the topology 2. The goal is to modify the playbook to configure the VYOS routers.

Read the roles to see how they have been modified for Vyos. See how the data model is structured compared to TP1.

#### TP3

The goal of this part is to fulfill the roles and data model to configure the topology shown on the diagram.

**The objective is to give the proctor the zip containing the ansible-tp3 working as asked. This course scoring will be based on the successful run of this playbook and on the comments done inline the code to explain the roles / playbook / vars put in place**



## Setup



#### GNS3

Direct Download for VM/Client: [Github Release page](https://github.com/GNS3/gns3-gui/releases) Download the client corresponding to your OS and the recommended VM (VMWare). Use VirtualBox if you must.

Documentation for VM/Client installation: [GNS3 VM](https://docs.gns3.com/1wdfvS-OlFfOf7HWZoSXMbG58C4pMSy7vKJFiKKVResc/index.html)

General documentation: [GNS3 Client](https://docs.gns3.com/)



#### Ansible

Linux/Mac: [Ansible](http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installation-guide) Due to a bug in one vyos module on the last Vyos 1.2, use Ansible devel (```pip install git+https://github.com/ansible/ansible.git@devel```)

Windows: Launch a Linux VM, install Ansible with the previous links.  Share with the VM the folder of the exercices.



#### GNS3 Portable projects

Download the projects at the following URLs:

- [Images](https://s3-eu-west-1.amazonaws.com/jmanteau/lprims-netautomation-images.gns3project)
- [TP1](https://s3-eu-west-1.amazonaws.com/jmanteau/lprims-netautomation-tp1.gns3project)
- [TP2](https://s3-eu-west-1.amazonaws.com/jmanteau/lprims-netautomation-tp2.gns3project)
- [TP3](https://s3-eu-west-1.amazonaws.com/jmanteau/lprims-netautomation-tp3.gns3project)



#### Ansible TP files

Either clone the repo (```git clone https://github.com/jmanteau/lprims-netautomation.git```) or [download    an zip of it](https://github.com/jmanteau/lprims-netautomation/archive/master.zip)

Then go to ansible-tpX folder corresponding to the current TP you are doing.

### Information

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



### Running and connecting to the routers

Open the project lprims-netautomation-images.gns3project, it will import the images for the VYOS and IOS routers used by the others projects.

When the TP requires it, for each topology lprims-netautomation-tpX.gns3project:

* open it
* Add a management cloud by drag and dropping on the topology ( GNS3 does not support cloud object in the portable projects)

![](/Users/jmanteau/PycharmProjects/lprims-netautomation/gns3_cloudmgt.png)

* Connect it from the management switch to your bridged VM interface (normally eth0). An easy way to check that, is to console the management switch and use the ```mac``` command. If this is properly connected you should learn others MAC addresses from your local network.

* Launch the devices. If you have an error on the launch for IOS routers, do the following on GNS3 VM shell:

  ```
  sudo su
  chmod +x /opt/gns3/images/IOU/*
  ```

* Connect by console to them

* Get the DHCP assigned IPs

* Fulfill the inventory with those IPs (use the commands at the end of the bootstrap to get them)



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
