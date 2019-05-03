from traceback import format_exc
try:
    from pureport.api.client import Client
    from pureport.exception.api import ClientHttpException
    HAS_PUREPORT_CLIENT = True
except ImportError:
    HAS_PUREPORT_CLIENT = False
    Client = None
    ClientHttpException = None


def get_client_argument_spec():
    """
    Return the basic account params
    :rtype: dict[str, dict]
    """
    return dict(
        api_base_url=dict(type='str'),
        api_key=dict(type='str', required=True),
        api_secret=dict(type='str', required=True, no_log=True)
    )


def get_client(module):
    """
    Get a Pureport Client instance
    :param ansible.module_utils.basic.AnsibleModule module: the Ansible module
    :rtype: Client
    """
    if not HAS_PUREPORT_CLIENT:
        module.fail_json(msg='pureport-client required for this module')
    client = Client(module.params.get('api_base_url'))
    try:
        client.login(module.params.get('api_key'), module.params.get('api_secret'))
    except ClientHttpException as e:
        module.fail_json(msg=e.response.text, exception=format_exc())
    return client


def get_account_argument_spec(required=False):
    """
    Return the basic account params
    :param bool required: are these params required
    :rtype: dict[str, dict]
    """
    return dict(
        account_href=dict(type='str', required=required)
    )


def get_account(module):
    """
    Get the account from the passed in module
    :param ansible.module_utils.basic.AnsibleModule module: the Ansible module
    :rtype: Account
    """
    return dict(href=module.params.get('account_href'))


def get_network_argument_spec(required=False):
    """
    Return the basic account params
    :param bool required: are these params required
    :rtype: dict[str, dict]
    """
    return dict(
        network_href=dict(type='str', required=required)
    )


def get_network(module):
    """
    Get the account from the passed in module
    :param ansible.module_utils.basic.AnsibleModule module: the Ansible module
    :rtype: Network
    """
    return dict(href=module.params.get('network_href'))
