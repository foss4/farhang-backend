class WordRepository:

    async def find_by_name(self, word, conn_pool):
        query = """
        SELECT name, meaning, dictionary.name FROM word WHERE
         name = $1; """
        async with conn_pool.acquire() as connection:
            async with connection.transaction():
                return await connection.fetc(query, word.name)

    async def find_by_name_and_dictionary(self, word, conn_pool):
        query = """
        SELECT name, meaning, dictionary.name FROM word
        WHERE name = $1 and dictionary.id = $2;
        """
        async with conn_pool.acquire() as connection:
            async with connection.transaction():
                return await connection.fetc(query, word.name, word.category)


class DictionaryRepository:
    async def find_by_name_and_dictionary(self, conn_pool):
        query = """SELECT id, name FROM dictionary;"""
        async with conn_pool.acquire() as connection:
            async with connection.transaction():
                return await connection.fetc(query)


WordRepositoryInstance = WordRepository()
DictionaryRepositoryInstance = DictionaryRepository()
