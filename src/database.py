from sqlalchemy.dialects.postgresql import insert
from setup import SessionLocal, logging, Phishing
from typing import List


# Listeyi 1000'er 1000'er bölen fonksiyon
def chunk_list(liste, chunk_size):
    """
    Helper function to divide a list into chunks of the specified size.

    Args:
        liste (List): The list to be divided into chunks.
        chunk_size (int): The size of each chunk.

    Yields:
        List: A chunk of the original list.
    """

    for i in range(0, len(liste), chunk_size):
        yield liste[i : i + chunk_size]


async def bulk_insert_phishing_url(urls: List[str]) -> None:
    """
    Asynchronously performs bulk insertion of phishing URLs into the database.

    Args:
        urls (List[str]): A list of phishing URLs to be inserted.

    Returns:
        Returns None.
    """

    if not urls:
        return

    with SessionLocal() as db:
        try:
            chunk_size = 1000
            for chunk in chunk_list(urls, chunk_size):
                url_objects = [Phishing(url=url) for url in chunk]
                stmt = (
                    insert(Phishing)
                    .values([{"url": url} for url in chunk])
                    .on_conflict_do_nothing(index_elements=["url"])
                )
                db.execute(stmt)
            db.commit()
        finally:
            logging.info("save process completed")
