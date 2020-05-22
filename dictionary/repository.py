import asyncpg


class WordRepository:
    async def find_by_name(self, word, db_dsn):
        query = """
        SELECT
            name, meaning, dictionary.fa_name
        FROM
            word inner join dictionary on word.dictionary_id = dictionary.id
        WHERE
            name = $1
        """
        conn = await asyncpg.connect(db_dsn)
        result = await conn.fetch(query, word.name)
        conn.close()
        return result

    async def find_by_name_and_dictionary(self, word, db_dsn):
        query = """
        SELECT
            name, meaning, dictionary.fa_name
        FROM
            word inner join dictionary on word.dictionary_id = dictionary.id
        WHERE name = $1 and dictionary.id = $2;
        """
        conn = await asyncpg.connect(db_dsn)
        result = await conn.fetch(query, word.name, word.dictionary)
        conn.close()
        return result


class DictionaryRepository:
    async def get_all_dictionaries(self, db_dsn):
        query = """SELECT id, fa_name FROM dictionary;"""
        conn = await asyncpg.connect(db_dsn)
        result = await conn.fetch(query)
        conn.close()
        return result


WordRepositoryInstance = WordRepository()
DictionaryRepositoryInstance = DictionaryRepository()
