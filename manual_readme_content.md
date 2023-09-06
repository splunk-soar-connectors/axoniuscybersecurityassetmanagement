[comment]: # " File: README.md"
[comment]: # ""
[comment]: # "  Copyright (c) Axonius, 2018-2023"
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
