from typing import List


class DB_engine:
    def __init__(self, conn):
        self.conn = conn

    async def add_user

    async def execute(self, query, params, ans):
        if ans:
            result = await self.conn.fetch(query, *params)
            return result
        else:
            await self.conn.execute(query, *params)