from models.BaseDataModel import BaseDataModel
from models.db_schemas import Project
from models.enums.DataBaseEnum import DataBaseEnum
from models.db_schemas.data_chunk import DataChunk
from pymongo import InsertOne

class ChunkModel(BaseDataModel):
    def __init__(self, db_client):
        super().__init__(db_client)
        self.collection=self.db_client[DataBaseEnum.COLLECTION_CHUNK_NAME.value]

    async def create_chunk(self,chunk:DataChunk):
        result=await self.collection.insert_one(chunk.dict())
        chunk.id=result.inserted_id
        return chunk
    async def get_chunk(self,chunk_id:str):
        record=await self.collection.find_one(
            {
                "chunk_id":chunk_id
            }
        )
        if record is None:
            return None
        return DataChunk(**record) 
    # Don't use get all without bagnation
    async def insert_many_chunks(self,chunks:list,batch_size: int=100):

        for i in range(0,len(chunks),batch_size):
            batch=chunks[i:i+batch_size]

            operations=[
                InsertOne(chunk.dict())
                for chunk in batch
            ]

            await self.collection.bulk_write(operations)

            return len(chunks)