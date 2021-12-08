# for help, run:
# python3 help.py

# Compartment OCID. The Security Lists will be assigned to this Compartment.
compartment_id = "<COMPARTMENT OCID>"

# VCN OCID. The Security Lists will be assigned to this VCN.
vcn_id = "<VCN OCID>"

# Maximum number of rules to assign to a Security List. Refer to documentation: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison
security_rules_limit = 200

# Friendly name for all Security Lists. Once deployed, the format will be: <security_list_display_name> <number starting from 1>
security_list_display_name = "Security List"

# Description for all egress rules. Once deployed, the format will be: <egress_rule_description> for CIDR range <a CIDR range from your list>
egress_rule_description = "Egress rule"

# Description for all ingress rules. Once deployed, the format will be: <ingress_rule_description> for CIDR range <a CIDR range from your list>
ingress_rule_description = "Ingress rule"

# Protocol to use for all rules. Refer to documentation: https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/core/models/oci.core.models.SecurityRule.html#oci.core.models.SecurityRule.protocol
protocol = "6" # TCP

# Path to your .csv file.
cidr_ranges_filepath = "cidrs_demo.csv"