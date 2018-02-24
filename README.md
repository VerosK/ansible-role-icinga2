# icinga2

Ansible role to install Icinga2 Headless alongside Plugins

## Requirements

EPEL is required on CentOS.

## Example Playbook

```yaml
---
- hosts: icinga
  roles:
   - role: VerosK.icinga2
```

Role Variables
--------------

See `defaults/main.yml`

License
-------

GNU General Public License Version 2

Author Information
------------------

Based on work of Valentino Gagliardi - Icinga Dev Team

Hacked by Veros Kaplan - https://github.com/VerosK/ansible-role-icinga2
