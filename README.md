# ansible-role-icinga2

Ansible role to install Icinga2 daemon and plugins.  

It can optionally setup PostgreSQL IDO on Icinga host.
To setup IDO on separate host, use role [`VerosK.icinga2-ido-pgsql`][ido-role]. 

## Requirements

EPEL is required on CentOS.  

## Example Playbook
    
    - hosts: icinga
      roles:
       - role: VerosK.icinga2


Role Variables
--------------

See `defaults/main.yml`

License
-------

GNU General Public License Version 2

Author Information
------------------

Based on work of Valentino Gagliardi from Icinga Dev Team. Updated by [Veros Kaplan][verosk]

[ido-role]: https://github.com/VerosK/ansible-role-icinga2-ido-pgsql
[verosk]: https://github.com/VerosK/ansible-role-icinga2-ido-pgsql