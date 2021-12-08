## OCI Security Rule Bulk-Create Tool

#### Create Security Lists that are populated with a bulk-number of Security Rules.

1. Install the OCI Python SDK using the instructions provided [here](https://docs.oracle.com/en-us/iaas/tools/python/2.45.1/installation.html).

2. Set up your OCI config file using the instructions provided [here](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File).

3. Install `pandas`:
```
     sudo pip3 install pandas
```
4. Format your CIDR ranges into a single column without a header in a `.csv` file, as in [this example](cidrs_demo.csv).

5. Replace the placeholder values with your own in `config.py`.

6. Bulk create Security Rules in your OCI environment with:
```
     python3 main.py
```
7. Assign your new Security Lists to your Subnets.