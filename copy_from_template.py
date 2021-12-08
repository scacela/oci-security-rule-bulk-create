from shutil import copyfile
from textwrap import dedent
from config import *

def main(processed, count_batches_added):
    src = f"security_list_create.template.py"
    dest = f"tmp_security_list_create_{count_batches_added}.py"

    modulename = dest.replace(".py", "")

    copyfile(src, dest)
    body_egress = ""
    body_ingress = ""
    for cidr in processed:
        body_egress += dedent(f"""
            oci.core.models.EgressSecurityRule(
            destination="{cidr}",
            protocol=protocol,
            destination_type="CIDR_BLOCK",
            is_stateless=False,
            tcp_options=oci.core.models.TcpOptions(),
            description="{egress_rule_description} for CIDR range {cidr}"),
        """)
        body_ingress += dedent(f"""
            oci.core.models.IngressSecurityRule(
            protocol=protocol,
            source="{cidr}",
            is_stateless=False,
            source_type="CIDR_BLOCK",
            tcp_options=oci.core.models.TcpOptions(
                destination_port_range=oci.core.models.PortRange(
                    max=22,
                    min=22)),
            description="{ingress_rule_description} for CIDR range {cidr}"),
        """)

    content_replace("body_egress", body_egress, dest)
    content_replace("body_ingress", body_ingress, dest)

    return modulename, dest

def content_replace(body_keyword, body_content, dest):
    reading_file = open(dest, "r")
    new_file_content = ""

    for line in reading_file:
        new_line = line.replace(r"{"f"{body_keyword}"r"}", body_content)
        new_file_content += new_line
    reading_file.close()

    writing_file = open(dest, "w")
    writing_file.write(new_file_content)
    writing_file.close()