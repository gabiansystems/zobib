# zobib: Zotero and bib(la)tex interactions

## Configuration file

Configuration file is a TOML file that gives informations on how to connect to Zotero, how to export collections, etc.

```toml
[credentials]

[credentials.gas]  # credentials for this username
library_id = 1234567  # UserID
library_type = 'user'  # This is a user library
api_key = 'XxfJTc47VqeZ65UiTss7llvK'  # Obtained from zotero.org/settings/keys

[credentials.gabian]  # credentials for this group
library_id = 7654321  # GroupID (look at the URL when accessing zotero.org's group)
library_type = 'group'  # This is a user library
api_key = 'XxfJTc47VqeZ65UiTss7llvK'  # Obtained from zotero.org/settings/keys
```

## Usage

Export a collection in biblatex format:

```bash
zobib export --credentials-name=gabian --collection-id=296VVHIQ --config config.toml > mybib.bib
```
