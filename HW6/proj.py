import os
import sys
import understand as und

class CheckEntities:
    def __init__(self, udb_path):
        self.udb_path = udb_path

    def get_all_variables(self, static=False):
        with und.open(self.udb_path) as _db:
            candidates = self._query_variables(_db, static)
            return candidates

    def _query_variables(self, db, static):
        candidates = []
        if static:
            query = db.ents("Static Variable")
            blacklist = ()
        else:
            query = db.ents("Variable")
            blacklist = ('static',)

        for ent in query:
            kind_name = ent.kindname().lower()

            if any(word in kind_name for word in blacklist):
                continue

            parent = ent.parent()

            if parent is None or not parent.kind().check("class") or parent.kind().check("anonymous"):
                continue

            long_name = ent.longname().split(".")

            if len(long_name) < 2:
                continue

            source_package = '.'.join(long_name[:-2]) if len(long_name) >= 3 else None
            source_class, field_name = long_name[-2:]

            is_public = ent.kind().check('public')
            is_private = ent.kind().check('private')

            external_references = sum(1 for ref in ent.refs('coupleby, createby') if '.'.join(long_name[:-1]) not in ref.ent().longname())

            candidate_info = {
                'source_package': source_package,
                'source_class': source_class,
                'field_name': field_name,
                'is_public': is_public,
                'is_private': is_private,
                'external_references': external_references
            }

            candidates.append(candidate_info)

            # Print each candidate on a new line
            print(candidate_info)

        return candidates

# Assuming you have an instance of CheckEntities
our_instance = CheckEntities("C:\\Users\\black\\compiler_design_fall_2023\\HW6\\g4.udb")
our_instance.get_all_variables()
