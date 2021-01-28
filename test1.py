import pandas as pd
from pycentral.base import ArubaCentralBase
from pycentral.configuration import ApSettings
from pprint import pprint
from pycentral.workflows.workflows_utils import get_conn_from_file

ssl_verify = True

filename = 'export_ap_2.xls'

aps = pd.read_excel(filename)
df = pd.DataFrame(aps, columns= ['DEVICE NAME', 'SERIAL'])
products_list = df.to_dict()
serials = [x for x in products_list['SERIAL'].values()]
device_names = [x for x in products_list['DEVICE NAME'].values()]

central_filename = "my_credentials.json"
central = get_conn_from_file(filename=central_filename)


g = ApSettings()

for x, y in zip(serials, device_names):
    module_resp = g.get_ap_settings(central, x)['msg']
    pprint(module_resp)
    new_dict = {'hostname': y}
    module_resp |= new_dict
    g.update_ap_settings(central, x, module_resp)
    print("***POST-UPDATE***")
    module_resp = g.get_ap_settings(central, x)['msg']
    pprint(module_resp)




