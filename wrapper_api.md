# Google API Wrapper

The goal is to implement a service that would allow to persist the data in the google docs / spreadsheets / slides format and store it in the google drive. Later I might extend it to other types of files like images.

The goal is not to imitate the half-baked Google API, but to provide a mechanism to create Google objects via API if the proper payload is provided. The documents will be fully replaced each time the persistence is being used.

The reason for that is that Google API lacks a lot of functionality in their API so incremental updates are just lacking.

| Type | ID | Description |
|------|----|-------------|
| document| 1a-28yTY23NuCa7vmyMABGgRDCErW58Q99F_2o9ZePGo | Simple sample google document |
| slide | 17rCbrfnQiFBWqHQCOJ5U7bug05C5XF9c4o4ptRrrOHY | Simple sample google slide |
| sheet | 1R3rJWb50oW2JNOqKd4l0XlP-9hdMPr1c9cxjYX3PWnY | Simple same google spreadsheet |
| parent | 1xa0a3Z4YUfDZ3FQS4LrpdOZEkVp8hrq7 | Parent id |

## Google Drive API

| Endpoint | Method | Description |
|----------|-------|------------|
| /drive/search?name=&mimeType= | GET | Search Google Drive objects by name with optional mimeType |
| /drive/navigate/{path:path}?mimeType= | GET | List google drive content in a specific path with optional mimeType filter |
| /drive/{file_id} | DELETE | Deletes and object by id from the Google Drive |
| /drive/{file_id}/comment | POST | Update new unanchored comment to the file |
| /drive/{file_id}/comment/{comment_id} | DELETE | Delete a comment |
| /drive/{file_id}/comment/{comment_id} | GET | Get specific comment
| /drive/{file_id}/comment/{comment_id}/reply | POST | Add a reply to the comment |
| /drive/{file_id}/comment/{comment_id}/resolve | POST | Resolve the comment |
| /drive/{file_id}/comment | GET | List all the comments |

NOTE: The comment system supports anchoring for various file types. But it very limited and thus the custom anchoring (not implemented upstream yet) is being used. The anchor field (Google Docs) contains custom data as a JSON string following the format: `{"offset": {"startIndex": int, "endIndex": int}}}` for text-based anchoring.
```
{
	"author": {
		"displayName": "Artsiom Tsaryonau",
		"kind": "drive#user",
		"me": true,
		"photoLink": "//lh3.googleusercontent.com/a/ACg8ocKR2dKfCqQUXJsYHibmiL9StNvS32e_ldTqS6GGauqbNwRZ-w=s50-c-k-no"
	},
	"id": "AAABnphfMkI",
	"createdTime": "2025-08-02T14:00:50.229Z",
	"modifiedTime": "2025-08-02T14:00:50.229Z",
	"htmlContent": "This is a comment with anchor",
	"content": "This is a comment with anchor",
	"deleted": false,
	"anchor": "{\"offset\": {\"startIndex\": 10, \"endIndex\": 20}}"
}
```

The Google Drive object information should look like this
```
{
    id: string
    name: string
    mimeType: string
    path: string
    parent_id: string
}
```
With `path` being a full path from the root to the object and parent_id. List and search functions return a list of objects, containing zero, one or more objects.

## Google Spreadsheets API

| Endpoint | Method | Description |
|----------|-------|------------|
| /drive/spreadsheets?parent=&title= | POST | Create new empty spreadsheet, with optional parent id |
| /drive/spreadsheets/{spreadsheet_id}| GET | Return a spreadsheet by id |
| /drive/spreadsheets/{spreadsheet_id} | DELETE | Delete a spreadsheet by id |

Right now the payload and response should adhere to the google's specification for Sheet API.

## Google Documents API

NOTE: adding new tabs is not possible https://stackoverflow.com/questions/79518064/how-to-create-google-doc-tabs-with-the-python-sdk
NOTE: adding anchored comments is not possible either

| Endpoint | Method | Description |
|----------|-------|------------|
| /drive/documents?parent=&title= | POST | Create new empty document, with optional parent id parameter |
| /drive/documents/{document_id} | GET | Return a specific document by id |
| /drive/documents/{document_id} | DELETE | Delete document by id |

Right now the payload and response should adhere to the google's specification for Docs API.

## Google Slides API

| Endpoint | Method | Description |
|----------|-------|------------|
| /drive/slides?parent=&title= | POST | Create new empty presentation, with optional parent id parameter |
| /drive/slides/{slides_id}| GET | Return a specific presentation |
| /drive/slides/{slides_id} | DELETE | Deletes existing presentation |

Right now the payload and response should adhere to the google's specification for Slides API.
