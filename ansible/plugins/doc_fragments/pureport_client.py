class ModuleDocFragment(object):
    DOCUMENTATION = r'''
options:
    api_base_url:
        description:
            - The host url for the Pureport API.
        required: false
        type: str
    api_key:
        description:
            - The pre-configured API Key for a Pureport Account.
            - Users should provide either the 'api_key' and 'api_secret' or the obtained 'api_access_token'.
        required: false
        type: str
    api_secret:
        description:
            - The pre-configured API Secret for a Pureport Account.
            - Users should provide either the 'api_key' and 'api_secret' or the obtained 'api_access_token'.
        required: false
        type: str
    api_access_token:
        description:
            - The access token to use with Pureport API.  This can be obtained from
            - the `pureport_access_token_fact` module.
            - Users should provide either the 'api_key' and 'api_secret' or the obtained 'api_access_token'.
        type: str
    '''
