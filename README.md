# icinga2

Ansible role to install Icinga2 Headless alongside Plugins

## Requirements

EPEL

## Example Playbook

```yaml
---
- hosts: icinga
  roles:
   - role: icinga2
```

Role Variables
--------------

See `defaults/main.yml`

License
-------

GNU General Public License Version 2

Author Information
------------------

Base on work of Valentino Gagliardi - Icinga Dev Team
Hacked by Veros Kaplan - https://github.com/VerosK/ansible-icinga2-role
