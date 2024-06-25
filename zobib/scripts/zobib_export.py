import argparse
import os
import sys

import toml
import bibtexparser

from ..api import ZoteroCredentials, get_zotero_api, ZoteroAPI

# TODO: add a parameter for that on the command line and a config format
exclusions = {'abstract', 'keywords', 'doi', 'issn', 'isbn', 'langid', 'note', 'urldate', 'rights'}


def filter_entries(items):
	for entry in items.entries:
		for excluded in exclusions:
			if excluded in entry:
				del entry[excluded]
				# Is there a better way to do that?


def get_all_items(zotapi: ZoteroAPI, format: str) -> bibtexparser.bibdatabase.BibDatabase:
	items = zotapi.items(format=format)
	filter_entries(items)
	return items


def get_collection_items(zotapi: ZoteroAPI, collection_id: str, format: str) -> bibtexparser.bibdatabase.BibDatabase:
	items = zotapi.everything(zotapi.collection_items(collection_id, format=format))
	filter_entries(items)
	return items


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--credentials-name", default=None)
	parser.add_argument("--collection-id", default=None)
	parser.add_argument("-c", "--config", default=os.getenv('ZOBIB_CONFIG'))
	parser.add_argument("-f", "--format", default="biblatex", choices=("biblatex", "bibtex"))
	args = parser.parse_args()

	if args.config is None:
		print("ERROR: no configuration file provided", file=sys.stderr)
		return 1

	config = toml.load(args.config)

	cred = ZoteroCredentials.from_config(config, name=args.credentials_name)
	assert cred is not None

	zotapi = get_zotero_api(cred)

	if args.collection_id:
		bibdb = get_collection_items(zotapi, args.collection_id, format=args.format)
	else:
		bibdb = get_all_items(zotapi, format=args.format)

	bibitems = bibtexparser.dumps(bibdb)
	print(bibitems)

	#print(.encode('utf-8'))

	# with open("../../zobib.bib", "wb") as ref_file:
	# 	ref_file.write(dumps(items).encode("utf-8"))

	return 0
