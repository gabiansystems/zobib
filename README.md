# zobib: Zotero and bib(la)tex interactions

## Installation

Installation in development mode:

```bash
VENV=path/to/a/venv/to/create
python3 -m venv $VENV
$VENV/bin/pip install -e .
```

## Configuration file

You must create a configuration file (in TOML format) with the credentials to use to connect to the Zotero API.
Obviously, you need to have a Zotero account.

```toml
# config.toml file
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
$VENV/bin/zobib export --credentials-name=gabian --collection-id=296VVHIQ --config config.toml > mybib.bib
```

The name of the credentials (`gabian`) refers to the credentials in the section `credentials.gabian`. The ID of the collection `296VVHIQ` must be retrieved from the URL of the collection when it is accessed on the Zotero web site.


