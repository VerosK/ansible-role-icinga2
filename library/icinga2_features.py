
from ansible.module_utils.basic import AnsibleModule, check_type_bool
import os

def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec      = dict(
            features       = dict(required=True, type='dict'),
            icinga2_featuredir =
                             dict(type='str',
                                  default='/etc/icinga2/features-enabled/'),
        )
    )
    #
    params = module.params
    features = params['features']
    to_enable, to_disable = [],[]
    config_mask = '%s/{}.conf' % params['icinga2_featuredir']

    for feature_name, should_enable in features.items():
        try:
            should_enable = check_type_bool(should_enable) 
        except TypeError:
            module.fail_json(
                msg="Feature {} should be 'on' or 'off', but is set to '{}'".\
                            format(feature_name, should_enable))
        config = config_mask.format(feature_name)
        if os.path.exists(config) and not should_enable:
            to_disable.append(feature_name)
        elif not os.path.exists(config) and should_enable:
            to_enable.append(feature_name)
    #
    if not to_enable and not to_disable:
        module.exit_json(
            changed=False,
            msg="No Icinga2 features changed",
            features=features
        )
    if module.check_mode:
        if to_enable or to_disable:
            module.exit_json(
                changed=True,
                msg="We should changed icinga2 features",
                enabled=to_disable, disabled=to_disable,
                features=features)
    # do the work now
    for feature in to_enable:
        rc, out, err = module.run_command(
            'icinga2 feature enable {}'.format(feature))
        if rc != 0:
            module.fail_json(msg="Failed to enable feature {}".format(feature))
    for feature in to_disable:
        rc, out, err = module.run_command(
            'icinga2 feature disable {}'.format(feature))
        if rc != 0:
            module.fail_json(msg="Failed to disale feature {}".format(feature))
    module.exit_json(
        changed=True, msg="Updated icinga2 features. Icinga should be restarted",
        enabled=to_enable, disabled=to_disable,
        features=features)

if __name__ == '__main__':
    main()
