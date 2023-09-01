[comment]: # "Auto-generated SOAR connector documentation"
# Axonius Cybersecurity Asset Management

Publisher: Axonius  
Connector Version: 2.1.2  
Product Vendor: Axonius  
Product Name: Axonius  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 5.5.0  

This app integrates with the Axonius Cybersecurity Asset Management Platform to enrich asset data for investigations

[comment]: # " File: README.md"
[comment]: # ""
[comment]: # "  Copyright (c) Axonius, 2018-2022"
[comment]: # ""
[comment]: # "  Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "  you may not use this file except in compliance with the License."
[comment]: # "  You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "      http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "  Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "  the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "  either express or implied. See the License for the specific language governing permissions"
[comment]: # "  and limitations under the License."
[comment]: # ""
## Playbook Backward Compatibility

-   A new action parameter has been added in the below existing actions. Hence, it is requested to
    the end-user to please update their existing playbooks by re-inserting | modifying | deleting
    the corresponding action blocks.

      

    -   The 'additional_fields' parameter has been added in all the actions mentioned below:

          

        -   devices by hostname
        -   devices by ip
        -   devices by mac
        -   users by mail
        -   users by username

-   The version 2.0.0 of this application is a complete rewrite and is not backward compatible.
    Hence, it is requested to the end-user to please update their existing playbooks by re-inserting
    | modifying | deleting the corresponding action blocks to ensure the correct functioning of
    the playbooks created on the earlier versions of the app. If the end-user does not want to
    upgrade their playbooks, they can remain on or downgrade to the old version(v1.0.0).


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Axonius asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api_key** |  required  | password | API Key
**api_secret** |  required  | password | API Secret
**url** |  required  | string | Axonius Instance URL
**proxy_url** |  optional  | string | HTTPS Proxy URL

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using the supplied configuration  
[devices by sq](#action-devices-by-sq) - Get devices by a saved query  
[devices by hostname](#action-devices-by-hostname) - Get devices by hostname  
[devices by ip](#action-devices-by-ip) - Get devices by IP address  
[devices by mac](#action-devices-by-mac) - Get devices by MAC address  
[users by sq](#action-users-by-sq) - Get users by a saved query  
[users by mail](#action-users-by-mail) - Get users by email address  
[users by username](#action-users-by-username) - Get users by username  

## action: 'test connectivity'
Validate the asset configuration for connectivity using the supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'devices by sq'
Get devices by a saved query

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**sq_name** |  required  | The name of the Axonius saved query | string | 
**max_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.sq_name | string |  |  
action_result.parameter.max_rows | numeric |  |  
action_result.data.\*.adapter_list_length | numeric |  |  
action_result.data.\*.adapters | string |  |  
action_result.data.\*.internal_axon_id | string |  |  
action_result.data.\*.aggregated_hostname | string |  `host name`  |  
action_result.data.\*.aggregated_name | string |  |  
action_result.data.\*.aggregated_last_seen | string |  |  
action_result.data.\*.aggregated_network_interfaces_macs | string |  |  
action_result.data.\*.aggregated_network_interfaces_ips | string |  `ip`  |  
action_result.data.\*.aggregated_os_type | string |  |  
action_result.data.\*.labels | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'devices by hostname'
Get devices by hostname

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**hostname** |  required  | The hostname of the Axonius asset | string |  `host name` 
**max_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional_fields** |  optional  | Additional fields to include as part of the request (comma-separated) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.hostname | string |  `host name`  |  
action_result.parameter.max_rows | numeric |  |   25 
action_result.parameter.additional_fields | string |  |  
action_result.data.\*.adapter_list_length | numeric |  |  
action_result.data.\*.adapters | string |  |  
action_result.data.\*.internal_axon_id | string |  |  
action_result.data.\*.aggregated_hostname | string |  `host name`  |  
action_result.data.\*.aggregated_name | string |  |  
action_result.data.\*.aggregated_last_seen | string |  |  
action_result.data.\*.aggregated_network_interfaces_macs | string |  |  
action_result.data.\*.aggregated_network_interfaces_ips | string |  `ip`  |  
action_result.data.\*.aggregated_os_type | string |  |  
action_result.data.\*.labels | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'devices by ip'
Get devices by IP address

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip** |  required  | The IP address of the Axonius asset | string |  `ip` 
**max_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional_fields** |  optional  | Additional fields to include as part of the request (comma-separated) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.ip | string |  `ip`  |  
action_result.parameter.max_rows | numeric |  |   25 
action_result.parameter.additional_fields | string |  |  
action_result.data.\*.adapter_list_length | numeric |  |  
action_result.data.\*.adapters | string |  |  
action_result.data.\*.internal_axon_id | string |  |  
action_result.data.\*.aggregated_hostname | string |  `host name`  |  
action_result.data.\*.aggregated_name | string |  |  
action_result.data.\*.aggregated_last_seen | string |  |  
action_result.data.\*.aggregated_network_interfaces_macs | string |  |  
action_result.data.\*.aggregated_network_interfaces_ips | string |  `ip`  |  
action_result.data.\*.aggregated_os_type | string |  |  
action_result.data.\*.labels | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'devices by mac'
Get devices by MAC address

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**mac** |  required  | The MAC address of the Axonius asset | string |  `mac address` 
**max_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional_fields** |  optional  | Additional fields to include as part of the request (comma-separated) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.mac | string |  `mac address`  |  
action_result.parameter.max_rows | numeric |  |   25 
action_result.parameter.additional_fields | string |  |  
action_result.data.\*.adapter_list_length | numeric |  |  
action_result.data.\*.adapters | string |  |  
action_result.data.\*.internal_axon_id | string |  |  
action_result.data.\*.aggregated_hostname | string |  `host name`  |  
action_result.data.\*.aggregated_name | string |  |  
action_result.data.\*.aggregated_last_seen | string |  |  
action_result.data.\*.aggregated_network_interfaces_macs | string |  |  
action_result.data.\*.aggregated_network_interfaces_ips | string |  `ip`  |  
action_result.data.\*.aggregated_os_type | string |  |  
action_result.data.\*.labels | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'users by sq'
Get users by a saved query

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**sq_name** |  required  | The name of the Axonius saved query | string | 
**max_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.sq_name | string |  |  
action_result.parameter.max_rows | numeric |  |   25 
action_result.data.\*.adapter_list_length | numeric |  |  
action_result.data.\*.adapters | string |  |  
action_result.data.\*.internal_axon_id | string |  |  
action_result.data.\*.aggregated_username | string |  |  
action_result.data.\*.aggregated_mail | string |  |  
action_result.data.\*.aggregated_last_seen | string |  |  
action_result.data.\*.aggregated_is_admin | string |  |  
action_result.data.\*.labels | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'users by mail'
Get users by email address

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**mail** |  required  | The email address of the Axonius user | string |  `email` 
**max_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional_fields** |  optional  | Additional fields to include as part of the request (comma-separated) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.mail | string |  `email`  |  
action_result.parameter.max_rows | numeric |  |   25 
action_result.parameter.additional_fields | string |  |  
action_result.data.\*.adapter_list_length | numeric |  |  
action_result.data.\*.adapters | string |  |  
action_result.data.\*.internal_axon_id | string |  |  
action_result.data.\*.aggregated_username | string |  |  
action_result.data.\*.aggregated_mail | string |  |  
action_result.data.\*.aggregated_last_seen | string |  |  
action_result.data.\*.aggregated_is_admin | string |  |  
action_result.data.\*.labels | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1   

## action: 'users by username'
Get users by username

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | The username of the Axonius user | string | 
**max_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional_fields** |  optional  | Additional fields to include as part of the request (comma-separated) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.username | string |  |  
action_result.parameter.max_rows | numeric |  |   25 
action_result.parameter.additional_fields | string |  |  
action_result.data.\*.adapter_list_length | numeric |  |  
action_result.data.\*.adapters | string |  |  
action_result.data.\*.internal_axon_id | string |  |  
action_result.data.\*.aggregated_username | string |  |  
action_result.data.\*.aggregated_mail | string |  |  
action_result.data.\*.aggregated_last_seen | string |  |  
action_result.data.\*.aggregated_is_admin | string |  |  
action_result.data.\*.labels | string |  |  
action_result.status | string |  |   success  failed 
action_result.message | string |  |  
action_result.summary | string |  |  
summary.total_objects | numeric |  |   1 
summary.total_objects_successful | numeric |  |   1 