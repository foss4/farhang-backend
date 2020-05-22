class WordRepository:
    async def find_by_name(self, word, pool):
        query = """
        SELECT
            name, meaning, dictionary.fa_name
        FROM
            word inner join dictionary on word.dictionary_id = dictionary.id
        WHERE
            name = $1
        """
        async with pool.acquire() as connection:
            async with connection.transaction():
                return await connection.fetch(query, word.name)

    async def find_by_name_and_dictionary(self, word, pool):
        query = """
        SELECT
            name, meaning, dictionary.fa_name
        FROM
            word inner join dictionary on word.dictionary_id = dictionary.id
        WHERE name = $1 and dictionary.id = $2;
        """
        async with pool.acquire() as connection:
            async with connection.transaction():
                return await connection.fetch(
                    query,
                    word.name,
                    word.dictionary
                )


class DictionaryRepository:
    async def get_all_dictionaries(self, pool):
        query = """SELECT id, fa_name FROM dictionary;"""
        async with pool.acquire() as connection:
            async with connection.transaction():
                return await connection.fetch(query)


WordRepositoryInstance = WordRepository()
DictionaryRepositoryInstance = DictionaryRepository()
