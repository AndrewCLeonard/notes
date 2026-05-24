# Understanding the Action Builder SQL Mirror

## Table Samples

Here are a few rows from the relevant tag tables to wrap your head around the schema.

Sample Query for all:

```SQL
SELECT
    *
FROM
    ENTITIES E
LIMIT
    5;
```

### `ENTITIES` Table

| "id"   | "first_name" | "nickname" | "middle_name" | "last_name" | "date_of_birth" | "preferred_language" | "organization_id" | "custom_id" | "dw_id" | "voterbase_id" | "linked_user_id" | "created_by_id" | "created_at"                 | "updated_at"                 | "interact_id"                          | "age" | "calculated_birth_date" | "custom_id_1" | "custom_id_2" | "custom_id_3" | "custom_id_4" | "updated_by_id" | "entity_type_id" | "pronouns" |
| ------ | ------------ | ---------- | ------------- | ----------- | --------------- | -------------------- | ----------------- | ----------- | ------- | -------------- | ---------------- | --------------- | ---------------------------- | ---------------------------- | -------------------------------------- | ----- | ----------------------- | ------------- | ------------- | ------------- | ------------- | --------------- | ---------------- | ---------- |
| 239301 | "Shadrack"   |            |               | "Baendafe"  |                 | "en"                 |                   |             |         |                |                  | 352             | "2024-01-04 21:13:09.042427" | "2024-01-04 21:13:09.042427" | "4d9d42bf-dee8-4d1a-ae31-b9d6e826a0f5" |       | false                   |               |               |               |               |                 | 1                |            |
| 30609  | "Tracey"     |            |               | "Adams"     |                 | "en"                 |                   |             |         |                |                  | 51              | "2019-12-13 21:20:32.665727" | "2023-12-08 11:49:05.215961" | "91906dec-5c3a-4c3d-ac63-1835016410c7" |       | false                   |               |               |               |               |                 | 1                |            |
| 104400 | "Brandon"    |            |               | "Carson"    |                 | "en"                 |                   |             |         |                |                  | 137             | "2022-07-13 23:15:51.952313" | "2022-07-14 11:14:44.995636" | "050a2c8f-2f88-475c-838d-eef5de0e502c" |       | false                   |               | "2764"        |               |               |                 | 1                |            |
| 203550 | "Alexa"      |            |               | "Lester"    |                 | "en"                 |                   |             |         |                |                  | 158             | "2023-09-11 18:30:55.339109" | "2023-12-08 11:49:17.738979" | "a9f5bd68-8ad4-494d-8b08-3cebd14d6900" |       | false                   |               |               |               |               |                 | 1                |            |
| 10562  | "Linda"      |            |               | "Welch"     |                 | "en"                 |                   |             |         |                |                  | 39              | "2019-08-15 15:35:12.507565" | "2023-12-08 12:09:52.591873" | "fb8b51be-12ff-42ff-8c51-8ad0a2db0277" |       | false                   |               |               |               |               |                 | 1                |            |

### `CAMPAIGNS_ENTITIES` Table

| "campaign_id" | "entity_id" | "created_at"                 | "updated_at"                 | "id" | "latest_assessment_id" | "latest_assessment_level" |
| ------------- | ----------- | ---------------------------- | ---------------------------- | ---- | ---------------------- | ------------------------- |
| 2             | 3           | "2019-04-26 13:20:09.401175" | "2019-04-26 13:20:09.401175" | 1    |                        | 0                         |
| 2             | 4           | "2019-04-26 13:20:09.547448" | "2019-04-26 13:20:09.547448" | 2    |                        | 0                         |
| 2             | 5           | "2019-04-26 13:20:09.599841" | "2019-04-26 13:20:09.599841" | 3    |                        | 0                         |
| 2             | 6           | "2019-04-26 13:20:09.662153" | "2019-04-26 13:20:09.662153" | 4    |                        | 0                         |
| 2             | 7           | "2019-04-26 13:20:09.716282" | "2019-04-26 13:20:09.716282" | 5    |                        | 0                         |

### `CAMPAIGNS` Table

| "id" | "name"                              | "created_by_id" | "created_at"                 | "updated_at"                 | "target_number" | "toplines_settings"                                                                                                                                                                                                                                                                                                                                      | "support_user_id" | "default_country" | "default_entity_type_id" | "status"   | "interact_id"                          | "show_custom_ids" | "allow_organizers_to_export" | "show_electoral_districts" | "restricted_exporting_settings" | "activity_stream_as_initial_entity_view" | "campaign_overview_enabled" | "default_homepage" | "calendar_event_canvassing_type" | "calendar_events_enabled" |
| ---- | ----------------------------------- | --------------- | ---------------------------- | ---------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------- | ------------------------ | ---------- | -------------------------------------- | ----------------- | ---------------------------- | -------------------------- | ------------------------------- | ---------------------------------------- | --------------------------- | ------------------ | -------------------------------- | ------------------------- |
| 136  | "ABC INC. not valid"                | 14              | "2020-07-24 14:17:57.559735" | "2021-05-19 12:28:47.471776" | 210             | "{""item_1"": {""entityId"": ""30"", ""entityType"": ""TagCategory""}, ""item_2"": {""entityId"": ""7"", ""entityType"": ""TagCategory""}, ""item_3"": {""entityId"": ""3"", ""entityType"": ""TagCategory""}, ""item_4"": {""entityId"": ""4"", ""entityType"": ""TagCategory""}, ""item_5"": {""entityId"": ""16"", ""entityType"": ""TagCategory""}}" | 55                | "US"              | 1                        | "archived" | "64fee6c8-c3f6-43ce-a1b5-981e40a79dce" | false             | false                        | false                      | "{}"                            | false                                    | false                       | "list"             |                                  | false                     |
| 21   | "AriaDealersLV11/19"                | 21              | "2019-05-27 19:51:49.335616" | "2021-05-19 12:29:45.80789"  | 563             | "{""item_1"": {""entityType"": ""EntityAddress""}, ""item_2"": {""entityType"": ""EntityPhone""}, ""item_3"": {""entityType"": ""EntityEmail""}, ""item_5"": {""entityId"": ""30"", ""entityType"": ""TagCategory""}}"                                                                                                                                   | 21                | "US"              | 1                        | "archived" | "a922f6a1-cebe-4b9f-84d5-87026e1968c0" | false             | false                        | false                      | "{}"                            | false                                    | false                       | "list"             |                                  | false                     |
| 102  | "Caesars Poker Dealers LV 3/4/2020" | 11              | "2020-03-04 18:19:32.168731" | "2021-05-19 12:31:31.358416" | 68              | "{""item_1"": {""entityId"": ""7"", ""entityType"": ""TagCategory""}, ""item_2"": {""entityId"": ""4"", ""entityType"": ""TagCategory""}, ""item_3"": {""entityId"": ""3"", ""entityType"": ""TagCategory""}, ""item_5"": {""entityId"": ""30"", ""entityType"": ""TagCategory""}}"                                                                      | 11                | "US"              | 1                        | "archived" | "591f4e5f-2b32-4fcd-990c-cb7deafb74c4" | false             | false                        | false                      | "{}"                            | false                                    | false                       | "list"             |                                  | false                     |
| 54   | "GoldenNuggetDRLV11/19"             | 11              | "2019-09-20 17:17:56.23991"  | "2021-05-19 12:36:21.849126" | 30              | "{""item_1"": {""entityType"": ""EntityPhone""}, ""item_2"": {""entityType"": ""EntityEmail""}, ""item_3"": {""entityId"": ""19"", ""entityType"": ""TagCategory""}, ""item_5"": {""entityId"": ""12"", ""entityType"": ""TagCategory""}}"                                                                                                               | 11                | "US"              | 1                        | "archived" | "b064f585-4516-42cf-bc4c-1f66266fd960" | false             | false                        | false                      | "{}"                            | false                                    | false                       | "list"             |                                  | false                     |
| 120  | "Tesla Lathrop CA 6.4.20"           | 25              | "2020-06-04 14:55:07.546448" | "2021-05-20 00:08:59.215601" | 200             | "{""item_1"": {""entityId"": ""30"", ""entityType"": ""TagCategory""}, ""item_3"": {""entityId"": ""3"", ""entityType"": ""TagCategory""}, ""item_4"": {""entityId"": ""4"", ""entityType"": ""TagCategory""}, ""item_5"": {""entityId"": ""16"", ""entityType"": ""TagCategory""}}"                                                                     | 43                | "US"              | 1                        | "archived" | "e01ff9f9-4d2d-4e83-8186-ade25909e340" | false             | false                        | false                      | "{}"                            | false                                    | false                       | "list"             |                                  | false                     |

### TAG_GROUPS

- Organizes `TAG_CATEGORIES` into groups in the UI.
- Not used in SQL queries

| "id" | "name"                       | "created_by" | "created_at"                 | "updated_at"                 | "target_type"          | "target_id" |
| ---- | ---------------------------- | ------------ | ---------------------------- | ---------------------------- | ---------------------- | ----------- |
| 9    | "Organizing Activities"      | 137          | "2022-01-11 21:07:09.434247" | "2022-01-11 21:07:09.434247" | "EntityType"           | 1           |
| 10   | "Contact Details"            | 137          | "2022-07-15 18:31:07.467765" | "2022-07-15 18:56:58.830112" | "EntityConnectionType" | 2           |
| 11   | "Connection Details"         | 137          | "2022-08-19 18:16:30.425732" | "2022-08-19 18:16:30.425732" | "EntityConnectionType" | 1           |
| 12   | "Research Data"              | 137          | "2022-08-19 18:22:00.145784" | "2022-08-19 18:22:00.145784" | "EntityConnectionType" | 3           |
| 13   | "Job Details"                | 137          | "2022-08-19 18:39:10.227824" | "2022-08-19 18:39:10.227824" | "EntityConnectionType" | 4           |
| 14   | "Campaigns Worked On"        | 3            | "2022-11-15 14:51:28.247625" | "2022-11-15 14:51:28.247625" | "EntityType"           | 1           |
| 16   | "Local Union Info"           | 3            | "2023-06-09 12:52:48.29993"  | "2023-06-09 12:52:48.29993"  | "EntityType"           | 2           |
| 15   | "Big 3 Actions "             | 3            | "2023-06-09 12:42:25.966267" | "2023-06-09 14:09:55.162865" | "EntityType"           | 2           |
| 17   | "Worker Info"                | 5            | "2023-06-30 12:17:07.852316" | "2023-06-30 12:17:07.852316" | "EntityType"           | 2           |
| 18   | "Gaming"                     | 137          | "2023-08-01 16:24:22.127399" | "2023-08-01 16:24:22.127399" | "EntityType"           | 1           |
| 19   | "Election Captain Checklist" | 382          | "2024-03-05 18:44:48.498597" | "2024-03-05 18:44:48.498597" | "EntityType"           | 1           |
| 1    | "Contact"                    | 3            | "2019-04-24 19:17:18.265464" | "2019-04-24 19:17:18.265464" | "EntityType"           | 1           |
| 2    | "Job Info"                   | 3            | "2019-04-24 19:24:30.952458" | "2019-04-24 19:24:30.952458" | "EntityType"           | 1           |
| 3    | "Support"                    | 3            | "2019-04-24 19:33:31.903953" | "2019-04-24 19:33:31.903953" | "EntityType"           | 1           |
| 4    | "Worker Info"                | 3            | "2019-04-24 19:41:50.572589" | "2019-04-24 19:41:50.572589" | "EntityType"           | 1           |
| 5    | "Higher Education"           | 49           | "2019-07-17 13:06:14.61202"  | "2019-07-17 13:06:14.61202"  | "EntityType"           | 1           |
| 6    | "Training Record"            | 9            | "2019-08-30 14:59:14.246337" | "2019-08-30 14:59:14.246337" | "EntityType"           | 1           |
| 7    | "For Technical Use Only"     | 25           | "2020-07-22 17:48:25.307326" | "2020-07-22 17:48:25.307326" | "EntityType"           | 1           |
| 8    | "Social Media"               | 137          | "2021-06-28 05:57:40.191909" | "2021-06-28 05:57:40.191909" | "EntityType"           | 1           |

### TAG_CATEGORIES

| "id" | "name"           | "multiselectable" | "locked" | "created_by" | "tag_group_id" | "allow_create_tag_type" | "created_at"                 | "updated_at"                 | "target_type" | "target_id" | "read_only_category" | "type"                    | "multiselect_same_tag_behavior" | "attachments_enabled" |
| ---- | ---------------- | ----------------- | -------- | ------------ | -------------- | ----------------------- | ---------------------------- | ---------------------------- | ------------- | ----------- | -------------------- | ------------------------- | ------------------------------- | --------------------- |
| 142  | "Home Facility " | true              | true     | 3            | 14             | "Notes"                 | "2022-11-15 14:52:58.629727" | "2023-06-07 18:50:09.770519" | "EntityType"  | 1           | false                | "TagCategoryMultiSelect"  | 1                               | false                 |
| 144  | "Public actions" | true              | true     | 3            | 15             | "Date"                  | "2023-06-09 12:43:13.12953"  | "2023-06-09 12:43:13.12953"  | "EntityType"  | 2           | false                | "TagCategoryMultiSelect"  | 0                               | false                 |
| 148  | "Text Opt In "   | false             | true     | 5            | 17             | "Standard"              | "2023-06-30 12:17:52.993401" | "2023-06-30 12:17:52.993401" | "EntityType"  | 2           | false                | "TagCategorySingleSelect" | 1                               | false                 |
| 149  | "Employer"       | false             | true     | 5            | 16             | "Standard"              | "2023-07-04 12:29:45.818425" | "2023-07-04 12:29:45.818425" | "EntityType"  | 2           | false                | "TagCategorySingleSelect" | 1                               | false                 |
| 150  | "Division"       | false             | false    | 5            | 16             | "Standard"              | "2023-07-08 00:09:47.683834" | "2023-07-10 11:41:08.929941" | "EntityType"  | 2           | false                | "TagCategoryMultiSelect"  | 1                               | false                 |

#### `TAG_CATEGORIES`: Sorted by Name

| "id" | "name"                                                                  | "allow\*create_tag_type" |
| ---- | ----------------------------------------------------------------------- | ------------------------ |
| 158  | "1:1 Relational Meeting"                                                | "Date"                   |
| 159  | "1:1 Relational Meetings with Notes"                                    | "Notes"                  |
| 74   | "Actively Campaigned Against"                                           | "Standard"               |
| 50   | "Activist"                                                              | "Standard"               |
| 195  | "Additional Phones"                                                     | "Notes"                  |
| 27   | "Advisor"                                                               | "Standard"               |
| 184  | "Airline"                                                               | "Standard"               |
| 83   | "Applied for a Job at"                                                  | "Standard"               |
| 128  | "Area"                                                                  | "Standard"               |
| 29   | "Area (Building)"                                                       | "Standard"               |
| 105  | "Ask"                                                                   | "Standard"               |
| 45   | "Assignment"                                                            | "Notes"                  |
| 95   | "Assignment Completed"                                                  | "Notes"                  |
| 93   | "Attended a Training"                                                   | "Date"                   |
| 192  | "Attended OC Meeting"                                                   | "Date"                   |
| 92   | "Attended Zoom"                                                         | "Date"                   |
| 30   | "Authorization Card"                                                    | "Date"                   |
| 90   | "Authorization Card Comments"                                           | "Notes"                  |
| 10   | "Authorization Witness "                                                | "Notes"                  |
| 75   | "Ballot Status "                                                        | "Standard"               |
| 139  | "Band/Pod"                                                              | "Standard"               |
| 185  | "Bargaining Survey"                                                     | "Date"                   |
| 204  | "Base Title"                                                            | "Standard"               |
| 157  | "Big 3 Online Card Source"                                              | "Standard"               |
| 55   | "Campus"                                                                | "Address"                |
| 154  | "Casino"                                                                | "Standard"               |
| 73   | "Challenged Voter"                                                      | "Standard"               |
| 198  | "Circulating Petitions"                                                 | "Standard"               |
| 3    | "Classification "                                                       | "Standard"               |
| 67   | "Classification Category"                                               | "Standard"               |
| 68   | "Classification Type"                                                   | "Standard"               |
| 48   | "Clock Number"                                                          | "Number"                 |
| 46   | "Commitment Question"                                                   | "Date"                   |
| 91   | "Committed to"                                                          | "Date"                   |
| 52   | "Committee Member"                                                      | "Standard"               |
| 43   | "Communication Team"                                                    | "Standard"               |
| 121  | "Connection Type"                                                       | "Standard"               |
| 2    | "Contact"                                                               | "Date"                   |
| 112  | "Data Change Notes"                                                     | "Notes"                  |
| 129  | "Date Hired"                                                            | "Date"                   |
| 106  | "Date of Contact"                                                       | "Date"                   |
| 110  | "Debrief Log"                                                           | "Date"                   |
| 51   | "Degree"                                                                | "Standard"               |
| 63   | "Demographics"                                                          | "Standard"               |
| 4    | "Department"                                                            | "Standard"               |
| 130  | "Department"                                                            | "Standard"               |
| 99   | "Department/Cost Center Number"                                         | "Standard"               |
| 25   | "Department or Program"                                                 | "Standard"               |
| 66   | "Department Type"                                                       | "Standard"               |
| 200  | "Division"                                                              | "Standard"               |
| 150  | "Division"                                                              | "Standard"               |
| 14   | "Do Not Contact"                                                        | "Standard"               |
| 89   | "Duplicate Record"                                                      | "Standard"               |
| 162  | "Election Captain"                                                      | "Date"                   |
| 163  | " Election Captain Checklist"                                           | "Date"                   |
| 178  | "Election Planning Meeting"                                             | "Date"                   |
| 149  | "Employer"                                                              | "Standard"               |
| 131  | "Employer"                                                              | "Standard"               |
| 5    | "Employer "                                                             | "Standard"               |
| 59   | "Employer with Address"                                                 | "Address"                |
| 132  | "Employment Dates"                                                      | "Date"                   |
| 78   | "Facebook"                                                              | "Notes"                  |
| 186  | "Facilitated Training"                                                  | "Date"                   |
| 190  | "Facility"                                                              | "Standard"               |
| 6    | "Full Time/Part Time"                                                   | "Standard"               |
| 155  | "Games"                                                                 | "Standard"               |
| 141  | "Group"                                                                 | "Standard"               |
| 142  | "Home Facility "                                                        | "Notes"                  |
| 145  | "Home Local"                                                            | "Number"                 |
| 146  | "Home plant"                                                            | "Standard"               |
| 1    | "Housecall Status "                                                     | "Standard"               |
| 102  | "Housecall with Notes"                                                  | "Notes"                  |
| 113  | "Immediate Supervisor"                                                  | "Notes"                  |
| 72   | "Initial Assessments"                                                   | "Notes"                  |
| 37   | "InPlant specialties "                                                  | "Standard"               |
| 114  | "Instagram"                                                             | "Notes"                  |
| 88   | "Interested in getting more involved"                                   | "Notes"                  |
| 15   | "Issues"                                                                | "Notes"                  |
| 70   | "Job End Date"                                                          | "Date"                   |
| 133  | "Job Name"                                                              | "Standard"               |
| 65   | "Job Notes"                                                             | "Notes"                  |
| 69   | "Job Start Date"                                                        | "Date"                   |
| 134  | "Job Title"                                                             | "Standard"               |
| 28   | "Job Titles"                                                            | "Notes"                  |
| 118  | "Languages (other than English)"                                        | "Standard"               |
| 40   | "Layoffs, Closings & Strikes: Role of the Community Services Committee" | "Date"                   |
| 33   | "Line"                                                                  | "Standard"               |
| 169  | "Line Plan"                                                             | "Date"                   |
| 80   | "LinkedIn"                                                              | "Notes"                  |
| 123  | "Links"                                                                 | "Notes"                  |
| 147  | "Local Position Held"                                                   | "Standard"               |
| 56   | "Local Union"                                                           | "Standard"               |
| 111  | "Location"                                                              | "Notes"                  |
| 57   | "Manager"                                                               | "Notes"                  |
| 42   | "Meetings"                                                              | "Date"                   |
| 31   | "Membership Card"                                                       | "Date"                   |
| 173  | "Mercedes Team Lead"                                                    | "Standard"               |
| 191  | "Model"                                                                 | "Standard"               |
| 143  | "Multiple Languages spoken "                                            | "Notes"                  |
| 87   | "Name on Tear Off"                                                      | "Notes"                  |
| 170  | "Name Source"                                                           | "Notes"                  |
| 199  | "Name Suffix"                                                           | "Standard"               |
| 32   | "Need SS#"                                                              | "Standard"               |
| 120  | "Negative Workplace Sentiments"                                         | "Standard"               |
| 16   | "Network"                                                               | "Standard"               |
| 44   | "Network"                                                               | "Standard"               |
| 49   | "NOTE FIELD"                                                            | "Notes"                  |
| 107  | "Notes"                                                                 | "Notes"                  |
| 17   | "Not In Unit"                                                           | "Standard"               |
| 24   | "Office/Labs"                                                           | "Notes"                  |
| 207  | "On Team"                                                               | "Standard"               |
| 108  | "Organizer"                                                             | "Standard"               |
| 41   | "Organizing trainings"                                                  | "Date"                   |
| 209  | "Original Roster Data Source"                                           | "Standard"               |
| 189  | "Other Activities"                                                      | "Date"                   |
| 115  | "Other Names"                                                           | "Notes"                  |
| 135  | "Other Notes"                                                           | "Notes"                  |
| 81   | "Other Social Media"                                                    | "Notes"                  |
| 62   | "Parking Lot"                                                           | "Standard"               |
| 171  | "Parking Lot Meetings"                                                  | "Date"                   |
| 96   | "Personal Info"                                                         | "Notes"                  |
| 103  | "Petition or Open Letter"                                               | "Notes"                  |
| 165  | "Phonebank/Textbank"                                                    | "Date"                   |
| 166  | "Pic and Quote"                                                         | "Date"                   |
| 175  | "PLACEHOLDER \* DO NOT USE"                                             | "Date"                   |
| 60   | "Plant"                                                                 | "Standard"               |
| 98   | "Position Number"                                                       | "Standard"               |
| 119  | "Positive Workplace Sentiments"                                         | "Standard"               |
| 117  | "Possible Supervisor"                                                   | "Standard"               |
| 12   | "Potential Leader"                                                      | "Standard"               |
| 77   | "Previous Employer"                                                     | "Standard"               |
| 85   | "Previous Employer with End Date"                                       | "Date"                   |
| 71   | "Previous Notes"                                                        | "Notes"                  |
| 19   | "Previous Supporter "                                                   | "Standard"               |
| 197  | "Previous Union"                                                        | "Notes"                  |
| 144  | "Public actions"                                                        | "Date"                   |
| 13   | "Public Support "                                                       | "Date"                   |
| 140  | "QR Codes and similar forms"                                            | "Date"                   |
| 212  | "Rally"                                                                 | "Standard"               |
| 213  | "Rally RSVP"                                                            | "Date"                   |
| 216  | "Recurring Uploads"                                                     | "Standard"               |
| 152  | "Region"                                                                | "Standard"               |
| 151  | "Region"                                                                | "Notes"                  |
| 124  | "Research Date"                                                         | "Date"                   |
| 127  | "Researcher"                                                            | "Standard"               |
| 125  | "Research Note"                                                         | "Notes"                  |
| 86   | "Research Notes"                                                        | "Notes"                  |
| 126  | "Research Source"                                                       | "Standard"               |
| 109  | "Response to Ask"                                                       | "Standard"               |
| 53   | "Semester"                                                              | "Standard"               |
| 136  | "Shift"                                                                 | "Standard"               |
| 7    | "Shift"                                                                 | "Standard"               |
| 97   | "Shift with Schedule"                                                   | "Shift"                  |
| 203  | "Simplified Title"                                                      | "Standard"               |
| 64   | "Social Media"                                                          | "Notes"                  |
| 167  | "Social Media Post"                                                     | "Date"                   |
| 122  | "Source"                                                                | "Standard"               |
| 137  | "Source"                                                                | "Standard"               |
| 61   | "Source List"                                                           | "Standard"               |
| 35   | "STANDARD FLAG 2"                                                       | "Standard"               |
| 36   | "STANDARD FLAG 3"                                                       | "Standard"               |
| 76   | "Start date"                                                            | "Date"                   |
| 47   | "Status"                                                                | "Notes"                  |
| 34   | "Strike Assessment"                                                     | "Standard"               |
| 214  | "Subarea"                                                               | "Standard"               |
| 201  | "Subdivision"                                                           | "Standard"               |
| 161  | "Sub-Line"                                                              | "Standard"               |
| 138  | "Supervisor"                                                            | "Standard"               |
| 206  | "Supervisor's Supervisor"                                               | "Standard"               |
| 82   | "Survey"                                                                | "Standard"               |
| 84   | "Survey Notes"                                                          | "Notes"                  |
| 196  | "Survey Organizer"                                                      | "Date"                   |
| 215  | "Targeted Online Engagement"                                            | "Notes"                  |
| 20   | "Target Followup"                                                       | "Notes"                  |
| 104  | "Team"                                                                  | "Standard"               |
| 183  | "Terminal"                                                              | "Standard"               |
| 210  | "Test Field - Single select, not Read Only"                             | "Standard"               |
| 211  | "Test Field - Single select, Read Only"                                 | "Standard"               |
| 148  | "Text Opt In "                                                          | "Standard"               |
| 21   | "Text Opt-In"                                                           | "Standard"               |
| 174  | "Text Responses"                                                        | "Date"                   |
| 202  | "Title"                                                                 | "Standard"               |
| 208  | "Title In Unit"                                                         | "Standard"               |
| 205  | "Title Rank/Suffix"                                                     | "Standard"               |
| 194  | "Town Hall"                                                             | "Date"                   |
| 182  | "T-Shirt Distribution"                                                  | "Standard"               |
| 179  | "T-Shirt Size"                                                          | "Standard"               |
| 180  | "T-Shirt Type"                                                          | "Standard"               |
| 54   | "Turf"                                                                  | "Standard"               |
| 79   | "Twitter"                                                               | "Notes"                  |
| 153  | "UAW Membership Status"                                                 | "Standard"               |
| 101  | "Uniting Auto Workers Convention (May 22, 2022)"                        | "Notes"                  |
| 176  | "Vote Plan"                                                             | "Notes"                  |
| 168  | "Vote Yes Sign-On"                                                      | "Date"                   |
| 177  | "Voting EC"                                                             | "Standard"               |
| 181  | "Voting Location"                                                       | "Standard"               |
| 172  | "Who Assessed Them?"                                                    | "Date"                   |
| 193  | "Who Organized Them?"                                                   | "Date"                   |
| 160  | "Who signed them up?"                                                   | "Standard"               |
| 188  | "Who Signed Them Up and When"                                           | "Date"                   |
| 94   | "Will Talk to Workers from their Area"                                  | "Date"                   |
| 164  | "Winning Union Elections Training"                                      | "Date"                   |
| 100  | "Work Area"                                                             | "Standard"               |
| 116  | "Work Email"                                                            | "Notes"                  |
| 187  | "Working Conditions Survey"                                             | "Date"                   |
| 58   | "Work Schedule Rule"                                                    | "Standard"               |
| 8    | "Worksite"                                                              | "Address"                |
| 156  | "Works Second Job"                                                      | "Notes"                  |
| 26   | "Year Entered"                                                          | "Notes"                  |

#### Full List by Number

| "id" | "name"                                                                  | "allow\*create_tag_type" |
| ---- | ----------------------------------------------------------------------- | ------------------------ |
| 1    | "Housecall Status "                                                     | "Standard"               |
| 2    | "Contact"                                                               | "Date"                   |
| 3    | "Classification "                                                       | "Standard"               |
| 4    | "Department"                                                            | "Standard"               |
| 5    | "Employer "                                                             | "Standard"               |
| 6    | "Full Time/Part Time"                                                   | "Standard"               |
| 7    | "Shift"                                                                 | "Standard"               |
| 8    | "Worksite"                                                              | "Address"                |
| 10   | "Authorization Witness "                                                | "Notes"                  |
| 12   | "Potential Leader"                                                      | "Standard"               |
| 13   | "Public Support "                                                       | "Date"                   |
| 14   | "Do Not Contact"                                                        | "Standard"               |
| 15   | "Issues"                                                                | "Notes"                  |
| 16   | "Network"                                                               | "Standard"               |
| 17   | "Not In Unit"                                                           | "Standard"               |
| 19   | "Previous Supporter "                                                   | "Standard"               |
| 20   | "Target Followup"                                                       | "Notes"                  |
| 21   | "Text Opt-In"                                                           | "Standard"               |
| 24   | "Office/Labs"                                                           | "Notes"                  |
| 25   | "Department or Program"                                                 | "Standard"               |
| 26   | "Year Entered"                                                          | "Notes"                  |
| 27   | "Advisor"                                                               | "Standard"               |
| 28   | "Job Titles"                                                            | "Notes"                  |
| 29   | "Area (Building)"                                                       | "Standard"               |
| 30   | "Authorization Card"                                                    | "Date"                   |
| 31   | "Membership Card"                                                       | "Date"                   |
| 32   | "Need SS#"                                                              | "Standard"               |
| 33   | "Line"                                                                  | "Standard"               |
| 34   | "Strike Assessment"                                                     | "Standard"               |
| 35   | "STANDARD FLAG 2"                                                       | "Standard"               |
| 36   | "STANDARD FLAG 3"                                                       | "Standard"               |
| 37   | "InPlant specialties "                                                  | "Standard"               |
| 40   | "Layoffs, Closings & Strikes: Role of the Community Services Committee" | "Date"                   |
| 41   | "Organizing trainings"                                                  | "Date"                   |
| 42   | "Meetings"                                                              | "Date"                   |
| 43   | "Communication Team"                                                    | "Standard"               |
| 44   | "Network"                                                               | "Standard"               |
| 45   | "Assignment"                                                            | "Notes"                  |
| 46   | "Commitment Question"                                                   | "Date"                   |
| 47   | "Status"                                                                | "Notes"                  |
| 48   | "Clock Number"                                                          | "Number"                 |
| 49   | "NOTE FIELD"                                                            | "Notes"                  |
| 50   | "Activist"                                                              | "Standard"               |
| 51   | "Degree"                                                                | "Standard"               |
| 52   | "Committee Member"                                                      | "Standard"               |
| 53   | "Semester"                                                              | "Standard"               |
| 54   | "Turf"                                                                  | "Standard"               |
| 55   | "Campus"                                                                | "Address"                |
| 56   | "Local Union"                                                           | "Standard"               |
| 57   | "Manager"                                                               | "Notes"                  |
| 58   | "Work Schedule Rule"                                                    | "Standard"               |
| 59   | "Employer with Address"                                                 | "Address"                |
| 60   | "Plant"                                                                 | "Standard"               |
| 61   | "Source List"                                                           | "Standard"               |
| 62   | "Parking Lot"                                                           | "Standard"               |
| 63   | "Demographics"                                                          | "Standard"               |
| 64   | "Social Media"                                                          | "Notes"                  |
| 65   | "Job Notes"                                                             | "Notes"                  |
| 66   | "Department Type"                                                       | "Standard"               |
| 67   | "Classification Category"                                               | "Standard"               |
| 68   | "Classification Type"                                                   | "Standard"               |
| 69   | "Job Start Date"                                                        | "Date"                   |
| 70   | "Job End Date"                                                          | "Date"                   |
| 71   | "Previous Notes"                                                        | "Notes"                  |
| 72   | "Initial Assessments"                                                   | "Notes"                  |
| 73   | "Challenged Voter"                                                      | "Standard"               |
| 74   | "Actively Campaigned Against"                                           | "Standard"               |
| 75   | "Ballot Status "                                                        | "Standard"               |
| 76   | "Start date"                                                            | "Date"                   |
| 77   | "Previous Employer"                                                     | "Standard"               |
| 78   | "Facebook"                                                              | "Notes"                  |
| 79   | "Twitter"                                                               | "Notes"                  |
| 80   | "LinkedIn"                                                              | "Notes"                  |
| 81   | "Other Social Media"                                                    | "Notes"                  |
| 82   | "Survey"                                                                | "Standard"               |
| 83   | "Applied for a Job at"                                                  | "Standard"               |
| 84   | "Survey Notes"                                                          | "Notes"                  |
| 85   | "Previous Employer with End Date"                                       | "Date"                   |
| 86   | "Research Notes"                                                        | "Notes"                  |
| 87   | "Name on Tear Off"                                                      | "Notes"                  |
| 88   | "Interested in getting more involved"                                   | "Notes"                  |
| 89   | "Duplicate Record"                                                      | "Standard"               |
| 90   | "Authorization Card Comments"                                           | "Notes"                  |
| 91   | "Committed to"                                                          | "Date"                   |
| 92   | "Attended Zoom"                                                         | "Date"                   |
| 93   | "Attended a Training"                                                   | "Date"                   |
| 94   | "Will Talk to Workers from their Area"                                  | "Date"                   |
| 95   | "Assignment Completed"                                                  | "Notes"                  |
| 96   | "Personal Info"                                                         | "Notes"                  |
| 97   | "Shift with Schedule"                                                   | "Shift"                  |
| 98   | "Position Number"                                                       | "Standard"               |
| 99   | "Department/Cost Center Number"                                         | "Standard"               |
| 100  | "Work Area"                                                             | "Standard"               |
| 101  | "Uniting Auto Workers Convention (May 22, 2022)"                        | "Notes"                  |
| 102  | "Housecall with Notes"                                                  | "Notes"                  |
| 103  | "Petition or Open Letter"                                               | "Notes"                  |
| 104  | "Team"                                                                  | "Standard"               |
| 105  | "Ask"                                                                   | "Standard"               |
| 106  | "Date of Contact"                                                       | "Date"                   |
| 107  | "Notes"                                                                 | "Notes"                  |
| 108  | "Organizer"                                                             | "Standard"               |
| 109  | "Response to Ask"                                                       | "Standard"               |
| 110  | "Debrief Log"                                                           | "Date"                   |
| 111  | "Location"                                                              | "Notes"                  |
| 112  | "Data Change Notes"                                                     | "Notes"                  |
| 113  | "Immediate Supervisor"                                                  | "Notes"                  |
| 114  | "Instagram"                                                             | "Notes"                  |
| 115  | "Other Names"                                                           | "Notes"                  |
| 116  | "Work Email"                                                            | "Notes"                  |
| 117  | "Possible Supervisor"                                                   | "Standard"               |
| 118  | "Languages (other than English)"                                        | "Standard"               |
| 119  | "Positive Workplace Sentiments"                                         | "Standard"               |
| 120  | "Negative Workplace Sentiments"                                         | "Standard"               |
| 121  | "Connection Type"                                                       | "Standard"               |
| 122  | "Source"                                                                | "Standard"               |
| 123  | "Links"                                                                 | "Notes"                  |
| 124  | "Research Date"                                                         | "Date"                   |
| 125  | "Research Note"                                                         | "Notes"                  |
| 126  | "Research Source"                                                       | "Standard"               |
| 127  | "Researcher"                                                            | "Standard"               |
| 128  | "Area"                                                                  | "Standard"               |
| 129  | "Date Hired"                                                            | "Date"                   |
| 130  | "Department"                                                            | "Standard"               |
| 131  | "Employer"                                                              | "Standard"               |
| 132  | "Employment Dates"                                                      | "Date"                   |
| 133  | "Job Name"                                                              | "Standard"               |
| 134  | "Job Title"                                                             | "Standard"               |
| 135  | "Other Notes"                                                           | "Notes"                  |
| 136  | "Shift"                                                                 | "Standard"               |
| 137  | "Source"                                                                | "Standard"               |
| 138  | "Supervisor"                                                            | "Standard"               |
| 139  | "Band/Pod"                                                              | "Standard"               |
| 140  | "QR Codes and similar forms"                                            | "Date"                   |
| 141  | "Group"                                                                 | "Standard"               |
| 142  | "Home Facility "                                                        | "Notes"                  |
| 143  | "Multiple Languages spoken "                                            | "Notes"                  |
| 144  | "Public actions"                                                        | "Date"                   |
| 145  | "Home Local"                                                            | "Number"                 |
| 146  | "Home plant"                                                            | "Standard"               |
| 147  | "Local Position Held"                                                   | "Standard"               |
| 148  | "Text Opt In "                                                          | "Standard"               |
| 149  | "Employer"                                                              | "Standard"               |
| 150  | "Division"                                                              | "Standard"               |
| 151  | "Region"                                                                | "Notes"                  |
| 152  | "Region"                                                                | "Standard"               |
| 153  | "UAW Membership Status"                                                 | "Standard"               |
| 154  | "Casino"                                                                | "Standard"               |
| 155  | "Games"                                                                 | "Standard"               |
| 156  | "Works Second Job"                                                      | "Notes"                  |
| 157  | "Big 3 Online Card Source"                                              | "Standard"               |
| 158  | "1:1 Relational Meeting"                                                | "Date"                   |
| 159  | "1:1 Relational Meetings with Notes"                                    | "Notes"                  |
| 160  | "Who signed them up?"                                                   | "Standard"               |
| 161  | "Sub-Line"                                                              | "Standard"               |
| 162  | "Election Captain"                                                      | "Date"                   |
| 163  | " Election Captain Checklist"                                           | "Date"                   |
| 164  | "Winning Union Elections Training"                                      | "Date"                   |
| 165  | "Phonebank/Textbank"                                                    | "Date"                   |
| 166  | "Pic and Quote"                                                         | "Date"                   |
| 167  | "Social Media Post"                                                     | "Date"                   |
| 168  | "Vote Yes Sign-On"                                                      | "Date"                   |
| 169  | "Line Plan"                                                             | "Date"                   |
| 170  | "Name Source"                                                           | "Notes"                  |
| 171  | "Parking Lot Meetings"                                                  | "Date"                   |
| 172  | "Who Assessed Them?"                                                    | "Date"                   |
| 173  | "Mercedes Team Lead"                                                    | "Standard"               |
| 174  | "Text Responses"                                                        | "Date"                   |
| 175  | "PLACEHOLDER \* DO NOT USE"                                             | "Date"                   |
| 176  | "Vote Plan"                                                             | "Notes"                  |
| 177  | "Voting EC"                                                             | "Standard"               |
| 178  | "Election Planning Meeting"                                             | "Date"                   |
| 179  | "T-Shirt Size"                                                          | "Standard"               |
| 180  | "T-Shirt Type"                                                          | "Standard"               |
| 181  | "Voting Location"                                                       | "Standard"               |
| 182  | "T-Shirt Distribution"                                                  | "Standard"               |
| 183  | "Terminal"                                                              | "Standard"               |
| 184  | "Airline"                                                               | "Standard"               |
| 185  | "Bargaining Survey"                                                     | "Date"                   |
| 186  | "Facilitated Training"                                                  | "Date"                   |
| 187  | "Working Conditions Survey"                                             | "Date"                   |
| 188  | "Who Signed Them Up and When"                                           | "Date"                   |
| 189  | "Other Activities"                                                      | "Date"                   |
| 190  | "Facility"                                                              | "Standard"               |
| 191  | "Model"                                                                 | "Standard"               |
| 192  | "Attended OC Meeting"                                                   | "Date"                   |
| 193  | "Who Organized Them?"                                                   | "Date"                   |
| 194  | "Town Hall"                                                             | "Date"                   |
| 195  | "Additional Phones"                                                     | "Notes"                  |
| 196  | "Survey Organizer"                                                      | "Date"                   |
| 197  | "Previous Union"                                                        | "Notes"                  |
| 198  | "Circulating Petitions"                                                 | "Standard"               |
| 199  | "Name Suffix"                                                           | "Standard"               |
| 200  | "Division"                                                              | "Standard"               |
| 201  | "Subdivision"                                                           | "Standard"               |
| 202  | "Title"                                                                 | "Standard"               |
| 203  | "Simplified Title"                                                      | "Standard"               |
| 204  | "Base Title"                                                            | "Standard"               |
| 205  | "Title Rank/Suffix"                                                     | "Standard"               |
| 206  | "Supervisor's Supervisor"                                               | "Standard"               |
| 207  | "On Team"                                                               | "Standard"               |
| 208  | "Title In Unit"                                                         | "Standard"               |
| 209  | "Original Roster Data Source"                                           | "Standard"               |
| 210  | "Test Field - Single select, not Read Only"                             | "Standard"               |
| 211  | "Test Field - Single select, Read Only"                                 | "Standard"               |
| 212  | "Rally"                                                                 | "Standard"               |
| 213  | "Rally RSVP"                                                            | "Date"                   |
| 214  | "Subarea"                                                               | "Standard"               |
| 215  | "Targeted Online Engagement"                                            | "Notes"                  |
| 216  | "Recurring Uploads"                                                     | "Standard"               |

### `TAGS` Table

| "id" | "name"        | "text" | "tag_type" | "created_by" | "tag_category_id" | "created_at"                 | "updated_at"                 | "target_type" | "target_id" | "status" | "interact_id"                          |
| ---- | ------------- | ------ | ---------- | ------------ | ----------------- | ---------------------------- | ---------------------------- | ------------- | ----------- | -------- | -------------------------------------- |
| 7118 | "Tyler Kania" |        | "Standard" | 12           | 16                | "2021-04-19 10:14:34.763027" | "2021-04-19 10:14:34.763027" | "EntityType"  | 1           | 1        | "8720b1f9-b14c-4690-a9dc-9591a915ef79" |
| 7137 | "Rear Beam"   |        | "Standard" | 12           | 33                | "2021-04-22 14:26:38.349436" | "2021-04-22 14:26:38.349436" | "EntityType"  | 1           | 1        | "f1f815ba-1509-4615-a693-4ccf7a17b332" |
| 7119 | "Bob Hammond" |        | "Standard" | 73           | 16                | "2021-04-19 20:34:22.230293" | "2021-04-19 20:34:22.230293" | "EntityType"  | 1           | 1        | "6599f690-c988-4bb0-8294-a574a6ab50e3" |
| 7138 | "Mod 7"       |        | "Standard" | 12           | 33                | "2021-04-22 14:27:42.445703" | "2021-04-22 14:27:42.445703" | "EntityType"  | 1           | 1        | "01d7a339-fd51-43c9-9f88-0c0be0351ace" |
| 7120 | "ZF"          |        | "Address"  | 25           | 8                 | "2021-04-20 21:15:45.166955" | "2021-04-20 21:15:45.17761"  | "EntityType"  | 1           | 1        | "0a7a9df8-bdbe-4e2a-8b01-87633b92d2b5" |

### TAGGABLE_LOGBOOK

| "id"    | "tag_id" | "campaign_id" | "notes" | "created_by" | "signature_id" | "deleted_at" | "created_at"                 | "updated_at"                 | "deleted_by" | "updated_by_id" | "available" | "taggable_id" | "taggable_type" | "interact_id"                          |
| ------- | -------- | ------------- | ------- | ------------ | -------------- | ------------ | ---------------------------- | ---------------------------- | ------------ | --------------- | ----------- | ------------- | --------------- | -------------------------------------- |
| 1048577 | 16675    | 485           |         | 247          |                |              | "2023-09-06 11:51:26.618395" | "2023-09-06 11:51:26.618395" |              |                 | true        | 200909        | "Entity"        | "a3b4642d-f375-485f-8320-cb51f3c30b1c" |
| 1225846 | 1926     | 572           |         | 47           |                |              | "2023-11-09 14:53:59.550042" | "2023-11-09 14:53:59.550042" |              |                 | true        | 216101        | "Entity"        | "46d0919c-4397-454a-b8fc-7f0138bafa24" |
| 1048630 | 16489    | 485           |         | 160          |                |              | "2023-09-06 12:03:17.638933" | "2023-09-06 12:03:17.638933" |              |                 | true        | 200918        | "Entity"        | "22690323-26c5-4077-a9f5-8cdede1d1b86" |
| 1231078 | 1926     | 589           |         | 257          |                |              | "2023-11-16 23:45:27.154527" | "2023-11-16 23:45:27.154527" |              |                 | true        | 221655        | "Entity"        | "4b72cd9e-05e4-40cf-9bed-367dce06259f" |
| 1048635 | 16791    | 485           |         | 247          |                |              | "2023-09-06 12:04:26.212161" | "2023-09-06 12:04:26.212161" |              |                 | true        | 200919        | "Entity"        | "e27e63e7-802f-4911-92df-189cd6f18ffc" |
| 1048646 | 16791    | 485           |         | 247          |                |              | "2023-09-06 12:07:02.013535" | "2023-09-06 12:07:02.013535" |              |                 | true        | 200921        | "Entity"        | "4d914686-71ae-4a6d-a8a3-7f45fb9623fb" |
| 1048681 | 16492    | 485           |         | 159          |                |              | "2023-09-06 12:13:34.618192" | "2023-09-06 12:13:34.618192" |              |                 | true        | 200927        | "Entity"        | "53ce5c78-fdcc-4fdc-bb9a-6b98eb4ac023" |
| 1048683 | 16490    | 485           |         | 247          |                |              | "2023-09-06 12:13:46.8016"   | "2023-09-06 12:13:46.8016"   |              |                 | true        | 200928        | "Entity"        | "7f449cab-6eaf-4f20-b121-e668edbc776f" |
| 1048685 | 16501    | 485           |         | 247          |                |              | "2023-09-06 12:13:53.745224" | "2023-09-06 12:13:53.745224" |              |                 | true        | 200928        | "Entity"        | "6f106c58-742d-4708-9b61-c282a2356867" |
| 1246622 | 10       | 76            |         | 267          |                |              | "2023-11-28 17:14:49.437878" | "2023-11-28 17:14:49.437878" |              |                 | true        | 42758         | "Entity"        | "8f201c78-843c-4f47-8f38-7f407787e776" |
| 1048735 | 16550    | 485           |         | 160          |                |              | "2023-09-06 12:19:30.066911" | "2023-09-06 12:19:30.066911" |              |                 | true        | 200936        | "Entity"        | "c75831d5-2777-4b97-8460-d5fb7274b587" |
| 1048752 | 16779    | 485           |         | 159          |                |              | "2023-09-06 12:21:07.214979" | "2023-09-06 12:21:07.214979" |              |                 | true        | 200939        | "Entity"        | "89df27d4-777d-4e00-983b-9bcca3c1d101" |
| 1048780 | 16639    | 485           |         | 159          |                |              | "2023-09-06 12:23:38.432711" | "2023-09-06 12:23:38.432711" |              |                 | true        | 200945        | "Entity"        | "5ca8a8c3-a356-4287-8f3f-fe497cb9f5e9" |
| 1048781 | 16490    | 485           |         | 159          |                |              | "2023-09-06 12:23:45.526994" | "2023-09-06 12:23:45.526994" |              |                 | true        | 200945        | "Entity"        | "a2530b38-1fa4-4f67-bcbd-ff758306a896" |
| 1048809 | 16501    | 485           |         | 247          |                |              | "2023-09-06 12:26:20.575967" | "2023-09-06 12:26:20.575967" |              |                 | true        | 200950        | "Entity"        | "da6f54eb-398c-4409-9ad8-09cd903c9843" |
| 1048810 | 16675    | 485           |         | 247          |                |              | "2023-09-06 12:26:24.987502" | "2023-09-06 12:26:24.987502" |              |                 | true        | 200950        | "Entity"        | "8618b765-f1d3-4b4c-91bd-793e45883ff6" |
| 1048814 | 16639    | 485           |         | 159          |                |              | "2023-09-06 12:26:55.076997" | "2023-09-06 12:26:55.076997" |              |                 | true        | 200951        | "Entity"        | "f3d83e57-06fc-43a2-84fd-25d02b4710ff" |
| 1048818 | 16489    | 485           |         | 160          |                |              | "2023-09-06 12:27:22.771615" | "2023-09-06 12:27:22.771615" |              |                 | true        | 200952        | "Entity"        | "639f1398-357d-454e-85cd-0332e0358f0c" |
| 1048819 | 16550    | 485           |         | 160          |                |              | "2023-09-06 12:27:28.758619" | "2023-09-06 12:27:28.758619" |              |                 | true        | 200952        | "Entity"        | "3f7b8e4f-939a-429b-86ea-b15d22c1bad2" |
| 1048829 | 33       | 485           |         | 159          |                |              | "2023-09-06 12:28:01.043692" | "2023-09-06 12:28:01.043692" |              |                 | true        | 200954        | "Entity"        | "71a57c07-8fac-41b3-8622-4c844d85a254" |

### `GLOBAL_NOTES`

#### Structure

| "id"   | "text"                                  | "owner_id" | "owner_type"      | "created_by_id" | "created_at"                 | "updated_at"                 | "campaign_id" | "updated_by_id" | "note_type" | "pinned_at" | "pinned_by_id" |
| ------ | --------------------------------------- | ---------- | ----------------- | --------------- | ---------------------------- | ---------------------------- | ------------- | --------------- | ----------- | ----------- | -------------- |
| 23031  | "Shift manager"                         | 50140      | "Entity"          | 74              | "2020-06-01 12:08:53.796659" | "2020-06-01 12:08:53.796659" | 83            |                 | "text"      |             |                |
| 23033  | "Worked at Caesar, and Harrahs "        | 50143      | "Entity"          | 74              | "2020-06-01 12:19:26.676208" | "2020-06-01 12:19:26.676208" | 90            |                 | "text"      |             |                |
| 353452 | "2016-04-11"                            | 1294606    | "TaggableLogbook" | 137             | "2023-12-08 02:33:56.725043" | "2023-12-08 02:33:56.725043" | 590           |                 | "date"      |             |                |
| 25356  | "attended conference call today"        | 50192      | "Entity"          | 73              | "2020-06-24 22:26:54.689778" | "2020-06-24 22:26:54.689778" | 122           |                 | "text"      |             |                |
| 27562  | "6/24/2020 rate 2 per Craig Richardson" | 54469      | "Entity"          | 12              | "2020-08-05 15:36:44.803423" | "2020-08-05 15:46:46.747124" | 127           | 12              | "text"      |             |                |

#### Important gn Tags for Name Matching

| id    | name         |
| ----- | ------------ |
| 11709 | Name Source  |
| 11610 | Work Email 1 |

### `EMAILS`

| "id"  | "email"                     | "email_type" | "owner_id" | "owner_type" | "created_by_id" | "status"     | "created_at"                 | "updated_at"                 | "updated_by_id" | "interact_id"                          | "source"         |
| ----- | --------------------------- | ------------ | ---------- | ------------ | --------------- | ------------ | ---------------------------- | ---------------------------- | --------------- | -------------------------------------- | ---------------- |
| 4143  | `"bswan91@hotmail.com"`       | "home"       | 30269      | "Entity"     | 46              | "verified"   | "2019-12-06 17:31:42.140195" | "2019-12-06 17:31:42.140195" |                 | "11137cd2-13ac-4138-809d-3f896e916eb9" | "action_builder" |
| 4144  | `"lhackett1959@aol.com"`      | "home"       | 30270      | "Entity"     | 46              | "verified"   | "2019-12-06 17:34:26.399753" | "2019-12-06 17:34:26.399753" |                 | "50fe148d-6262-4614-b02d-abb89c60446e" | "action_builder" |
| 30088 | `"ethangerthert11@gmail.com"` | "home"       | 129338     | "Entity"     | 112             | "user_added" | "2022-09-28 17:34:02.415002" | "2022-09-28 17:34:02.415002" |                 | "d2f70aec-093d-4a0c-8d75-0113628a4bc4" | "action_builder" |
| 30090 | `"kennalee2250@gmail.com"`    | "home"       | 129344     | "Entity"     | 237             | "user_added" | "2022-09-28 19:29:04.35976"  | "2022-09-28 19:29:04.35976"  |                 | "3306e7c8-edc3-4c60-b5fc-888c3633fe88" | "action_builder" |
| 509   | `"fmathis4o@deviantart.com"`  | "home"       | 4527       | "Entity"     | 2               | "user_added" | "2019-07-03 22:22:19.298942" | "2019-07-03 22:22:19.298942" |                 | "9a8ea42f-7a17-4e49-9a08-049029bfcdc0" | "upload"         |

### `PHONE_NUMBERS`

| id    | number       | ext | number_type | owner_id | owner_type | created_by_id | status     | created_at              | updated_at              | updated_by_id | dw_id | interact_id                          | source         |
| ----- | ------------ | --- | ----------- | -------- | ---------- | ------------- | ---------- | ----------------------- | ----------------------- | ------------- | ----- | ------------------------------------ | -------------- |
| 55537 | +13343138197 |     | cell        | 129323   | Entity     | 239           | verified   | 2022-09-27 21:49:12.227 | 2022-09-27 22:30:24.166 | 239           |       | 8a6f3fa6-175e-4b37-a9fe-7747f6881f44 | action_builder |
| 25330 | +18123505113 |     | cell        | 56073    | Entity     | 47            | user_added | 2020-12-14 21:56:42.763 | 2020-12-14 21:56:42.763 |               |       | debea0da-36b1-4777-afeb-25f28d35fe29 | action_builder |
| 27078 | +19375087451 |     | cell        | 64481    | Entity     | 73            | user_added | 2021-03-24 16:31:29.413 | 2021-03-24 16:31:29.413 |               |       | 70218faf-fbb2-4a92-8d7b-866474f9c56e | action_builder |
| 27935 | +18108828993 |     | cell        | 67957    | Entity     | 12            | user_added | 2021-06-10 14:16:50.356 | 2021-06-10 14:16:50.356 |               |       | 66bb2375-d8e6-449e-b91e-3adc965a360e | action_builder |

## Queries

## Get Names from a Campaign

```SQL
SELECT
    ENTITIES.FIRST_NAME,
    ENTITIES.LAST_NAME
FROM
    ENTITIES
JOIN
    CAMPAIGNS_ENTITIES ON ENTITIES.ID = CAMPAIGNS_ENTITIES.ENTITY_ID
JOIN
    CAMPAIGNS ON CAMPAIGNS_ENTITIES.CAMPAIGN_ID = CAMPAIGNS.ID
WHERE
    CAMPAIGNS.ID = 649
ORDER BY ENTITIES.LAST_NAME, ENTITIES.FIRST_NAME ASC;
```

## Emails

```SQL
SELECT
    E.ID,
    E.INTERACT_ID,
    E.FIRST_NAME,
    E.LAST_NAME,
    EMAILS.EMAIL
FROM
    ENTITIES E
    JOIN CAMPAIGNS_ENTITIES CE ON E.ID = CE.ENTITY_ID
    JOIN CAMPAIGNS C ON CE.CAMPAIGN_ID = C.ID
    JOIN EMAILS ON E.ID = EMAILS.OWNER_ID
WHERE
    C.ID = 683
```

## Get Specific Tag ("Petition or Open Letter", `TL.TAG_ID = 28451`) from VW Campaign (`TL.CAMPAIGN_ID = 76`)

```SQL
SELECT
    E.ID,
    E.INTERACT_ID,
    E.FIRST_NAME,
    E.LAST_NAME,
    GN.TEXT
FROM
    ENTITIES E
    INNER JOIN TAGGABLE_LOGBOOK TL ON E.ID = TL.TAGGABLE_ID
    LEFT JOIN GLOBAL_NOTES GN ON GN.OWNER_ID = TL.ID
WHERE
    TL.TAG_ID = 28451
    AND TL.DELETED_AT IS NULL
    AND TL.CAMPAIGN_ID = 76
```

```SQL
/*Single Select Tags Query 1*/
WITH
    TL AS (
        SELECT
            CE.ENTITY_ID AS E_ID,
            TLX.*
        FROM
            CAMPAIGNS_ENTITIES CE
            LEFT JOIN TAGGABLE_LOGBOOK TLX ON CE.ENTITY_ID = TLX.TAGGABLE_ID
        WHERE
            (
                TLX.CAMPAIGN_ID = 279
                OR TLX.CAMPAIGN_ID IS NULL
            )
            AND CE.CAMPAIGN_ID = 279
        ORDER BY
            TLX.UPDATED_AT
    )
SELECT
    E.ID,
    E.FIRST_NAME,
    E.MIDDLE_NAME,
    E.LAST_NAME,
    E.INTERACT_ID,
    CE.LATEST_ASSESSMENT_LEVEL AS CURRENT_ASSESSMENT,
    TS.MAXCARDDATE AS MOST_RECENT_CARD,
    TS.MINCARDDATE AS EARLIEST_CARD,
    TS.SIGNEDCARD AS SIGNED_CARD,
    MIN(r   .NAME) FILTER (
        WHERE
            TC2.NAME = 'Department'
            AND TL.DELETED_AT IS NULL
    ) AS DEPARTMENT,
    MIN(T2.NAME) FILTER (
        WHERE
            TC2.NAME = 'Work Area'
            AND TL.DELETED_AT IS NULL
    ) AS AREA,
    MIN(T2.NAME) FILTER (
        WHERE
            TC2.NAME = 'Shift'
            AND TL.DELETED_AT IS NULL
    ) AS SHIFT,
    MIN(T2.NAME) FILTER (
        WHERE
            TC2.NAME = 'Immediate Supervisor'
            AND TL.DELETED_AT IS NULL
    ) AS SUPERVISOR,
    MIN(T2.NAME) FILTER (
        WHERE
            TC2.NAME = 'Classification '
            AND TL.DELETED_AT IS NULL
    ) AS CLASSIFICATION,
    MIN(T2.NAME) FILTER (
        WHERE
            TC2.NAME = 'Facility'
            AND TL.DELETED_AT IS NULL
    ) AS FACILITY,
    MIN(T2.NAME) FILTER (
        WHERE
            TC2.NAME = 'Line'
            AND TL.DELETED_AT IS NULL
    ) AS LINE,
    MIN(T2.CREATED_AT) FILTER (
        WHERE
            TC2.NAME = 'Contact'
            AND TL.DELETED_AT IS NULL
    ) AS CONTACT_CREATED_AT,
    MIN(T2.NAME) FILTER (
        WHERE
            TC2.NAME = 'Potential Leader'
            AND TL.DELETED_AT IS NULL
    ) AS POTENTIAL_LEADER,
    MIN(T2.NAME) FILTER (
        WHERE
            TC2.NAME = 'Text Opt-In'
            AND TL.DELETED_AT IS NULL
    ) AS TEXT_OPT_IN,
    MIN(T2.NAME) FILTER (
        WHERE
            TC2.NAME = 'Who Signed Them Up and When?'
            AND TL.DELETED_AT IS NULL
    ) AS WHOSIGNEDTHEMUP,
    MAX(TL.CREATED_AT) FILTER (
        WHERE
            TC2.NAME = 'Contact'
            AND T2.NAME = 'Contacted by VOC'
            AND TL.DELETED_AT IS NULL
    ) AS LASTCONTACTEDBYVOC,
    'TRUE' AS INUNIT,
    (
        (TS.MINCARDENTRYDATE AT TIME ZONE 'UTC') AT TIME ZONE 'America/Los_Angeles'
    ) AS EARLIEST_CARD_ENTRY_DATE,
    E.NICKNAME,
    TS2.MEETING_DATE,
    E.INTERACT_ID AS ABID,
    TS3.LOCATION_DETAILS
FROM
    CAMPAIGNS_ENTITIES CE
    INNER JOIN ENTITIES E ON E.ID = CE.ENTITY_ID
    INNER JOIN TL ON TL.E_ID = E.ID
    LEFT JOIN TAGS T2 ON T2.ID = TL.TAG_ID
    LEFT JOIN TAG_CATEGORIES TC2 ON TC2.ID = T2.TAG_CATEGORY_ID
    LEFT JOIN CAMPAIGNS_TAGS CT ON CT.TAG_ID = T2.ID
    LEFT JOIN (
        SELECT
            TL3.TAGGABLE_ID,
            MAX(GN.TEXT) AS MAXCARDDATE,
            MIN(GN.TEXT) AS MINCARDDATE,
            'TRUE' AS SIGNEDCARD,
            MIN(TL3.CREATED_AT) AS MINCARDENTRYDATE
        FROM
            GLOBAL_NOTES GN
            INNER JOIN TAGGABLE_LOGBOOK TL3 ON TL3.ID = GN.OWNER_ID
        WHERE
            (
                TL3.TAG_ID = 634
                OR TL3.TAG_ID = 8039
            )
            AND GN.OWNER_TYPE = 'TaggableLogbook'
            AND GN.TEXT > '2023-07-31'
            AND TL3.DELETED_AT IS NULL
            AND TL3.CAMPAIGN_ID = 279
        GROUP BY
            TL3.TAGGABLE_ID
    ) TS ON TS.TAGGABLE_ID = CE.ENTITY_ID
    LEFT JOIN (
        SELECT
            TL4.TAGGABLE_ID,
            MAX(GN.TEXT) AS MEETING_DATE
        FROM
            GLOBAL_NOTES GN
            INNER JOIN TAGGABLE_LOGBOOK TL4 ON TL4.ID = GN.OWNER_ID
        WHERE
            (
                TL4.TAG_ID = 8
                OR TL4.TAG_ID = 15229
            )
            AND GN.OWNER_TYPE = 'TaggableLogbook'
            AND TL4.DELETED_AT IS NULL
            AND TL4.CAMPAIGN_ID = 279
        GROUP BY
            TL4.TAGGABLE_ID
    ) TS2 ON TS2.TAGGABLE_ID = CE.ENTITY_ID
    LEFT JOIN (
        SELECT
            TL.TAGGABLE_ID,
            CONCAT(MAX(T.NAME), ' ', MAX(GN.TEXT)) AS LOCATION_DETAILS
        FROM
            TAGGABLE_LOGBOOK TL
            INNER JOIN TAGS T ON TL.TAG_ID = T.ID
            INNER JOIN TAG_CATEGORIES TC ON T.TAG_CATEGORY_ID = TC.ID
            LEFT JOIN GLOBAL_NOTES GN ON GN.OWNER_ID = TL.ID
        WHERE
            TC.ID = 111
            AND TL.DELETED_AT IS NULL
        GROUP BY
            TL.TAGGABLE_ID
    ) TS3 ON TS3.TAGGABLE_ID = CE.ENTITY_ID
WHERE
    CE.CAMPAIGN_ID IN (279)
    AND CE.ENTITY_ID NOT IN (
        SELECT DISTINCT
            TL2.TAGGABLE_ID
        FROM
            TAGS T
            JOIN TAG_CATEGORIES TC ON TC.ID = T.TAG_CATEGORY_ID
            INNER JOIN TAGGABLE_LOGBOOK TL2 ON TL2.TAG_ID = T.ID
        WHERE
            TC.ID = 17
            AND TL2.CAMPAIGN_ID IN (279)
            AND TL2.DELETED_BY IS NULL
    )
    AND (
        CT.CAMPAIGN_ID = 279
        OR CT.CAMPAIGN_ID IS NULL
    )
GROUP BY
    E.ID,
    CE.ID,
    TS.MAXCARDDATE,
    TS.MINCARDDATE,
    TS.SIGNEDCARD,
    TS.MINCARDENTRYDATE,
    TS2.MEETING_DATE,
    TS3.LOCATION_DETAILS;
```

## Name Source Query

used in BOSK campaigns to get name sources

```SQL
SELECT
    e.id,
    gn."text",
    t.name,
    e.first_name,
    e.last_name
FROM
    entities e
    -- entities --> campaigns
JOIN campaigns_entities ce ON
    ce.entity_id = e.id
JOIN campaigns c ON
    c.id = ce.campaign_id
    -- entities --> tags
JOIN taggable_logbook tl ON
    tl.taggable_id = e.id
JOIN tags t ON
    t.id = tl.tag_id
JOIN tag_categories tc ON
    tc.id = t.tag_category_id
LEFT JOIN global_notes gn ON
    gn.owner_id = tl.id
WHERE
    tl.campaign_id = 683
    AND tc.id = 170
GROUP BY
    e.id,
    gn.TEXT,
    t.name
ORDER BY
    gn.text ASC

/*
    entity.id --> campaigns_entities --> campaigns --> taggable_logbook
*/
```
