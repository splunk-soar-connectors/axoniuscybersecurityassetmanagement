[comment]: # "Auto-generated SOAR connector documentation"
# Axonius Cybersecurity Asset Management

Publisher: Axonius  
Connector Version: 2\.1\.1  
Product Vendor: Axonius  
Product Name: Axonius  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.10\.0\.40961  

This app integrates with the Axonius Cybersecurity Asset Management Platform to enrich asset data for investigations

[comment]: # " File: readme.md"
[comment]: # ""
[comment]: # "    Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
## Playbook Backward Compatibility

-   A new action parameter has been added in the below existing actions. Hence, it is requested to
    the end-user to please update their existing playbooks by re-inserting \| modifying \| deleting
    the corresponding action blocks.

      

    -   The 'additional_fields' parameter has been added in all the actions mentioned below:

          

        -   devices by hostname
        -   devices by ip
        -   devices by mac
        -   users by mail
        -   users by username

-   The version 2.0.0 of this application is a complete rewrite and is not backward compatible.
    Hence, it is requested to the end-user to please update their existing playbooks by re-inserting
    \| modifying \| deleting the corresponding action blocks to ensure the correct functioning of
    the playbooks created on the earlier versions of the app. If the end-user does not want to
    upgrade their playbooks, they can remain on or downgrade to the old version(v1.0.0).


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Axonius asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**api\_key** |  required  | password | API Key
**api\_secret** |  required  | password | API Secret
**url** |  required  | string | Axonius Instance URL
**proxy\_url** |  optional  | string | HTTPS Proxy URL

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
**sq\_name** |  required  | The name of the Axonius saved query | string | 
**max\_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.sq\_name | string | 
action\_result\.parameter\.max\_rows | numeric | 
action\_result\.data\.\*\.adapter\_list\_length | numeric | 
action\_result\.data\.\*\.adapters | string | 
action\_result\.data\.\*\.internal\_axon\_id | string | 
action\_result\.data\.\*\.aggregated\_hostname | string |  `host name` 
action\_result\.data\.\*\.aggregated\_name | string | 
action\_result\.data\.\*\.aggregated\_last\_seen | string | 
action\_result\.data\.\*\.aggregated\_network\_interfaces\_macs | string | 
action\_result\.data\.\*\.aggregated\_network\_interfaces\_ips | string |  `ip` 
action\_result\.data\.\*\.aggregated\_os\_type | string | 
action\_result\.data\.\*\.labels | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'devices by hostname'
Get devices by hostname

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**hostname** |  required  | The hostname of the Axonius asset | string |  `host name` 
**max\_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional\_fields** |  optional  | Additional fields to include as part of the request \(comma\-separated\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.hostname | string |  `host name` 
action\_result\.parameter\.max\_rows | numeric | 
action\_result\.parameter\.additional\_fields | string | 
action\_result\.data\.\*\.adapter\_list\_length | numeric | 
action\_result\.data\.\*\.adapters | string | 
action\_result\.data\.\*\.internal\_axon\_id | string | 
action\_result\.data\.\*\.aggregated\_hostname | string |  `host name` 
action\_result\.data\.\*\.aggregated\_name | string | 
action\_result\.data\.\*\.aggregated\_last\_seen | string | 
action\_result\.data\.\*\.aggregated\_network\_interfaces\_macs | string | 
action\_result\.data\.\*\.aggregated\_network\_interfaces\_ips | string |  `ip` 
action\_result\.data\.\*\.aggregated\_os\_type | string | 
action\_result\.data\.\*\.labels | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'devices by ip'
Get devices by IP address

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**ip** |  required  | The IP address of the Axonius asset | string |  `ip` 
**max\_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional\_fields** |  optional  | Additional fields to include as part of the request \(comma\-separated\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.ip | string |  `ip` 
action\_result\.parameter\.max\_rows | numeric | 
action\_result\.parameter\.additional\_fields | string | 
action\_result\.data\.\*\.adapter\_list\_length | numeric | 
action\_result\.data\.\*\.adapters | string | 
action\_result\.data\.\*\.internal\_axon\_id | string | 
action\_result\.data\.\*\.aggregated\_hostname | string |  `host name` 
action\_result\.data\.\*\.aggregated\_name | string | 
action\_result\.data\.\*\.aggregated\_last\_seen | string | 
action\_result\.data\.\*\.aggregated\_network\_interfaces\_macs | string | 
action\_result\.data\.\*\.aggregated\_network\_interfaces\_ips | string |  `ip` 
action\_result\.data\.\*\.aggregated\_os\_type | string | 
action\_result\.data\.\*\.labels | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'devices by mac'
Get devices by MAC address

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**mac** |  required  | The MAC address of the Axonius asset | string |  `mac address` 
**max\_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional\_fields** |  optional  | Additional fields to include as part of the request \(comma\-separated\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.mac | string |  `mac address` 
action\_result\.parameter\.max\_rows | numeric | 
action\_result\.parameter\.additional\_fields | string | 
action\_result\.data\.\*\.adapter\_list\_length | numeric | 
action\_result\.data\.\*\.adapters | string | 
action\_result\.data\.\*\.internal\_axon\_id | string | 
action\_result\.data\.\*\.aggregated\_hostname | string |  `host name` 
action\_result\.data\.\*\.aggregated\_name | string | 
action\_result\.data\.\*\.aggregated\_last\_seen | string | 
action\_result\.data\.\*\.aggregated\_network\_interfaces\_macs | string | 
action\_result\.data\.\*\.aggregated\_network\_interfaces\_ips | string |  `ip` 
action\_result\.data\.\*\.aggregated\_os\_type | string | 
action\_result\.data\.\*\.labels | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'users by sq'
Get users by a saved query

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**sq\_name** |  required  | The name of the Axonius saved query | string | 
**max\_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.sq\_name | string | 
action\_result\.parameter\.max\_rows | numeric | 
action\_result\.data\.\*\.adapter\_list\_length | numeric | 
action\_result\.data\.\*\.adapters | string | 
action\_result\.data\.\*\.internal\_axon\_id | string | 
action\_result\.data\.\*\.aggregated\_username | string | 
action\_result\.data\.\*\.aggregated\_mail | string | 
action\_result\.data\.\*\.aggregated\_last\_seen | string | 
action\_result\.data\.\*\.aggregated\_is\_admin | string | 
action\_result\.data\.\*\.labels | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'users by mail'
Get users by email address

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**mail** |  required  | The email address of the Axonius user | string |  `email` 
**max\_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional\_fields** |  optional  | Additional fields to include as part of the request \(comma\-separated\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.mail | string |  `email` 
action\_result\.parameter\.max\_rows | numeric | 
action\_result\.parameter\.additional\_fields | string | 
action\_result\.data\.\*\.adapter\_list\_length | numeric | 
action\_result\.data\.\*\.adapters | string | 
action\_result\.data\.\*\.internal\_axon\_id | string | 
action\_result\.data\.\*\.aggregated\_username | string | 
action\_result\.data\.\*\.aggregated\_mail | string | 
action\_result\.data\.\*\.aggregated\_last\_seen | string | 
action\_result\.data\.\*\.aggregated\_is\_admin | string | 
action\_result\.data\.\*\.labels | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'users by username'
Get users by username

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**username** |  required  | The username of the Axonius user | string | 
**max\_rows** |  optional  | The maximum number of rows to be returned by Axonius | numeric | 
**additional\_fields** |  optional  | Additional fields to include as part of the request \(comma\-separated\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.username | string | 
action\_result\.parameter\.max\_rows | numeric | 
action\_result\.parameter\.additional\_fields | string | 
action\_result\.data\.\*\.adapter\_list\_length | numeric | 
action\_result\.data\.\*\.adapters | string | 
action\_result\.data\.\*\.internal\_axon\_id | string | 
action\_result\.data\.\*\.aggregated\_username | string | 
action\_result\.data\.\*\.aggregated\_mail | string | 
action\_result\.data\.\*\.aggregated\_last\_seen | string | 
action\_result\.data\.\*\.aggregated\_is\_admin | string | 
action\_result\.data\.\*\.labels | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 