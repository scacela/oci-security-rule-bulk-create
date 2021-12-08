import oci
from config import *
import json

def main(count):
    config = oci.config.from_file()
    retry_strategy = oci.retry.DEFAULT_RETRY_STRATEGY
    core_client = oci.core.VirtualNetworkClient(config, retry_strategy=retry_strategy)
    create_security_list_response = core_client.create_security_list(
    create_security_list_details = oci.core.models.CreateSecurityListDetails(
    compartment_id=compartment_id,
    egress_security_rules=[
    {body_egress}
    ],
    ingress_security_rules=[
    {body_ingress}
    ],
    vcn_id=vcn_id,
    display_name=f"{security_list_display_name} {count}"))
    data = json.loads(str(create_security_list_response.data))
    return data["id"]
