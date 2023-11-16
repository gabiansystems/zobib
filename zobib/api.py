# https://www.zotero.org/support/dev/web_api/v3/basics
# https://pyzotero.readthedocs.io/en/latest/
from pyzotero.zotero import Zotero as ZoteroAPI


class ZoteroCredentials(object):

	def __init__(self, library_id, library_type, api_key):
		self.library_id = library_id
		self.library_type = library_type
		self.api_key = api_key

	@classmethod
	def from_config(cls, config:dict, name:str=None):
		credentials = config['credentials']
		if name is None:
			name = credentials['default']
		creds = credentials[name]
		return cls(**creds)


def get_zotero_api(cred: ZoteroCredentials) -> ZoteroAPI:
	return ZoteroAPI(cred.library_id, cred.library_type, cred.api_key)
